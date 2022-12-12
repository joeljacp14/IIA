extends Area2D

onready var walls = get_parent().get_node("Navigation2D/Walls")
var path3 = []
var direction = Vector2(0,0)
var speed = 40

func _ready():
	position = walls.get_fantasma_pos()
	path3 = walls.get_path_to_player()
	
func _process(delta):
	if (path3.size() > 1):
		var pos_to_move = path3[0]
		direction = (pos_to_move - position).normalized()
		var distance = position.distance_to(path3[0])
		if (distance>1):
			position += speed * delta * direction
		else:
			path3.remove(0)
	else:
		path3 = walls.get_path_to_player()


func _on_orange_ghost_area_entered(area):
	if (area.name == "Pacman"):
		print("GAME OVER")
