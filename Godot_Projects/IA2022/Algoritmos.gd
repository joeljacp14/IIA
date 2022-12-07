extends Node2D

onready var tile_map = $"Obstaculos"
onready var red_ghost = $"RedGhost" #Greedy
#onready var blue_ghost = $"BlueGhost" #fuerza bruta	BFS
onready var yellow_ghost = $"YellowGhost" #fuerzabruta	DFS
onready var pink_ghost = $"PinkGhost" #A*
onready var pacman = $"PacMan" #goal

onready var greedy_visits : Array = []
onready var greedy_fringe : Array = []
onready var astar_visits = []
onready var astar_fringe = []


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _ready():
	var tile_pos
	var bfs_path
	var dfs_path
	var greedy_path
	var astar_path
	
	tile_pos = tile_map.world_to_map(pacman.global_position)
	print("PAC MAN: ", tile_pos.x, " ", tile_pos.y)
	var goal = Vector2(int(round(tile_pos.x)), int(round(tile_pos.y)))
	
	tile_pos = tile_map.world_to_map(red_ghost.global_position)
	print("RED GHOST: ", tile_pos.x, " ", tile_pos.y)
	var greedy_root = GreedyNode.new(tile_pos.x, tile_pos.y)
	greedy_path = greedy_root.search(goal, greedy_visits, greedy_fringe, tile_map)
	
	if not greedy_path == null:
		print("camino a la solucion")
		for pos in greedy_path:
			pos.print_position()

class GreedyNode:
	var posx
	var posy
	var h # es el valor de la heuristica del nodo
	var branches
	var parent
	
	func _init(posx, posy, parent = null):
		self.posx = posx
		self.posy = posy
		self.h = 0
		self.branches = []
		self.parent = parent
	
	func print_position():
		print("x: ", self.posx, ", y: ", self.posy)
	
	func heuristic(goal):
		var h = 0
		h += abs(goal.x - self.posx) + abs(goal.y - self.posy)
		self.h = h
	
	func expand(goal, fringe, tile_map):
		var move
		
		if tile_map.get_cell(self.posx, self.posy - 1) == -1:
			move = GreedyNode.new(self.posx, self.posy - 1, self)
			move.heuristic(goal)
			self.branches.append(move)
		
		if tile_map.get_cell(self.posx + 1, self.posy) == -1:
			move = GreedyNode.new(self.posx + 1, self.posy, self)
			move.heuristic(goal)
			self.branches.append(move)
		
		if tile_map.get_cell(self.posx, self.posy + 1) == -1:
			move = GreedyNode.new(self.posx, self.posy + 1, self)
			move.heuristic(goal)
			self.branches.append(move)
		
		if tile_map.get_cell(self.posx - 1, self.posy) == -1:
			move = GreedyNode.new(self.posx - 1, self.posy, self)
			move.heuristic(goal)
			self.branches.append(move)
		
		for branch in self.branches:
			if fringe == []:
				fringe.append(branch)
			else:
				var pos = 0
				for node in fringe:
					if node.h > branch.h:
						fringe.insert(pos, branch)
						break
					pos += 1
		
	
	func search(goal, visits, fringe, tile_map):
		print("Se atiende")
		self.print_position()
		if self.posx == goal.x and self.posy == goal.y:
			print("SE ENCONTRO LA META!!!")
			# CONSIDERAR AGREGAR AL CAMINO SOLO VECTORES X, Y EN LUGAR DEL NODO
			var way = []
			way.append(self)
			var parent = self.parent
			print("padre de la sulocion")
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
			self.expand(goal, fringe, tile_map)
		
		if not fringe == []:
			return fringe.pop_front().search(goal, visits, fringe, tile_map)
		
		
		
		
# Clase tipo arbol referente a la busqueda por anchura
# Para este caso no hay heuritica que implementar, las expansiones son a la % $ @ # &

#class BFSNode:
#	var turns
#	var connections
#	var position
#	var branches
#	var parent
#	var queue = []
#	var visited = []
#
#	func _init(position, parent, turns, connections):
#		self.position = position
#		self.parent = parent
#		self.branches = []
#		self.turns = turns
#		self.connections = connections
#
#	func expand():
#		for item in connections[self.position]:
#			branches.append(BFSNode.new(item, self, self.turns, self.connections))
#
#	func is_goal(goal):
#		return self.position == goal
#
#	func get_way():
#		var way
#		if !self.parent:
#			return [self.position]
#		way = [self.position]
#		way.append_array(self.parent.get_way())
#		return way
#
#	func BFS(goal): #	Breadth First Search
#		queue.append(self)
#		for item in queue:
#			if item.is_goal(goal):
#				return item.get_way()
#			visited.append(item.position)
#			item.expand()
#			for branch in item.branches:
#				if not branch.position in visited:
#					queue.append(branch)
