extends KinematicBody2D
var pos = Vector2()
var velocidad = 150
onready var player = get_parent().get_node("Agente")

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
	pos.x = player.global_position.x - global_position.x
	pos.y = player.global_position.y - global_position.y
	print(pos)
#
	move_and_collide(pos.normalized() * velocidad * delta)
