#	Implementacion de el algoritmo Busqueda Primero en Anchura 
#	(BFS / BPA)	Breadth First Search
extends Node2D

var pos = Vector2()
var velocidad = 150
var camino = []
var franja = []
var visitado = {}
var MAX = 5000
onready var walls = $"../Obstaculos"
onready var pacman = $"../PacMan"
onready var blue_ghost = $BlueGhost

func _ready():
	pass
	
	
#	Lo que tenia antes del desmadre que estoy apunto de hacer ._.
#func _process(delta):
#	pos.x = pacman.global_position.x - global_position.x
#	pos.y = pacman.global_position.y - global_position.y
#
#	move_and_collide(pos.normalized() * velocidad * delta)
	
	

func _process(delta):
	var mapa_pos 
	mapa_pos = walls.world_to_map(blue_ghost.global_position)
	var ghost_pos = {"x": int(round(mapa_pos.x)), "y": int(round(mapa_pos.y))}

	mapa_pos = walls.world_to_map(pacman.global_position)
	var pacman_pos = {"x": int(round(mapa_pos.x)), "y": int(round(mapa_pos.y))}

	camino = []
	camino = BFS(ghost_pos, pacman_pos)
	pos = blue_ghost.global_position
	#print(ruta)

	if camino.size() > 0:
		var meta = walls.map_to_world(Vector2(camino[0].x, camino[0].y)) + Vector2(32, 32)
		blue_ghost.global_position = lerp(pos, meta, delta/velocidad)


func posicion_valida(casilla):
	var get_celda = walls.get_cell(casilla.x, casilla.y)
	if (get_celda == 5):
		return get_celda

func BFS (estado, meta):
	if posicion_valida(meta):
		return []
	franja = []
	visitado = []
	franja.push_back({"actual": estado, "anterior": null})
	var iteraciones = 0

	while franja.size() > 0:
		var cuadro_pos = franja.pop_front()
		if es_meta(cuadro_pos.actual, cuadro_pos.anterior, meta):
			break
		iteraciones += 1
		if iteraciones >= MAX:
			return []

	var recorrido = []
	var pos_actual = meta

	while str(pos_actual) in visitado and visitado[str(pos_actual)] != null:
		if pos_actual != null:
			recorrido.append(pos_actual)
		pos_actual = visitado[str(pos_actual)]

	recorrido.invert()
	return recorrido

func es_meta(pos_actual, ultima_pos, meta):
	if !posicion_valida(pos_actual):
		return false

	if str(pos_actual) in visitado:
		return false

	visitado[str(pos_actual)] = ultima_pos

	if pos_actual.x == meta.x and pos_actual.y == meta.y:
		return true

	franja.push_back({"actual": {"x": pos_actual.x, "y": pos_actual.y + 1}, "anterior": pos_actual})
	franja.push_back({"actual": {"x": pos_actual.x + 1, "y": pos_actual.y}, "anterior": pos_actual})
	franja.push_back({"actual": {"x": pos_actual.x, "y": pos_actual.y - 1}, "anterior": pos_actual})
	franja.push_back({"actual": {"x": pos_actual.x - 1, "y": pos_actual.y}, "anterior": pos_actual})

	return false
