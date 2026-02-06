extends Node

## Orchestrates story progression - bridges DialoguePlayer with GameManager.

signal dialogue_file_started(file_path: String)
signal dialogue_file_ended(file_path: String)
signal act_changed(act: String)

var _dialogue_player: Node # Set by GameScene


func set_dialogue_player(player: Node) -> void:
	_dialogue_player = player


func start_dialogue(file_path: String) -> void:
	GameManager.current_dialogue_file = file_path
	dialogue_file_started.emit(file_path)
	if _dialogue_player:
		_dialogue_player.load_and_start(file_path)


func on_dialogue_ended() -> void:
	var file := GameManager.current_dialogue_file
	dialogue_file_ended.emit(file)


func set_act(act: String) -> void:
	GameManager.current_act = act
	act_changed.emit(act)
