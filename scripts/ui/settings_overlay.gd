extends PanelContainer

## In-game settings overlay with audio, text, and display options.

const SB := preload("res://scripts/ui/settings_builder.gd")

signal closed

var _text_speed_slider: HSlider
var _auto_advance_check: CheckButton
var _fullscreen_check: CheckButton
var _content_vbox: VBoxContainer


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

	var outer_vbox := VBoxContainer.new()
	outer_vbox.add_theme_constant_override("separation", 8)
	margin.add_child(outer_vbox)

	# Title
	var title := Label.new()
	title.text = Locale.t("SETTINGS_TITLE")
	title.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	title.add_theme_font_size_override("font_size", UITheme.s(34))
	title.add_theme_color_override("font_color", UITheme.GOLD)
	title.add_theme_font_override("font", UITheme.font_title())
	outer_vbox.add_child(title)

	outer_vbox.add_child(UITheme.create_ornament_label(UITheme.ORNAMENT_LINE, 16))

	var scroll := ScrollContainer.new()
	scroll.size_flags_vertical = Control.SIZE_EXPAND_FILL
	outer_vbox.add_child(scroll)

	_content_vbox = VBoxContainer.new()
	_content_vbox.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	_content_vbox.add_theme_constant_override("separation", 16)
	scroll.add_child(_content_vbox)

	_build_settings()

	# Close button
	var close_btn := Button.new()
	close_btn.text = Locale.t("CLOSE")
	close_btn.custom_minimum_size = Vector2(UITheme.s(200), UITheme.s(45))
	close_btn.size_flags_horizontal = Control.SIZE_SHRINK_CENTER
	UITheme.style_button(close_btn, 22)
	close_btn.pressed.connect(close_settings)
	outer_vbox.add_child(close_btn)


func _build_settings() -> void:
	var on_save := SB.save_settings

	SB.build_language_section(_content_vbox, _rebuild)
	SB.build_audio_section(_content_vbox, on_save)

	var text_refs := SB.build_text_section(_content_vbox, on_save)
	_text_speed_slider = text_refs["text_speed_slider"]
	_auto_advance_check = text_refs["auto_advance_check"]

	var display_refs := SB.build_display_section(_content_vbox, on_save)
	_fullscreen_check = display_refs["fullscreen_check"]


func _rebuild() -> void:
	for child in _content_vbox.get_children():
		child.queue_free()
	await get_tree().process_frame
	_build_settings()


func open_settings() -> void:
	show()


func close_settings() -> void:
	hide()
	closed.emit()


func _input(event: InputEvent) -> void:
	if not visible:
		return
	if event.is_action_pressed("ui_cancel"):
		close_settings()
		get_viewport().set_input_as_handled()
