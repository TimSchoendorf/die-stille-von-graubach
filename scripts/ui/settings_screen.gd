extends Control

## Settings screen for audio, text speed, display, and language options.
## Settings are persisted to user://settings.json.

const SETTINGS_PATH := "user://settings.json"

var _text_speed_slider: HSlider
var _auto_advance_check: CheckButton
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
	vbox.add_theme_constant_override("separation", 20)
	vbox.custom_minimum_size.x = 600
	center.add_child(vbox)

	# Title
	var title := Label.new()
	title.text = Locale.t("SETTINGS_TITLE")
	title.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	title.add_theme_font_size_override("font_size", 40)
	title.add_theme_color_override("font_color", Color(0.8, 0.75, 0.65))
	vbox.add_child(title)

	# ── Language ──
	_add_section_label(vbox, Locale.t("LANGUAGE"))

	var lang_hbox := HBoxContainer.new()
	lang_hbox.add_theme_constant_override("separation", 16)
	vbox.add_child(lang_hbox)

	var lang_label := Label.new()
	lang_label.text = Locale.t("LANGUAGE")
	lang_label.custom_minimum_size.x = 150
	lang_label.add_theme_font_size_override("font_size", 22)
	lang_label.add_theme_color_override("font_color", Color(0.7, 0.65, 0.6))
	lang_hbox.add_child(lang_label)

	var lang_option := OptionButton.new()
	lang_option.custom_minimum_size = Vector2(250, 36)
	lang_option.add_theme_font_size_override("font_size", 20)
	var current_idx := 0
	for i in Locale.LOCALES.size():
		var code: String = Locale.LOCALES[i]
		lang_option.add_item(Locale.get_locale_display_name(code), i)
		if code == Locale.current_locale:
			current_idx = i
	lang_option.selected = current_idx
	lang_option.item_selected.connect(func(idx: int):
		Locale.set_locale(Locale.LOCALES[idx])
		_save_settings()
		# Rebuild UI with new language
		_setup_ui())
	lang_hbox.add_child(lang_option)

	# ── Audio ──
	_add_section_label(vbox, Locale.t("AUDIO"))

	_create_slider(vbox, Locale.t("MASTER_VOLUME"), AudioManager.master_volume, func(val: float):
		AudioManager.set_master_volume(val)
		_save_settings())

	_create_slider(vbox, Locale.t("MUSIC"), AudioManager.music_volume, func(val: float):
		AudioManager.set_music_volume(val)
		_save_settings())

	_create_slider(vbox, Locale.t("EFFECTS"), AudioManager.sfx_volume, func(val: float):
		AudioManager.set_sfx_volume(val)
		_save_settings())

	_create_slider(vbox, Locale.t("AMBIENCE"), AudioManager.ambience_volume, func(val: float):
		AudioManager.set_ambience_volume(val)
		_save_settings())

	# ── Text ──
	_add_section_label(vbox, Locale.t("TEXT"))

	_text_speed_slider = _create_slider_raw(vbox, Locale.t("TEXT_SPEED"), GameManager.text_speed, 20.0, 80.0, 5.0, func(val: float):
		GameManager.text_speed = val
		_save_settings())

	_auto_advance_check = CheckButton.new()
	_auto_advance_check.text = Locale.t("AUTO_ADVANCE")
	_auto_advance_check.button_pressed = GameManager.auto_advance
	_auto_advance_check.add_theme_font_size_override("font_size", 22)
	_auto_advance_check.add_theme_color_override("font_color", Color(0.7, 0.65, 0.6))
	_auto_advance_check.toggled.connect(func(on: bool):
		GameManager.auto_advance = on
		_save_settings())
	vbox.add_child(_auto_advance_check)

	# ── Display ──
	_add_section_label(vbox, Locale.t("DISPLAY"))

	_fullscreen_check = CheckButton.new()
	_fullscreen_check.text = Locale.t("FULLSCREEN")
	_fullscreen_check.button_pressed = DisplayServer.window_get_mode() == DisplayServer.WINDOW_MODE_FULLSCREEN
	_fullscreen_check.add_theme_font_size_override("font_size", 22)
	_fullscreen_check.add_theme_color_override("font_color", Color(0.7, 0.65, 0.6))
	_fullscreen_check.toggled.connect(func(on: bool):
		if on:
			DisplayServer.window_set_mode(DisplayServer.WINDOW_MODE_FULLSCREEN)
		else:
			DisplayServer.window_set_mode(DisplayServer.WINDOW_MODE_WINDOWED)
		_save_settings())
	vbox.add_child(_fullscreen_check)

	var spacer := Control.new()
	spacer.custom_minimum_size.y = 20
	vbox.add_child(spacer)

	# Back button
	var back_btn := Button.new()
	back_btn.text = Locale.t("BACK")
	back_btn.custom_minimum_size = Vector2(200, 50)
	back_btn.size_flags_horizontal = Control.SIZE_SHRINK_CENTER
	back_btn.add_theme_font_size_override("font_size", 24)
	_style_button(back_btn)
	back_btn.pressed.connect(_on_back)
	vbox.add_child(back_btn)


