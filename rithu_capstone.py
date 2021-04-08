import turtle
import os

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

class Sprite():
    def __init__(self, x, y, shape, color):
        self.direction = 270 
        self.x = x
        self.y = y
        self.shape = shape
        self.color = color
    
    def render(self, pen):
        pen.goto(self.x, self.y)
        pen.shape(self.shape)
        pen.color(self.color)
        pen.showturtle()
        # ~ pen.setheading(self.direction)
        pen.stamp()
        pen.hideturtle()
    
        

class Player():
    def __init__(self, x, y, shape, color):
        Sprite.__init__(self, x, y, shape, color)
    
    def render(self, pen):
        pen.goto(self.x, self.y)
        pen.shape(self.shape)
        pen.color(self.color)
        pen.showturtle()
        # ~ pen.setheading(self.direction)
        pen.stamp()
        pen.hideturtle()
    
    def move_right(self):
        self.x += 3
      
    def move_left(self):
        self.x -= 3 
        
    def move_up(self):
        self.y += 3
        
    def move_down(self):
        self.y -= 3
    
    
class Puck():
    def __init__(self, x, y, shape, color):
        Sprite.__init__(self, x, y, shape, color)   
    

# ~ class Goal():
    # ~ def __init__(self, x, y, shape, color):
        # ~ Sprite.__init__(self, x, y, shape, color)
    
    # ~ def score(self):
        # ~ pass 
        


#forming componets of the game
player_1 = Player(-300 , 0, "circle", "light yellow")

player_2 = Player(300 , 0, "circle", "light green")

# ~ puck = Puck(Player(0 , 0, "circle", "red")

sprites = [player_1, player_2]

#keyboard binding
wn.listen()
wn.onkeypress(player_1.move_left, "Left")
wn.onkeypress(player_1.move_right, "Right")
wn.onkeypress(player_1.move_up, "Up")
wn.onkeypress(player_1.move_down, "Down")

wn.onkeypress(player_2.move_left, "a")
wn.onkeypress(player_2.move_right, "d")
wn.onkeypress(player_2.move_up, "w")
wn.onkeypress(player_2.move_down, "s")

while True:
    wn.update()
    pen.clear()
    
    for sprite in sprites:
        sprite.render(pen)
    


#Create mainloop
wn.mainloop()
