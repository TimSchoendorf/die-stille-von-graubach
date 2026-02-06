extends PanelContainer

## The main text display box at the bottom of the screen.
## Handles typewriter effect and speaker name display.

signal text_finished
signal advance_requested

@export var characters_per_second: float = 40.0
@export var typewriter_enabled: bool = true

var _speaker_label: RichTextLabel
var _text_label: RichTextLabel
var _full_text: String = ""
var _visible_chars: float = 0.0
var _is_typing: bool = false
var _is_text_complete: bool = false

# Continue indicator
var _continue_indicator: Label


func _ready() -> void:
	_setup_ui()
	hide()


func _setup_ui() -> void:
	custom_minimum_size = Vector2(1920, 250)

	# Dark semi-transparent background
	var style := StyleBoxFlat.new()
	style.bg_color = Color(0.05, 0.05, 0.08, 0.85)
	style.border_color = Color(0.3, 0.25, 0.2, 0.6)
	style.border_width_top = 2
	style.corner_radius_top_left = 4
	style.corner_radius_top_right = 4
	style.content_margin_left = 60
	style.content_margin_right = 60
	style.content_margin_top = 20
	style.content_margin_bottom = 20
	add_theme_stylebox_override("panel", style)

	var vbox := VBoxContainer.new()
	vbox.add_theme_constant_override("separation", 8)
	add_child(vbox)

	# Speaker name
	_speaker_label = RichTextLabel.new()
	_speaker_label.bbcode_enabled = true
	_speaker_label.fit_content = true
	_speaker_label.custom_minimum_size.y = 32
	_speaker_label.add_theme_font_size_override("normal_font_size", 28)
	_speaker_label.scroll_active = false
	vbox.add_child(_speaker_label)

	# Text body
	_text_label = RichTextLabel.new()
	_text_label.bbcode_enabled = true
	_text_label.fit_content = true
	_text_label.custom_minimum_size.y = 120
	_text_label.add_theme_font_size_override("normal_font_size", 24)
	_text_label.scroll_active = false
	vbox.add_child(_text_label)

	# Continue indicator
	_continue_indicator = Label.new()
	_continue_indicator.text = "▼"
	_continue_indicator.horizontal_alignment = HORIZONTAL_ALIGNMENT_RIGHT
	_continue_indicator.add_theme_font_size_override("font_size", 20)
	_continue_indicator.add_theme_color_override("font_color", Color(0.7, 0.7, 0.7, 0.8))
	_continue_indicator.hide()
	vbox.add_child(_continue_indicator)


func show_dialogue(speaker: String, text: String, color: Color = Color.WHITE) -> void:
	show()
	_speaker_label.clear()
	if not speaker.is_empty():
		_speaker_label.append_text(TextEffects.format_speaker(speaker, color))
		_speaker_label.show()
	else:
		_speaker_label.hide()

	_text_label.clear()
	_full_text = text
	_text_label.append_text(text)
	_continue_indicator.hide()

	if typewriter_enabled:
		_text_label.visible_characters = 0
		_visible_chars = 0.0
		_is_typing = true
		_is_text_complete = false
	else:
		_text_label.visible_characters = -1
		_is_typing = false
		_is_text_complete = true
		_continue_indicator.show()
		text_finished.emit()


func show_narration(text: String) -> void:
	show_dialogue("", text, Color.WHITE)


var _auto_advance_timer: float = 0.0


func _process(delta: float) -> void:
	# Use GameManager text speed if available
	var speed: float = GameManager.text_speed if GameManager.text_speed > 0 else characters_per_second

	if not _is_typing:
		# Blink the continue indicator
		if _is_text_complete and _continue_indicator.visible:
			_continue_indicator.modulate.a = 0.5 + 0.5 * sin(Time.get_ticks_msec() * 0.005)
			# Auto-advance
			if GameManager.auto_advance:
				_auto_advance_timer += delta
				if _auto_advance_timer >= 3.0:
					_auto_advance_timer = 0.0
					_is_text_complete = false
					_continue_indicator.hide()
					advance_requested.emit()
		return

	_visible_chars += speed * delta
	_text_label.visible_characters = int(_visible_chars)

	if _text_label.visible_characters >= _text_label.get_total_character_count():
		_is_typing = false
		_is_text_complete = true
		_auto_advance_timer = 0.0
		_text_label.visible_characters = -1
		_continue_indicator.show()
		text_finished.emit()


func _gui_input(event: InputEvent) -> void:
	if not visible:
		return

	if event is InputEventMouseButton and event.pressed and event.button_index == MOUSE_BUTTON_LEFT:
		_handle_advance()
		accept_event()


func _unhandled_input(event: InputEvent) -> void:
	if not visible:
		return

	# Click anywhere on screen to advance text
	if event is InputEventMouseButton and event.pressed and event.button_index == MOUSE_BUTTON_LEFT:
		_handle_advance()
		get_viewport().set_input_as_handled()
	elif event.is_action_pressed("advance_text"):
		_handle_advance()
		get_viewport().set_input_as_handled()


func _handle_advance() -> void:
	if _is_typing:
		# Skip typewriter, show all text
		_is_typing = false
		_is_text_complete = true
		_text_label.visible_characters = -1
		_visible_chars = _text_label.get_total_character_count()
		_continue_indicator.show()
		text_finished.emit()
	elif _is_text_complete:
		_is_text_complete = false
		_continue_indicator.hide()
		advance_requested.emit()


func hide_textbox() -> void:
	hide()
	_is_typing = false
	_is_text_complete = false


func is_typing() -> bool:
	return _is_typing
