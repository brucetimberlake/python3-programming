import turtle

side = 10

wn = turtle.Screen()
wn.bgcolor("yellow")

a = turtle.Turtle()
a.shape("turtle")
a.speed(10)
a.color("blue")

for _ in range(40):
    a.forward(side)
    a.left(90)
    side = int(side + 5)

wn.exitonclick()
