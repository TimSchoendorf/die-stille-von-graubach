class_name DialoguePlayer
extends Node

## Processes dialogue nodes sequentially, dispatching to UI components.

signal text_requested(speaker: String, text: String, speaker_color: Color, speaker_id: String)
signal narration_requested(text: String)
signal choices_requested(choices: Array)
signal choice_made(choice_index: int)
signal background_requested(bg_path: String, transition: String)
signal character_requested(char_id: String, expression: String, position: String, action: String)
signal effect_requested(effect_name: String, params: Dictionary)
signal sound_requested(sound_type: String, path: String)
signal transition_requested(transition_type: String, duration: float)
signal journal_requested(entry_id: String, title: String, content: String)
signal wait_requested(duration: float)
signal scene_ended(next_file: String)
signal dialogue_finished

var _dialogue_data: Dictionary = {}
var _current_node_id: String = ""
var _is_waiting_for_input: bool = false
var _is_waiting_for_choice: bool = false
var _is_processing: bool = false


func load_and_start(file_path: String, start_node: String = "") -> void:
	_dialogue_data = DialogueLoader.load_dialogue(file_path)
	if _dialogue_data.is_empty():
		push_error("Failed to load dialogue: " + file_path)
		return

	if not start_node.is_empty() and not DialogueLoader.get_node(_dialogue_data, start_node).is_empty():
		_current_node_id = start_node
	else:
		_current_node_id = DialogueLoader.get_start_node_id(_dialogue_data)
	_is_processing = true
	_process_current_node()


func advance() -> void:
	if _is_waiting_for_input:
		_is_waiting_for_input = false
		_go_to_next()
	# Choices are handled through select_choice()


func select_choice(index: int) -> void:
	if not _is_waiting_for_choice:
		return

	_is_waiting_for_choice = false
	choice_made.emit(index)

	var node := _get_current_node()
	var choices: Array = node.get("choices", [])
	if index < 0 or index >= choices.size():
		push_error("Invalid choice index: " + str(index))
		return

	var choice: Dictionary = choices[index]

	# Set flags from this choice
	var set_flags: Dictionary = choice.get("set_flags", {})
	for flag_name in set_flags:
		GameManager.set_flag(flag_name, set_flags[flag_name])

	# Navigate to the choice's target
	var next_id: String = choice.get("next", "")
	if next_id.is_empty():
		_end_dialogue()
	else:
		_current_node_id = next_id
		GameManager.current_node_id = _current_node_id
		_process_current_node()


func is_active() -> bool:
	return _is_processing


func _get_current_node() -> Dictionary:
	return DialogueLoader.get_node(_dialogue_data, _current_node_id)


func _process_current_node() -> void:
	if _current_node_id.is_empty():
		_end_dialogue()
		return

	var node := _get_current_node()
	if node.is_empty():
		push_error("Node not found: " + _current_node_id)
		_end_dialogue()
		return

	GameManager.current_node_id = _current_node_id

	var node_type: String = node.get("type", "")
	match node_type:
		"dialogue":
			_handle_dialogue(node)
		"narration":
			_handle_narration(node)
		"choice":
			_handle_choice(node)
		"background":
			_handle_background(node)
			_go_to_next()
		"character":
			_handle_character(node)
			_go_to_next()
		"transition":
			_handle_transition(node)
			# Wait for transition duration before continuing
			var duration: float = node.get("duration", 0.5)
			await get_tree().create_timer(duration).timeout
			_go_to_next()
		"set_flag":
			_handle_set_flag(node)
			_go_to_next()
		"flag_check":
			_handle_flag_check(node)
		"effect":
			_handle_effect(node)
			_go_to_next()
		"journal":
			_handle_journal(node)
			_go_to_next()
		"wait":
			_handle_wait(node)
			var duration: float = node.get("duration", 1.0)
			await get_tree().create_timer(duration).timeout
			_go_to_next()
		"sound":
			_handle_sound(node)
			_go_to_next()
		"scene_end":
			_handle_scene_end(node)
		_:
			push_warning("Unknown node type: " + node_type)
			_go_to_next()


