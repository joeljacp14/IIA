extends Node2D


# Declare member variables here. Examples:
# var a = 2
# var b = "text"
var greedy_visits = []
var greedy_fringe = []

# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
#func _process(delta):
#	pass

class GreedyNode:
	var posx
	var posy
	var h # is te heuristic value
	var branches
	var parent
	
	func _init(posx, posy, parent = null):
		self.posx = posx
		self.posy = posy
		self.h = 0
		self.branches = []
		self.parent = parent
	
	func print_position():
		pass
		#print("("self.posx"")
	
	func heuristic(goal):
		var h = 0
		h = abs(goal.posx - self.posx) + abs(goal.posy - self.posy)
		self.h = h
	
	func expand(goal):
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
		
		#for branch in self.branches:
		#	if fringe == []:
		#		fringe.append(branch)
		#	else:
		#		var pos = 0
		#		for node in fringe:
		#			if node.h > branch.h:
		#				fringe.insert(pos, branch)
		#				break
		#			pos += 1
		
	
	func search(goal):
		if self.posx == goal.posx and self.posy == goal.posy:
			var way = []
			way.append(self)
			var parent = self.parent
			while parent:
				way.append(parent)
				parent = parent.parent
			return way
		
		var is_visited = false
		#if not greedy_visits == []:
			#for visited in visits:
				#if self.posx == visited.posx and self.posy == visited.posy:
					#is_visited = true
					#break
		if not is_visited:
			#visits.append(self)
			self.expand(goal)
		
		#if not greedy_fringe == []:
			#return greedy_fringe.pop_front().search(goal)
		#else:
			#return null
		
		
		
		
# Clase tipo arbol referente a la busqueda por anchura
# Para este caso no hay heuritica que implementar, las expansiones son a la % $ @ # &

class BFSNode:
	var turns
	var connections
	var position
	var branches
	var parent
	var queue = []
	var visited = []

	func _init(position, parent, turns, connections):
		self.position = position
		self.parent = parent
		self.branches = []
		self.turns = turns
		self.connections = connections

	func expand():
		for item in connections[self.position]:
			branches.append(BFSNode.new(item, self, self.turns, self.connections))

	func is_goal(goal):
		return self.position == goal

	func get_way():
		var way
		if !self.parent:
			return [self.position]
		way = [self.position]
		way.append_array(self.parent.get_way())
		return way

	func BFS(goal): #	Breadth First Search
		queue.append(self)
		for item in queue:
			if item.is_goal(goal):
				return item.get_way()
			visited.append(item.position)
			item.expand()
			for branch in item.branches:
				if not branch.position in visited:
					queue.append(branch)
