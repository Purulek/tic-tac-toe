import turtle 
import random 



class board:
    def __init__(self) -> None:
        self.pen1 = turtle.Turtle()
        self.pen2 = turtle.Turtle()
        self.pen3 = turtle.Turtle()
        self.pen4 = turtle.Turtle()
        self.pen3.right(90)
        self.pen4.right(90)

    def draw_line (self,pen,positon_x,posytion_y):
        pen.color("white")
        pen.penup()
        pen.setposition(positon_x,posytion_y)
        pen.pendown()
        pen.color("black")
        pen.forward(300)

    def __call__(self):
        self.draw_line(self.pen1,-150,-60)
        self.draw_line(self.pen2,-150,60)
        self.draw_line(self.pen3,-60,125)
        self.draw_line(self.pen4,60,125)

class circle_player:
    def __init__(self) -> None:
        self.circle = turtle.Turtle()
    
    def draw_circle(self):
        self.circle.circle(40)
    def __call__(self, xcor,ycor):
        self.circle.penup()
        self.circle.setposition(xcor,ycor)
        self.circle.pendown()
        self.draw_circle()





test = board()
test()
dra = circle_player()
dra(0,-40)