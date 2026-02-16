class_name SettingsBuilder

## Shared builder for settings UI sections used by both
## settings_screen.gd and settings_overlay.gd.

const SETTINGS_PATH := "user://settings.json"


static func add_section_label(parent: VBoxContainer, text: String) -> void:
	var sep := HSeparator.new()
	sep.add_theme_constant_override("separation", 4)
	parent.add_child(sep)
	var lbl := Label.new()
	lbl.text = text
	lbl.add_theme_font_size_override("font_size", UITheme.s(18))
	lbl.add_theme_color_override("font_color", UITheme.GOLD_DIM)
	parent.add_child(lbl)


static func create_slider(parent: VBoxContainer, label_text: String, initial: float, callback: Callable) -> void:
	create_slider_raw(parent, label_text, initial, 0.0, 1.0, 0.05, callback)


static func create_slider_raw(parent: VBoxContainer, label_text: String, initial: float, min_val: float, max_val: float, step_val: float, callback: Callable) -> HSlider:
	var hbox := HBoxContainer.new()
	hbox.add_theme_constant_override("separation", UITheme.s(16))
	parent.add_child(hbox)

	var label := Label.new()
	label.text = label_text
	label.custom_minimum_size.x = UITheme.s(150)
	label.add_theme_font_size_override("font_size", UITheme.s(22))
	label.add_theme_color_override("font_color", UITheme.TEXT_LIGHT)
	hbox.add_child(label)

	var slider := HSlider.new()
	slider.min_value = min_val
	slider.max_value = max_val
	slider.step = step_val
	slider.value = initial
	slider.custom_minimum_size = Vector2(UITheme.s(350), UITheme.s(30))
	slider.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	slider.value_changed.connect(callback)
	hbox.add_child(slider)

	var val_label := Label.new()
	val_label.custom_minimum_size.x = UITheme.s(60)
	val_label.add_theme_font_size_override("font_size", UITheme.s(20))
	val_label.add_theme_color_override("font_color", UITheme.TEXT_DIM)
	hbox.add_child(val_label)

	var _update_label := func(val: float):
		if max_val <= 1.0:
			val_label.text = str(int(val * 100)) + "%"
		else:
			val_label.text = str(int(val))
	_update_label.call(initial)
	slider.value_changed.connect(_update_label)

	return slider


static func build_language_section(parent: VBoxContainer, on_change: Callable) -> void:
	add_section_label(parent, Locale.t("LANGUAGE"))

	var lang_hbox := HBoxContainer.new()
	lang_hbox.add_theme_constant_override("separation", 16)
	parent.add_child(lang_hbox)

	var lang_label := Label.new()
	lang_label.text = Locale.t("LANGUAGE")
	lang_label.custom_minimum_size.x = UITheme.s(150)
	lang_label.add_theme_font_size_override("font_size", UITheme.s(22))
	lang_label.add_theme_color_override("font_color", UITheme.TEXT_LIGHT)
	lang_hbox.add_child(lang_label)

	var lang_option := OptionButton.new()
	lang_option.custom_minimum_size = Vector2(UITheme.s(250), UITheme.s(36))
	lang_option.add_theme_font_size_override("font_size", UITheme.s(20))
	var current_idx := 0
	for i in Locale.LOCALES.size():
		var code: String = Locale.LOCALES[i]
		lang_option.add_item(Locale.get_locale_display_name(code), i)
		if code == Locale.current_locale:
			current_idx = i
	lang_option.selected = current_idx
	lang_option.item_selected.connect(func(idx: int):
		Locale.set_locale(Locale.LOCALES[idx])
		save_settings()
		on_change.call())
	lang_hbox.add_child(lang_option)


