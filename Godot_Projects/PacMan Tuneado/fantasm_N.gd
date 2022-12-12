extends Area2D

onready var walls = get_find_parent().get_node("walls")

func _ready():
	position = walls.get_enemy_pos()
	pass
# Declare member variables here. Examples:
# var a = 2
