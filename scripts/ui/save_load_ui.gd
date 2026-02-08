extends PanelContainer

## Save/Load overlay panel with slot selection.

signal closed

enum Mode { SAVE, LOAD }

var _current_mode: Mode = Mode.SAVE
var _slot_container: VBoxContainer
var _title_label: Label


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
	margin.add_theme_constant_override("margin_left", UITheme.margin_h())
	margin.add_theme_constant_override("margin_right", UITheme.margin_h())
	margin.add_theme_constant_override("margin_top", UITheme.margin_v())
	margin.add_theme_constant_override("margin_bottom", UITheme.margin_v())
	add_child(margin)

	var vbox := VBoxContainer.new()
	vbox.add_theme_constant_override("separation", 16)
	margin.add_child(vbox)

	# Title (serif font)
	_title_label = Label.new()
	_title_label.text = Locale.t("SAVE_TITLE")
	_title_label.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	_title_label.add_theme_font_size_override("font_size", UITheme.s(38))
	_title_label.add_theme_color_override("font_color", UITheme.GOLD)
	_title_label.add_theme_font_override("font", UITheme.font_title())
	vbox.add_child(_title_label)

	# Ornament under title
	vbox.add_child(UITheme.create_ornament_label(UITheme.ORNAMENT_LINE, 16))

	# Slots container
	_slot_container = VBoxContainer.new()
	_slot_container.add_theme_constant_override("separation", 8)
	vbox.add_child(_slot_container)

	# Close button
	var close_btn := Button.new()
	close_btn.text = Locale.t("CLOSE")
	close_btn.custom_minimum_size = Vector2(UITheme.s(200), UITheme.s(45))
	close_btn.size_flags_horizontal = Control.SIZE_SHRINK_CENTER
	UITheme.style_button(close_btn, 22)
	close_btn.pressed.connect(close_panel)
	vbox.add_child(close_btn)


func open_save() -> void:
	_current_mode = Mode.SAVE
	_refresh_slots()
	_title_label.text = Locale.t("SAVE_TITLE")
	show()


func open_load() -> void:
	_current_mode = Mode.LOAD
	_refresh_slots()
	_title_label.text = Locale.t("LOAD_TITLE")
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
			slot_btn.text = "Slot %d - %s" % [i, Locale.t("SLOT_EMPTY")]
		else:
			slot_btn.text = "Slot %d - %s (%s)" % [i, info.get("act", "?"), info.get("timestamp", "?")]

		slot_btn.custom_minimum_size = Vector2(0, UITheme.s(60))
		UITheme.style_button(slot_btn, 20)

		var slot := i
		slot_btn.pressed.connect(func(): _on_slot_pressed(slot))
		_slot_container.add_child(slot_btn)


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
	if visible and (event.is_action_pressed("toggle_menu") or event.is_action_pressed("ui_cancel")):
		close_panel()
		get_viewport().set_input_as_handled()
