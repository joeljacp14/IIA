extends Area2D

onready var walls = get_parent().get_node("Navigation2D/Walls")
onready var game = get_parent()
onready var pacman = get_parent().get_node("Pacman") #goal

onready var visits : Array = []
onready var fringe : Array = []

var path = []
var direction = Vector2(0,0)
var speed = 30
var greedy_root
var tile_pos

func _ready():
	
	position = walls.get_fantasma_pos()
	
	tile_pos = walls.world_to_map(pacman.global_position)
	print("PAC MAN: ", tile_pos.x, " ", tile_pos.y)
	var goal = Vector2(int(round(tile_pos.x)), int(round(tile_pos.y)))
	
	tile_pos = walls.world_to_map(global_position)
	print("RED GHOST: ", tile_pos.x, " ", tile_pos.y)
	greedy_root = GreedyNode.new(tile_pos.x, tile_pos.y)
	path = greedy_root.search(goal, visits, fringe, walls)
			
	path = walls.get_path_to_player("red_ghost")
	
func _process(delta):
	if not path == null:
		if (path.size() > 1):
			var pos_to_move = path[0]
			direction = (pos_to_move - position).normalized()
			var distance = position.distance_to(path[0])
			if (distance>1):
				position += speed * delta * direction
			else:
				path.remove(0)
		else:
			#position = walls.get_fantasma_pos()
			
			tile_pos = walls.world_to_map(pacman.global_position)
			print("PAC MAN: ", tile_pos.x, " ", tile_pos.y)
			var goal = Vector2(int(round(tile_pos.x)), int(round(tile_pos.y)))
			
			tile_pos = walls.world_to_map(global_position)
			print("RED GHOST: ", tile_pos.x, " ", tile_pos.y)
			greedy_root = GreedyNode.new(tile_pos.x, tile_pos.y)
			visits.clear()
			fringe.clear()
			path = greedy_root.search(goal, visits, fringe, walls)
			
			#path = walls.get_path_to_player("red_ghost")
	else:
		#position = walls.get_fantasma_pos()
		print("ya no hay camino rojo")
		return


func _on_red_ghost_area_entered(area):
	if (area.name == "Pacman"):
		print("GAME OVER")

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
		self.h = abs(goal.x - self.posx) + abs(goal.y - self.posy)
	
	func expand(goal, fringe, tile_map):
		var move
		var cell
		
		cell = tile_map.get_cell(self.posx, self.posy - 1)
		if cell == 12 or cell == 13 or cell == 14:
			move = GreedyNode.new(self.posx, self.posy - 1, self)
			move.heuristic(goal)
			self.branches.append(move)
		
		cell = tile_map.get_cell(self.posx + 1, self.posy)
		if cell == 12 or cell == 13 or cell == 14:
			move = GreedyNode.new(self.posx + 1, self.posy, self)
			move.heuristic(goal)
			self.branches.append(move)
		
		cell = tile_map.get_cell(self.posx, self.posy + 1)
		if cell == 12 or cell == 13 or cell == 14:
			move = GreedyNode.new(self.posx, self.posy + 1, self)
			move.heuristic(goal)
			self.branches.append(move)
		
		cell = tile_map.get_cell(self.posx - 1, self.posy)
		if cell == 12 or cell == 13 or cell == 14:
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
		
	
	func search(goal, visits, fringe, tile_map):# la busqueda greedy es totalmente recursiva
		print("Se atiende rojo")
		self.print_position()
		if self.posx == goal.x and self.posy == goal.y:
			print("SE ENCONTRO LA META!!!")
			var way = []
			way.append(Vector2(self.posx, self.posy))
			var parent = self.parent
			while parent:
				way.append(Vector2(parent.posx, parent.posy))
				parent = parent.parent
			way.invert()
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
		print("No hay solucion rojo")
		return null
		
