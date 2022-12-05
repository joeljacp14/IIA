extends TileMap


# Declare member variables here. Examples:
var mitadc = get_cell_size()/2


# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
#func _process(delta):
#	pass

func get_initial(x, y): #funcion para poner a cualquiera en la posición inicial
	var pos = map_to_world(Vector2(x, y))
	pos.y += mitadc.y #arregla pos en y 
	return pos

func fin_partida(ghost, pacman):
	return ghost == pacman
