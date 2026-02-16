extends PanelContainer

## Scrollable log of past dialogue text with node references.

signal closed

var _scroll: ScrollContainer
var _content: VBoxContainer
var _entries: Array[Dictionary] = [] # {speaker, text, color, file_path, node_id}
var _page_label: Label
var _page_up_btn: Button
var _page_down_btn: Button
var _page_index: int = 0

const MAX_ENTRIES := 500  # Prevent memory bloat on long sessions
const PAGE_SIZE := 22  # Entries per section/page (mobile-friendly)


func _ready() -> void:
	_setup_ui()
	hide()


func _setup_ui() -> void:
	position = Vector2(0, 0)
	size = Vector2(1920, 1080)
	mouse_filter = Control.MOUSE_FILTER_STOP

	var style := StyleBoxFlat.new()
	style.bg_color = Color(0.02, 0.02, 0.05, 0.92)
	add_theme_stylebox_override("panel", style)

	var margin := MarginContainer.new()
	margin.position = Vector2(0, 0)
	margin.size = Vector2(1920, 1080)
	margin.mouse_filter = Control.MOUSE_FILTER_STOP
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

	var pager := HBoxContainer.new()
	pager.alignment = BoxContainer.ALIGNMENT_CENTER
	pager.add_theme_constant_override("separation", UITheme.s(12))
	vbox.add_child(pager)

	_page_up_btn = Button.new()
	_page_up_btn.text = "▲"
	_page_up_btn.custom_minimum_size = Vector2(UITheme.s(64), UITheme.s(44))
	UITheme.style_button(_page_up_btn, 24)
	_page_up_btn.pressed.connect(_on_prev_page)
	pager.add_child(_page_up_btn)

	_page_label = Label.new()
	_page_label.text = "1 / 1"
	_page_label.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	_page_label.custom_minimum_size = Vector2(UITheme.s(180), UITheme.s(40))
	_page_label.add_theme_font_size_override("font_size", UITheme.s(18))
	_page_label.add_theme_color_override("font_color", UITheme.TEXT_DIM)
	pager.add_child(_page_label)

	_page_down_btn = Button.new()
	_page_down_btn.text = "▼"
	_page_down_btn.custom_minimum_size = Vector2(UITheme.s(64), UITheme.s(44))
	UITheme.style_button(_page_down_btn, 24)
	_page_down_btn.pressed.connect(_on_next_page)
	pager.add_child(_page_down_btn)

	_scroll = ScrollContainer.new()
	_scroll.size_flags_vertical = Control.SIZE_EXPAND_FILL
	_scroll.mouse_filter = Control.MOUSE_FILTER_STOP
	_scroll.vertical_scroll_mode = ScrollContainer.SCROLL_MODE_AUTO
	_scroll.horizontal_scroll_mode = ScrollContainer.SCROLL_MODE_DISABLED
	vbox.add_child(_scroll)

	_content = VBoxContainer.new()
	_content.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	_content.add_theme_constant_override("separation", UITheme.s(10))
	_scroll.add_child(_content)

	var close_btn := Button.new()
	close_btn.text = Locale.t("CLOSE")
	close_btn.custom_minimum_size = Vector2(UITheme.s(220), UITheme.s(50))
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
	_page_index = _get_total_pages() - 1
	_rebuild_content()
	show()
	# Always start at top of selected section for consistent mobile touch scroll
	await get_tree().process_frame
	_scroll.scroll_vertical = 0


func close_log() -> void:
	hide()
	closed.emit()


func _rebuild_content() -> void:
	for child in _content.get_children():
		child.queue_free()

	var total_pages := _get_total_pages()
	_page_index = clampi(_page_index, 0, total_pages - 1)
	_page_label.text = "%d / %d" % [_page_index + 1, total_pages]
	_page_up_btn.disabled = _page_index <= 0
	_page_down_btn.disabled = _page_index >= total_pages - 1

	var start_idx := _page_index * PAGE_SIZE
	var end_idx := mini(_entries.size(), start_idx + PAGE_SIZE)

	for i in range(start_idx, end_idx):
		var entry: Dictionary = _entries[i]
		var rtl := RichTextLabel.new()
		rtl.bbcode_enabled = true
		rtl.fit_content = true
		rtl.scroll_active = false
		rtl.size_flags_horizontal = Control.SIZE_EXPAND_FILL
		rtl.add_theme_font_size_override("normal_font_size", UITheme.s(24) if UITheme.is_mobile() else UITheme.s(21))
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


func _get_total_pages() -> int:
	return maxi(1, int(ceil(float(_entries.size()) / float(PAGE_SIZE))))


func _on_prev_page() -> void:
	if _page_index > 0:
		_page_index -= 1
		_rebuild_content()
		_scroll.scroll_vertical = 0


func _on_next_page() -> void:
	if _page_index < _get_total_pages() - 1:
		_page_index += 1
		_rebuild_content()
		_scroll.scroll_vertical = 0


func clear_log() -> void:
	_entries.clear()
	_page_index = 0


func _input(event: InputEvent) -> void:
	if not visible:
		return
	if event.is_action_pressed("toggle_history") or event.is_action_pressed("toggle_menu") or event.is_action_pressed("ui_cancel"):
		close_log()
		get_viewport().set_input_as_handled()
		return
	if event.is_action_pressed("ui_up"):
		_on_prev_page()
		get_viewport().set_input_as_handled()
		return
	if event.is_action_pressed("ui_down"):
		_on_next_page()
		get_viewport().set_input_as_handled()
