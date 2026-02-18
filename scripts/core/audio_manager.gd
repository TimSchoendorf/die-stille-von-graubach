extends Node

## Manages music, sound effects, and ambience playback.
## Looping via finished signal (runtime loop_mode breaks QOA streams).

var music_player: AudioStreamPlayer
var sfx_player: AudioStreamPlayer
var ambience_player: AudioStreamPlayer

var music_volume: float = 0.8
var sfx_volume: float = 1.0
var ambience_volume: float = 0.6
var master_volume: float = 1.0

var _current_music: String = ""
var _current_ambience: String = ""

# Fade tween reference
var _music_tween: Tween


func _ready() -> void:
	music_player = AudioStreamPlayer.new()
	music_player.bus = "Master"
	add_child(music_player)
	music_player.finished.connect(_on_music_finished)

	sfx_player = AudioStreamPlayer.new()
	sfx_player.bus = "Master"
	add_child(sfx_player)

	ambience_player = AudioStreamPlayer.new()
	ambience_player.bus = "Master"
	add_child(ambience_player)
	ambience_player.finished.connect(_on_ambience_finished)

	_apply_volumes()


func play_music(path: String, fade_duration: float = 1.0) -> void:
	if path == _current_music and music_player.playing:
		return

	var full_path := "res://assets/audio/music/" + path
	if not ResourceLoader.exists(full_path):
		push_warning("Music not found: " + full_path)
		return

	_current_music = path

	if music_player.playing and fade_duration > 0.0:
		_crossfade_music(full_path, fade_duration)
	else:
		music_player.stream = load(full_path)
		music_player.volume_db = linear_to_db(music_volume * master_volume)
		music_player.play()


func stop_music(fade_duration: float = 1.0) -> void:
	_current_music = ""
	if fade_duration > 0.0 and music_player.playing:
		if _music_tween:
			_music_tween.kill()
			_music_tween = null
		_music_tween = create_tween()
		_music_tween.tween_property(music_player, "volume_db", -80.0, fade_duration)
		_music_tween.tween_callback(func():
			music_player.stop()
			_music_tween = null)
	else:
		music_player.stop()
		if _music_tween:
			_music_tween.kill()
			_music_tween = null


func play_sfx(path: String) -> void:
	var full_path := "res://assets/audio/sfx/" + path
	if not ResourceLoader.exists(full_path):
		# TODO(audio): Replace fallback once dedicated sfx_knock_3x.wav is finalized in assets/audio/sfx.
		if path == "sfx_knock_3x.wav":
			var fallback_path := "res://assets/audio/sfx/door_creak.wav"
			if ResourceLoader.exists(fallback_path):
				push_warning("SFX not found: " + full_path + " — using fallback: " + fallback_path)
				full_path = fallback_path
			else:
				push_warning("SFX not found: " + full_path + " (fallback missing: " + fallback_path + ")")
				return
		else:
			push_warning("SFX not found: " + full_path)
			return

	sfx_player.stream = load(full_path)
	sfx_player.volume_db = linear_to_db(sfx_volume * master_volume)
	sfx_player.play()


func play_ambience(path: String, fade_duration: float = 2.0) -> void:
	if path == _current_ambience and ambience_player.playing:
		return

	var full_path := "res://assets/audio/ambience/" + path
	if not ResourceLoader.exists(full_path):
		push_warning("Ambience not found: " + full_path)
		return

	_current_ambience = path
	ambience_player.stream = load(full_path)
	ambience_player.volume_db = -80.0
	ambience_player.play()

	var tween := create_tween()
	tween.tween_property(ambience_player, "volume_db",
		linear_to_db(ambience_volume * master_volume), fade_duration)


func stop_ambience(fade_duration: float = 2.0) -> void:
	_current_ambience = ""
	if fade_duration > 0.0 and ambience_player.playing:
		var tween := create_tween()
		tween.tween_property(ambience_player, "volume_db", -80.0, fade_duration)
		tween.tween_callback(ambience_player.stop)
	else:
		ambience_player.stop()


func set_music_volume(vol: float) -> void:
	music_volume = clampf(vol, 0.0, 1.0)
	_apply_volumes()


func set_sfx_volume(vol: float) -> void:
	sfx_volume = clampf(vol, 0.0, 1.0)
	_apply_volumes()


func set_ambience_volume(vol: float) -> void:
	ambience_volume = clampf(vol, 0.0, 1.0)
	_apply_volumes()


func set_master_volume(vol: float) -> void:
	master_volume = clampf(vol, 0.0, 1.0)
	_apply_volumes()


func _on_music_finished() -> void:
	if not _current_music.is_empty():
		music_player.play()


func _on_ambience_finished() -> void:
	if not _current_ambience.is_empty():
		ambience_player.play()


func _apply_volumes() -> void:
	if music_player.playing:
		music_player.volume_db = linear_to_db(music_volume * master_volume)
	if ambience_player.playing:
		ambience_player.volume_db = linear_to_db(ambience_volume * master_volume)


func _crossfade_music(new_path: String, duration: float) -> void:
	if _music_tween:
		_music_tween.kill()
		_music_tween = null

	_music_tween = create_tween()
	_music_tween.tween_property(music_player, "volume_db", -80.0, duration * 0.5)
	_music_tween.tween_callback(func():
		music_player.stream = load(new_path)
		music_player.play()
	)
	_music_tween.tween_property(music_player, "volume_db",
		linear_to_db(music_volume * master_volume), duration * 0.5)
	_music_tween.tween_callback(func(): _music_tween = null)
