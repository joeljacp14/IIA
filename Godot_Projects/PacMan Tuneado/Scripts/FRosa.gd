extends Area2D

onready var walls = get_parent().get_node("Navigation2D/Walls")
var pacman #goal

onready var visits : Array = []
onready var fringe : Array = []

var path
var direction = Vector2(0,0)
var speed = 30

var greedy_root
var tile_pos

func _ready():
	
	position = walls.get_fantasma_pos()
	
	pacman = get_parent().get_node("Pacman")
	
	tile_pos = walls.world_to_map(pacman.global_position)
	print("PAC MAN: ", tile_pos.x, " ", tile_pos.y)
	var goal = Vector2(int(round(tile_pos.x)), int(round(tile_pos.y)))
	
	tile_pos = walls.world_to_map(global_position)
	print("PINK GHOST: ", tile_pos.x, " ", tile_pos.y)
	greedy_root = GreedyNode.new(tile_pos.x, tile_pos.y)
	path = greedy_root.search(goal, visits, fringe, walls)
			
	#path = walls.get_path_to_player("red_ghost")
	
func _process(delta):
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
		
		pacman = get_parent().get_node("Pacman")
		
		tile_pos = walls.world_to_map(pacman.global_position)
		print("PAC MAN: ", tile_pos.x, " ", tile_pos.y)
		var goal = Vector2(int(round(tile_pos.x)), int(round(tile_pos.y)))
		
		tile_pos = walls.world_to_map(global_position)
		print("PINK GHOST: ", tile_pos.x, " ", tile_pos.y)
		greedy_root = GreedyNode.new(tile_pos.x, tile_pos.y)
		visits.clear()
		fringe.clear()
		path = greedy_root.search(goal, visits, fringe, walls)
		
		#path = walls.get_path_to_player("red_ghost")


class GreedyNode:
	var posx
	var posy
	var h # es el valor de la heuristica del nodo
	var branches
	var parent
	var peso
	var fn
	
	func _init(posx, posy, parent = null):
		self.posx = posx
		self.posy = posy
		self.h = 0
		self.fn
		self.branches = []
		self.parent = parent
		
		if (parent):       #AGREGAMOS PESO 
			self.peso = parent.peso+1
		else:
			self.peso=0
	
	func print_position():
		print("x: ", self.posx, ", y: ", self.posy)
		
	func f_nAS():                   #A*
		self.fn = self.peso + self.h
	
	func heuristic(goal):
		self.h = abs(goal.x - self.posx) + abs(goal.y - self.posy)
	
	func expand(goal, fringe, tile_map):
		var move
		var cell
		
		cell = tile_map.get_cell(self.posx, self.posy - 1)
		if cell == 12 or cell == 13 or cell == 14:
			move = GreedyNode.new(self.posx, self.posy - 1, self)
			move.heuristic(goal)
			move.f_nAS()
			self.branches.append(move)
		
		cell = tile_map.get_cell(self.posx + 1, self.posy)
		if cell == 12 or cell == 13 or cell == 14:
			move = GreedyNode.new(self.posx + 1, self.posy, self)
			move.heuristic(goal)
			move.f_nAS()
			self.branches.append(move)
		
		cell = tile_map.get_cell(self.posx, self.posy + 1)
		if cell == 12 or cell == 13 or cell == 14:
			move = GreedyNode.new(self.posx, self.posy + 1, self)
			move.heuristic(goal)
			move.f_nAS()
			self.branches.append(move)
		
		cell = tile_map.get_cell(self.posx - 1, self.posy)
		if cell == 12 or cell == 13 or cell == 14:
			move = GreedyNode.new(self.posx - 1, self.posy, self)
			move.heuristic(goal)
			move.f_nAS()
			self.branches.append(move)
		
		for branch in self.branches:
			if fringe == []:
				fringe.append(branch)
			else:
				var pos = 0
				for node in fringe:
					if node.fn > branch.fn:
						fringe.insert(pos, branch)
						break
					pos += 1
		
	
	func search(goal, visits, fringe, tile_map):# la busqueda greedy es totalmente recursiva
#		print("Se atiende rosa")
#		self.print_position()
		if self.posx == goal.x and self.posy == goal.y:
			print("Fantasma llegó a PACMAN X_x")
			var way = []
			var world_pos
			world_pos = tile_map.map_to_world(Vector2(self.posx, self.posy))
			world_pos.x = world_pos.x + 1
			world_pos.y = world_pos.y + 1
			way.append(world_pos)
			var parent = self.parent
			while parent:
				world_pos = tile_map.map_to_world(Vector2(parent.posx, parent.posy))
				world_pos.x = world_pos.x + 1
				world_pos.y = world_pos.y + 1
				way.append(world_pos)
				parent = parent.parent
			way.invert()
			return PoolVector2Array(way)
			#return way
		
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
		print("No hay solucion de rosa")
		return []
		


func _on_pink_ghost_area_entered(area):
	if (area.name == "Pacman"):
		print("GAME OVER")
		get_tree().change_scene("res://GameOver.tscn")
