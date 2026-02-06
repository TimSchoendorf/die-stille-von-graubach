class_name ScreenEffects
extends RefCounted

## Utility for applying screen-level visual effects.


static func create_vignette(parent: Node, intensity: float = 0.3) -> ColorRect:
	var rect := ColorRect.new()
	rect.set_anchors_preset(Control.PRESET_FULL_RECT)
	rect.color = Color(0, 0, 0, intensity)
	rect.mouse_filter = Control.MOUSE_FILTER_IGNORE
	parent.add_child(rect)
	return rect


static func pulse_vignette(rect: ColorRect, target_alpha: float, duration: float) -> Tween:
	var tween := rect.create_tween()
	tween.tween_property(rect, "color:a", target_alpha, duration * 0.5)
	tween.tween_property(rect, "color:a", rect.color.a, duration * 0.5)
	return tween


static func apply_shake(node: CanvasItem, intensity: float = 5.0, duration: float = 0.5) -> void:
	var original_pos: Vector2 = node.position
	var tween := node.create_tween()
	var steps := int(duration / 0.05)
	for i in steps:
		var offset := Vector2(
			randf_range(-intensity, intensity),
			randf_range(-intensity, intensity)
		)
		tween.tween_property(node, "position", original_pos + offset, 0.05)
	tween.tween_property(node, "position", original_pos, 0.05)


static func flicker(node: CanvasItem, count: int = 3, interval: float = 0.1) -> void:
	var tween := node.create_tween()
	for i in count:
		tween.tween_property(node, "modulate:a", 0.0, interval * 0.3)
		tween.tween_property(node, "modulate:a", 1.0, interval * 0.7)
