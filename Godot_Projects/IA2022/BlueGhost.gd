#	Implementacion de el algoritmo Busqueda Primero en Anchura 
#	(BFS / BPA)	Breadth First Search
extends KinematicBody2D

var camino = []
onready var blue_ghost = $"../BlueGhost"
onready var pacman = $"../PacMan"
var ghost_position : Vector2
var pacman_position : Vector2

var pos = Vector2()
var velocidad = 150


func _ready():
	pass

#func _process(delta):
#	pos.x = 20 * delta
#	move_and_collide(pos)
#	if $RayCast2D.is_colliding():
#		pos.x = 0
#		pos.y = 10 * delta
#		move_and_collide(pos)	

func _process(delta):
	pos.x = pacman.global_position.x - global_position.x
	pos.y = pacman.global_position.y - global_position.y
	print(pos)
#
	move_and_collide(pos.normalized() * velocidad * delta)
