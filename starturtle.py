import turtle

t = turtle.Turtle()
t.getscreen().bgcolor("#994444")
t.penup()
t.goto((-200,100))
t.pendown()
t.speed(10)
def star(turtle, size):
	if size <= 10:
		return
	else:
		turtle.begin_fill()
		for i in range(5):

			turtle.forward(size)
			star(turtle, size/3)
			turtle.left(216)
		turtle.end_fill()

star(t, 200)

turtle.done()
