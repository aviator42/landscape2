import turtle

scn = turtle.Screen()
scn.bgcolor("light blue")


jim = turtle.Turtle()
dwight = turtle.Turtle()
mike =  turtle.Turtle()

jim.penup()
jim.goto(0, 0)
jim.pendown()

jim.fillcolor("green")
jim.begin_fill()

jim.forward(300)
jim.right(90)
jim.forward(340)
jim.right(90)


turtle.exitonclick()
