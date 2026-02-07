extends Control

## Main game scene - orchestrates all gameplay UI components.

var _dialogue_player: DialoguePlayer
var _background: Node # BackgroundDisplay
var _character_display: Node # CharacterDisplay
var _textbox: Node # Textbox
var _choice_panel: Node # ChoicePanel
var _history_log: Node # HistoryLog
var _journal_ui: Node # JournalUI
var _save_load_ui: Node # SaveLoadUI
var _ending_screen: Node # EndingScreen
var _quick_menu: HBoxContainer

# Effect layer
var _effect_layer: CanvasLayer
var _vignette: ColorRect
var _vignette_tween: Tween


func _ready() -> void:
	# Let clicks pass through to _unhandled_input for text advance
	mouse_filter = Control.MOUSE_FILTER_IGNORE
	_setup_layers()
	_setup_dialogue_player()
	_connect_signals()

	# Always restore journal data into JournalUI
	_restore_journal_data()

	# Detect if we're loading a save (node_id set means resuming mid-dialogue)
	var is_loading := not GameManager.current_node_id.is_empty()

	if is_loading:
		_restore_visual_state()
		_dialogue_player.load_and_start(GameManager.current_dialogue_file, GameManager.current_node_id)
	elif not GameManager.current_dialogue_file.is_empty():
		_dialogue_player.load_and_start(GameManager.current_dialogue_file)
	else:
		# Default: start prologue
		GameManager.current_dialogue_file = "res://data/dialogue/prologue.json"
		_dialogue_player.load_and_start("res://data/dialogue/prologue.json")


func _setup_layers() -> void:
	# Background Layer
	_background = preload("res://scripts/ui/background_display.gd").new()
	_background.name = "BackgroundLayer"
	add_child(_background)

	# Character Layer
	_character_display = preload("res://scripts/ui/character_display.gd").new()
	_character_display.name = "CharacterLayer"
	_character_display.anchor_right = 1.0
	_character_display.anchor_bottom = 1.0
	_character_display.size = Vector2(1920, 1080)
	add_child(_character_display)

	# Effect Layer
	_effect_layer = CanvasLayer.new()
	_effect_layer.name = "EffectLayer"
	_effect_layer.layer = 5
	add_child(_effect_layer)

	_vignette = ColorRect.new()
	_vignette.size = Vector2(1920, 1080)
	_vignette.color = Color(0, 0, 0, 0)
	_vignette.mouse_filter = Control.MOUSE_FILTER_IGNORE
	_effect_layer.add_child(_vignette)

	# UI Layer
	var ui_layer := CanvasLayer.new()
	ui_layer.name = "UILayer"
	ui_layer.layer = 10
	add_child(ui_layer)

	# Quick menu (top right)
	_quick_menu = HBoxContainer.new()
	_quick_menu.name = "QuickMenu"
	_quick_menu.position = Vector2(1920 - 4 * 120 - 3 * 8 - 20, 10)
	_quick_menu.add_theme_constant_override("separation", 8)
	ui_layer.add_child(_quick_menu)

	_create_quick_button(Locale.t("SAVE"), _on_save)
	_create_quick_button(Locale.t("LOAD_SHORT"), _on_load)
	_create_quick_button(Locale.t("HISTORY"), _on_history)
	_create_quick_button(Locale.t("JOURNAL"), _on_journal)

	# Textbox (bottom) — explicit position for CanvasLayer children
	_textbox = preload("res://scripts/ui/textbox.gd").new()
	_textbox.name = "Textbox"
	_textbox.position = Vector2(0, 830)
	_textbox.size = Vector2(1920, 250)
	ui_layer.add_child(_textbox)

	# Choice panel (center)
	_choice_panel = preload("res://scripts/ui/choice_panel.gd").new()
	_choice_panel.name = "ChoicePanel"
	_choice_panel.position = Vector2(660, 300)
	ui_layer.add_child(_choice_panel)

	# Overlay Layer
	var overlay_layer := CanvasLayer.new()
	overlay_layer.name = "OverlayLayer"
	overlay_layer.layer = 20
	add_child(overlay_layer)

	_history_log = preload("res://scripts/ui/history_log.gd").new()
	_history_log.name = "HistoryLog"
	overlay_layer.add_child(_history_log)

	_journal_ui = preload("res://scripts/ui/journal_ui.gd").new()
	_journal_ui.name = "JournalUI"
	overlay_layer.add_child(_journal_ui)

	_save_load_ui = preload("res://scripts/ui/save_load_ui.gd").new()
	_save_load_ui.name = "SaveLoadUI"
	overlay_layer.add_child(_save_load_ui)

	_ending_screen = preload("res://scripts/ui/ending_screen.gd").new()
	_ending_screen.name = "EndingScreen"
	overlay_layer.add_child(_ending_screen)


