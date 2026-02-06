extends Control

## Title screen with main menu options.


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
	vbox.add_theme_constant_override("separation", 20)
	center.add_child(vbox)

	# Title
	var title := Label.new()
	title.text = "Die Stille von Graubach"
	title.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	title.add_theme_font_size_override("font_size", 56)
	title.add_theme_color_override("font_color", Color(0.8, 0.75, 0.65))
	vbox.add_child(title)

	# Subtitle
	var subtitle := Label.new()
	subtitle.text = "Schwarzwald, November 1923"
	subtitle.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	subtitle.add_theme_font_size_override("font_size", 22)
	subtitle.add_theme_color_override("font_color", Color(0.5, 0.45, 0.4))
	vbox.add_child(subtitle)

	# Spacer
	var spacer := Control.new()
	spacer.custom_minimum_size.y = 60
	vbox.add_child(spacer)

	# Buttons
	_create_menu_button(vbox, "Neues Spiel", _on_new_game)
	_create_menu_button(vbox, "Fortsetzen", _on_continue)
	_create_menu_button(vbox, "Einstellungen", _on_settings)
	_create_menu_button(vbox, "Beenden", _on_quit)


func _create_menu_button(parent: VBoxContainer, text: String, callback: Callable) -> Button:
	var btn := Button.new()
	btn.text = text
	btn.custom_minimum_size = Vector2(400, 55)
	btn.size_flags_horizontal = Control.SIZE_SHRINK_CENTER

	var style := StyleBoxFlat.new()
	style.bg_color = Color(0.08, 0.08, 0.12, 0.7)
	style.border_color = Color(0.3, 0.28, 0.25, 0.5)
	style.border_width_bottom = 1
	style.border_width_top = 1
	style.border_width_left = 1
	style.border_width_right = 1
	style.corner_radius_top_left = 2
	style.corner_radius_top_right = 2
	style.corner_radius_bottom_left = 2
	style.corner_radius_bottom_right = 2
	style.content_margin_top = 10
	style.content_margin_bottom = 10
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

	btn.add_theme_font_size_override("font_size", 26)
	btn.add_theme_color_override("font_color", Color(0.8, 0.75, 0.7))
	btn.add_theme_color_override("font_hover_color", Color(1.0, 0.95, 0.85))

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


func _on_settings() -> void:
	SceneManager.change_scene("res://scenes/SettingsScreen.tscn")


func _on_quit() -> void:
	get_tree().quit()
