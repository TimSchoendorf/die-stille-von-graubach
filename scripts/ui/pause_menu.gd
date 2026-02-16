extends PanelContainer

## Central pause menu overlay with all game options.

signal resumed
signal save_requested
signal load_requested
signal history_requested
signal journal_requested
signal settings_requested
signal main_menu_requested

var _was_auto_advance: bool = false


func _ready() -> void:
	_setup_ui()
	hide()


func _setup_ui() -> void:
	position = Vector2(0, 0)
	size = Vector2(1920, 1080)

	var style := StyleBoxFlat.new()
	style.bg_color = Color(0.02, 0.02, 0.05, 0.92)
	add_theme_stylebox_override("panel", style)

	var center := CenterContainer.new()
	center.position = Vector2(0, 0)
	center.size = Vector2(1920, 1080)
	add_child(center)

	var vbox := VBoxContainer.new()
	vbox.add_theme_constant_override("separation", UITheme.s(12))
	center.add_child(vbox)

	# Title
	var title := Label.new()
	title.text = Locale.t("PAUSE_TITLE")
	title.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	title.add_theme_font_size_override("font_size", UITheme.s(38))
	title.add_theme_color_override("font_color", UITheme.GOLD)
	title.add_theme_font_override("font", UITheme.font_title())
	vbox.add_child(title)

	vbox.add_child(UITheme.create_ornament_label(UITheme.ORNAMENT_LINE, 16))

	# Add spacer
	var spacer := Control.new()
	spacer.custom_minimum_size.y = UITheme.s(20)
	vbox.add_child(spacer)

	# Menu buttons
	_add_menu_button(vbox, Locale.t("RESUME"), _on_resume)
	_add_menu_button(vbox, Locale.t("SAVE_TITLE"), _on_save)
	_add_menu_button(vbox, Locale.t("LOAD_TITLE"), _on_load)
	_add_menu_button(vbox, Locale.t("HISTORY_TITLE"), _on_history)
	_add_menu_button(vbox, Locale.t("JOURNAL_TITLE"), _on_journal)
	_add_menu_button(vbox, Locale.t("SETTINGS_TITLE"), _on_settings)

	# Spacer before dangerous options
	var spacer2 := Control.new()
	spacer2.custom_minimum_size.y = UITheme.s(10)
	vbox.add_child(spacer2)

	_add_menu_button(vbox, Locale.t("MAIN_MENU"), _on_main_menu)
	_add_menu_button(vbox, Locale.t("QUIT_GAME"), _on_quit)


func _add_menu_button(parent: VBoxContainer, text: String, callback: Callable) -> void:
	var btn := Button.new()
	btn.text = text
	btn.custom_minimum_size = Vector2(UITheme.s(350), UITheme.s(50))
	btn.size_flags_horizontal = Control.SIZE_SHRINK_CENTER
	UITheme.style_menu_button(btn)
	btn.pressed.connect(callback)
	parent.add_child(btn)


func open_pause() -> void:
	# Pause auto-advance and skip
	_was_auto_advance = GameManager.auto_advance
	GameManager.auto_advance = false
	GameManager.skip_mode = false
	# Dampen audio
	AudioManager.set_master_volume(AudioManager.master_volume * 0.3)
	show()


func close_pause() -> void:
	# Restore auto-advance
	GameManager.auto_advance = _was_auto_advance
	# Restore audio
	AudioManager.set_master_volume(AudioManager.master_volume / 0.3)
	hide()
	resumed.emit()


func _on_resume() -> void:
	close_pause()


func _on_save() -> void:
	close_pause()
	save_requested.emit()


func _on_load() -> void:
	close_pause()
	load_requested.emit()


func _on_history() -> void:
	close_pause()
	history_requested.emit()


func _on_journal() -> void:
	close_pause()
	journal_requested.emit()


func _on_settings() -> void:
	close_pause()
	settings_requested.emit()


func _on_main_menu() -> void:
	close_pause()
	AudioManager.stop_music(0.5)
	AudioManager.stop_ambience(0.5)
	SceneManager.change_scene("res://scenes/TitleScreen.tscn")


func _on_quit() -> void:
	get_tree().quit()


func _input(event: InputEvent) -> void:
	if not visible:
		return
	if event.is_action_pressed("ui_cancel") or event.is_action_pressed("toggle_menu"):
		close_pause()
		get_viewport().set_input_as_handled()
