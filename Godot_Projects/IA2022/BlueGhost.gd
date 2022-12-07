extends KinematicBody2D

var velocidad = 150

func _physics_process(delta):
	var movimiento = Vector2()
	
	movimiento = movimiento.normalized()
	movimiento = move_and_slide(movimiento * velocidad)
