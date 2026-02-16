extends Control

## Manages character sprite display with 3 positions (left, center, right).

var _positions: Dictionary = {
	"left": Vector2(300, 180),
	"center": Vector2(960, 180),
	"right": Vector2(1620, 180),
}

# Active character sprites: char_id → {sprite: TextureRect, position: String}
var _active_characters: Dictionary = {}
var _texture_cache: Dictionary = {}  # path → Texture2D

const SPRITE_WIDTH := 600
const SPRITE_HEIGHT := 900
const MAX_CACHE_SIZE := 30


func _ready() -> void:
	mouse_filter = Control.MOUSE_FILTER_IGNORE


func _load_cached(path: String) -> Texture2D:
	if path in _texture_cache:
		return _texture_cache[path]
	var tex: Texture2D = load(path)
	if _texture_cache.size() >= MAX_CACHE_SIZE:
		# Remove oldest entry
		var first_key: String = _texture_cache.keys()[0]
		_texture_cache.erase(first_key)
	_texture_cache[path] = tex
	return tex


func _resolve_sprite_path(char_id: String, expression: String) -> String:
	var path := "res://assets/sprites/characters/%s/%s.png" % [char_id, expression]
	if ResourceLoader.exists(path):
		return path
	# Fallback to neutral expression
	if expression != "neutral":
		var neutral_path := "res://assets/sprites/characters/%s/neutral.png" % char_id
		if ResourceLoader.exists(neutral_path):
			push_warning("Sprite not found: %s, using neutral" % path)
			return neutral_path
	push_warning("No sprite found for character: " + char_id)
	return ""


func show_character(char_id: String, expression: String, pos: String) -> void:
	var sprite_path := _resolve_sprite_path(char_id, expression)

	# Check if character already shown
	if char_id in _active_characters:
		var entry: Dictionary = _active_characters[char_id]
		var sprite: TextureRect = entry["sprite"]

		# Update expression
		if not sprite_path.is_empty():
			sprite.texture = _load_cached(sprite_path)

		# Move if position changed
		if entry["position"] != pos:
			_move_character(char_id, pos)
		return

	# Create new sprite
	var sprite := TextureRect.new()
	sprite.mouse_filter = Control.MOUSE_FILTER_IGNORE

	if not sprite_path.is_empty():
		sprite.texture = _load_cached(sprite_path)
	else:
		# Placeholder: semi-transparent silhouette
		sprite.custom_minimum_size = Vector2(SPRITE_WIDTH, SPRITE_HEIGHT)

	sprite.stretch_mode = TextureRect.STRETCH_KEEP_ASPECT_CENTERED
	sprite.custom_minimum_size = Vector2(SPRITE_WIDTH, SPRITE_HEIGHT)
	sprite.size = Vector2(SPRITE_WIDTH, SPRITE_HEIGHT)

	var target_pos: Vector2 = _positions.get(pos, _positions["center"])
	sprite.position = target_pos - Vector2(SPRITE_WIDTH / 2.0, 0)

	# Fade in
	sprite.modulate.a = 0.0
	add_child(sprite)

	var tween := create_tween()
	tween.tween_property(sprite, "modulate:a", 1.0, 0.3)

	_active_characters[char_id] = {"sprite": sprite, "position": pos}


func hide_character(char_id: String) -> void:
	if char_id not in _active_characters:
		return

	var entry: Dictionary = _active_characters[char_id]
	var sprite: TextureRect = entry["sprite"]

	var tween := create_tween()
	tween.tween_property(sprite, "modulate:a", 0.0, 0.3)
	tween.tween_callback(sprite.queue_free)

	_active_characters.erase(char_id)


func hide_all_characters() -> void:
	for char_id in _active_characters.keys():
		hide_character(char_id)


func _move_character(char_id: String, new_pos: String) -> void:
	if char_id not in _active_characters:
		return

	var entry: Dictionary = _active_characters[char_id]
	var sprite: TextureRect = entry["sprite"]
	var target: Vector2 = _positions.get(new_pos, _positions["center"])
	target -= Vector2(SPRITE_WIDTH / 2.0, 0)

	var tween := create_tween()
	tween.tween_property(sprite, "position", target, 0.4).set_ease(Tween.EASE_IN_OUT)

	entry["position"] = new_pos


func update_expression(char_id: String, expression: String) -> void:
	if char_id not in _active_characters:
		return

	var sprite_path := _resolve_sprite_path(char_id, expression)
	if not sprite_path.is_empty():
		var sprite: TextureRect = _active_characters[char_id]["sprite"]
		sprite.texture = _load_cached(sprite_path)
