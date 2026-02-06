class_name TextEffects
extends RefCounted

## Provides text manipulation effects for the dialogue system.
## Used for typewriter effect, glitch text, etc.


## Returns text with BBCode for character name coloring
static func format_speaker(name: String, color: Color) -> String:
	var hex := color.to_html(false)
	return "[color=#%s]%s[/color]" % [hex, name]


## Applies a glitch effect by randomly replacing characters
static func glitch_text(text: String, intensity: float = 0.1) -> String:
	var glitch_chars := "̷̸̶̵̴̢̧̨̡̛̖̗̘̙̜̝̞̟̠̣̤̥̦̩̪̫̬̭̮̯̰̱̲̳̹̺̻̼"
	var result := ""
	for i in text.length():
		result += text[i]
		if randf() < intensity:
			result += glitch_chars[randi() % glitch_chars.length()]
	return result


## Creates a slow-reveal effect string (returns array of progressive strings)
static func typewriter_steps(text: String) -> PackedStringArray:
	var steps: PackedStringArray = []
	for i in range(1, text.length() + 1):
		steps.append(text.substr(0, i))
	return steps


## Wraps text in a "shaking" BBCode effect (requires custom RichTextEffect)
static func shake_text(text: String) -> String:
	return "[shake rate=20 level=5]%s[/shake]" % text


## Wraps text in a "wave" BBCode effect
static func wave_text(text: String) -> String:
	return "[wave amp=30 freq=5]%s[/wave]" % text


## Fades text by reducing alpha progressively
static func fade_text(text: String) -> String:
	return "[fade]%s[/fade]" % text


## Redacts text with block characters
static func redact_text(text: String, percentage: float = 0.5) -> String:
	var result := ""
	for c in text:
		if c == " ":
			result += " "
		elif randf() < percentage:
			result += "█"
		else:
			result += c
	return result
