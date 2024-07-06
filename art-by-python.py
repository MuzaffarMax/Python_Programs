import turtle 
turtle.bgcolor ('black')
a=turtle.Turtle()
colors = ['red','dark red']
for number in range(500):
    a.forward(number+1)
    a.right(89)
    a.pencolor(colors[number%2])
turtle.done