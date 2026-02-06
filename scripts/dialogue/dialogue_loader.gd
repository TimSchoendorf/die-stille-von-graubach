class_name DialogueLoader
extends RefCounted

## Loads and parses dialogue JSON files into usable node structures.


static func load_dialogue(file_path: String) -> Dictionary:
	var full_path := file_path
	if not file_path.begins_with("res://"):
		full_path = "res://data/dialogue/" + file_path

	if not FileAccess.file_exists(full_path):
		push_error("Dialogue file not found: " + full_path)
		return {}

	var file := FileAccess.open(full_path, FileAccess.READ)
	if not file:
		push_error("Failed to open dialogue file: " + full_path)
		return {}

	var json := JSON.new()
	var err := json.parse(file.get_as_text())
	if err != OK:
		push_error("JSON parse error in %s at line %d: %s" % [
			full_path, json.get_error_line(), json.get_error_message()])
		return {}

	var data: Dictionary = json.data
	if not _validate_dialogue(data, full_path):
		return {}

	return data


static func _validate_dialogue(data: Dictionary, path: String) -> bool:
	if not data.has("start"):
		push_error("Dialogue missing 'start' field: " + path)
		return false

	if not data.has("nodes"):
		push_error("Dialogue missing 'nodes' field: " + path)
		return false

	if not data["nodes"] is Dictionary:
		push_error("'nodes' must be a Dictionary: " + path)
		return false

	var start_id: String = data["start"]
	if start_id not in data["nodes"]:
		push_error("Start node '%s' not found in nodes: %s" % [start_id, path])
		return false

	return true


static func get_node(data: Dictionary, node_id: String) -> Dictionary:
	if data.has("nodes") and node_id in data["nodes"]:
		return data["nodes"][node_id]
	return {}


static func get_start_node_id(data: Dictionary) -> String:
	return data.get("start", "")
