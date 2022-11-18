extends KinematicBody2D


# Declare member variables here. Examples:
var a = 10
# var b = "text"
var pos = Vector2()


# Called when the node enters the scene tree for the first time.
func _ready():
	print("Arranca agente . . .")


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	pos = Vector2()
	var girar = 0
	print("Entra al proceso . . .")
	if Input.is_action_pressed("ui_right"):
		pos.x = 200*delta
#		girar += 1
	if Input.is_action_pressed("ui_left"):
		pos.x = -200*delta
#		girar -= 1
	if Input.is_action_pressed("ui_up"):
		pos.y = -200*delta
#		pos = Vector2(100, 0).rotated(girar)
	if Input.is_action_pressed("ui_down"):
		pos.y = 200*delta	
#		pos = Vector2(-100, 0).rotated(girar)		
	#get_input()	
#	print(a)
#	a += 1
#	pos.x = 10*delta
	move_and_collide(pos)
#	move_and_collide(pos * delta)
	
func get_input():
	pos = Vector2()
	if Input.is_action_pressed("ui_right"):
		pos.x += 1
	if Input.is_action_pressed("ui_left"):
		pos.x -= 1
	if Input.is_action_pressed("ui_up"):
		pos.y -= 1
	if Input.is_action_pressed("ui_down"):
		pos.y += 1	
	pos = pos.normalized() * a
	
