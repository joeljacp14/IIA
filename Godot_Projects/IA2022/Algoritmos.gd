extends Node2D

onready var tile_map = $"Obstaculos"
onready var red_ghost = $"RedGhost" #Greedy
#onready var blue_ghost = $"BlueGhost" #fuerza bruta	BFS
onready var yellow_ghost = $"YellowGhost" #fuerzabruta	DFS
onready var pink_ghost = $"PinkGhost" #A*
onready var pacman = $"PacMan" #goal

onready var greedy_visits = []
onready var greedy_fringe = []
onready var astar_visits = []
onready var astar_fringe = []

# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	var tile_pos
	var bfs_path
	var dfs_path
	var greedy_path
	var astar_path
	
	tile_pos = tile_map.world_to_map(pacman.global_position)
	var goal = Vector2(int(round(tile_pos.x)), int(round(tile_pos.y)))
	
	tile_pos = tile_map.world_to_map(red_ghost.global_position)
	var greedy_root = GreedyNode.new(tile_pos.x, tile_pos.y)
	greedy_path = greedy_root.search(goal, greedy_visits, greedy_fringe)
	
	if not greedy_path == null:
		for pos in greedy_path:
			pos.print_position()
	

class Goal: #unused xd
	var posx
	var posy
	
	func _init(posx, posy):
		self.posx = posx
		self.posy = posy

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
		print("Pocision", self.posx, self.posy)
	
	func heuristic(goal):
		var h = 0
		h += abs(goal.x - self.posx) + abs(goal.y - self.posy)
		self.h = h
	
	func expand(goal, fringe):
		var move
		move = GreedyNode.new(0, -1)
		move.heuristic(goal)
		self.branches.append(move)
		
		move = GreedyNode.new(1, 0)
		move.heuristic(goal)
		self.branches.append(move)
		
		move = GreedyNode.new(0, 1)
		move.heuristic(goal)
		self.branches.append(move)
		
		move = GreedyNode.new(-1, 0)
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
		
	
	func search(goal, visits, fringe):
		if self.posx == goal.x and self.posy == goal.y:
			# CONSIDERAR AGREGAR AL CAMINO SOLO VECTORES X, Y EN LUGAR DEL NODO
			var way = []
			way.append(self)
			var parent = self.parent
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
			self.expand(goal, fringe)
		
		if not fringe == []:
			return fringe.pop_front().search(goal, visits, fringe)
		else:
			return null
		
		
		
		
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