func _create_quick_button(text: String, callback: Callable) -> void:
	var btn := Button.new()
	btn.text = text
	btn.custom_minimum_size = Vector2(120, 44)
	UITheme.style_quick_button(btn)
	btn.pressed.connect(callback)
	_quick_menu.add_child(btn)


func _setup_dialogue_player() -> void:
	_dialogue_player = DialoguePlayer.new()
	_dialogue_player.name = "DialoguePlayer"
	add_child(_dialogue_player)


func _connect_signals() -> void:
	_dialogue_player.text_requested.connect(_on_text_requested)
	_dialogue_player.narration_requested.connect(_on_narration_requested)
	_dialogue_player.choices_requested.connect(_on_choices_requested)
	_dialogue_player.background_requested.connect(_on_background_requested)
	_dialogue_player.character_requested.connect(_on_character_requested)
	_dialogue_player.effect_requested.connect(_on_effect_requested)
	_dialogue_player.sound_requested.connect(_on_sound_requested)
	_dialogue_player.transition_requested.connect(_on_transition_requested)
	_dialogue_player.journal_requested.connect(_on_journal_requested)
	_dialogue_player.scene_ended.connect(_on_scene_ended)
	_dialogue_player.dialogue_finished.connect(_on_dialogue_finished)

	_textbox.advance_requested.connect(_dialogue_player.advance)
	_choice_panel.choice_selected.connect(_dialogue_player.select_choice)


func _on_text_requested(speaker: String, text: String, color: Color, speaker_id: String = "") -> void:
	_textbox.show_dialogue(speaker, text, color)
	_history_log.add_entry(speaker, text, color)
	_highlight_speaker(speaker_id)


func _on_narration_requested(text: String) -> void:
	_textbox.show_narration(text)
	_history_log.add_entry("", text)
	_highlight_speaker("")


func _on_choices_requested(choices: Array) -> void:
	_textbox.hide_textbox()
	_choice_panel.show_choices(choices)


func _on_background_requested(bg_path: String, transition: String) -> void:
	GameManager.current_background = bg_path
	_background.change_background(bg_path, transition)


func _on_character_requested(char_id: String, expression: String, pos: String, action: String) -> void:
	match action:
		"show":
			_character_display.show_character(char_id, expression, pos)
			GameManager.active_characters[char_id] = {"expression": expression, "position": pos}
		"hide":
			_character_display.hide_character(char_id)
			GameManager.active_characters.erase(char_id)
		"move":
			_character_display.show_character(char_id, expression, pos)
			GameManager.active_characters[char_id] = {"expression": expression, "position": pos}
		"update_expression":
			_character_display.update_expression(char_id, expression)
			if char_id in GameManager.active_characters:
				GameManager.active_characters[char_id]["expression"] = expression
		_:
			_character_display.show_character(char_id, expression, pos)
			GameManager.active_characters[char_id] = {"expression": expression, "position": pos}


