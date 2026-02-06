extends PanelContainer

## Journal/diary overlay showing collected entries.

signal closed

var _content: VBoxContainer
var _scroll: ScrollContainer

# Journal data: entry_id → {title, content}
var _journal_data: Dictionary = {}


func _ready() -> void:
	_setup_ui()
	hide()


func _setup_ui() -> void:
	position = Vector2(0, 0)
	size = Vector2(1920, 1080)

	var style := StyleBoxFlat.new()
	style.bg_color = Color(0.05, 0.04, 0.03, 0.95)
	add_theme_stylebox_override("panel", style)

	var margin := MarginContainer.new()
	margin.position = Vector2(0, 0)
	margin.size = Vector2(1920, 1080)
	margin.add_theme_constant_override("margin_left", 250)
	margin.add_theme_constant_override("margin_right", 250)
	margin.add_theme_constant_override("margin_top", 80)
	margin.add_theme_constant_override("margin_bottom", 80)
	add_child(margin)

	var vbox := VBoxContainer.new()
	vbox.add_theme_constant_override("separation", 16)
	margin.add_child(vbox)

	var title := Label.new()
	title.text = "Tagebuch"
	title.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	title.add_theme_font_size_override("font_size", 36)
	title.add_theme_color_override("font_color", Color(0.7, 0.6, 0.45))
	vbox.add_child(title)

	_scroll = ScrollContainer.new()
	_scroll.size_flags_vertical = Control.SIZE_EXPAND_FILL
	vbox.add_child(_scroll)

	_content = VBoxContainer.new()
	_content.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	_content.add_theme_constant_override("separation", 20)
	_scroll.add_child(_content)

	var close_btn := Button.new()
	close_btn.text = "Schließen"
	close_btn.custom_minimum_size = Vector2(200, 45)
	close_btn.size_flags_horizontal = Control.SIZE_SHRINK_CENTER
	close_btn.add_theme_font_size_override("font_size", 22)
	_style_button(close_btn)
	close_btn.pressed.connect(close_journal)
	vbox.add_child(close_btn)


func add_entry(entry_id: String, title: String, content: String) -> void:
	_journal_data[entry_id] = {"title": title, "content": content}


func open_journal() -> void:
	_rebuild_content()
	show()


func close_journal() -> void:
	hide()
	closed.emit()


func _rebuild_content() -> void:
	for child in _content.get_children():
		child.queue_free()

	if GameManager.journal_entries.is_empty():
		var empty := Label.new()
		empty.text = "Noch keine Einträge."
		empty.add_theme_font_size_override("font_size", 22)
		empty.add_theme_color_override("font_color", Color(0.5, 0.45, 0.4))
		_content.add_child(empty)
		return

	for entry_id in GameManager.journal_entries:
		if entry_id not in _journal_data:
			continue

		var data: Dictionary = _journal_data[entry_id]

		var entry_title := Label.new()
		entry_title.text = data.get("title", entry_id)
		entry_title.add_theme_font_size_override("font_size", 26)
		entry_title.add_theme_color_override("font_color", Color(0.8, 0.7, 0.55))
		_content.add_child(entry_title)

		var entry_text := RichTextLabel.new()
		entry_text.bbcode_enabled = true
		entry_text.fit_content = true
		entry_text.scroll_active = false
		entry_text.size_flags_horizontal = Control.SIZE_EXPAND_FILL
		entry_text.add_theme_font_size_override("normal_font_size", 20)
		entry_text.append_text(data.get("content", ""))
		_content.add_child(entry_text)

		var sep := HSeparator.new()
		sep.add_theme_constant_override("separation", 8)
		_content.add_child(sep)


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


func _input(event: InputEvent) -> void:
	if visible and event.is_action_pressed("toggle_menu"):
		close_journal()
		get_viewport().set_input_as_handled()
