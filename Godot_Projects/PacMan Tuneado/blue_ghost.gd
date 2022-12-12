extends Area2D

onready var walls = get_parent().get_node("Navigation2D/Walls")
var path4 = []
var direction = Vector2(0,0)
var speed = 45

func _ready():
	position = walls.get_fantasma_pos()
	path4 = walls.get_path_to_player()
	
func _process(delta):
	if (path4.size() > 1):
		var pos_to_move = path4[0]
		direction = (pos_to_move - position).normalized()
		var distance = position.distance_to(path4[0])
		if (distance>1):
			position += speed * delta * direction
		else:
			path4.remove(0)
	else:
		path4 = walls.get_path_to_player()

func _on_blue_ghost_area_entered(area):
	if (area.name == "Pacman"):
		print("GAME OVER")