func _on_effect_requested(effect_name: String, params: Dictionary) -> void:
	match effect_name:
		"vignette":
			var intensity: float = params.get("intensity", 0.3)
			_animate_vignette(intensity, params.get("duration", 0.5))
		"shake":
			_apply_shake(params.get("intensity", 5.0), params.get("duration", 0.5))
		"flash":
			SceneManager.flash_white(params.get("duration", 0.3))
		"clear":
			_animate_vignette(0.0, 0.3)
			_background.modulate = Color(1, 1, 1, 1)
		"desaturate":
			var amount: float = params.get("amount", 0.5)
			HorrorEffects.desaturate(_background, amount)
		"color_glitch":
			HorrorEffects.color_glitch(_background, params.get("duration", 0.3))
		"flicker":
			ScreenEffects.flicker(_background, params.get("count", 3), params.get("interval", 0.1))
		"heavy_glitch":
			HorrorEffects.heavy_glitch(_background, params.get("duration", 0.8))
		"bg_corruption":
			HorrorEffects.bg_corruption(_background, params.get("intensity", 0.5), params.get("duration", 3.0))
		"sprite_distortion":
			HorrorEffects.sprite_distortion(_character_display, params.get("duration", 2.0))
		"ui_degradation":
			HorrorEffects.ui_degradation(_textbox, params.get("duration", 3.0))
		"breathing_darkness":
			HorrorEffects.breathing_darkness(_background, params.get("min", 0.7), params.get("max", 1.0), params.get("cycle", 4.0))
		"slow_drift":
			HorrorEffects.slow_drift(_background, params.get("offset", 3.0), params.get("duration", 8.0))
		"text_glitch":
			_apply_text_glitch(params.get("intensity", 0.3), params.get("duration", 2.0))


func _animate_vignette(target_alpha: float, duration: float) -> void:
	if _vignette_tween:
		_vignette_tween.kill()
	_vignette_tween = create_tween()
	_vignette_tween.tween_property(_vignette, "color:a", target_alpha, duration)


func _on_sound_requested(sound_type: String, path: String) -> void:
	match sound_type:
		"music":
			AudioManager.play_music(path)
			GameManager.current_music = path
		"sfx":
			AudioManager.play_sfx(path)
		"ambience":
			AudioManager.play_ambience(path)
			GameManager.current_ambience = path
		"stop_music":
			AudioManager.stop_music()
			GameManager.current_music = ""
		"stop_ambience":
			AudioManager.stop_ambience()
			GameManager.current_ambience = ""


func _on_transition_requested(transition_type: String, duration: float) -> void:
	match transition_type:
		"fade_out":
			SceneManager.fade_to_black(duration)
		"fade_in":
			SceneManager.fade_from_black(duration)
		"flash":
			SceneManager.flash_white(duration)


func _on_journal_requested(entry_id: String, title: String, content: String) -> void:
	_journal_ui.add_entry(entry_id, title, content)


func _highlight_speaker(speaker_id: String) -> void:
	# Dim non-speaking characters, brighten the speaker
	for char_id in _character_display._active_characters:
		var entry: Dictionary = _character_display._active_characters[char_id]
		var sprite: TextureRect = entry["sprite"]
		var target_alpha: float = 1.0 if (char_id == speaker_id or speaker_id.is_empty()) else 0.6
		var tween := create_tween()
		tween.tween_property(sprite, "modulate:a", target_alpha, 0.2)


func _restore_journal_data() -> void:
	for entry_id in GameManager.journal_data:
		var data: Dictionary = GameManager.journal_data[entry_id]
		_journal_ui.add_entry(entry_id, data.get("title", ""), data.get("content", ""))


func _restore_visual_state() -> void:
	# Restore background instantly (no fade)
	if not GameManager.current_background.is_empty():
		_background.change_background(GameManager.current_background, "instant")

	# Restore characters instantly
	for char_id in GameManager.active_characters:
		var data: Dictionary = GameManager.active_characters[char_id]
		_character_display.show_character(char_id, data.get("expression", "neutral"), data.get("position", "center"))

	# Restore audio
	if not GameManager.current_music.is_empty():
		AudioManager.play_music(GameManager.current_music, 0.0)
	if not GameManager.current_ambience.is_empty():
		AudioManager.play_ambience(GameManager.current_ambience, 0.0)


