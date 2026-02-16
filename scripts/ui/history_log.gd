extends PanelContainer

## Scrollable log of past dialogue text with node references.

signal closed

var _scroll: ScrollContainer
var _content: VBoxContainer
var _entries: Array[Dictionary] = [] # {speaker, text, color, file_path, node_id}

const MAX_ENTRIES := 500  # Prevent memory bloat on long sessions
const RENDER_BATCH := 100  # Only render last N entries for performance


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
	margin.add_theme_constant_override("margin_left", UITheme.margin_h())
	margin.add_theme_constant_override("margin_right", UITheme.margin_h())
	margin.add_theme_constant_override("margin_top", UITheme.margin_v())
	margin.add_theme_constant_override("margin_bottom", UITheme.margin_v())
	add_child(margin)

	var vbox := VBoxContainer.new()
	vbox.add_theme_constant_override("separation", 8)
	margin.add_child(vbox)

	# Title (serif font)
	var title := Label.new()
	title.text = Locale.t("HISTORY_TITLE")
	title.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	title.add_theme_font_size_override("font_size", UITheme.s(34))
	title.add_theme_color_override("font_color", UITheme.GOLD)
	title.add_theme_font_override("font", UITheme.font_title())
	vbox.add_child(title)

	# Ornament under title
	vbox.add_child(UITheme.create_ornament_label(UITheme.ORNAMENT_LINE, 16))

	_scroll = ScrollContainer.new()
	_scroll.size_flags_vertical = Control.SIZE_EXPAND_FILL
	vbox.add_child(_scroll)

	_content = VBoxContainer.new()
	_content.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	_content.add_theme_constant_override("separation", 12)
	_scroll.add_child(_content)

	var close_btn := Button.new()
	close_btn.text = Locale.t("CLOSE")
	close_btn.custom_minimum_size = Vector2(UITheme.s(200), UITheme.s(45))
	close_btn.size_flags_horizontal = Control.SIZE_SHRINK_CENTER
	UITheme.style_button(close_btn, 22)
	close_btn.pressed.connect(close_log)
	vbox.add_child(close_btn)


func add_entry(speaker: String, text: String, color: Color = Color.WHITE, file_path: String = "", node_id: String = "") -> void:
	_entries.append({
		"speaker": speaker,
		"text": text,
		"color": color,
		"file_path": file_path,
		"node_id": node_id,
	})
	# Trim oldest entries to prevent memory bloat
	if _entries.size() > MAX_ENTRIES:
		_entries = _entries.slice(_entries.size() - MAX_ENTRIES)


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

	# Only render last RENDER_BATCH entries for performance
	var start_idx := maxi(0, _entries.size() - RENDER_BATCH)

	# Show "earlier entries" hint if truncated
	if start_idx > 0:
		var hint := Label.new()
		hint.text = "... (%d)" % start_idx
		hint.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
		hint.add_theme_font_size_override("font_size", UITheme.s(16))
		hint.add_theme_color_override("font_color", UITheme.TEXT_DIM)
		_content.add_child(hint)

	for i in range(start_idx, _entries.size()):
		var entry: Dictionary = _entries[i]
		var rtl := RichTextLabel.new()
		rtl.bbcode_enabled = true
		rtl.fit_content = true
		rtl.scroll_active = false
		rtl.size_flags_horizontal = Control.SIZE_EXPAND_FILL
		rtl.add_theme_font_size_override("normal_font_size", UITheme.s(20))
		rtl.add_theme_font_override("normal_font", UITheme.font_body())

		var speaker: String = entry["speaker"]
		var text: String = entry["text"]
		var color: Color = entry["color"]

		if not speaker.is_empty():
			var hex := color.to_html(false)
			rtl.append_text("[color=#%s]%s:[/color] %s" % [hex, speaker, text])
		else:
			rtl.append_text("[i]%s[/i]" % text)

		_content.add_child(rtl)


func clear_log() -> void:
	_entries.clear()


func _input(event: InputEvent) -> void:
	if not visible:
		return
	if event.is_action_pressed("toggle_history") or event.is_action_pressed("toggle_menu") or event.is_action_pressed("ui_cancel"):
		close_log()
		get_viewport().set_input_as_handled()
