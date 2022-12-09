extends KinematicBody2D

var pos : Vector2
var nodo : Vector2
var speed = 50
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
	pos.x = 0
	pos.y = 0
	move_and_slide(pos)
	print(tile_map.map_to_world(Vector2(1, 1)))
	if way == []:
		print("Se termino el camino")
		return
	nodo = way.pop_front()
	print("Nodo map ", nodo)
	nodo = tile_map.map_to_world(nodo)
	print("Nodo world", nodo)
	print("Current position ", global_position)
	if global_position.y == nodo.y:
		pos.x = nodo.x * delta * speed
		pos.y = 0
	if global_position.x == nodo.x:
		pos.x = 0
		pos.y = nodo.y * delta * speed
		
	print("Moverse a ", pos)
	print("====================================")
	
	move_and_slide(pos)
