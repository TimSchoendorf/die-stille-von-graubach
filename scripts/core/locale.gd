extends Node

## Lightweight localization system using a flat Dictionary of translations.
## Supports: de, en, fr, es, it
## UI translation data lives in locale_data.gd (LocaleData class).

signal locale_changed

const LOCALES: Array[String] = ["de", "en", "fr", "es", "it"]
const _Data := preload("res://scripts/core/locale_data.gd")
const _Builder := preload("res://scripts/ui/settings_builder.gd")

var current_locale: String = "de"

# Dialogue translations loaded from data/translations/{locale}.json
var _dialogue_translations: Dictionary = {}


func _ready() -> void:
	# Load saved settings (including language) at startup
	_Builder.load_settings()
	_load_dialogue_translations()


func t(key: String) -> String:
	if key in _Data.TRANSLATIONS:
		var entry: Dictionary = _Data.TRANSLATIONS[key]
		if current_locale in entry:
			return entry[current_locale]
		# Fallback to German
		if "de" in entry:
			return entry["de"]
	push_warning("Locale: missing translation key '%s'" % key)
	return key


func set_locale(code: String) -> void:
	if code in _Data.LOCALE_NAMES:
		current_locale = code
		_load_dialogue_translations()
		locale_changed.emit()


func get_locale_display_name(code: String) -> String:
	return _Data.LOCALE_NAMES.get(code, code)


# ── Dialogue Translation System ──

func _load_dialogue_translations() -> void:
	_dialogue_translations.clear()
	if current_locale == "de":
		return
	var path := "res://data/translations/%s.json" % current_locale
	if not FileAccess.file_exists(path):
		return
	var file := FileAccess.open(path, FileAccess.READ)
	if not file:
		return
	var json := JSON.new()
	if json.parse(file.get_as_text()) == OK:
		_dialogue_translations = json.data


## Translate dialogue/narration text. Returns fallback (German) if no translation exists.
func td(file_path: String, node_id: String, field: String, fallback: String) -> String:
	if current_locale == "de":
		return fallback
	var file_data: Dictionary = _dialogue_translations.get(file_path, {})
	var node_data = file_data.get(node_id, {})
	if node_data is Dictionary and field in node_data:
		return node_data[field]
	return fallback


## Translate choice text by index.
func td_choice(file_path: String, node_id: String, choice_index: int, fallback: String) -> String:
	if current_locale == "de":
		return fallback
	var file_data: Dictionary = _dialogue_translations.get(file_path, {})
	var node_data = file_data.get(node_id, {})
	if node_data is Dictionary:
		var choices: Array = node_data.get("choices", [])
		if choice_index < choices.size():
			return choices[choice_index]
	return fallback


## Translate character display name.
func tc(char_id: String, fallback: String) -> String:
	if current_locale == "de":
		return fallback
	var chars: Dictionary = _dialogue_translations.get("_characters", {})
	var translated_name = chars.get(char_id, "")
	if translated_name is String and translated_name != "":
		return translated_name
	return fallback
