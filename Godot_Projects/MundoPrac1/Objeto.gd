extends KinematicBody2D


# Declare member variables here. Examples:
# var a = 2
# var b = "text"
var mov = 0
var pos = Vector2()
#var rc = RayCast()
onready var agente = get_parent().get_node("Agente")
var velocidad = 50

# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
#	el objeto persigue a nuestro agente ******************
	pos.x = agente.global_position.x - global_position.x
	pos.y = agente.global_position.y - global_position.y
	#******************************************************
	
	#el objeto trata de esquivar al agente cuando colisionan mediante el RayCast ********
	#if $RayCast2D.is_colliding():
	#	pos.x = 0
	#	pos.y = mov * delta
	#else:
	#	pos.y = 0
	#	pos.x = mov * delta
	#********************************************************
	
	move_and_collide(pos.normalized() * velocidad * delta)
