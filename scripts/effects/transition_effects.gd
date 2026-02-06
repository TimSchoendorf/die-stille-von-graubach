class_name TransitionEffects
extends RefCounted

## Scene transition effects beyond simple fades.


## Iris wipe (circle closing/opening) - creates a mask effect
static func iris_close(parent: Node, duration: float = 1.0, color: Color = Color.BLACK) -> void:
	var rect := ColorRect.new()
	rect.set_anchors_preset(Control.PRESET_FULL_RECT)
	rect.color = color
	rect.modulate.a = 0.0
	parent.add_child(rect)

	var tween := rect.create_tween()
	tween.tween_property(rect, "modulate:a", 1.0, duration)
	tween.tween_callback(rect.queue_free)


static func iris_open(parent: Node, duration: float = 1.0, color: Color = Color.BLACK) -> void:
	var rect := ColorRect.new()
	rect.set_anchors_preset(Control.PRESET_FULL_RECT)
	rect.color = color
	rect.modulate.a = 1.0
	parent.add_child(rect)

	var tween := rect.create_tween()
	tween.tween_property(rect, "modulate:a", 0.0, duration)
	tween.tween_callback(rect.queue_free)


## Slide transition - wipes from one side
static func wipe(parent: Node, direction: String = "left", duration: float = 0.5) -> void:
	var rect := ColorRect.new()
	rect.color = Color.BLACK
	rect.size = Vector2(1920, 1080)
	parent.add_child(rect)

	match direction:
		"left":
			rect.position.x = -1920
			var tween := rect.create_tween()
			tween.tween_property(rect, "position:x", 0.0, duration)
			tween.tween_callback(rect.queue_free)
		"right":
			rect.position.x = 1920
			var tween := rect.create_tween()
			tween.tween_property(rect, "position:x", 0.0, duration)
			tween.tween_callback(rect.queue_free)
