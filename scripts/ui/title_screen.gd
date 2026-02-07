extends Control

## Title screen with main menu options.

var _continue_btn: Button
var _save_load_ui: Node


func _ready() -> void:
	_setup_ui()
	AudioManager.play_music("main_theme.wav")


func _setup_ui() -> void:
	# Background image
	var bg_tex_path := "res://assets/sprites/backgrounds/title_screen.png"
	if ResourceLoader.exists(bg_tex_path):
		var bg_img := TextureRect.new()
		bg_img.texture = load(bg_tex_path)
		bg_img.stretch_mode = TextureRect.STRETCH_KEEP_ASPECT_COVERED
		bg_img.position = Vector2(0, 0)
		bg_img.size = Vector2(1920, 1080)
		bg_img.mouse_filter = Control.MOUSE_FILTER_IGNORE
		add_child(bg_img)

		# Dark overlay for text readability
		var overlay := ColorRect.new()
		overlay.color = Color(0.0, 0.0, 0.02, 0.45)
		overlay.position = Vector2(0, 0)
		overlay.size = Vector2(1920, 1080)
		overlay.mouse_filter = Control.MOUSE_FILTER_IGNORE
		add_child(overlay)
	else:
		# Fallback: solid dark background
		var bg := ColorRect.new()
		bg.color = Color(0.02, 0.02, 0.05)
		bg.set_anchors_preset(PRESET_FULL_RECT)
		add_child(bg)

	# Center container
	var center := CenterContainer.new()
	center.set_anchors_preset(PRESET_FULL_RECT)
	add_child(center)

	var vbox := VBoxContainer.new()
	vbox.alignment = BoxContainer.ALIGNMENT_CENTER
	vbox.add_theme_constant_override("separation", 16)
	center.add_child(vbox)

	# Title
	var title := Label.new()
	title.text = Locale.t("TITLE")
	title.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	title.add_theme_font_size_override("font_size", 64)
	title.add_theme_color_override("font_color", UITheme.GOLD)
	title.add_theme_font_override("font", UITheme.font_title())
	vbox.add_child(title)

	# Subtitle
	var subtitle := Label.new()
	subtitle.text = Locale.t("TITLE_SUBTITLE")
	subtitle.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	subtitle.add_theme_font_size_override("font_size", 22)
	subtitle.add_theme_color_override("font_color", UITheme.TEXT_DIM)
	subtitle.add_theme_font_override("font", UITheme.font_body())
	vbox.add_child(subtitle)

	# Ornament divider
	vbox.add_child(UITheme.create_ornament_label(UITheme.ORNAMENT_WIDE, 20))

	# Spacer
	var spacer := Control.new()
	spacer.custom_minimum_size.y = 40
	vbox.add_child(spacer)

	# Buttons
	_create_menu_button(vbox, Locale.t("NEW_GAME"), _on_new_game)
	_continue_btn = _create_menu_button(vbox, Locale.t("CONTINUE"), _on_continue)
	_create_menu_button(vbox, Locale.t("LOAD"), _on_load)
	_create_menu_button(vbox, Locale.t("SETTINGS"), _on_settings)
	_create_menu_button(vbox, Locale.t("QUIT"), _on_quit)

	# Disable "Fortsetzen" if no quick save exists
	if not SaveManager.has_save(0):
		_continue_btn.disabled = true
		_continue_btn.add_theme_color_override("font_color", Color(0.4, 0.38, 0.35, 0.5))

	# Save/Load overlay for manual saves
	var overlay_layer := CanvasLayer.new()
	overlay_layer.layer = 20
	add_child(overlay_layer)

	_save_load_ui = preload("res://scripts/ui/save_load_ui.gd").new()
	_save_load_ui.name = "SaveLoadUI"
	overlay_layer.add_child(_save_load_ui)

	# Stop music when a save is loaded from this screen
	SaveManager.load_completed.connect(_on_save_loaded)


func _create_menu_button(parent: VBoxContainer, text: String, callback: Callable) -> Button:
	var btn := Button.new()
	btn.text = text
	btn.custom_minimum_size = Vector2(450, 58)
	btn.size_flags_horizontal = Control.SIZE_SHRINK_CENTER
	UITheme.style_menu_button(btn, 26)
	btn.pressed.connect(callback)
	parent.add_child(btn)
	return btn


func _on_new_game() -> void:
	AudioManager.stop_music(1.5)
	GameManager.start_new_game()
	SceneManager.change_scene("res://scenes/GameScene.tscn")


func _on_continue() -> void:
	if SaveManager.has_save(0):
		AudioManager.stop_music(1.5)
		SaveManager.load_game(0)
		SceneManager.change_scene("res://scenes/GameScene.tscn")


func _on_load() -> void:
	var has_any_save := false
	for i in range(SaveManager.MAX_SLOTS):
		if SaveManager.has_save(i):
			has_any_save = true
			break
	if has_any_save:
		_save_load_ui.open_load()


func _on_save_loaded(_slot: int) -> void:
	AudioManager.stop_music(1.5)


func _on_settings() -> void:
	SceneManager.change_scene("res://scenes/SettingsScreen.tscn")


func _on_quit() -> void:
	get_tree().quit()


func _input(event: InputEvent) -> void:
	if event.is_action_pressed("ui_cancel"):
		get_tree().quit()