func _add_section_label(parent: VBoxContainer, text: String) -> void:
	var sep := HSeparator.new()
	sep.add_theme_constant_override("separation", 4)
	parent.add_child(sep)
	var lbl := Label.new()
	lbl.text = text
	lbl.add_theme_font_size_override("font_size", 18)
	lbl.add_theme_color_override("font_color", Color(0.5, 0.45, 0.4))
	parent.add_child(lbl)


func _create_slider(parent: VBoxContainer, label_text: String, initial: float, callback: Callable) -> void:
	_create_slider_raw(parent, label_text, initial, 0.0, 1.0, 0.05, callback)


func _create_slider_raw(parent: VBoxContainer, label_text: String, initial: float, min_val: float, max_val: float, step_val: float, callback: Callable) -> HSlider:
	var hbox := HBoxContainer.new()
	hbox.add_theme_constant_override("separation", 16)
	parent.add_child(hbox)

	var label := Label.new()
	label.text = label_text
	label.custom_minimum_size.x = 150
	label.add_theme_font_size_override("font_size", 22)
	label.add_theme_color_override("font_color", Color(0.7, 0.65, 0.6))
	hbox.add_child(label)

	var slider := HSlider.new()
	slider.min_value = min_val
	slider.max_value = max_val
	slider.step = step_val
	slider.value = initial
	slider.custom_minimum_size = Vector2(350, 30)
	slider.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	slider.value_changed.connect(callback)
	hbox.add_child(slider)

	var val_label := Label.new()
	val_label.custom_minimum_size.x = 60
	val_label.add_theme_font_size_override("font_size", 20)
	val_label.add_theme_color_override("font_color", Color(0.6, 0.55, 0.5))
	hbox.add_child(val_label)

	# Display format depends on range
	var _update_label := func(val: float):
		if max_val <= 1.0:
			val_label.text = str(int(val * 100)) + "%"
		else:
			val_label.text = str(int(val))
	_update_label.call(initial)
	slider.value_changed.connect(_update_label)

	return slider


func _save_settings() -> void:
	var data := {
		"master_volume": AudioManager.master_volume,
		"music_volume": AudioManager.music_volume,
		"sfx_volume": AudioManager.sfx_volume,
		"ambience_volume": AudioManager.ambience_volume,
		"text_speed": GameManager.text_speed,
		"auto_advance": GameManager.auto_advance,
		"fullscreen": DisplayServer.window_get_mode() == DisplayServer.WINDOW_MODE_FULLSCREEN,
		"language": Locale.current_locale,
	}
	var file := FileAccess.open(SETTINGS_PATH, FileAccess.WRITE)
	if file:
		file.store_string(JSON.stringify(data, "\t"))


static func load_settings() -> void:
	if not FileAccess.file_exists(SETTINGS_PATH):
		return
	var file := FileAccess.open(SETTINGS_PATH, FileAccess.READ)
	if not file:
		return
	var json := JSON.new()
	if json.parse(file.get_as_text()) != OK:
		return
	var data: Dictionary = json.data
	AudioManager.set_master_volume(data.get("master_volume", 1.0))
	AudioManager.set_music_volume(data.get("music_volume", 0.8))
	AudioManager.set_sfx_volume(data.get("sfx_volume", 1.0))
	AudioManager.set_ambience_volume(data.get("ambience_volume", 0.6))
	GameManager.text_speed = data.get("text_speed", 40.0)
	GameManager.auto_advance = data.get("auto_advance", false)
	if data.get("fullscreen", false):
		DisplayServer.window_set_mode(DisplayServer.WINDOW_MODE_FULLSCREEN)
	var lang: String = data.get("language", "de")
	Locale.set_locale(lang)


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


func _on_back() -> void:
	SceneManager.change_scene("res://scenes/TitleScreen.tscn")
