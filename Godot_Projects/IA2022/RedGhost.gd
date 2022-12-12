extends KinematicBody2D

var pos : Vector2
var nodo_map : Vector2
var nodo_world : Vector2

var current_position
var nodo
var destinity
var speed = 20
var way = []
onready var player = get_parent().get_node("PacMan")
onready var tile_map = get_parent().get_node("Obstaculos")

#func _process(delta):
#	pos.x = 20 * delta
#	move_and_collide(pos)
#	if $RayCast2D.is_colliding():
#		pos.x = 0
#		pos.y = 10 * delta
#		move_and_collide(pos)	

#func _process(delta):
#	pos.x = player.global_position.x - global_position.x
#	pos.y = player.global_position.y - global_position.y
#
#	move_and_slide(pos.normalized() * velocidad * delta)

func _process(delta):
	current_position = global_position
	if not way == []:
		nodo = way.pop_front()
		destinity = tile_map.map_to_world(Vector2(nodo.x, nodo.y)) + Vector2(16, 16)
		global_position = lerp(current_position, destinity, delta * speed)
