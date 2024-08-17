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
        pen.forward(350)

    def __call__(self):
        self.draw_line(self.pen1,-160,-60)
        self.draw_line(self.pen2,-160,60)
        self.draw_line(self.pen3,-60,150)
        self.draw_line(self.pen4,60,150)

class circle_player:
    def __init__(self) -> None:
        self.circle = turtle.Turtle()
    
    def draw_circle(self):
        self.circle.circle(40)

    def where (self):
        wich_row = turtle.textinput("row")
        wich_colum = turtle.textinput("colum")
        if wich_row == "mid":
            y = -35
            if wich_colum == "mid":
                x = 0
            elif wich_colum == "left":
                x = -115
            elif wich_colum == "right":
                x = 115
        elif wich_row == "down":
            y = -150
            if wich_colum == "mid":
                x = 0
            elif wich_colum == "left":
                x = -115
            elif wich_colum == "right":
                x = 115
        elif wich_row == "up":
            y = 150

    def __call__(self):
        self.circle.penup()
        self.circle.setposition(0,-155)
        self.circle.pendown()
        self.draw_circle()





test = board()
test()
dra = circle_player()
dra()