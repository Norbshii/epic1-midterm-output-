import turtle
turtle.title('VIRUS x Turtle')

riri = turtle.Turtle()
rin = turtle.Screen()

a=0
b=0


rin.bgcolor("black")
riri.speed(0)
riri.pencolor("green")
riri.penup()
riri.goto(0, 200)
riri.pendown()

while True:
    riri.forward(a)
    riri.right(b)
    a+=3
    b+=1
    if b == 200:
        break

riri.color("white")
riri.penup()
riri.goto(110, 230)
riri.pendown()
style=("Courier New",20,"italic")
riri.write("7 Line Virus",font=style,align='right')
riri.hideturtle()

rin.exitonclick()
