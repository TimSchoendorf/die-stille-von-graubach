class_name ChoiceManager
extends RefCounted

## Utility for evaluating choice availability based on flags.


static func filter_available_choices(choices: Array) -> Array:
	var available: Array = []
	for choice in choices:
		if is_choice_available(choice):
			available.append(choice)
	return available


static func is_choice_available(choice: Dictionary) -> bool:
	var required: Dictionary = choice.get("require_flags", {})
	if required.is_empty():
		return true
	return GameManager.check_flags(required)


static func apply_choice_flags(choice: Dictionary) -> void:
	var set_flags: Dictionary = choice.get("set_flags", {})
	for flag_name in set_flags:
		GameManager.set_flag(flag_name, set_flags[flag_name])
