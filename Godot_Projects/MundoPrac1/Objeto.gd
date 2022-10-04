extends KinematicBody2D


# Declare member variables here. Examples:
# var a = 2
# var b = "text"
var mov = 80
var pos = Vector2()
#var rc = RayCast()


# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
#	pass
	
	if $RayCast2D.is_colliding():
		pos.x = 0
		pos.y = mov * delta
	else:
		pos.y = 0
		pos.x = mov * delta
	move_and_collide(pos)
