extends Node

## Central game state manager. Holds flags, character data, and current game state.

signal flag_changed(flag_name: String, value: int)
signal game_state_changed(new_state: String)

# Story flags - flat dictionary, String → int
var flags: Dictionary = {}

# Character definitions loaded from characters.json
var characters: Dictionary = {}

# Current game state
var current_act: String = "prologue"
var current_scene: String = ""
var current_dialogue_file: String = ""
var current_node_id: String = ""

# Journal entries collected by the player
var journal_entries: Array[String] = []

# Endings unlocked (for completion tracker)
var endings_unlocked: Array[String] = []

# Game state enum-like
var game_state: String = "title" # title, playing, paused, ending

# Settings (persisted via settings_screen.gd)
var text_speed: float = 40.0  # characters per second
var auto_advance: bool = false  # auto-advance after text finishes


func _ready() -> void:
	_load_characters()
	_load_default_flags()


func _load_characters() -> void:
	var file := FileAccess.open("res://data/characters.json", FileAccess.READ)
	if file:
		var json := JSON.new()
		var err := json.parse(file.get_as_text())
		if err == OK:
			characters = json.data
		else:
			push_warning("Failed to parse characters.json: " + json.get_error_message())
	else:
		push_warning("characters.json not found, using empty character data")


func _load_default_flags() -> void:
	var file := FileAccess.open("res://data/story_flags.json", FileAccess.READ)
	if file:
		var json := JSON.new()
		var err := json.parse(file.get_as_text())
		if err == OK:
			for key in json.data:
				flags[key] = json.data[key]
		else:
			push_warning("Failed to parse story_flags.json")
	else:
		push_warning("story_flags.json not found, using empty flags")


func set_flag(flag_name: String, value: int = 1) -> void:
	flags[flag_name] = value
	flag_changed.emit(flag_name, value)


func get_flag(flag_name: String, default: int = 0) -> int:
	return flags.get(flag_name, default)


func has_flag(flag_name: String) -> bool:
	return flags.has(flag_name) and flags[flag_name] != 0


func check_flags(required_flags: Dictionary) -> bool:
	for flag_name in required_flags:
		var required_value: int = required_flags[flag_name]
		if get_flag(flag_name) != required_value:
			return false
	return true


func add_journal_entry(entry_id: String) -> void:
	if entry_id not in journal_entries:
		journal_entries.append(entry_id)


func has_journal_entry(entry_id: String) -> bool:
	return entry_id in journal_entries


func get_character_name(char_id: String) -> String:
	if char_id in characters:
		return characters[char_id].get("name", char_id)
	return char_id


func get_character_color(char_id: String) -> Color:
	if char_id in characters:
		var hex: String = characters[char_id].get("color", "#FFFFFF")
		return Color.from_string(hex, Color.WHITE)
	return Color.WHITE


func set_game_state(new_state: String) -> void:
	game_state = new_state
	game_state_changed.emit(new_state)


func start_new_game() -> void:
	flags.clear()
	_load_default_flags()
	journal_entries.clear()
	current_act = "prologue"
	current_scene = ""
	current_dialogue_file = ""
	current_node_id = ""
	set_game_state("playing")


func get_save_data() -> Dictionary:
	return {
		"flags": flags.duplicate(),
		"current_act": current_act,
		"current_scene": current_scene,
		"current_dialogue_file": current_dialogue_file,
		"current_node_id": current_node_id,
		"journal_entries": journal_entries.duplicate(),
		"endings_unlocked": endings_unlocked.duplicate(),
	}


func load_save_data(data: Dictionary) -> void:
	flags = data.get("flags", {})
	current_act = data.get("current_act", "prologue")
	current_scene = data.get("current_scene", "")
	current_dialogue_file = data.get("current_dialogue_file", "")
	current_node_id = data.get("current_node_id", "")
	journal_entries.assign(data.get("journal_entries", []))
	endings_unlocked.assign(data.get("endings_unlocked", []))
	set_game_state("playing")
