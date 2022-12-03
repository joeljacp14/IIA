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
		#todo code here!
		pass
	
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
		if not visits == []:
			for visited in visits:
				if self.posx == visited.posx and self.posy == visited.posy:
					is_visited = true
					break
		if not is_visited:
			visits.append(self)
			self.expand(goal)
		
