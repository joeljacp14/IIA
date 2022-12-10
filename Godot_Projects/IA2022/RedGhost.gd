extends KinematicBody2D

var pos : Vector2
var nodo_map : Vector2
var nodo_world : Vector2
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
	#pos.x = 0
	#pos.y = 0
	#move_and_slide(pos)
	var curren_position_world = global_position
	print("Current position world: ", curren_position_world)
	var curren_position_map = tile_map.world_to_map(Vector2(int(round(curren_position_world.x)), int(round(curren_position_world.y))))
	#curren_position = Vector2(int(round(curren_position.x)), int(round(curren_position.y)))
	
	if way == []:
		return
		
	nodo_map = way.pop_front()
	nodo_world = tile_map.map_to_world(nodo_map)
	nodo_world.x = nodo_world.x + 32
	nodo_world.y = nodo_world.y + 32
	
	print("Nodo map ", nodo_map)
	print("Nodo world centered", nodo_world)
	print("Current position map: ", curren_position_map)
	
	if curren_position_map.x == nodo_map.x and curren_position_map.y == nodo_map.y:
		pos.x = 0
		pos.y = 0
	else:
		if curren_position_map.y == nodo_map.y:
			pos.x = nodo_world.x - curren_position_world.x 
			pos.y = 0
		if curren_position_map.x == nodo_map.x:
			pos.x = 0
			pos.y = nodo_world.y - curren_position_world.y
	
	print("Se tiene que mover a -> ", pos)
	print("====================================")
	
	move_and_slide(pos)
	#move_toward(curren_position_world, nodo_world)
