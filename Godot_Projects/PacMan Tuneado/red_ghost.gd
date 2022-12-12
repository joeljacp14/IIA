extends Area2D

onready var walls = get_parent().get_node("Navigation2D/Walls")
var path2 = []
var direction = Vector2(0,0)
var speed = 30

func _ready():
	position = walls.get_fantasma_pos()
	path2 = walls.get_path_to_player()
	
func _process(delta):
	if (path2.size() > 1):
		var pos_to_move = path2[0]
		direction = (pos_to_move - position).normalized()
		var distance = position.distance_to(path2[0])
		if (distance>1):
			position += speed * delta * direction
		else:
			path2.remove(0)
	else:
		path2 = walls.get_path_to_player()


func _on_red_ghost_area_entered(area):
	if (area.name == "Pacman"):
		print("GAME OVER")
