import turtle
import os

#Screen size
WIDTH = 800
HEIGHT = 600

#Set up window
wn = turtle.Screen()
wn.title("AIR HOCKEY!")
wn.bgcolor("black")
wn.setup(WIDTH, HEIGHT)
wn.tracer(0)

pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()
pen.penup()

class Game():
    def __init__(self, width, height):
        self.width = width 
        self.height = height
        
    def render_border(self, pen):
        pen.color("white")
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
    def __init__(self, x, y, shape, color):
        self.direction = 270 
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0
        self.shape = shape
        self.color = color

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
    
    def border_check(self):
        if self.x > game.width/2.0:
            self.x = game.width/2.0
            self.dx *= -0.3
    
        if self.y > game.height/2.0:
            self.y = game.height/2.0
            self.dy *= -0.3

        if self.x < -game.width/2.0:
            self.x = -game.width/2.0
            self.dx *= -0.3
    
        if self.y < -game.height/2.0:
            self.y = -game.height/2.0
            self.dy *= -0.3
        

class Player(Sprite):
    def __init__(self, x, y, shape, color):
        Sprite.__init__(self, x, y, shape, color)
    
    def render(self, pen):
        pen.goto(self.x, self.y)
        pen.shape(self.shape)
        pen.color(self.color)
        pen.showturtle()
        pen.stamp()
        pen.hideturtle()
    
    def move_right(self):
        self.dx = 0.5
        
    def move_left(self):
        self.dx = -0.5 
        
    def move_up(self):
        self.dy = 0.5
    
    def move_down(self):
        self.dy = -0.5
        

class Puck(Sprite):
    def __init__(self, x, y, shape, color):
        Sprite.__init__(self, x, y, shape, color)   
    
    def render(self, pen):
        pen.goto(self.x, self.y)
        pen.shape(self.shape)
        pen.color(self.color)
        pen.showturtle()
        pen.stamp()
        pen.hideturtle()
        
    
# ~ class Goal():
    # ~ def __init__(self, x, y, shape, color):
        # ~ Sprite.__init__(self, x, y, shape, color)
    
    # ~ def score(self):
        # ~ pass 

game = Game(700, 500)

#forming componets of the game
player_1 = Player(-300 , 0, "circle", "light yellow")

player_2 = Player(300 , 0, "circle", "light green")

puck = Puck(0 , 0, "circle", "red")

sprites = [player_1, player_2, puck]

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
    
    game.render_border(pen)

    #Check collisions


#Create mainloop
wn.mainloop()