func _handle_dialogue(node: Dictionary) -> void:
	var speaker: String = node.get("speaker", "")
	var text: String = node.get("text", "")
	var color := GameManager.get_character_color(speaker)
	var display_name := GameManager.get_character_name(speaker)

	# Update expression if specified in dialogue node
	var expression: String = node.get("expression", "")
	if not expression.is_empty() and not speaker.is_empty():
		character_requested.emit(speaker, expression, "", "update_expression")

	text_requested.emit(display_name, text, color, speaker)
	_is_waiting_for_input = true


func _handle_narration(node: Dictionary) -> void:
	var text: String = node.get("text", "")
	narration_requested.emit(text)
	_is_waiting_for_input = true


func _handle_choice(node: Dictionary) -> void:
	var choices: Array = node.get("choices", [])
	var available_choices: Array = []

	for choice in choices:
		var required: Dictionary = choice.get("require_flags", {})
		if required.is_empty() or GameManager.check_flags(required):
			available_choices.append(choice)

	if available_choices.is_empty():
		# No valid choices, use fallback or go to next
		var fallback: String = node.get("fallback", "")
		if not fallback.is_empty():
			_current_node_id = fallback
			_process_current_node()
		else:
			_go_to_next()
		return

	# Replace choices with only the available ones for indexing
	node["choices"] = available_choices
	choices_requested.emit(available_choices)
	_is_waiting_for_choice = true


func _handle_background(node: Dictionary) -> void:
	var bg: String = node.get("background", "")
	var transition: String = node.get("transition", "fade")
	background_requested.emit(bg, transition)


func _handle_character(node: Dictionary) -> void:
	var char_id: String = node.get("character", "")
	var expression: String = node.get("expression", "neutral")
	var position: String = node.get("position", "center")
	var action: String = node.get("action", "show") # show, hide, move
	character_requested.emit(char_id, expression, position, action)


func _handle_transition(node: Dictionary) -> void:
	var ttype: String = node.get("transition", "fade")
	var duration: float = node.get("duration", 0.5)
	transition_requested.emit(ttype, duration)


func _handle_set_flag(node: Dictionary) -> void:
	var flag_name: String = node.get("flag", "")
	var value: int = node.get("value", 1)
	if not flag_name.is_empty():
		GameManager.set_flag(flag_name, value)


func _handle_flag_check(node: Dictionary) -> void:
	var flag_name: String = node.get("flag", "")
	var expected_value: int = node.get("value", 1)
	var true_next: String = node.get("true_next", "")
	var false_next: String = node.get("false_next", "")

	if GameManager.get_flag(flag_name) == expected_value:
		if not true_next.is_empty():
			_current_node_id = true_next
			_process_current_node()
		else:
			_go_to_next()
	else:
		if not false_next.is_empty():
			_current_node_id = false_next
			_process_current_node()
		else:
			_go_to_next()


func _handle_effect(node: Dictionary) -> void:
	var effect_name: String = node.get("effect", "")
	var params: Dictionary = node.get("params", {})
	effect_requested.emit(effect_name, params)


func _handle_journal(node: Dictionary) -> void:
	var entry_id: String = node.get("entry_id", "")
	var title: String = node.get("title", "")
	var content: String = node.get("content", "")
	GameManager.add_journal_entry(entry_id, title, content)
	journal_requested.emit(entry_id, title, content)


func _handle_wait(node: Dictionary) -> void:
	var duration: float = node.get("duration", 1.0)
	wait_requested.emit(duration)


func _handle_sound(node: Dictionary) -> void:
	var sound_type: String = node.get("sound_type", "sfx") # sfx, music, ambience
	var path: String = node.get("path", "")
	sound_requested.emit(sound_type, path)


func _handle_scene_end(node: Dictionary) -> void:
	var next_file: String = node.get("next_file", "")
	_is_processing = false
	scene_ended.emit(next_file)


func _go_to_next() -> void:
	var node := _get_current_node()
	var next_id: String = node.get("next", "")
	if next_id.is_empty():
		_end_dialogue()
	else:
		_current_node_id = next_id
		_process_current_node()


func _end_dialogue() -> void:
	_is_processing = false
	_is_waiting_for_input = false
	_is_waiting_for_choice = false
	dialogue_finished.emit()
