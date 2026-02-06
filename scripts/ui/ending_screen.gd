extends Control

## Displayed after reaching an ending. Shows ending name and completion status.

var _ending_data: Dictionary = {
	"seal": {"name": "Das Siegel", "description": "Du hast Großmutters Ritual vollendet und die Entität gebunden.", "type": "Best"},
	"escape": {"name": "Die Flucht", "description": "Georg opferte sich, damit du entkommen konntest. Das Dorf verschwand hinter dir.", "type": "Gut"},
	"pact": {"name": "Der Pakt", "description": "Du bist die neue Hüterin. Die Tradition lebt weiter.", "type": "Ambivalent"},
	"awakening": {"name": "Das Erwachen", "description": "Das Ritual scheiterte. Die Realität zerfiel um dich herum.", "type": "Horror"},
	"truth": {"name": "Die Wahrheit", "description": "Du hast die volle Erkenntnis erlangt. Es gibt Hunderte solcher dünnen Stellen.", "type": "Kosmisch"},
	"sacrifice": {"name": "Das Opfer", "description": "Aus Liebe nahmst du Konrads Platz als Gefäß ein.", "type": "Tragisch"},
}


func _ready() -> void:
	hide()


func show_ending(ending_id: String) -> void:
	# Record ending as unlocked
	if ending_id not in GameManager.endings_unlocked:
		GameManager.endings_unlocked.append(ending_id)

	_build_ending_screen(ending_id)
	show()


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

	var data: Dictionary = _ending_data.get(ending_id, {
		"name": "Ende", "description": "...", "type": "?"
	})

	# "ENDE" header
	var end_label := Label.new()
	end_label.text = "- ENDE -"
	end_label.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	end_label.add_theme_font_size_override("font_size", 28)
	end_label.add_theme_color_override("font_color", Color(0.5, 0.45, 0.4))
	vbox.add_child(end_label)

	# Ending name
	var name_label := Label.new()
	name_label.text = data["name"]
	name_label.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	name_label.add_theme_font_size_override("font_size", 48)
	name_label.add_theme_color_override("font_color", Color(0.8, 0.7, 0.55))
	vbox.add_child(name_label)

	# Ending type
	var type_label := Label.new()
	type_label.text = "[%s]" % data["type"]
	type_label.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	type_label.add_theme_font_size_override("font_size", 20)
	type_label.add_theme_color_override("font_color", Color(0.5, 0.45, 0.4))
	vbox.add_child(type_label)

	# Description
	var desc := Label.new()
	desc.text = data["description"]
	desc.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	desc.add_theme_font_size_override("font_size", 22)
	desc.add_theme_color_override("font_color", Color(0.6, 0.55, 0.5))
	desc.autowrap_mode = TextServer.AUTOWRAP_WORD_SMART
	desc.custom_minimum_size.x = 800
	vbox.add_child(desc)

	var spacer := Control.new()
	spacer.custom_minimum_size.y = 40
	vbox.add_child(spacer)

	# Completion tracker
	var completion := Label.new()
	var count := GameManager.endings_unlocked.size()
	completion.text = "Enden entdeckt: %d / 6" % count
	completion.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	completion.add_theme_font_size_override("font_size", 20)
	completion.add_theme_color_override("font_color", Color(0.4, 0.38, 0.35))
	vbox.add_child(completion)

	var spacer2 := Control.new()
	spacer2.custom_minimum_size.y = 30
	vbox.add_child(spacer2)

	# Return to title button
	var btn := Button.new()
	btn.text = "Zum Hauptmenü"
	btn.custom_minimum_size = Vector2(300, 50)
	btn.size_flags_horizontal = Control.SIZE_SHRINK_CENTER
	btn.add_theme_font_size_override("font_size", 24)
	_style_button(btn)
	btn.pressed.connect(func():
		SceneManager.change_scene("res://scenes/TitleScreen.tscn"))
	vbox.add_child(btn)


func _style_button(btn_to_style: Button) -> void:
	var style := StyleBoxFlat.new()
	style.bg_color = Color(0.08, 0.08, 0.12, 0.7)
	style.border_color = Color(0.3, 0.28, 0.25, 0.5)
	style.set_border_width_all(1)
	style.set_corner_radius_all(2)
	style.content_margin_left = 12
	style.content_margin_right = 12
	style.content_margin_top = 8
	style.content_margin_bottom = 8
	btn_to_style.add_theme_stylebox_override("normal", style)

	var hover := style.duplicate()
	hover.bg_color = Color(0.15, 0.12, 0.1, 0.9)
	hover.border_color = Color(0.5, 0.45, 0.35, 0.8)
	btn_to_style.add_theme_stylebox_override("hover", hover)

	var pressed := style.duplicate()
	pressed.bg_color = Color(0.05, 0.05, 0.08, 0.95)
	btn_to_style.add_theme_stylebox_override("pressed", pressed)

	var focus := style.duplicate()
	btn_to_style.add_theme_stylebox_override("focus", focus)

	btn_to_style.add_theme_color_override("font_color", Color(0.8, 0.75, 0.7))
	btn_to_style.add_theme_color_override("font_hover_color", Color(1.0, 0.95, 0.85))
