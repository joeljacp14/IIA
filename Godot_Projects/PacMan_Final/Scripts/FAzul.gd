#BUSQUEDA PRIMERO EN ANCHURA (BPA - BFS)
extends Area2D

onready var walls = get_parent().get_node("Navigation2D/Walls")
var pacman #goal

onready var bfs_visits : Array = []
onready var bfs_fringe : Array = []

var path
var direction = Vector2(0,0)
var speed = 30

var bfs_root
var tile_pos

func _ready():
	
	position = walls.get_fantasma_pos()
	
	pacman = get_parent().get_node("Pacman")
	
	tile_pos = walls.world_to_map(pacman.global_position)
	print("PAC-MAN: ", tile_pos.x, " ", tile_pos.y)
	var goal = Vector2(int(round(tile_pos.x)), int(round(tile_pos.y)))
	
	tile_pos = walls.world_to_map(global_position)
	print("BLUE GHOST: ", tile_pos.x, " ", tile_pos.y)
	bfs_root = BFSNode.new(tile_pos.x, tile_pos.y)
	path = bfs_root.search(goal, bfs_visits, bfs_fringe, walls)
			
	#path = walls.get_path_to_player("blue_ghost")
	
func _process(delta):
	if (path.size() > 1):
		var pos_to_move = path[0]
		direction = (pos_to_move - position).normalized()
		var distance = position.distance_to(path[0])
		if (distance > 1):
			position += speed * delta * direction
		else:
			path.remove(0)
	else:
#		position = walls.get_fantasma_pos()
		
		pacman = get_parent().get_node("Pacman")
		
		tile_pos = walls.world_to_map(pacman.global_position)
		print("PAC-MAN: ", tile_pos.x, " ", tile_pos.y)
		var goal = Vector2(int(round(tile_pos.x)), int(round(tile_pos.y)))
		
		tile_pos = walls.world_to_map(global_position)
		print("BLUE GHOST: ", tile_pos.x, " ", tile_pos.y)
		var bfs_root = BFSNode.new(tile_pos.x, tile_pos.y)
		bfs_visits.clear()
		bfs_fringe.clear()
		path = bfs_root.search(goal, bfs_visits, bfs_fringe, walls)
	
		#path = walls.get_path_to_player("blue_ghost")


func _on_blue_ghost_area_entered(area):
	if (area.name == "Pacman"):
		print("GAME OVER")
		get_tree().change_scene("res://GameOver.tscn")

class BFSNode:
	var posx
	var posy
	var branches
	var parent
	
	func _init(posx, posy, parent = null):
		self.posx = posx
		self.posy = posy
		self.branches = []
		self.parent = parent
	
	func print_position():
		print("x: ", self.posx, ", y: ", self.posy)
	
	func expand(goal, fringe, tile_map):
		var move
		var cell
		
		cell = tile_map.get_cell(self.posx, self.posy - 1)
		if cell == 12 or cell == 13 or cell == 14:
			move = BFSNode.new(self.posx, self.posy - 1, self)
			self.branches.append(move)
		
		cell = tile_map.get_cell(self.posx + 1, self.posy)
		if cell == 12 or cell == 13 or cell == 14:
			move = BFSNode.new(self.posx + 1, self.posy, self)
			self.branches.append(move)
		
		cell = tile_map.get_cell(self.posx, self.posy + 1)
		if cell == 12 or cell == 13 or cell == 14:
			move = BFSNode.new(self.posx, self.posy + 1, self)
			self.branches.append(move)
		
		cell = tile_map.get_cell(self.posx - 1, self.posy)
		if cell == 12 or cell == 13 or cell == 14:
			move = BFSNode.new(self.posx - 1, self.posy, self)
			self.branches.append(move)
		
		for branch in self.branches:          #no ordena los hijos, solo los mete a la franja
			fringe.append(branch)
		

	func search(goal, visits, fringe, tile_map):	
		var way = []	
		var world_pos
#		print("* Entra a la cola *")
#		self.print_position()
		if self.posx == goal.x and self.posy == goal.y:
			print("* Encuentra la meta *")
			
			
#			way.append(Vector2(self.posx, self.posy))
			world_pos = tile_map.map_to_world(Vector2(self.posx, self.posy))
			world_pos.x = world_pos.x + 2
			world_pos.y = world_pos.y + 2
			way.append(world_pos)
			
			var parent = self.parent
			while parent:
				world_pos = tile_map.map_to_world(Vector2(parent.posx, parent.posy))
				world_pos.x = world_pos.x + 2
				world_pos.y = world_pos.y + 2
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
		print("No hay solucion AZUL")
		return []
