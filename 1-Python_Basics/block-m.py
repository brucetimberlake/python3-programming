import turtle

wn = turtle.Screen()
wn.bgcolor("darkblue")
a = turtle.Turtle()

a.shape("blank")
a.speed(10)
a.color("yellow")
a.fillcolor("yellow")
a.pensize(5)

serif_full_width = 80
serif_height = int(serif_full_width * .416666)
serif_lip = int(serif_full_width / 4)
vertical_inner_height = int(serif_full_width * .666666)
vertical_outer_height = serif_full_width

point_angle_from_serif = 55
point_angle_from_vertical = 145
point_angle = 110
point_length = serif_full_width

a.begin_fill()

# left vertical
a.forward(serif_full_width)
a.left(90)
a.forward(serif_height)
a.left(90)
a.forward(serif_lip)
a.right(90)
a.forward(vertical_inner_height)

# bottom of point
a.right(point_angle_from_vertical)
a.forward(point_length)
a.left(point_angle)
a.forward(point_length)
a.right(point_angle_from_vertical)
a.forward(vertical_inner_height)

a.right(90)
a.forward(serif_lip)
a.left(90)
a.forward(serif_height)
a.left(90)
a.forward(serif_full_width)
a.left(90)
a.forward(serif_height)
a.left(90)
a.forward(serif_lip)

# right vertical
a.right(90)
a.forward(vertical_outer_height)

# top right serif
a.right(90)
a.forward(serif_lip)
a.left(90)
a.forward(serif_height)
a.left(90)
a.forward(serif_full_width - serif_lip)

# top of point
a.left(point_angle_from_serif)
a.forward(point_length)
a.right(point_angle)
a.forward(point_length)

# top left serif
a.left(point_angle_from_serif)
a.forward(serif_full_width - serif_lip)
a.left(90)
a.forward(serif_height)
a.left(90)
a.forward(serif_lip)
a.right(90)
a.forward(vertical_outer_height)
a.right(90)
a.forward(serif_lip)
a.left(90)
a.forward(serif_height)
a.left(90)

a.end_fill()

wn.exitonclick()
