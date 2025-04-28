import turtle

polygon=turtle.Turtle()
turtle.Screen().bgcolor("Aqua")
side=6
angel=70
length=90
for i in range(4):
    polygon.fd(100)
    polygon.left(90)
'''
import turtle

def draw_chessboard():
    turtle.speed(0)
    
    

    square_size = 50
    colors = ["white", "black"]

    for row in range(8):
        for col in range(8):
            turtle.penup()
            turtle.goto(col * square_size - 200, row * square_size - 200)
            turtle.pendown()
            color = colors[(row + col) % 2]
            turtle.fillcolor(color)
            turtle.begin_fill()
            for _ in range(4):
                turtle.forward(square_size)
                turtle.right(90)
            turtle.end_fill()

    turtle.hideturtle()
    turtle.done()

draw_chessboard()
'''   
   


