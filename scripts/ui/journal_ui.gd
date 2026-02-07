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

	# Title (serif font, warm gold)
	var title := Label.new()
	title.text = Locale.t("JOURNAL_TITLE")
	title.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	title.add_theme_font_size_override("font_size", 38)
	title.add_theme_color_override("font_color", UITheme.GOLD)
	title.add_theme_font_override("font", UITheme.font_title())
	vbox.add_child(title)

	# Ornament under title
	vbox.add_child(UITheme.create_ornament_label(UITheme.ORNAMENT_WIDE, 18))

	_scroll = ScrollContainer.new()
	_scroll.size_flags_vertical = Control.SIZE_EXPAND_FILL
	vbox.add_child(_scroll)

	_content = VBoxContainer.new()
	_content.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	_content.add_theme_constant_override("separation", 20)
	_scroll.add_child(_content)

	var close_btn := Button.new()
	close_btn.text = Locale.t("CLOSE")
	close_btn.custom_minimum_size = Vector2(200, 45)
	close_btn.size_flags_horizontal = Control.SIZE_SHRINK_CENTER
	UITheme.style_button(close_btn, 22)
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
		empty.text = Locale.t("NO_ENTRIES")
		empty.add_theme_font_size_override("font_size", 22)
		empty.add_theme_color_override("font_color", UITheme.TEXT_DIM)
		empty.add_theme_font_override("font", UITheme.font_body())
		_content.add_child(empty)
		return

	for entry_id in GameManager.journal_entries:
		if entry_id not in _journal_data:
			continue

		var data: Dictionary = _journal_data[entry_id]

		var entry_title := Label.new()
		entry_title.text = data.get("title", entry_id)
		entry_title.add_theme_font_size_override("font_size", 26)
		entry_title.add_theme_color_override("font_color", UITheme.GOLD)
		entry_title.add_theme_font_override("font", UITheme.font_title())
		_content.add_child(entry_title)

		var entry_text := RichTextLabel.new()
		entry_text.bbcode_enabled = true
		entry_text.fit_content = true
		entry_text.scroll_active = false
		entry_text.size_flags_horizontal = Control.SIZE_EXPAND_FILL
		entry_text.add_theme_font_size_override("normal_font_size", 20)
		entry_text.add_theme_font_override("normal_font", UITheme.font_body())
		entry_text.append_text(data.get("content", ""))
		_content.add_child(entry_text)

		# Ornament separator instead of HSeparator
		_content.add_child(UITheme.create_ornament_label(UITheme.ORNAMENT_NARROW, 14))


func _input(event: InputEvent) -> void:
	if visible and (event.is_action_pressed("toggle_menu") or event.is_action_pressed("ui_cancel")):
		close_journal()
		get_viewport().set_input_as_handled()
