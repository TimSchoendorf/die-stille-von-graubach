extends PanelContainer

## Save/Load overlay panel with slot selection.

signal closed

enum Mode { SAVE, LOAD }

var _current_mode: Mode = Mode.SAVE
var _slot_container: VBoxContainer


func _ready() -> void:
	_setup_ui()
	hide()


func _setup_ui() -> void:
	position = Vector2(0, 0)
	size = Vector2(1920, 1080)
	# Semi-transparent overlay
	var style := StyleBoxFlat.new()
	style.bg_color = Color(0.0, 0.0, 0.0, 0.85)
	add_theme_stylebox_override("panel", style)

	var margin := MarginContainer.new()
	margin.position = Vector2(0, 0)
	margin.size = Vector2(1920, 1080)
	margin.add_theme_constant_override("margin_left", 300)
	margin.add_theme_constant_override("margin_right", 300)
	margin.add_theme_constant_override("margin_top", 100)
	margin.add_theme_constant_override("margin_bottom", 100)
	add_child(margin)

	var vbox := VBoxContainer.new()
	vbox.add_theme_constant_override("separation", 16)
	margin.add_child(vbox)

	# Title
	var title := Label.new()
	title.name = "TitleLabel"
	title.text = "Speichern"
	title.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	title.add_theme_font_size_override("font_size", 36)
	title.add_theme_color_override("font_color", Color(0.8, 0.75, 0.65))
	vbox.add_child(title)

	# Slots container
	_slot_container = VBoxContainer.new()
	_slot_container.add_theme_constant_override("separation", 8)
	vbox.add_child(_slot_container)

	# Close button
	var close_btn := Button.new()
	close_btn.text = "Schließen"
	close_btn.custom_minimum_size = Vector2(200, 45)
	close_btn.size_flags_horizontal = Control.SIZE_SHRINK_CENTER
	close_btn.add_theme_font_size_override("font_size", 22)
	_style_button(close_btn)
	close_btn.pressed.connect(close_panel)
	vbox.add_child(close_btn)


func open_save() -> void:
	_current_mode = Mode.SAVE
	_refresh_slots()
	find_child("TitleLabel").text = "Speichern"
	show()


func open_load() -> void:
	_current_mode = Mode.LOAD
	_refresh_slots()
	find_child("TitleLabel").text = "Laden"
	show()


func close_panel() -> void:
	hide()
	closed.emit()


func _refresh_slots() -> void:
	for child in _slot_container.get_children():
		child.queue_free()

	for i in range(1, SaveManager.MAX_SLOTS):
		var slot_btn := Button.new()
		var info := SaveManager.get_save_info(i)

		if info.is_empty():
			slot_btn.text = "Slot %d - Leer" % i
		else:
			slot_btn.text = "Slot %d - %s (%s)" % [i, info.get("act", "?"), info.get("timestamp", "?")]

		slot_btn.custom_minimum_size = Vector2(0, 50)
		slot_btn.add_theme_font_size_override("font_size", 20)
		_style_button(slot_btn)

		var slot := i
		slot_btn.pressed.connect(func(): _on_slot_pressed(slot))
		_slot_container.add_child(slot_btn)


func _style_button(btn: Button) -> void:
	var style := StyleBoxFlat.new()
	style.bg_color = Color(0.08, 0.08, 0.12, 0.7)
	style.border_color = Color(0.3, 0.28, 0.25, 0.5)
	style.set_border_width_all(1)
	style.set_corner_radius_all(2)
	style.content_margin_left = 12
	style.content_margin_right = 12
	style.content_margin_top = 8
	style.content_margin_bottom = 8
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

	btn.add_theme_color_override("font_color", Color(0.8, 0.75, 0.7))
	btn.add_theme_color_override("font_hover_color", Color(1.0, 0.95, 0.85))


func _on_slot_pressed(slot: int) -> void:
	match _current_mode:
		Mode.SAVE:
			SaveManager.save_game(slot)
			_refresh_slots()
		Mode.LOAD:
			if SaveManager.has_save(slot):
				SaveManager.load_game(slot)
				close_panel()
				# Reload game scene
				SceneManager.change_scene("res://scenes/GameScene.tscn")


func _input(event: InputEvent) -> void:
	if visible and event.is_action_pressed("toggle_menu"):
		close_panel()
		get_viewport().set_input_as_handled()
