extends PanelContainer

## Scrollable log of past dialogue text.

signal closed

var _scroll: ScrollContainer
var _content: VBoxContainer
var _entries: Array[Dictionary] = [] # {speaker, text, color}


func _ready() -> void:
	_setup_ui()
	hide()


func _setup_ui() -> void:
	position = Vector2(0, 0)
	size = Vector2(1920, 1080)

	var style := StyleBoxFlat.new()
	style.bg_color = Color(0.02, 0.02, 0.05, 0.92)
	add_theme_stylebox_override("panel", style)

	var margin := MarginContainer.new()
	margin.position = Vector2(0, 0)
	margin.size = Vector2(1920, 1080)
	margin.add_theme_constant_override("margin_left", 200)
	margin.add_theme_constant_override("margin_right", 200)
	margin.add_theme_constant_override("margin_top", 60)
	margin.add_theme_constant_override("margin_bottom", 60)
	add_child(margin)

	var vbox := VBoxContainer.new()
	vbox.add_theme_constant_override("separation", 8)
	margin.add_child(vbox)

	var title := Label.new()
	title.text = "Verlauf"
	title.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	title.add_theme_font_size_override("font_size", 32)
	title.add_theme_color_override("font_color", Color(0.7, 0.65, 0.6))
	vbox.add_child(title)

	_scroll = ScrollContainer.new()
	_scroll.size_flags_vertical = Control.SIZE_EXPAND_FILL
	vbox.add_child(_scroll)

	_content = VBoxContainer.new()
	_content.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	_content.add_theme_constant_override("separation", 12)
	_scroll.add_child(_content)

	var close_btn := Button.new()
	close_btn.text = "Schließen"
	close_btn.custom_minimum_size = Vector2(200, 45)
	close_btn.size_flags_horizontal = Control.SIZE_SHRINK_CENTER
	close_btn.add_theme_font_size_override("font_size", 22)
	_style_button(close_btn)
	close_btn.pressed.connect(close_log)
	vbox.add_child(close_btn)


func add_entry(speaker: String, text: String, color: Color = Color.WHITE) -> void:
	_entries.append({"speaker": speaker, "text": text, "color": color})


func open_log() -> void:
	_rebuild_content()
	show()
	# Scroll to bottom
	await get_tree().process_frame
	_scroll.scroll_vertical = int(_scroll.get_v_scroll_bar().max_value)


func close_log() -> void:
	hide()
	closed.emit()


func _rebuild_content() -> void:
	for child in _content.get_children():
		child.queue_free()

	for entry in _entries:
		var rtl := RichTextLabel.new()
		rtl.bbcode_enabled = true
		rtl.fit_content = true
		rtl.scroll_active = false
		rtl.size_flags_horizontal = Control.SIZE_EXPAND_FILL
		rtl.add_theme_font_size_override("normal_font_size", 20)

		var speaker: String = entry["speaker"]
		var text: String = entry["text"]
		var color: Color = entry["color"]

		if not speaker.is_empty():
			var hex := color.to_html(false)
			rtl.append_text("[color=#%s]%s:[/color] %s" % [hex, speaker, text])
		else:
			rtl.append_text("[i]%s[/i]" % text)

		_content.add_child(rtl)


func _style_button(btn: Button) -> void:
	var style := StyleBoxFlat.new()
	style.bg_color = Color(0.08, 0.08, 0.12, 0.7)
	style.border_color = Color(0.3, 0.28, 0.25, 0.5)
	style.set_border_width_all(1)
	style.set_corner_radius_all(2)
	style.content_margin_left = 12
	style.content_margin_right = 12
	style.content_margin_top = 8
	style.content_margin_bottom = 8
	btn.add_theme_stylebox_override("normal", style)

	var hover := style.duplicate()
	hover.bg_color = Color(0.15, 0.12, 0.1, 0.9)
	hover.border_color = Color(0.5, 0.45, 0.35, 0.8)
	btn.add_theme_stylebox_override("hover", hover)

	var pressed := style.duplicate()
	pressed.bg_color = Color(0.05, 0.05, 0.08, 0.95)
	btn.add_theme_stylebox_override("pressed", pressed)

	var focus := style.duplicate()
	btn.add_theme_stylebox_override("focus", focus)

	btn.add_theme_color_override("font_color", Color(0.8, 0.75, 0.7))
	btn.add_theme_color_override("font_hover_color", Color(1.0, 0.95, 0.85))


func clear_log() -> void:
	_entries.clear()


func _input(event: InputEvent) -> void:
	if event.is_action_pressed("toggle_history"):
		if visible:
			close_log()
		else:
			open_log()
		get_viewport().set_input_as_handled()
