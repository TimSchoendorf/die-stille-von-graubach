extends Node

## Handles scene transitions with fade effects.

signal transition_started
signal transition_midpoint
signal transition_completed

var _transition_layer: CanvasLayer
var _color_rect: ColorRect
var _is_transitioning: bool = false


func _ready() -> void:
	_setup_transition_layer()


func _setup_transition_layer() -> void:
	_transition_layer = CanvasLayer.new()
	_transition_layer.layer = 100
	add_child(_transition_layer)

	_color_rect = ColorRect.new()
	_color_rect.color = Color.BLACK
	_color_rect.position = Vector2(0, 0)
	_color_rect.size = Vector2(1920, 1080)
	_color_rect.mouse_filter = Control.MOUSE_FILTER_IGNORE
	_color_rect.modulate.a = 0.0
	_transition_layer.add_child(_color_rect)


func change_scene(scene_path: String, duration: float = 0.5) -> void:
	if _is_transitioning:
		return

	_is_transitioning = true
	transition_started.emit()

	# Fade to black
	var tween := create_tween()
	tween.tween_property(_color_rect, "modulate:a", 1.0, duration)
	await tween.finished

	transition_midpoint.emit()

	# Change scene
	get_tree().change_scene_to_file(scene_path)

	# Wait a frame for the new scene to load
	await get_tree().process_frame

	# Fade from black
	tween = create_tween()
	tween.tween_property(_color_rect, "modulate:a", 0.0, duration)
	await tween.finished

	_is_transitioning = false
	transition_completed.emit()


func fade_to_black(duration: float = 0.5) -> void:
	var tween := create_tween()
	tween.tween_property(_color_rect, "modulate:a", 1.0, duration)
	await tween.finished


func fade_from_black(duration: float = 0.5) -> void:
	var tween := create_tween()
	tween.tween_property(_color_rect, "modulate:a", 0.0, duration)
	await tween.finished


func flash_white(duration: float = 0.3) -> void:
	_color_rect.color = Color.WHITE
	_color_rect.modulate.a = 1.0
	var tween := create_tween()
	tween.tween_property(_color_rect, "modulate:a", 0.0, duration)
	await tween.finished
	_color_rect.color = Color.BLACK


func is_transitioning() -> bool:
	return _is_transitioning
