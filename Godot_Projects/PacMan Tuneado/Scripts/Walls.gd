extends TileMap

onready var half_cell_size = get_cell_size()/2                             #Variable para posición enmedio de la celda
onready var player = get_parent().get_parent().get_node("Pacman")          #Obteniendo nodos de cada personaje
onready var FRosa = get_parent().get_parent().get_node("pink_ghost")
onready var FRojo = get_parent().get_parent().get_node("red_ghost")
onready var FNaranja = get_parent().get_parent().get_node("orange_ghost")
onready var FAzul = get_parent().get_parent().get_node("blue_ghost")

func get_player_init_pos():                   #La posición inicial del jugador
	var pos = map_to_world(Vector2(14,23))    #Convierte tiles a pixeles
	pos.y += half_cell_size.y                 #Posiciona el player en medio de la celda
	return pos

func is_tile_vacant(pos, direction):                                         #Evalúa y devuelve los tiles de navegación                        
	var curr_tile = world_to_map(pos)
	var next_tile = get_cellv(curr_tile + direction)
	var next_tile_pos = Vector2()
	if (next_tile == 12 or next_tile == 13 or next_tile == 14):
		next_tile_pos = map_to_world(curr_tile + direction)+half_cell_size
	else:
		next_tile_pos = relocate(pos)
	return next_tile_pos

func relocate(pos):                                 
	var tile = world_to_map(pos)                        #vuelve la posicón pixeles a tiles
	return map_to_world(tile) + half_cell_size          #los tiles regresa a pixeles pero ahora centrados

func comer(pos):                             #Funcion del pacman comiendo
	var curr_tile= world_to_map(pos)      
	var tile = get_cellv(curr_tile)
	if (tile == 12 or tile == 13):           #Si el pacman pasa por los tile 12 o 13, que son las bolitas, estaría "comiendo"
		set_cellv(curr_tile, 14)             #Los tiles pasan a ser tipo tile 14 que es el recuadro negro sin pac dots
		
func _process(delta):                        
	var contador=0
	for i in range(get_used_rect().size.x):             #Contador de pacdots, si no hay bolitas dentro del mapa, ganas
		for j in range(get_used_rect().size.y):
			var tile = get_cell(i,j)
			if (tile == 12):
				contador += 1
	if (contador == 0):
		print("*****FELICIDADES HAS GANADO*****")
		set_process(false)
		get_tree().change_scene("res://YouWin.tscn")    #llama script para proyectar escena ganadora

func get_fantasma_pos():                    #Posicion incial de los fantasmas
	var pos = map_to_world(Vector2(14,11))
	pos.y += half_cell_size.y               #Posiciona el fantasma enmedio de la celda
	return pos                              #Regresa la posición
