from turtle import *
#drawing a castle
#drawing a rectangle

color("blue")
width(7)

forward(450)
left(90)
forward(200)
left(90)
forward(450)
left(90)
forward(200)
#end of the rectangle

#drawing a door

left(90)
forward(180)
color("red")
begin_fill()
left(90)
forward(120)         #haight of the door
right(90)
forward(70)
right(90)
forward(120)
end_fill()

#end of the door

#drawing a roofs

penup()
goto(450, 200)
pendown()

color("green")
begin_fill()

right(180)
forward(40)
left(90)
forward(90)
left(90)
forward(40)
right(180)
forward(40)
left(90)
forward(30)
right(150)
forward(90)
right(60)
forward(90)
right(150)
forward(40)
end_fill()

penup()
goto(0, 200)
pendown()

color("green")
begin_fill()

right(90)
forward(40)
right(90)
forward(90)
right(90)
forward(40)
left(180)
forward(40)
right(90)
forward(40)
left(150)
forward(90)
left(60)
forward(90)
left(150)
forward(40)
end_fill()
#end of the roofs

#drawing a windows

penup()
goto(410, 170)
pendown()

color("yellow")
begin_fill()

right(90)
forward(40)
right(90)
forward(70)
right(90)
forward(40)
right(90)
forward(70)
end_fill()

penup()
goto(40, 170)
pendown()

color("yellow")
begin_fill()

forward(70)
right(90)
forward(40)
right(90)
forward(70)
right(90)
forward(40)
end_fill()
#end of the windows

exitonclick()

name = " ალექსანდრე "
age1 = 12
age2 = " წლის "
surname = " ებრალიძე "
greeting = " გამარჯობა "
introducing = " მე ვარ "
history = " მე გოას შესახებ გავიგე facebook_დან და დავინტერესდი ამიტომ შემოვედი და ძალიან მომწონს "
results = " მე გოას პირველი გაკვეთილი ორი დღის წინ დავესწარი და ძაან კაი შთაბეჭდილებები დამრჩა და დარწმუნებული ვარ იმედი არ გამიცრუვდება "

print(name + surname + age1 + age2 + greeting + introducing + history + results)

num1 =3
num2 =8
num3 =14
num4 =5

print(str(num1) + " + " + str(num2) + " + " + str(num3) + " + " + str(num4) + " = " + str(num1 + num2 + num3 + num4))
print(str(num1) + " - " + str(num2) + " - " + str(num3) + " - " + str(num4) + " = " + str(num1 - num2 - num3 - num4))
print(str(num1) + " * " + str(num2) + " * " + str(num3) + " * " + str(num4) + " = " + str(num1 * num2 * num3 * num4))
print(str(num1) + " / " + str(num2) + " / " + str(num3) + " / " + str(num4) + " = " + str(num1 / num2 / num3 / num4))