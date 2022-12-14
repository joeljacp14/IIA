extends Control

func _on_Again_pressed():
	get_tree().change_scene("res://Juego.tscn")


func _on_Exit_pressed():
	get_tree().quit()
