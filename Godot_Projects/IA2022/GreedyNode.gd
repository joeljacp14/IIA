extends Node2D


# Declare member variables here. Examples:
# var a = 2
# var b = "text"


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
		h = 0
		#todo code here!
		self.h = h
