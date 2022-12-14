extends Area2D

var direction = Vector2(0,0)
var speed= 15
onready var walls = get_parent().get_node("Navigation2D/Walls")   #Obtiene nodo walls

func _ready():
	$AnimatedSprite.play("moviendose")                           #Reproduce la animación llamada "moviendose"
	position = walls.get_player_init_pos()                       #Ubica al pacman en su posición inicial

func _process(delta):                                            #Función para controlar le pacman por medio de
	if Input.is_action_pressed("ui_up"):                         # las teclas de dirección
		direction = Vector2(0,-1)
		rotation = deg2rad(-90)                                  #Rota el sprite en dirección al movimiento
	elif Input.is_action_pressed("ui_down"):
		direction = Vector2(0,1)
		rotation = deg2rad(90)                                   #Rota el sprite en dirección al movimiento   
	elif Input.is_action_pressed("ui_left"):
		direction = Vector2(-1,0)
		rotation = deg2rad(180)                                  #Rota el sprite en dirección al movimiento
	elif Input.is_action_pressed("ui_right"):
		direction = Vector2(1,0)
		rotation = deg2rad(0)                                    #Rota el sprite en dirección al movimiento
	
	var pos_to_move = walls.is_tile_vacant(position, direction)  #Llama a función dentro de walls para ubicar el pacman dentro del mapa      
	if (direction != Vector2(0,0)):                              #Si la dirección no está en el vector (0,0)
		position = position.linear_interpolate(pos_to_move, speed * delta)  #Mueve de un punto a otro el pacman respecto a su velocidad y su posición
		walls.comer(position)                                    #Mientras avanza va comiendo 
