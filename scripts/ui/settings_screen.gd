extends Control

## Settings screen (full-page) for audio, text speed, display, and language options.

const SB := preload("res://scripts/ui/settings_builder.gd")

var _text_speed_slider: HSlider
var _fullscreen_check: CheckButton


func _ready() -> void:
	_setup_ui()


func _setup_ui() -> void:
	# Clear all children (needed for language-switch rebuild)
	for child in get_children():
		child.queue_free()

	var bg := ColorRect.new()
	bg.color = Color(0.02, 0.02, 0.05)
	bg.set_anchors_preset(PRESET_FULL_RECT)
	add_child(bg)

	var scroll := ScrollContainer.new()
	scroll.set_anchors_preset(PRESET_FULL_RECT)
	add_child(scroll)

	var center := CenterContainer.new()
	center.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	center.size_flags_vertical = Control.SIZE_EXPAND_FILL
	scroll.add_child(center)

	var vbox := VBoxContainer.new()
	vbox.alignment = BoxContainer.ALIGNMENT_CENTER
	vbox.add_theme_constant_override("separation", UITheme.s(20))
	vbox.custom_minimum_size.x = UITheme.s(600)
	center.add_child(vbox)

	# Title
	var title := Label.new()
	title.text = Locale.t("SETTINGS_TITLE")
	title.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	title.add_theme_font_size_override("font_size", UITheme.s(40))
	title.add_theme_color_override("font_color", Color(0.8, 0.75, 0.65))
	vbox.add_child(title)

	# Sections via shared builder
	SB.build_language_section(vbox, _setup_ui)
	SB.build_audio_section(vbox, SB.save_settings)

	var text_refs := SB.build_text_section(vbox, SB.save_settings)
	_text_speed_slider = text_refs["text_speed_slider"]

	var display_refs := SB.build_display_section(vbox, SB.save_settings)
	_fullscreen_check = display_refs["fullscreen_check"]

	var spacer := Control.new()
	spacer.custom_minimum_size.y = 20
	vbox.add_child(spacer)

	# Back button
	var back_btn := Button.new()
	back_btn.text = Locale.t("BACK")
	back_btn.custom_minimum_size = Vector2(UITheme.s(200), UITheme.s(50))
	back_btn.size_flags_horizontal = Control.SIZE_SHRINK_CENTER
	back_btn.add_theme_font_size_override("font_size", UITheme.s(24))
	UITheme.style_button(back_btn, 24)
	back_btn.pressed.connect(_on_back)
	vbox.add_child(back_btn)


func _on_back() -> void:
	SceneManager.change_scene("res://scenes/TitleScreen.tscn")
