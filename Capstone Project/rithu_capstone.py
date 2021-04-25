import turtle
import os
import math
import tkinter as tk
import tkinter.messagebox
import time

#Screen size
WIDTH = 800
HEIGHT = 600

#Set up window
wn = turtle.Screen()
wn.title("AIR HOCKEY!")
wn.bgcolor("floralwhite")
wn.setup(WIDTH, HEIGHT)
wn.tracer(0)
pen = turtle.Turtle()

pen.speed(0)
pen.hideturtle()
pen.penup()

score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("indianred")
score_pen.penup()
score_pen.hideturtle()
score_pen.goto(0,260)
score_pen.write("PLAYER 1:    SCORE                        PLAYER 2:    SCORE", align="center", font=("Comic Sans", 24, "normal"))


#images
wn.register_shape("player1.gif")
wn.register_shape("player2.gif")
wn.register_shape("puck.gif")
wn.register_shape("goal1.gif")
wn.register_shape("goal2.gif")
wn.bgpic("rink.gif")

class Game():
    def __init__(self, width, height):
        self.width = width 
        self.height = height
        
    def render_border(self, pen):
        pen.color("indianred")
        pen.width(2)
        pen.penup()
    
        left = -self.width/2.0
        right = self.width/2.0
        top = -self.height/2.0
        bottom = self.height/2.0
        
        pen.goto(left, top)
        pen.pendown()
        pen.goto(right, top)
        pen.pendown()
        pen.goto(right, bottom)
        pen.goto(left, bottom)
        pen.goto(left, top)
        pen.penup()

class Sprite():
    def __init__(self, x, y, shape, color, width, height):
        self.direction = 270 
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0
        self.shape = shape
        self.color = color
        self.width = width
        self.height = height
        self.thrust = 0
        self.friction = 0.98
    
    def accelerate(self):
        h = self.heading() 
        self.dx += math.cos(h*math.pi/180)*self.thrust
        self.dy += math.sin(h*math.pi/180)*self.thrust
        
    def render(self, pen):
        pen.goto(self.x, self.y)
        pen.shape(self.shape)
        pen.color(self.color)
        pen.showturtle()
        pen.stamp()
        pen.hideturtle()
        
    def move(self):
        self.x += self.dx
        self.y += self.dy
        self.dx *= self.friction
        self.dy *= self.friction
    
    def border_check(self):
        if self.x > game.width/2.0 - 30:
            self.x = game.width/2.0 - 30
            self.dx *= -1
    
        if self.y > game.height/2.0 - 30:
            self.y = game.height/2.0 - 30
            self.dy *= -1

        if self.x < -game.width/2.0 + 30:
            self.x = -game.width/2.0 + 30 
            self.dx *= -1
    
        if self.y < -game.height/2.0 + 30:
            self.y = -game.height/2.0 + 30
            self.dy *= -1
            
    def is_distance_collision(self, other):
        distance = (((self.x-other.x) ** 2) + ((self.y-other.y) ** 2)) ** 0.5
        if distance < (self.width/2.0) + (other.width/2.0):
            return True
        else:
            return False
    
    def set_coordinates(self, x, y):
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0

class Player(Sprite):
    def __init__(self, x, y, shape, color, width, height):
        Sprite.__init__(self, x, y, shape, color, width, height)
    
    def render(self, pen):
        pen.goto(self.x, self.y)
        pen.shape(self.shape)
        pen.color(self.color)
        pen.showturtle()
        pen.stamp()
        pen.hideturtle()
    
    def move_right(self):
        self.dx = 4
        
    def move_left(self):
        self.dx = -4 
        
    def move_up(self):
        self.dy = 4
    
    def move_down(self):
        self.dy = -4

class Puck(Sprite):
    def __init__(self, x, y, shape, color, width, height):
        Sprite.__init__(self, x, y, shape, color, width, height)  
        
    def render(self, pen):
        pen.goto(self.x, self.y)
        pen.shape(self.shape)
        pen.color(self.color)
        pen.showturtle()
        pen.stamp()
        pen.hideturtle()
    
class Goal():
    def __init__(self, x, y, shape, color, width, height):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = color
        self.width = width
        self.height = height
        
    def render(self, pen):
        pen.goto(self.x, self.y)
        pen.shape(self.shape)
        pen.shapesize(self.width/20, self.height/20, 0)
        pen.color(self.color)
        pen.showturtle()
        pen.stamp()
        pen.hideturtle()
        pen.shapesize(1, 1, 0)
        
    def is_aabb_collision(self, other):
        # Axis Aligned Bounding Box
        x_collision = (math.fabs(self.x - other.x) * 2) < (self.width + other.width)
        y_collision = (math.fabs(self.y - other.y) * 2) < (self.height + other.height)
        return (x_collision and y_collision)
    
    
    
