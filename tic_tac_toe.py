import turtle 
import random 
import time

circle_place ={}
cross_place = {}



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
        wich_row = turtle.textinput("Circle Player","row")
        wich_colum = turtle.textinput("Circle Player","colum")
        if wich_row == "mid":
            y = -35
            if wich_colum == "mid":
                x = 0
                circle_place["mid"] = "mid"
            elif wich_colum == "left":
                x = -115
                
                circle_place["mid"] = "left"
            elif wich_colum == "right":
                x = 115
                circle_place["mid"] = "right"
        elif wich_row == "down":
            y = -155
            if wich_colum == "mid":
                x = 0
                circle_place["down"] = "mid"
            elif wich_colum == "left":
                x = -115
            elif wich_colum == "right":
                x = 115
        elif wich_row == "up":
            y = 80
            if wich_colum == "mid":
                x = 0
            elif wich_colum == "left":
                x = -115
            elif wich_colum == "right":
                x = 115
        return [x,y]
    def __call__(self):
        self.circle.penup()
        position = self.where()
        self.circle.setposition(position[0],position[1])
        self.circle.pendown()
        self.draw_circle()

class cross_player:
    def __init__(self) -> None:
        self.cross = turtle.Turtle()
    
    def draw_cross(self):
        self.cross.setheading(-45)
        self.cross.forward(130)
        self.cross.penup()
        self.cross.setposition(self.cross.xcor()-85, self.cross.ycor())
        self.cross.pendown()
        self.cross.setheading(45)
        self.cross.forward(130)
        time.sleep(3)


    def where (self):
        wich_row = turtle.textinput("Cross Player","row")
        wich_colum = turtle.textinput("Cross Player","colum")
        if wich_row == "mid":
            y = 40
            if wich_colum == "mid":
                x = -45
            elif wich_colum == "left":
                x = -160
            elif wich_colum == "right":
                x = 80
        elif wich_row == "down":
            y = -80
            if wich_colum == "mid":
                x = -45
            elif wich_colum == "left":
                x = - 160
            elif wich_colum == "right":
                x = 80
        elif wich_row == "up":
            y = 155
            if wich_colum == "mid":
                x = -45
            elif wich_colum == "left":
                x = -160
            elif wich_colum == "right":
                x = 80
        return [x,y]
    def __call__(self):
        self.cross.penup()
        position = self.where()
        self.cross.setposition(position[0],position[1])
        self.cross.pendown()
        self.draw_cross()





test = board()
test()
cra = cross_player()

dra = circle_player()



for i in range(9):
    if i % 2 == 0:
        cra()
    else:
        dra()

