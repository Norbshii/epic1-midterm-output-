#Norberto Pingoy    BSCS 1-B
import turtle
turtle.title('Rick and Morty x Turtle')
turtle.bgcolor('black')

colors = ['#7CFC00', '#228B22', '#008000']
riri=turtle.Screen()
rin = turtle.Pen()


for x in range(200):
    rin.pencolor(colors[x%3])
    rin.width(x//100+1)
    rin.forward(x)
    rin.left(50)

rin.color("white")
rin.penup()
rin.goto(230, 230)
rin.pendown()
style=("Courier New",20,"italic")
rin.write("Simple Rick and Morty Portal",font=style,align='right')
rin.hideturtle()

riri.exitonclick()
