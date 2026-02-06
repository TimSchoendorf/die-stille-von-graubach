extends TextureRect

## Manages background image display with transition effects.

var _transition_tween: Tween


func _ready() -> void:
	expand_mode = TextureRect.EXPAND_IGNORE_SIZE
	stretch_mode = TextureRect.STRETCH_KEEP_ASPECT_COVERED
	mouse_filter = Control.MOUSE_FILTER_IGNORE

	# Manual anchors + offsets (set_anchors_preset gives size 0 on code-created nodes)
	anchor_left = 0.0
	anchor_top = 0.0
	anchor_right = 1.0
	anchor_bottom = 1.0
	offset_left = 0
	offset_top = 0
	offset_right = 0
	offset_bottom = 0
	set_deferred("size", Vector2(1920, 1080))

	# Start hidden (SceneManager handles initial black screen)
	modulate = Color(1, 1, 1, 0)


func change_background(bg_name: String, transition: String = "fade") -> void:
	var bg_path := "res://assets/sprites/backgrounds/" + bg_name
	if not bg_path.ends_with(".png") and not bg_path.ends_with(".jpg"):
		bg_path += ".png"

	if not ResourceLoader.exists(bg_path):
		push_warning("Background not found: " + bg_path)
		return

	var new_texture: Texture2D = load(bg_path)

	match transition:
		"fade":
			_fade_transition(new_texture)
		"instant", "cut":
			texture = new_texture
			modulate = Color.WHITE
		"dissolve":
			_dissolve_transition(new_texture)
		_:
			_fade_transition(new_texture)


func _fade_transition(new_texture: Texture2D, duration: float = 0.5) -> void:
	if _transition_tween:
		_transition_tween.kill()

	_transition_tween = create_tween()
	# Fade out current image
	_transition_tween.tween_property(self, "modulate:a", 0.0, duration * 0.5)
	# Swap texture while invisible, reset to white-but-transparent
	_transition_tween.tween_callback(func():
		texture = new_texture
		modulate = Color(1, 1, 1, 0)
	)
	# Fade in new image
	_transition_tween.tween_property(self, "modulate:a", 1.0, duration * 0.5)


func _dissolve_transition(new_texture: Texture2D, duration: float = 1.0) -> void:
	# Simple dissolve: just a slower fade for now
	_fade_transition(new_texture, duration)


func clear_background() -> void:
	if _transition_tween:
		_transition_tween.kill()

	_transition_tween = create_tween()
	_transition_tween.tween_property(self, "modulate:a", 0.0, 0.5)
	_transition_tween.tween_callback(func():
		texture = null
	)
