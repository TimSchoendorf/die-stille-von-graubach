extends Control

## Credits screen showing attributions for tools and assets used in the project.


func _ready() -> void:
	_setup_ui()


func _setup_ui() -> void:
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
	vbox.add_theme_constant_override("separation", UITheme.s(12))
	vbox.custom_minimum_size.x = mini(UITheme.s(700), 1800)
	center.add_child(vbox)

	# Title
	var title := Label.new()
	title.text = Locale.t("CREDITS_TITLE")
	title.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	title.add_theme_font_size_override("font_size", UITheme.s(40))
	title.add_theme_color_override("font_color", UITheme.GOLD)
	title.add_theme_font_override("font", UITheme.font_title())
	vbox.add_child(title)

	vbox.add_child(UITheme.create_ornament_label(UITheme.ORNAMENT_WIDE, 18))

	_add_spacer(vbox, 10)

	# ── Game Engine ──
	_add_section(vbox, Locale.t("CREDITS_ENGINE"))
	_add_entry(vbox, "Godot Engine 4.5", "MIT License — godotengine.org")

	# ── Image Generation ──
	_add_section(vbox, Locale.t("CREDITS_GRAPHICS"))
	_add_entry(vbox, "Stable Diffusion WebUI Forge", Locale.t("CREDITS_SD_DESC"))
	_add_entry(vbox, "Animagine XL 3.1", Locale.t("CREDITS_ANIMAGINE_DESC"))
	_add_entry(vbox, "juggernautXL", Locale.t("CREDITS_JUGGER_DESC"))
	_add_entry(vbox, "rembg (isnet-anime)", Locale.t("CREDITS_REMBG_DESC"))

	# ── Audio ──
	_add_section(vbox, Locale.t("CREDITS_AUDIO"))
	_add_entry(vbox, "AudioCraft by Meta", Locale.t("CREDITS_AUDIOCRAFT_DESC"))

	# ── Programming & Tools ──
	_add_section(vbox, Locale.t("CREDITS_TOOLS"))
	_add_entry(vbox, "Python 3.11", Locale.t("CREDITS_PYTHON_DESC"))
	_add_entry(vbox, "scipy / numpy", Locale.t("CREDITS_SCIPY_DESC"))

	# ── Fonts ──
	_add_section(vbox, Locale.t("CREDITS_FONTS"))
	_add_entry(vbox, "Palatino Linotype, Georgia, Segoe UI", Locale.t("CREDITS_FONTS_DESC"))

	# ── Created by ──
	_add_section(vbox, Locale.t("CREDITS_CREATED_BY"))
	var creator_lbl := Label.new()
	creator_lbl.text = "Tim — Cinder & Soul"
	creator_lbl.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	creator_lbl.add_theme_font_size_override("font_size", UITheme.s(22))
	creator_lbl.add_theme_color_override("font_color", UITheme.GOLD_LIGHT)
	creator_lbl.add_theme_font_override("font", UITheme.font_title())
	vbox.add_child(creator_lbl)

	_add_spacer(vbox, 10)
	vbox.add_child(UITheme.create_ornament_label(UITheme.ORNAMENT_LINE, 16))
	_add_spacer(vbox, 10)

	# Back button
	var back_btn := Button.new()
	back_btn.text = Locale.t("BACK")
	back_btn.custom_minimum_size = Vector2(UITheme.s(200), UITheme.s(50))
	back_btn.size_flags_horizontal = Control.SIZE_SHRINK_CENTER
	UITheme.style_button(back_btn, 24)
	back_btn.pressed.connect(_on_back)
	vbox.add_child(back_btn)

	_add_spacer(vbox, 20)


func _add_section(parent: VBoxContainer, text: String) -> void:
	var sep := HSeparator.new()
	sep.add_theme_constant_override("separation", 4)
	parent.add_child(sep)

	var lbl := Label.new()
	lbl.text = text
	lbl.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	lbl.add_theme_font_size_override("font_size", UITheme.s(22))
	lbl.add_theme_color_override("font_color", UITheme.GOLD)
	lbl.add_theme_font_override("font", UITheme.font_title())
	parent.add_child(lbl)


func _add_entry(parent: VBoxContainer, title_text: String, desc_text: String) -> void:
	var title_lbl := Label.new()
	title_lbl.text = title_text
	title_lbl.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	title_lbl.add_theme_font_size_override("font_size", UITheme.s(19))
	title_lbl.add_theme_color_override("font_color", UITheme.TEXT_LIGHT)
	title_lbl.add_theme_font_override("font", UITheme.font_body())
	parent.add_child(title_lbl)

	var desc_lbl := Label.new()
	desc_lbl.text = desc_text
	desc_lbl.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	desc_lbl.add_theme_font_size_override("font_size", UITheme.s(16))
	desc_lbl.add_theme_color_override("font_color", UITheme.TEXT_DIM)
	desc_lbl.add_theme_font_override("font", UITheme.font_ui())
	desc_lbl.autowrap_mode = TextServer.AUTOWRAP_WORD_SMART
	parent.add_child(desc_lbl)


func _add_spacer(parent: VBoxContainer, height: float) -> void:
	var spacer := Control.new()
	spacer.custom_minimum_size.y = height
	parent.add_child(spacer)


func _on_back() -> void:
	SceneManager.change_scene("res://scenes/TitleScreen.tscn")


func _input(event: InputEvent) -> void:
	if event.is_action_pressed("ui_cancel"):
		_on_back()
