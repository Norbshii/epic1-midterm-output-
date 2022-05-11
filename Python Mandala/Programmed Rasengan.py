#Norberto Pingoy    BSCS 1-B
import turtle
turtle.title('Rasengan x Turtle')

riri=turtle.Turtle()
rin=turtle.Screen()
rin.bgcolor("Black")
riri.speed("fastest")
riri.hideturtle()


#Outer Clockwise
def square(x):
    riri.color("#87CEFA")
    riri.forward(x)
    for i in range(3):
        riri.left(90)
        riri.forward(x)
    riri.left(90)

for i in range(130):
        square(145)
        riri.left(-183)


#Outer Cover
riri.penup()
riri.goto(-103.8, -180)
riri.color("#00FFFF")
riri.pendown()
riri.circle(208)


#Inner Counter Clockwise
riri.penup()
riri.goto(-110, 130)
riri.color("#40E0D0")
riri.pendown()
def inner(x):
        riri.forward(200)
        riri.right(60)
        riri.forward(120)
        riri.left(60)
        riri.forward(60)

for i in range(120):
        inner(120)
        riri.left(183)


#Inner Spiral Circle
riri.penup()
riri.goto(0, 0)
riri.color("#00CED1")
riri.pendown()
def waves(x):
    riri.circle(105)

for i in range(40):
        waves(40)
        riri.left(-15)

riri.color("white")
riri.penup()
riri.goto(230, 230)
riri.pendown()
style=("Courier New",30,"italic")
riri.write("Turtle Type Rasengan",font=style,align='right')


rin.exitonclick()
