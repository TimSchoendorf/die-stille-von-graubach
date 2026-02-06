class_name HorrorEffects
extends RefCounted

## Horror-specific visual effects for atmosphere.

# Glitch characters for text corruption
const GLITCH_CHARS := "̷̸̵̶̴̢̧̨̡̛̖̗̘̙̜̝̞̟̠̣̤̥̦̩̪̫̬̭̮̯̰̱̲̳̹̺̻̼"
const CORRUPT_CHARS := "█▓▒░╫╬╧╨╩╪╤╥╦╣╠╟╞╝╜╛╚╙╘╗╖╕╔╓╒║═"


## Slowly pulses the screen darker and lighter
static func breathing_darkness(node: CanvasItem, min_mod: float = 0.7, max_mod: float = 1.0, cycle: float = 4.0) -> Tween:
	var tween := node.create_tween()
	tween.set_loops()
	tween.tween_property(node, "modulate",
		Color(min_mod, min_mod, min_mod), cycle * 0.5).set_ease(Tween.EASE_IN_OUT)
	tween.tween_property(node, "modulate",
		Color(max_mod, max_mod, max_mod), cycle * 0.5).set_ease(Tween.EASE_IN_OUT)
	return tween


## Creates a brief visual distortion (color shift)
static func color_glitch(node: CanvasItem, duration: float = 0.3) -> void:
	var original: Color = node.modulate
	var tween := node.create_tween()
	tween.tween_property(node, "modulate", Color(1.3, 0.8, 0.8), duration * 0.2)
	tween.tween_property(node, "modulate", Color(0.8, 1.1, 1.2), duration * 0.2)
	tween.tween_property(node, "modulate", Color(0.5, 0.5, 0.6), duration * 0.2)
	tween.tween_property(node, "modulate", original, duration * 0.4)


## Desaturates the scene gradually
static func desaturate(node: CanvasItem, amount: float = 0.5, duration: float = 2.0) -> Tween:
	var gray := lerpf(1.0, 0.6, amount)
	var target := Color(gray, gray, gray)
	var tween := node.create_tween()
	tween.tween_property(node, "modulate", target, duration)
	return tween


## Subtle offset for an unsettling feel
static func slow_drift(node: CanvasItem, max_offset: float = 3.0, duration: float = 8.0) -> Tween:
	var origin: Vector2 = node.position
	var tween := node.create_tween()
	tween.set_loops()
	tween.tween_property(node, "position",
		origin + Vector2(max_offset, max_offset * 0.5), duration * 0.25).set_ease(Tween.EASE_IN_OUT)
	tween.tween_property(node, "position",
		origin + Vector2(-max_offset * 0.7, max_offset), duration * 0.25).set_ease(Tween.EASE_IN_OUT)
	tween.tween_property(node, "position",
		origin + Vector2(-max_offset, -max_offset * 0.3), duration * 0.25).set_ease(Tween.EASE_IN_OUT)
	tween.tween_property(node, "position",
		origin, duration * 0.25).set_ease(Tween.EASE_IN_OUT)
	return tween


## Rapid multi-color glitch with chromatic aberration feel
static func heavy_glitch(node: CanvasItem, duration: float = 0.8) -> void:
	var original: Color = node.modulate
	var tween := node.create_tween()
	var steps := 8
	var step_dur := duration / (steps + 1)
	for i in steps:
		var r := randf_range(0.5, 1.5)
		var g := randf_range(0.5, 1.5)
		var b := randf_range(0.5, 1.5)
		tween.tween_property(node, "modulate", Color(r, g, b), step_dur)
	tween.tween_property(node, "modulate", original, step_dur)


## Gradually corrupts a background by darkening and tinting it sickly green
static func bg_corruption(node: CanvasItem, intensity: float = 0.5, duration: float = 3.0) -> Tween:
	var r := lerpf(1.0, 0.6, intensity)
	var g := lerpf(1.0, 0.7, intensity)
	var b := lerpf(1.0, 0.5, intensity)
	var tween := node.create_tween()
	tween.tween_property(node, "modulate", Color(r, g, b), duration)
	return tween


## Distorts a character sprite: scale wobble + position jitter
static func sprite_distortion(node: CanvasItem, duration: float = 2.0) -> void:
	var original_scale: Vector2 = node.scale
	var original_pos: Vector2 = node.position
	var tween := node.create_tween()
	var steps := 12
	var step_dur := duration / (steps + 1)
	for i in steps:
		var sx := randf_range(0.95, 1.05)
		var sy := randf_range(0.97, 1.03)
		var ox := randf_range(-4.0, 4.0)
		var oy := randf_range(-2.0, 2.0)
		tween.tween_property(node, "scale", Vector2(sx, sy), step_dur)
		tween.parallel().tween_property(node, "position", original_pos + Vector2(ox, oy), step_dur)
	tween.tween_property(node, "scale", original_scale, step_dur)
	tween.parallel().tween_property(node, "position", original_pos, step_dur)


## Makes a UI element appear to degrade: flicker + slight offset + alpha instability
static func ui_degradation(node: CanvasItem, duration: float = 3.0) -> void:
	var tween := node.create_tween()
	var steps := 15
	var step_dur := duration / (steps + 1)
	for i in steps:
		var alpha := randf_range(0.4, 1.0)
		var ox := randf_range(-3.0, 3.0)
		tween.tween_property(node, "modulate:a", alpha, step_dur * 0.3)
		tween.tween_property(node, "position:x", node.position.x + ox, step_dur * 0.7)
	tween.tween_property(node, "modulate:a", 1.0, step_dur)
	tween.tween_property(node, "position:x", node.position.x, step_dur * 0.1)


## Returns a corrupted version of text with random block characters
static func corrupt_text(text: String, intensity: float = 0.3) -> String:
	var result := ""
	for ch in text:
		if randf() < intensity and ch != " ":
			result += CORRUPT_CHARS[randi() % CORRUPT_CHARS.length()]
		else:
			result += ch
	return result
