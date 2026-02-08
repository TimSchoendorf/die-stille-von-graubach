extends PanelContainer

## In-game settings overlay with audio, text, and display options.

signal closed

const SETTINGS_PATH := "user://settings.json"

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
	# ── Language ──
	_add_section_label(_content_vbox, Locale.t("LANGUAGE"))

	var lang_hbox := HBoxContainer.new()
	lang_hbox.add_theme_constant_override("separation", 16)
	_content_vbox.add_child(lang_hbox)

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
		_save_settings()
		# Rebuild overlay UI with new language
		_rebuild())
	lang_hbox.add_child(lang_option)

	# ── Audio ──
	_add_section_label(_content_vbox, Locale.t("AUDIO"))

	_create_slider(_content_vbox, Locale.t("MASTER_VOLUME"), AudioManager.master_volume, func(val: float):
		AudioManager.set_master_volume(val)
		_save_settings())

	_create_slider(_content_vbox, Locale.t("MUSIC"), AudioManager.music_volume, func(val: float):
		AudioManager.set_music_volume(val)
		_save_settings())

	_create_slider(_content_vbox, Locale.t("EFFECTS"), AudioManager.sfx_volume, func(val: float):
		AudioManager.set_sfx_volume(val)
		_save_settings())

	_create_slider(_content_vbox, Locale.t("AMBIENCE"), AudioManager.ambience_volume, func(val: float):
		AudioManager.set_ambience_volume(val)
		_save_settings())

	# ── Text ──
	_add_section_label(_content_vbox, Locale.t("TEXT"))

	_text_speed_slider = _create_slider_raw(_content_vbox, Locale.t("TEXT_SPEED"), GameManager.text_speed, 20.0, 80.0, 5.0, func(val: float):
		GameManager.text_speed = val
		_save_settings())

	_create_slider_raw(_content_vbox, Locale.t("FONT_SIZE"), GameManager.font_size, 18.0, 36.0, 2.0, func(val: float):
		GameManager.font_size = int(val)
		_save_settings())

	_auto_advance_check = CheckButton.new()
	_auto_advance_check.text = Locale.t("AUTO_ADVANCE")
	_auto_advance_check.button_pressed = GameManager.auto_advance
	_auto_advance_check.add_theme_font_size_override("font_size", UITheme.s(22))
	_auto_advance_check.add_theme_color_override("font_color", UITheme.TEXT_LIGHT)
	_auto_advance_check.toggled.connect(func(on: bool):
		GameManager.auto_advance = on
		_save_settings())
	_content_vbox.add_child(_auto_advance_check)

	# ── Display ──
	_add_section_label(_content_vbox, Locale.t("DISPLAY"))

	_fullscreen_check = CheckButton.new()
	_fullscreen_check.text = Locale.t("FULLSCREEN")
	_fullscreen_check.button_pressed = DisplayServer.window_get_mode() == DisplayServer.WINDOW_MODE_FULLSCREEN
	_fullscreen_check.add_theme_font_size_override("font_size", UITheme.s(22))
	_fullscreen_check.add_theme_color_override("font_color", UITheme.TEXT_LIGHT)
	_fullscreen_check.toggled.connect(func(on: bool):
		if on:
			DisplayServer.window_set_mode(DisplayServer.WINDOW_MODE_FULLSCREEN)
		else:
			DisplayServer.window_set_mode(DisplayServer.WINDOW_MODE_WINDOWED)
		_save_settings())
	_content_vbox.add_child(_fullscreen_check)


func _rebuild() -> void:
	for child in _content_vbox.get_children():
		child.queue_free()
	await get_tree().process_frame
	_build_settings()


func _add_section_label(parent: VBoxContainer, text: String) -> void:
	var sep := HSeparator.new()
	sep.add_theme_constant_override("separation", 4)
	parent.add_child(sep)
	var lbl := Label.new()
	lbl.text = text
	lbl.add_theme_font_size_override("font_size", UITheme.s(18))
	lbl.add_theme_color_override("font_color", UITheme.GOLD_DIM)
	parent.add_child(lbl)


func _create_slider(parent: VBoxContainer, label_text: String, initial: float, callback: Callable) -> void:
	_create_slider_raw(parent, label_text, initial, 0.0, 1.0, 0.05, callback)


func _create_slider_raw(parent: VBoxContainer, label_text: String, initial: float, min_val: float, max_val: float, step_val: float, callback: Callable) -> HSlider:
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


func _save_settings() -> void:
	var data := {
		"master_volume": AudioManager.master_volume,
		"music_volume": AudioManager.music_volume,
		"sfx_volume": AudioManager.sfx_volume,
		"ambience_volume": AudioManager.ambience_volume,
		"text_speed": GameManager.text_speed,
		"font_size": GameManager.font_size,
		"auto_advance": GameManager.auto_advance,
		"fullscreen": DisplayServer.window_get_mode() == DisplayServer.WINDOW_MODE_FULLSCREEN,
		"language": Locale.current_locale,
	}
	var file := FileAccess.open(SETTINGS_PATH, FileAccess.WRITE)
	if file:
		file.store_string(JSON.stringify(data, "\t"))


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
