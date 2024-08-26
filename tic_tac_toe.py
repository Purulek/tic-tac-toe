import turtle 
import random 
import time
from tkinter import messagebox


circle_place ={"mid":[],
               "up":[],
               "down":[]}
cross_place = {"mid":[],
               "up":[],
               "down":[]}



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

    def win_con(self,wich_player,who_wins):
        m = 0
        l = 0
        r = 0
        for row in wich_player:
        
            if "mid" in wich_player[row]:
                    m += 1
            elif "left" in wich_player[row]:
                    l += 1
            elif "right" in wich_player[row]:
                    r += 1
            
            if len(wich_player[row]) == 3 :
                messagebox.showinfo("congratuliations",who_wins)
                turtle.bye()
            elif m == 3 or l == 3 or r ==3:
                messagebox.showinfo("congratuliations",who_wins)
                turtle.bye()
            elif "left" in wich_player["up"]  and "mid" in wich_player["mid"] and  "right" in wich_player["down"]:
                messagebox.showinfo("congratuliations","wins:",who_wins)
                turtle.bye()
            elif "right" in wich_player["up"]  and "mid" in wich_player["mid"] and  "left" in wich_player["down"]:
                messagebox.showinfo("congratuliations","wins:",who_wins)
                turtle.bye()
            

class circle_player:
    def __init__(self) -> None:
        self.circle = turtle.Turtle()
    
    
    def Chek_if_move_is_posible(self,row,colum):
        if row in circle_place and colum in circle_place[row] or row in cross_place and colum in cross_place[row]:
            messagebox.showinfo( "inforamtion","hex is alerady engaged")
            return True
    
    def draw_circle(self):
        self.circle.circle(40)

    def where (self):
        wich_row = turtle.textinput("Circle Player","row")
        wich_colum = turtle.textinput("Circle Player","colum")
        try:
            if self.Chek_if_move_is_posible(wich_row, wich_colum) == True:
                return True
        
            elif wich_row == "mid":
                y = -35
                if wich_colum == "mid":
                    x = 0
                    circle_place["mid"].append("mid")

                elif wich_colum == "left":
                    x = -115
                    circle_place["mid"].append("left")

                elif wich_colum == "right":
                    x = 115
                    circle_place["mid"].append("right")


            elif wich_row == "down":
                y = -155
                if wich_colum == "mid":
                    x = 0
                    circle_place["down"].append("mid")

                elif wich_colum == "left":
                    x = -115
                    circle_place["down"].append("left")

                elif wich_colum == "right":
                    x = 115
                    circle_place["down"].append("right")


            elif wich_row == "up":
                y = 80
                

                if wich_colum == "mid":
                    x = 0
                    circle_place["up"].append( "mid")

                elif wich_colum == "left":
                    x = -115
                    circle_place["up"].append("left")

                elif wich_colum == "right":
                    x = 115
                    circle_place["up"].append("right")
            elif wich_colum == "exit" or wich_row == "exit":
                turtle.bye()

            return [x,y]
        except:
            messagebox.showinfo("Error in data", "wrong colum or row")
            return True
    def __call__(self):
        i = 0
        while i < 1:
            self.circle.penup()
            position = self.where()
            if position == True:
                pass
            else:
                self.circle.setposition(position[0],position[1])
                self.circle.pendown()
                self.draw_circle()
                i += 1


class cross_player:
    def __init__(self) -> None:
        self.cross = turtle.Turtle()

    def Chek_if_move_is_posible(self,row,colum):
        if row in circle_place and colum in circle_place[row] or row in cross_place and colum in cross_place[row]:
            messagebox.showinfo( "inforamtion","hex is alerady engaged")
            return True

    def draw_cross(self):
        self.cross.setheading(-45)
        self.cross.forward(130)
        self.cross.penup()
        self.cross.setposition(self.cross.xcor()-85, self.cross.ycor())
        self.cross.pendown()
        self.cross.setheading(45)
        self.cross.forward(130)

    def where (self):
        self.wich_row = turtle.textinput("Cross Player","row")
        self.wich_colum = turtle.textinput("Cross Player","colum")
        try:
            if self.Chek_if_move_is_posible(self.wich_row, self.wich_colum) == True:
                return True
            elif self.wich_row == "mid":
                y = 40
                if self.wich_colum == "mid":
                    x = -45
                    cross_place ["mid"].append("mid")

                elif self.wich_colum == "left":
                    x = -160
                    cross_place ["mid"].append("left")

                elif self.wich_colum == "right":
                    x = 80
                    cross_place ["mid"].append("right")


            elif self.wich_row == "down":
                y = -80
                if self.wich_colum == "mid":
                    x = -45
                    cross_place ["down"].append("mid")

                elif self.wich_colum == "left":
                    x = - 160
                    cross_place ["down"].append("left")

                elif self.wich_colum == "right":
                    x = 80
                    cross_place ["down"].append( "right")


            elif self.wich_row == "up":
                y = 155
                if self.wich_colum == "mid":
                    x = -45
                    cross_place ["up"].append( "mid")

                elif self.wich_colum == "left":
                    x = -160
                    cross_place ["up"].append("left")

                elif self.wich_colum == "right":
                    x = 80
                    cross_place ["up"] .append("right")
            elif self.wich_colum == "exit" or self.wich_row == "exit":
                turtle.bye()

            return [x,y]
        except:
            messagebox.showinfo("Error in data", "wrong colum or row")
            return True
    def __call__(self):
        i = 0
        while i < 1:
            self.cross.penup()
            position = self.where()
            if position == True:
                pass
            else:
                self.cross.setposition(position[0],position[1])
                self.cross.pendown()
                self.draw_cross()
                i += 1





test = board()
test()
cra = cross_player()

dra = circle_player()


i = 0
while i <9:
    if i % 2 == 0:
        cra()
    else:
        dra()
    i += 1
    test.win_con(cross_place,"cross")
    test.win_con(circle_place,"circle")
print (cross_place)
print(circle_place)
