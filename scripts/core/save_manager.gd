extends Node

## Handles saving and loading game state to user://saves/
## Features: atomic writes, backup rotation, validation, checksum, versioning.

const SAVE_DIR := "user://saves/"
const MAX_SLOTS := 10
const SAVE_VERSION := 2
const BACKUP_COUNT := 3

signal save_completed(slot: int)
signal load_completed(slot: int)

# Block saves during transitions
var save_blocked: bool = false


func _ready() -> void:
	DirAccess.make_dir_recursive_absolute(SAVE_DIR)


func save_game(slot: int) -> bool:
	if save_blocked:
		push_warning("Save blocked during transition")
		return false

	var save_data := {
		"version": SAVE_VERSION,
		"timestamp": Time.get_datetime_string_from_system(),
		"checksum": "",
		"game_data": GameManager.get_save_data(),
	}

	# Compute checksum over game_data
	var game_json := JSON.stringify(save_data["game_data"])
	save_data["checksum"] = _compute_checksum(game_json)

	var path := _get_save_path(slot)
	var tmp_path := path + ".tmp"

	# Atomic write: write to .tmp first, then rename
	var file := FileAccess.open(tmp_path, FileAccess.WRITE)
	if not file:
		push_error("Failed to open temp save file: " + tmp_path)
		return false

	file.store_string(JSON.stringify(save_data, "\t"))
	file.close()

	# Rotate backups before overwriting
	if FileAccess.file_exists(path):
		_rotate_backups(slot)

	# Rename .tmp to final path (atomic on most filesystems)
	var dir := DirAccess.open(SAVE_DIR)
	if dir:
		# Remove existing file first (rename requires target not existing on some platforms)
		if FileAccess.file_exists(path):
			dir.remove(path.get_file())
		var err := dir.rename(tmp_path.get_file(), path.get_file())
		if err != OK:
			push_error("Failed to rename temp save to final: error " + str(err))
			return false
	else:
		push_error("Failed to open save directory")
		return false

	save_completed.emit(slot)
	return true


func load_game(slot: int) -> bool:
	var path := _get_save_path(slot)
	if not FileAccess.file_exists(path):
		push_warning("Save file not found: " + path)
		return false

	var save_data := _read_and_validate(path)
	if save_data.is_empty():
		# Try backups
		push_warning("Primary save corrupt, trying backups for slot " + str(slot))
		save_data = _try_load_backup(slot)
		if save_data.is_empty():
			push_error("All saves for slot " + str(slot) + " are corrupt")
			return false

	# Migrate if needed
	save_data = _migrate_save(save_data)

	GameManager.load_save_data(save_data.get("game_data", {}))
	load_completed.emit(slot)
	return true


func delete_save(slot: int) -> bool:
	var path := _get_save_path(slot)
	var deleted := false
	if FileAccess.file_exists(path):
		DirAccess.remove_absolute(path)
		deleted = true

	# Also delete backups
	for i in range(1, BACKUP_COUNT + 1):
		var bak := path + ".bak" + str(i)
		if FileAccess.file_exists(bak):
			DirAccess.remove_absolute(bak)

	return deleted


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


## Returns the slot index of the newest save, or -1 if no saves exist.
func get_newest_save_slot() -> int:
	var best_slot := -1
	var best_time := ""
	for i in range(MAX_SLOTS):
		var info := get_save_info(i)
		if not info.is_empty():
			var ts: String = info.get("timestamp", "")
			if ts > best_time:
				best_time = ts
				best_slot = i
	return best_slot


func quick_save() -> bool:
	return save_game(0)


func quick_load() -> bool:
	return load_game(0)


func _get_save_path(slot: int) -> String:
	return SAVE_DIR + "save_" + str(slot) + ".json"


## Validates a save file: JSON parse, required fields, checksum
func _read_and_validate(path: String) -> Dictionary:
	var file := FileAccess.open(path, FileAccess.READ)
	if not file:
		return {}

	var json := JSON.new()
	var err := json.parse(file.get_as_text())
	if err != OK:
		push_warning("JSON parse error in save: " + json.get_error_message())
		return {}

	var data: Dictionary = json.data

	# Check required top-level fields
	if not data.has("game_data") or not data["game_data"] is Dictionary:
		push_warning("Save missing game_data")
		return {}

	var game_data: Dictionary = data["game_data"]

	# Validate essential game_data fields
	if not game_data.has("current_dialogue_file") or not game_data["current_dialogue_file"] is String:
		push_warning("Save missing current_dialogue_file")
		return {}
	if not game_data.has("flags") or not game_data["flags"] is Dictionary:
		push_warning("Save missing flags")
		return {}

	# Validate checksum (if present - v1 saves don't have it)
	var stored_checksum: String = data.get("checksum", "")
	if not stored_checksum.is_empty():
		var game_json := JSON.stringify(game_data)
		var computed := _compute_checksum(game_json)
		if computed != stored_checksum:
			push_warning("Save checksum mismatch - file may be tampered")
			# Still load but warn - don't block players who hand-edited saves

	return data


## Rotates backup files: .bak3 deleted, .bak2 -> .bak3, .bak1 -> .bak2, current -> .bak1
func _rotate_backups(slot: int) -> void:
	var path := _get_save_path(slot)
	var dir := DirAccess.open(SAVE_DIR)
	if not dir:
		return

	# Delete oldest backup
	var oldest := path + ".bak" + str(BACKUP_COUNT)
	if FileAccess.file_exists(oldest):
		dir.remove(oldest.get_file())

	# Shift backups up
	for i in range(BACKUP_COUNT, 1, -1):
		var src := path + ".bak" + str(i - 1)
		var dst := path + ".bak" + str(i)
		if FileAccess.file_exists(src):
			if FileAccess.file_exists(dst):
				dir.remove(dst.get_file())
			dir.rename(src.get_file(), dst.get_file())

	# Current -> .bak1
	var bak1 := path + ".bak1"
	if FileAccess.file_exists(path):
		dir.copy(path.get_file(), bak1.get_file())


## Tries to load from backup files when primary is corrupt
func _try_load_backup(slot: int) -> Dictionary:
	var path := _get_save_path(slot)
	for i in range(1, BACKUP_COUNT + 1):
		var bak := path + ".bak" + str(i)
		if FileAccess.file_exists(bak):
			var data := _read_and_validate(bak)
			if not data.is_empty():
				push_warning("Recovered save from backup " + str(i))
				return data
	return {}


## Migrates old save formats to current version
func _migrate_save(data: Dictionary) -> Dictionary:
	var version: int = data.get("version", 1)

	if version < 2:
		# v1 -> v2: add read_nodes set (empty for old saves)
		var game_data: Dictionary = data.get("game_data", {})
		if not game_data.has("read_nodes"):
			game_data["read_nodes"] = []
		data["game_data"] = game_data
		data["version"] = 2

	return data


## Simple CRC32-based checksum for tamper detection
func _compute_checksum(text: String) -> String:
	return str(text.hash())