static func build_audio_section(parent: VBoxContainer, on_save: Callable) -> void:
	add_section_label(parent, Locale.t("AUDIO"))

	create_slider(parent, Locale.t("MASTER_VOLUME"), AudioManager.master_volume, func(val: float):
		AudioManager.set_master_volume(val)
		on_save.call())

	create_slider(parent, Locale.t("MUSIC"), AudioManager.music_volume, func(val: float):
		AudioManager.set_music_volume(val)
		on_save.call())

	create_slider(parent, Locale.t("EFFECTS"), AudioManager.sfx_volume, func(val: float):
		AudioManager.set_sfx_volume(val)
		on_save.call())

	create_slider(parent, Locale.t("AMBIENCE"), AudioManager.ambience_volume, func(val: float):
		AudioManager.set_ambience_volume(val)
		on_save.call())


## Builds text section. Returns Dictionary with "text_speed_slider".
static func build_text_section(parent: VBoxContainer, on_save: Callable) -> Dictionary:
	add_section_label(parent, Locale.t("TEXT"))

	var text_speed_slider := create_slider_raw(parent, Locale.t("TEXT_SPEED"), GameManager.text_speed, 20.0, 80.0, 5.0, func(val: float):
		GameManager.text_speed = val
		on_save.call())

	create_slider_raw(parent, Locale.t("FONT_SIZE"), GameManager.font_size, 18.0, 36.0, 2.0, func(val: float):
		GameManager.font_size = int(val)
		on_save.call())

	create_slider_raw(parent, Locale.t("AUTO_SPEED"), GameManager.auto_advance_speed, 0.5, 3.0, 0.25, func(val: float):
		GameManager.auto_advance_speed = val
		on_save.call())

	add_section_label(parent, Locale.t("DISPLAY"))

	create_slider(parent, Locale.t("TEXTBOX_OPACITY"), GameManager.textbox_opacity, func(val: float):
		GameManager.textbox_opacity = val
		on_save.call())

	return {"text_speed_slider": text_speed_slider}


## Builds display section. Returns Dictionary with "fullscreen_check".
static func build_display_section(parent: VBoxContainer, on_save: Callable) -> Dictionary:
	add_section_label(parent, Locale.t("DISPLAY"))

	var fullscreen_check := CheckButton.new()
	fullscreen_check.text = Locale.t("FULLSCREEN")
	fullscreen_check.button_pressed = DisplayServer.window_get_mode() == DisplayServer.WINDOW_MODE_FULLSCREEN
	fullscreen_check.add_theme_font_size_override("font_size", UITheme.s(22))
	fullscreen_check.add_theme_color_override("font_color", UITheme.TEXT_LIGHT)
	fullscreen_check.toggled.connect(func(on: bool):
		if on:
			DisplayServer.window_set_mode(DisplayServer.WINDOW_MODE_FULLSCREEN)
		else:
			DisplayServer.window_set_mode(DisplayServer.WINDOW_MODE_WINDOWED)
		on_save.call())
	parent.add_child(fullscreen_check)

	return {"fullscreen_check": fullscreen_check}


static func save_settings() -> void:
	var data := {
		"master_volume": AudioManager.master_volume,
		"music_volume": AudioManager.music_volume,
		"sfx_volume": AudioManager.sfx_volume,
		"ambience_volume": AudioManager.ambience_volume,
		"text_speed": GameManager.text_speed,
		"font_size": GameManager.font_size,
		"auto_advance": GameManager.auto_advance,
		"auto_advance_speed": GameManager.auto_advance_speed,
		"textbox_opacity": GameManager.textbox_opacity,
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
	GameManager.font_size = int(data.get("font_size", 24))
	GameManager.auto_advance = data.get("auto_advance", false)
	GameManager.auto_advance_speed = data.get("auto_advance_speed", 1.0)
	GameManager.textbox_opacity = data.get("textbox_opacity", 0.88)
	if data.get("fullscreen", false):
		DisplayServer.window_set_mode(DisplayServer.WINDOW_MODE_FULLSCREEN)
	var lang: String = data.get("language", "de")
	Locale.set_locale(lang)
