extends KinematicBody2D

var pos : Vector2
var speed = 5
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
	if way == []:
		print("Se termino el camino")
		return
	pos = tile_map.map_to_world(way.pop_front())
	print(pos)
	
	move_and_slide(pos * delta * speed)