game = Game(700, 500)

#forming componets of the game
player_1 = Player(-250 , 0, "player1.gif", "light yellow", 95, 95)

player_2 = Player(250 , 0, "player2.gif", "light green", 95, 95)

puck = Puck(0 , 0, "puck.gif", "red", 20, 20)

goal_1 = Goal(-320, 0, "goal1.gif", "saddlebrown", 60, 100)
goal_2 = Goal(322, 0, "goal2.gif", "saddlebrown", 60, 100)


sprites = [player_1, player_2, puck]
goals = [goal_1, goal_2]
players = [player_1, player_2]

#Score
score_1 = 0 
score_2 = 0

#keyboard binding
wn.listen()
wn.onkeypress(player_2.move_left, "Left")
wn.onkeypress(player_2.move_right, "Right")
wn.onkeypress(player_2.move_up, "Up")
wn.onkeypress(player_2.move_down, "Down")

wn.onkeypress(player_1.move_left, "a")
wn.onkeypress(player_1.move_right, "d")
wn.onkeypress(player_1.move_up, "w")
wn.onkeypress(player_1.move_down, "s")

while True:
    wn.update()
    pen.clear()
    
    for sprite in sprites:
        sprite.render(pen)
        sprite.move()
        sprite.border_check()
        
        if goal_1.is_aabb_collision(puck):
                score_2 += 1
                puck.set_coordinates(0,0)
                player_1.set_coordinates(-250 , 0)
                player_2.set_coordinates(250 , 0)
                print(f"Score_2 = {score_2}")
                score_pen.clear()
                score_pen.write("PLAYER   2'S   TURN", align="center", font=("Comic Sans",24,"normal"))
                time.sleep(2)
                score_pen.clear()
                score_pen.write("PLAYER 1:    {}                              PLAYER 2:   {}".format(score_1,score_2), align="center", font=("Comic Sans",24,"normal"))
            
        if goal_2.is_aabb_collision(puck):
                score_1 += 1
                puck.set_coordinates(0,0)
                player_1.set_coordinates(-250 , 0)
                player_2.set_coordinates(250 , 0)
                print(f"Score_1 = {score_1}")
                score_pen.clear()
                score_pen.write("PLAYER   1'S   TURN", align="center", font=("Comic Sans",24,"normal"))
                time.sleep(2)
                score_pen.clear()
                score_pen.write("PLAYER 1:    {}                              PLAYER 2:   {}".format(score_1,score_2), align="center", font=("Comic Sans",24,"normal"))
            
    game.render_border(pen)
    
    for goal in goals:
        goal.render(pen)
    
    game.render_border(pen)
    
    for player in players:
        if player.is_distance_collision(puck):
            print("collision")
            # ~ os.system("afplay puck_2.wav&")
            puck.dx += player.dx
            puck.dy += player.dy
            
    if score_1 == 5:
        print("player_1 wins")
        os.system("afplay victory.wav&")
        score_pen.clear()
        score_pen.write("PLAYER 1 WINS!", align="center", font=("Comic Sans",24,"normal"))
        time.sleep(2.5)
        
        if tkinter.messagebox.askyesno("Please confirm", "Would you like to play again?") == True:
            score_1 = 0 
            score_2 = 0
            score_pen.clear()
            score_pen.write("PLAYER 1:    {}                        PLAYER 2:   {}".format(score_1,score_2), align="center", font=("Comic Sans",24,"normal"))
            
        else:
            exit()
    
    if score_2 == 5:
        print("player_2 wins")
        os.system("afplay victory.wav&")
        score_pen.clear()
        score_pen.write("PLAYER 2 WINS!", align="center", font=("Comic Sans",24,"normal"))
        time.sleep(2.5)
        
        if tkinter.messagebox.askyesno("Please confirm", "Would you like to play again?") == True:
            score_1 = 0 
            score_2 = 0
            score_pen.clear()
            score_pen.write("PLAYER 1:    {}                        PLAYER 2:   {}".format(score_1,score_2), align="center", font=("Comic Sans",24,"normal"))
        else:
            exit()
        

#Create mainloop
wn.mainloop()
