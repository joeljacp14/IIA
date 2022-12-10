#	Implementacion de el algoritmo Busqueda Primero en Anchura 
#	(BFS / BPA)	Breadth First Search

# Estabamos usando clases anidadas inconsientemente u.u
extends Node2D

var pos = Vector2()
var velocidad = 15000
var camino = []
onready var franja : Array = []
onready var visitado : Array = []
var MAX = 5000
onready var walls = $"../Obstaculos"
onready var pacman = $"../PacMan"
onready var blue_ghost = $BlueGhost

var outerblue = self

var bfs_path = []

#func _ready():
#	pass
	
	
#	Lo que tenia antes del desmadre que estoy apunto de hacer ._.
#func _process(delta):
#	pos.x = pacman.global_position.x - global_position.x
#	pos.y = pacman.global_position.y - global_position.y
#
#	move_and_collide(pos.normalized() * velocidad * delta)
	
	

#func _process(delta):
#	var mapa_pos 
#	mapa_pos = walls.world_to_map(blue_ghost.global_position)
#	var ghost_pos = {"x": int(round(mapa_pos.x)), "y": int(round(mapa_pos.y))}
#
#	mapa_pos = walls.world_to_map(pacman.global_position)
#	var pacman_pos = {"x": int(round(mapa_pos.x)), "y": int(round(mapa_pos.y))}
#
#	camino = []
#	camino = BFS(ghost_pos, pacman_pos)
#	pos = blue_ghost.global_position
#	#print(ruta)
#
#	if camino.size() > 0:
#		var meta = walls.map_to_world(Vector2(camino[0].x, camino[0].y)) + Vector2(32, 32)
#		blue_ghost.global_position = lerp(pos, meta, delta/velocidad)
#
#
#func posicion_valida(casilla):
#	var get_celda = walls.get_cell(casilla.x, casilla.y)
#	if (get_celda == 5):
#		return get_celda
#
#func BFS (estado, meta):
#	if posicion_valida(meta):
#		return []
#	franja = []
#	visitado = []
#	franja.push_back({"actual": estado, "anterior": null})
#	var iteraciones = 0
#
#	while franja.size() > 0:
#		var cuadro_pos = franja.pop_front()
#		if es_meta(cuadro_pos.actual, cuadro_pos.anterior, meta):
#			break
#		iteraciones += 1
#		if iteraciones >= MAX:
#			return []
#
#	var recorrido = []
#	var pos_actual = meta
#
#	while str(pos_actual) in visitado and visitado[str(pos_actual)] != null:
#		if pos_actual != null:
#			recorrido.append(pos_actual)
#		pos_actual = visitado[str(pos_actual)]
#
#	recorrido.invert()
#	return recorrido
#
#func es_meta(pos_actual, ultima_pos, meta):
#	if !posicion_valida(pos_actual):
#		return false
#
#	if str(pos_actual) in visitado:
#		return false
#
#	visitado[str(pos_actual)] = ultima_pos
#
#	if pos_actual.x == meta.x and pos_actual.y == meta.y:
#		return true
#
#	franja.push_back({"actual": {"x": pos_actual.x, "y": pos_actual.y + 1}, "anterior": pos_actual})
#	franja.push_back({"actual": {"x": pos_actual.x + 1, "y": pos_actual.y}, "anterior": pos_actual})
#	franja.push_back({"actual": {"x": pos_actual.x, "y": pos_actual.y - 1}, "anterior": pos_actual})
#	franja.push_back({"actual": {"x": pos_actual.x - 1, "y": pos_actual.y}, "anterior": pos_actual})
#
#	return false


func _ready():
	var tile_pos
	var bfs_path
	
	tile_pos = walls.world_to_map(pacman.global_position)
	print("PacMan: ", tile_pos.x, " ", tile_pos.y)
	var goal = Vector2(int(round(tile_pos.x)), int(round(tile_pos.y)))
	
	tile_pos = walls.world_to_map(blue_ghost.global_position)
	print("Blue Ghost: ", tile_pos.x, " ", tile_pos.y)
	var bfs_root = BFSNode.new(tile_pos.x, tile_pos.y, self)
	bfs_path = bfs_root.search(goal, visitado, franja, walls)
	
	if not bfs_path == null:
		print("El camino es: ")
		for posi in bfs_path:
			posi.print_position()
			
func _process(delta):
	var blue_ghost_init = blue_ghost.global_position
	if not bfs_path == []:
		var goal = walls.map_to_world(Vector2(bfs_path[0].posx, bfs_path[0].posy)) + Vector2(32, 32)
		blue_ghost.global_position = lerp(blue_ghost_init, goal, delta/velocidad)			

class BFSNode:
	var posx
	var posy
	var branches
	var parent
	var outerblue

	
	func _init(posx, posy, outerblue=null, parent = null):
		self.posx = posx
		self.posy = posy
		self.branches = []
		self.outerblue = outerblue
		self.parent = parent
	
	func print_position():
		print("x: ", self.posx, ", y: ", self.posy)
	
	func expand(goal, fringe, walls):
		var move
		
		if walls.get_cell(self.posx, self.posy - 1) == -1:
			move = BFSNode.new(self.posx, self.posy - 1, self)
			self.branches.append(move)
		
		if walls.get_cell(self.posx + 1, self.posy) == -1:
			move = BFSNode.new(self.posx + 1, self.posy, self)
			self.branches.append(move)
		
		if walls.get_cell(self.posx, self.posy + 1) == -1:
			move = BFSNode.new(self.posx, self.posy + 1, self)
			self.branches.append(move)
		
		if walls.get_cell(self.posx - 1, self.posy) == -1:
			move = BFSNode.new(self.posx - 1, self.posy, self)
			self.branches.append(move)
		
		for branch in self.branches:
#			fringe.push_in_back(branch)
			fringe.append(branch)
		
#	func search(goal, visits, fringe, walls):
#		var primero = []
#		fringe.append(self)
#		while not fringe == []:
#			primero = fringe.pop_front()
#			if (primero.posx == goal.x) and (primero.posy == goal.y):
#				self.outerblue.camino.append(primero)
#				var papa = primero.parent
#				while papa:
#					self.outerblue.camino.append(papa)
#					papa = papa.parent
#				print("Te encontre!!!")
#				return self.outerblue.camino
#
#			es_visitado = false
#			for x, y in visits:
#				if (primero.posx == x) and (primero.posy == y):
#					es_visitado = true
#					break
#			if not es_visitado:
#				visits.append([primero.posx, primero.posy])
#
#				primero.expand()
#
#				for hijo in primero.branches:
#					if fringe == []:
#						fringe.append(hijo)
#					else:
#						break
#		return []
		
	
	func search(goal, visits, fringe, walls):
		var way = []
		#print("Se atiende azul: (", self.posx, ", ", self.posy, ")")
		if self.posx == goal.x and self.posy == goal.y:
			print("Te encontre!!!")
			# CONSIDERAR AGREGAR AL CAMINO SOLO VECTORES X, Y EN LUGAR DEL NODO
			way.append(self)
			var parent = self.outerblue
			print("Padre de la Solucion")
			parent.print_position()
			while parent:
				way.append(parent)
				parent = parent.parent
			return way

		var is_visited = false
		if not visits == []:
			for visited in visits:
				if self.posx == visited.posx and self.posy == visited.posy:
					is_visited = true
					break

		if not is_visited:
			visits.append(self)
			self.expand(goal, fringe, walls)

		if not fringe == []:
			return fringe.pop_front().search(goal, visits, fringe, walls)
