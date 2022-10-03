extends KinematicBody2D


# Declare member variables here. Examples:
var a = 5
# var b = "text"
var mov = 100
var pos = Vector2()


# Called when the node enters the scene tree for the first time.
func _ready():
	print("Inicia agente")


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	#print("Inicia el proceso")
	if Input.is_action_pressed("ui_right"):
		pos.x = mov * delta
		pos.y = 0
	if Input.is_action_pressed("ui_left"):
		pos.x = -mov * delta
		pos.y = 0
	if Input.is_action_pressed("ui_down"):
		pos.y = mov * delta
		pos.x = 0
	if Input.is_action_pressed("ui_up"):
		pos.y = -mov * delta
		pos.x = 0
	if Input.is_action_pressed("ui_accept"):
		pos.y = 0
		pos.x = 0
	
	move_and_collide(pos)
