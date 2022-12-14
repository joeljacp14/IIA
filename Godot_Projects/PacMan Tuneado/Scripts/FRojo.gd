#BUSQUEDA POR ALGORITMO GREEDY
extends Area2D

onready var walls = get_parent().get_node("Navigation2D/Walls")
var pacman #goal

onready var visits : Array = []            #lISTAS DE VISITADOS Y COLA DE ESPERA (FRINGE)
onready var fringe : Array = []

var path                                   #Camino
var direction = Vector2(0,0)         
var speed = 30

var greedy_root                           #Raíz greede, objeto
var tile_pos

func _ready():
	
	position = walls.get_fantasma_pos()                   #Posicion del fantasma dentro del walls
	
	pacman = get_parent().get_node("Pacman")              #Se obtiene el nodo del pacman para saber cual es la meta
	
	tile_pos = walls.world_to_map(pacman.global_position)   #Convertimos posición global de Pacman en tiles
	print("PAC MAN: ", tile_pos.x, " ", tile_pos.y)         
	var goal = Vector2(int(round(tile_pos.x)), int(round(tile_pos.y))) #Declaramos variable meta que es un vector con
																	   #posiciones enteras redondeadas del tile
	
	tile_pos = walls.world_to_map(global_position)          #convertimos la posición del fantasma a tiles
	print("RED GHOST: ", tile_pos.x, " ", tile_pos.y)       
	greedy_root = GreedyNode.new(tile_pos.x, tile_pos.y)    #Instanciamos raíz greedy con la pos inicial del fantasma
	path = greedy_root.search(goal, visits, fringe, walls)  #mandamos lo que nos devuelve la busqueda
			
	#path = walls.get_path_to_player("red_ghost")
	
func _process(delta):                                      #Mientras la lista no esté vacía va a ir recorriendo
	if (path.size() > 1):
		var pos_to_move = path[0]
		direction = (pos_to_move - position).normalized()
		var distance = position.distance_to(path[0])
		if (distance>1):
			position += speed * delta * direction
		else:
			path.remove(0)
	else:
		pacman = get_parent().get_node("Pacman")                      #SI el camino se queda vacío vuelve a hacer
																	  #vuelve a hacer la bsuqyeda greedy
		tile_pos = walls.world_to_map(pacman.global_position)
		print("PAC MAN: ", tile_pos.x, " ", tile_pos.y)                       #nueva pos del fantasma hace la busqueda a partir de donde se quedó
		var goal = Vector2(int(round(tile_pos.x)), int(round(tile_pos.y)))
		
		tile_pos = walls.world_to_map(global_position)
		print("RED GHOST: ", tile_pos.x, " ", tile_pos.y)
		greedy_root = GreedyNode.new(tile_pos.x, tile_pos.y)
		visits.clear()
		fringe.clear()
		path = greedy_root.search(goal, visits, fringe, walls)

func _on_red_ghost_area_entered(area):                   
	if (area.name == "Pacman"):                            #Cuando el fantasma entra en el área del pacman pierdes
		print("GAME OVER")
		get_tree().change_scene("res://GameOver.tscn")     #Manda escena de GAME OVER

class GreedyNode:                                                   
	var posx
	var posy
	var h # es el valor de la heuristica del nodo
	var branches             #hijos
	var parent               #el jefe
	
	func _init(posx, posy, parent = null):    #Metodo constructor, si no tiene padre es NULO
		self.posx = posx                      #Si no tiene padre quiere decir que llegó al final del camino
		self.posy = posy
		self.h = 0
		self.branches = []
		self.parent = parent
	
	func print_position():                           #Imprime la posición del fantasma
		print("x: ", self.posx, ", y: ", self.posy)
	
	func heuristic(goal):
		self.h = abs(goal.x - self.posx) + abs(goal.y - self.posy)              #Se agrega el valor de la heuristica al nodo
	
	func expand(goal, fringe, tile_map):                               #Expande, crea nuevos hijos
		var move  #siguiente movimiento
		var cell  #donde se almacena el valor de la celda
		
		#movimiento hacia arriba
		cell = tile_map.get_cell(self.posx, self.posy - 1)            
		if cell == 12 or cell == 13 or cell == 14:
			move = GreedyNode.new(self.posx, self.posy - 1, self)
			move.heuristic(goal)
			self.branches.append(move)
		
		#movimiento hacia la derecha
		cell = tile_map.get_cell(self.posx + 1, self.posy)
		if cell == 12 or cell == 13 or cell == 14:
			move = GreedyNode.new(self.posx + 1, self.posy, self)
			move.heuristic(goal)
			self.branches.append(move)
		
		#movimiento hacia abajo
		cell = tile_map.get_cell(self.posx, self.posy + 1)
		if cell == 12 or cell == 13 or cell == 14:
			move = GreedyNode.new(self.posx, self.posy + 1, self)
			move.heuristic(goal)
			self.branches.append(move)
		
		#movimiento hacia la izquierda
		cell = tile_map.get_cell(self.posx - 1, self.posy)
		if cell == 12 or cell == 13 or cell == 14:
			move = GreedyNode.new(self.posx - 1, self.posy, self)
			move.heuristic(goal)
			self.branches.append(move)
		
		#Agrega hijos a la franja odenados por heurística 
		for branch in self.branches:
			if fringe == []:
				fringe.append(branch)        #si está vacía agrega hijo
			else:
				var pos = 0
				for node in fringe:
					if node.h > branch.h:              #ordena por heurística de menor a mayor
						fringe.insert(pos, branch)
						break
					pos += 1
		
	
	func search(goal, visits, fringe, tile_map):# la busqueda greedy es totalmente recursiva
		if self.posx == goal.x and self.posy == goal.y:      #evalua si la pos del nodo es igual a la meta
			print("SE ENCONTRO LA META!!!")
			var way = []
			var world_pos
			world_pos = tile_map.map_to_world(Vector2(self.posx, self.posy))    #Conversión de la posición de tile a pixeles
			world_pos.x = world_pos.x + 1            #centrando 
			world_pos.y = world_pos.y + 1
			way.append(world_pos)                    #agregamos al camino
			var parent = self.parent
			
			while parent:                           #mientras haya padre agregará nodos al camino
				world_pos = tile_map.map_to_world(Vector2(parent.posx, parent.posy))
				world_pos.x = world_pos.x + 1        #centrando x2
				world_pos.y = world_pos.y + 1
				way.append(world_pos)
				parent = parent.parent
			way.invert()                             #Cambia el sentido del camino para que sea de principio a fin
			return PoolVector2Array(way)             #Convierte el arreglo a pull vector
		
		#BANDERA
		var is_visited = false                       
		if not visits == []:                        #Si no es vacía la llista 
			for visited in visits:                  #Recorre bbsucando si el nodo actual se encuentra en VISITADOS
				if self.posx == visited.posx and self.posy == visited.posy:
					is_visited = true               #Si es visitado se vuelve verdadero
					break                           #Rompe el ciclo
					
		if not is_visited:                          #Si no es visitado
			visits.append(self)                     #Se agrega a la liksta de visitados
			self.expand(goal, fringe, tile_map)     #Expande sus hijos
		
		if not fringe == []:                        #Si la franja no está vacía
			return fringe.pop_front().search(goal, visits, fringe, tile_map)    #Se hace una recursión con la busqueda del siguiente nodo de la lista
		print("No hay solucion rojo")               #Si no hay solución se regresa una lista vacía
		return []
		
