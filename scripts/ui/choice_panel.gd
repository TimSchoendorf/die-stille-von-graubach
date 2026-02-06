extends VBoxContainer

## Displays choice buttons when the player needs to make a decision.

signal choice_selected(index: int)

var _buttons: Array[Button] = []


func _ready() -> void:
	alignment = BoxContainer.ALIGNMENT_CENTER
	add_theme_constant_override("separation", 12)
	hide()


func show_choices(choices: Array) -> void:
	clear_choices()
	show()

	for i in choices.size():
		var choice: Dictionary = choices[i]
		var btn := Button.new()
		btn.text = choice.get("text", "???")
		btn.custom_minimum_size = Vector2(600, 50)
		btn.size_flags_horizontal = Control.SIZE_SHRINK_CENTER

		# Style the button
		var style := StyleBoxFlat.new()
		style.bg_color = Color(0.1, 0.1, 0.15, 0.9)
		style.border_color = Color(0.4, 0.35, 0.3, 0.8)
		style.border_width_bottom = 1
		style.border_width_top = 1
		style.border_width_left = 1
		style.border_width_right = 1
		style.corner_radius_top_left = 3
		style.corner_radius_top_right = 3
		style.corner_radius_bottom_left = 3
		style.corner_radius_bottom_right = 3
		style.content_margin_left = 20
		style.content_margin_right = 20
		style.content_margin_top = 10
		style.content_margin_bottom = 10
		btn.add_theme_stylebox_override("normal", style)

		var hover_style := style.duplicate()
		hover_style.bg_color = Color(0.2, 0.18, 0.15, 0.95)
		hover_style.border_color = Color(0.6, 0.5, 0.4, 1.0)
		btn.add_theme_stylebox_override("hover", hover_style)

		var pressed_style := style.duplicate()
		pressed_style.bg_color = Color(0.15, 0.12, 0.1, 0.95)
		btn.add_theme_stylebox_override("pressed", pressed_style)

		var focus_style := style.duplicate()
		btn.add_theme_stylebox_override("focus", focus_style)

		btn.add_theme_font_size_override("font_size", 22)
		btn.add_theme_color_override("font_color", Color(0.9, 0.85, 0.8))
		btn.add_theme_color_override("font_hover_color", Color(1.0, 0.95, 0.9))

		var idx := i
		btn.pressed.connect(func(): _on_choice_pressed(idx))
		add_child(btn)
		_buttons.append(btn)

	# Focus first button
	if _buttons.size() > 0:
		_buttons[0].grab_focus()


func clear_choices() -> void:
	for btn in _buttons:
		btn.queue_free()
	_buttons.clear()
	hide()


func _on_choice_pressed(index: int) -> void:
	choice_selected.emit(index)
	clear_choices()
