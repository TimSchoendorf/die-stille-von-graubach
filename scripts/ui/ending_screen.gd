extends Control

## Displayed after reaching an ending. Shows ending name and completion status.

const ENDING_KEYS: Dictionary = {
	"seal": "SEAL",
	"escape": "ESCAPE",
	"pact": "PACT",
	"awakening": "AWAKENING",
	"truth": "TRUTH",
	"sacrifice": "SACRIFICE",
}


func _ready() -> void:
	hide()


func show_ending(ending_id: String) -> void:
	# Record ending as unlocked
	if ending_id not in GameManager.endings_unlocked:
		GameManager.endings_unlocked.append(ending_id)

	_build_ending_screen(ending_id)
	show()

	# Fade-in animation
	modulate.a = 0.0
	var tween := create_tween()
	tween.tween_property(self, "modulate:a", 1.0, 1.5).set_ease(Tween.EASE_OUT)


func _build_ending_screen(ending_id: String) -> void:
	# Clear previous
	for child in get_children():
		child.queue_free()

	var bg := ColorRect.new()
	bg.color = Color(0.0, 0.0, 0.0)
	bg.position = Vector2(0, 0)
	bg.size = Vector2(1920, 1080)
	add_child(bg)

	var center := CenterContainer.new()
	center.position = Vector2(0, 0)
	center.size = Vector2(1920, 1080)
	add_child(center)

	var vbox := VBoxContainer.new()
	vbox.alignment = BoxContainer.ALIGNMENT_CENTER
	vbox.add_theme_constant_override("separation", 24)
	center.add_child(vbox)

	var suffix: String = ENDING_KEYS.get(ending_id, "")
	var ending_name: String = Locale.t("ENDING_%s_NAME" % suffix) if not suffix.is_empty() else "Ende"
	var ending_desc: String = Locale.t("ENDING_%s_DESC" % suffix) if not suffix.is_empty() else "..."
	var ending_type: String = Locale.t("ENDING_%s_TYPE" % suffix) if not suffix.is_empty() else "?"

	# Top ornament frame
	vbox.add_child(UITheme.create_ornament_label(UITheme.ORNAMENT_WIDE, 20))

	# "ENDE" header
	var end_label := Label.new()
	end_label.text = Locale.t("END_HEADER")
	end_label.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	end_label.add_theme_font_size_override("font_size", 28)
	end_label.add_theme_color_override("font_color", UITheme.TEXT_DIM)
	end_label.add_theme_font_override("font", UITheme.font_ui())
	vbox.add_child(end_label)

	# Ending name (larger serif)
	var name_label := Label.new()
	name_label.text = ending_name
	name_label.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	name_label.add_theme_font_size_override("font_size", 56)
	name_label.add_theme_color_override("font_color", UITheme.GOLD)
	name_label.add_theme_font_override("font", UITheme.font_title())
	vbox.add_child(name_label)

	# Ending type
	var type_label := Label.new()
	type_label.text = "[%s]" % ending_type
	type_label.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	type_label.add_theme_font_size_override("font_size", 20)
	type_label.add_theme_color_override("font_color", UITheme.GOLD_DIM)
	type_label.add_theme_font_override("font", UITheme.font_ui())
	vbox.add_child(type_label)

	# Narrow ornament
	vbox.add_child(UITheme.create_ornament_label(UITheme.ORNAMENT_NARROW, 16))

	# Description
	var desc := Label.new()
	desc.text = ending_desc
	desc.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	desc.add_theme_font_size_override("font_size", 22)
	desc.add_theme_color_override("font_color", UITheme.TEXT_LIGHT)
	desc.add_theme_font_override("font", UITheme.font_body())
	desc.autowrap_mode = TextServer.AUTOWRAP_WORD_SMART
	desc.custom_minimum_size.x = 800
	vbox.add_child(desc)

	var spacer := Control.new()
	spacer.custom_minimum_size.y = 30
	vbox.add_child(spacer)

	# Completion tracker
	var completion := Label.new()
	var count := GameManager.endings_unlocked.size()
	completion.text = Locale.t("ENDINGS_DISCOVERED") % count
	completion.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	completion.add_theme_font_size_override("font_size", 20)
	completion.add_theme_color_override("font_color", UITheme.TEXT_DIM)
	completion.add_theme_font_override("font", UITheme.font_ui())
	vbox.add_child(completion)

	# Bottom ornament frame
	vbox.add_child(UITheme.create_ornament_label(UITheme.ORNAMENT_WIDE, 20))

	var spacer2 := Control.new()
	spacer2.custom_minimum_size.y = 20
	vbox.add_child(spacer2)

	# Return to title button
	var btn := Button.new()
	btn.text = Locale.t("RETURN_TO_MENU")
	btn.custom_minimum_size = Vector2(300, 50)
	btn.size_flags_horizontal = Control.SIZE_SHRINK_CENTER
	UITheme.style_menu_button(btn, 24)
	btn.pressed.connect(func():
		SceneManager.change_scene("res://scenes/TitleScreen.tscn"))
	vbox.add_child(btn)
