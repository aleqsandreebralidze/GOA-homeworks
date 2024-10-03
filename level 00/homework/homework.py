from turtle import *
#we want to paint a house
#drawing a square

color("blue")
width(7)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door

forward(70)
color("green")
begin_fill()
left(90)
forward(120)         #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()
#end of the door-

#drawing a roof

penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
#end of the roof

#drawing a windous

penup()
goto(170, 170)
pendown()

right(60)
forward(30)
color("blue")
begin_fill()
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)

penup()
goto(30, 170)
pendown()

right(90)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
right(90)
forward(30)  
end_fill()
exitonclick()