func _on_scene_ended(next_file: String) -> void:
	if next_file.is_empty():
		_on_dialogue_finished()
		return

	# Check if it's an ending
	if next_file.begins_with("ending:"):
		var ending_id := next_file.substr(7)
		_textbox.hide_textbox()
		_character_display.hide_all_characters()
		GameManager.active_characters.clear()
		_ending_screen.show_ending(ending_id)
		return

	# Clear characters when transitioning to next file
	_character_display.hide_all_characters()
	GameManager.active_characters.clear()

	# Update dialogue file and reset node_id before auto-save
	GameManager.current_dialogue_file = next_file
	GameManager.current_node_id = ""
	SaveManager.quick_save()

	# Load next dialogue file
	_dialogue_player.load_and_start(next_file)


func _on_dialogue_finished() -> void:
	_textbox.hide_textbox()
	AudioManager.stop_music(1.5)
	AudioManager.stop_ambience(1.5)
	await get_tree().create_timer(1.5).timeout
	SceneManager.change_scene("res://scenes/TitleScreen.tscn")


func _apply_text_glitch(intensity: float, duration: float) -> void:
	# Temporarily corrupt displayed text, then restore
	if not _textbox.visible:
		return
	var original_text: String = _textbox._full_text
	var corrupted := HorrorEffects.corrupt_text(original_text, intensity)
	_textbox._text_label.clear()
	_textbox._text_label.append_text(corrupted)
	_textbox._text_label.visible_characters = -1
	await get_tree().create_timer(duration).timeout
	_textbox._text_label.clear()
	_textbox._text_label.append_text(original_text)
	_textbox._text_label.visible_characters = -1


func _apply_shake(intensity: float, duration: float) -> void:
	var original_pos := position
	var tween := create_tween()
	var steps := int(duration / 0.05)
	for i in steps:
		var offset := Vector2(randf_range(-intensity, intensity), randf_range(-intensity, intensity))
		tween.tween_property(self, "position", original_pos + offset, 0.05)
	tween.tween_property(self, "position", original_pos, 0.05)


func _is_any_overlay_open() -> bool:
	return _save_load_ui.visible or _history_log.visible or _journal_ui.visible


func _on_save() -> void:
	if not _is_any_overlay_open():
		_save_load_ui.open_save()

func _on_load() -> void:
	if not _is_any_overlay_open():
		_save_load_ui.open_load()

func _on_history() -> void:
	if not _is_any_overlay_open():
		_history_log.open_log()

func _on_journal() -> void:
	if not _is_any_overlay_open():
		_journal_ui.open_journal()


func _unhandled_input(event: InputEvent) -> void:
	# Click anywhere to advance text (only when textbox visible, no choices/overlays)
	if event is InputEventMouseButton and event.pressed and event.button_index == MOUSE_BUTTON_LEFT:
		if _textbox.visible and not _choice_panel.visible:
			if not _save_load_ui.visible and not _history_log.visible and not _journal_ui.visible:
				_textbox._handle_advance()
				get_viewport().set_input_as_handled()


func _input(event: InputEvent) -> void:
	if event.is_action_pressed("quick_save"):
		if not _is_any_overlay_open():
			SaveManager.quick_save()
		get_viewport().set_input_as_handled()
	elif event.is_action_pressed("quick_load"):
		if not _is_any_overlay_open() and SaveManager.has_save(0):
			SaveManager.quick_load()
			SceneManager.change_scene("res://scenes/GameScene.tscn")
		get_viewport().set_input_as_handled()
	elif event.is_action_pressed("toggle_history"):
		if not _is_any_overlay_open():
			_history_log.open_log()
		get_viewport().set_input_as_handled()
