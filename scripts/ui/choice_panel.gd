extends VBoxContainer

## Displays choice buttons when the player needs to make a decision.

signal choice_selected(index: int)

var _buttons: Array[Button] = []


func _ready() -> void:
	alignment = BoxContainer.ALIGNMENT_CENTER
	add_theme_constant_override("separation", UITheme.s(14))
	hide()


func show_choices(choices: Array) -> void:
	clear_choices()
	show()

	for i in choices.size():
		var choice: Dictionary = choices[i]
		var btn := Button.new()
		btn.text = choice.get("text", "???")
		btn.custom_minimum_size = Vector2(mini(UITheme.s(650), 1800), UITheme.s(65))
		btn.size_flags_horizontal = Control.SIZE_SHRINK_CENTER

		# Style with gold accent border on left
		var style := StyleBoxFlat.new()
		style.bg_color = Color(0.07, 0.07, 0.1, 0.9)
		style.border_color = UITheme.BORDER
		style.border_width_bottom = 1
		style.border_width_top = 1
		style.border_width_right = 1
		style.border_width_left = UITheme.s(3)
		style.set_corner_radius_all(3)
		style.content_margin_left = UITheme.s(24)
		style.content_margin_right = UITheme.s(20)
		style.content_margin_top = UITheme.s(12)
		style.content_margin_bottom = UITheme.s(12)
		btn.add_theme_stylebox_override("normal", style)

		var hover_style := style.duplicate()
		hover_style.bg_color = Color(0.14, 0.11, 0.08, 0.95)
		hover_style.border_color = UITheme.GOLD
		btn.add_theme_stylebox_override("hover", hover_style)

		var pressed_style := style.duplicate()
		pressed_style.bg_color = Color(0.1, 0.08, 0.06, 0.95)
		pressed_style.border_color = UITheme.GOLD_LIGHT
		btn.add_theme_stylebox_override("pressed", pressed_style)

		var focus_style := style.duplicate()
		focus_style.border_color = UITheme.GOLD_DIM
		btn.add_theme_stylebox_override("focus", focus_style)

		btn.add_theme_font_size_override("font_size", UITheme.s(22))
		btn.add_theme_font_override("font", UITheme.font_body())
		btn.add_theme_color_override("font_color", UITheme.TEXT_LIGHT)
		btn.add_theme_color_override("font_hover_color", UITheme.GOLD_LIGHT)

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
