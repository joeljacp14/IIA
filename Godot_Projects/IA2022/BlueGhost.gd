extends KinematicBody2D

var pos = Vector2()
var velocidad = 3000
onready var pacman = get_parent().get_parent().get_node("PacMan")

#func _physics_process(delta):
#	var movimiento = Vector2()
#
#	movimiento = movimiento.normalized()
#	movimiento = move_and_collide(movimiento * velocidad)

func _process(delta):
	pos.x = pacman.global_position.x - global_position.x
	pos.y = pacman.global_position.y - global_position.y

	move_and_slide(pos.normalized() * velocidad * delta)
	
