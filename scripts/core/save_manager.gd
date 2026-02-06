extends Node

## Handles saving and loading game state to user://saves/

const SAVE_DIR := "user://saves/"
const MAX_SLOTS := 10

signal save_completed(slot: int)
signal load_completed(slot: int)


func _ready() -> void:
	DirAccess.make_dir_recursive_absolute(SAVE_DIR)


func save_game(slot: int) -> bool:
	var save_data := {
		"version": 1,
		"timestamp": Time.get_datetime_string_from_system(),
		"game_data": GameManager.get_save_data(),
	}

	var path := _get_save_path(slot)
	var file := FileAccess.open(path, FileAccess.WRITE)
	if not file:
		push_error("Failed to open save file: " + path)
		return false

	file.store_string(JSON.stringify(save_data, "\t"))
	save_completed.emit(slot)
	return true


func load_game(slot: int) -> bool:
	var path := _get_save_path(slot)
	if not FileAccess.file_exists(path):
		push_warning("Save file not found: " + path)
		return false

	var file := FileAccess.open(path, FileAccess.READ)
	if not file:
		push_error("Failed to open save file: " + path)
		return false

	var json := JSON.new()
	var err := json.parse(file.get_as_text())
	if err != OK:
		push_error("Failed to parse save file: " + json.get_error_message())
		return false

	var save_data: Dictionary = json.data
	GameManager.load_save_data(save_data.get("game_data", {}))
	load_completed.emit(slot)
	return true


func delete_save(slot: int) -> bool:
	var path := _get_save_path(slot)
	if FileAccess.file_exists(path):
		DirAccess.remove_absolute(path)
		return true
	return false


func has_save(slot: int) -> bool:
	return FileAccess.file_exists(_get_save_path(slot))


func get_save_info(slot: int) -> Dictionary:
	var path := _get_save_path(slot)
	if not FileAccess.file_exists(path):
		return {}

	var file := FileAccess.open(path, FileAccess.READ)
	if not file:
		return {}

	var json := JSON.new()
	var err := json.parse(file.get_as_text())
	if err != OK:
		return {}

	var data: Dictionary = json.data
	return {
		"slot": slot,
		"timestamp": data.get("timestamp", "Unknown"),
		"act": data.get("game_data", {}).get("current_act", "???"),
		"scene": data.get("game_data", {}).get("current_scene", "???"),
	}


func get_all_save_info() -> Array[Dictionary]:
	var saves: Array[Dictionary] = []
	for i in range(MAX_SLOTS):
		var info := get_save_info(i)
		if not info.is_empty():
			saves.append(info)
	return saves


func quick_save() -> bool:
	return save_game(0)


func quick_load() -> bool:
	return load_game(0)


func _get_save_path(slot: int) -> String:
	return SAVE_DIR + "save_" + str(slot) + ".json"
