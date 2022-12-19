import turtle
from math import *

pencil = turtle.Turtle()
def rectangle(g):
    for i in range(2):
        pencil.forward(g*1.5)
        pencil.left(90)
        pencil.forward(g)
        pencil.left(90)

def areaPainting(x, y, color):
    pencil.penup()
    pencil.goto(x, y)
    pencil.pendown()
    pencil.color(color)
    pencil.begin_fill()

def drawMoon(raduis):
    pencil.circle(raduis)
    pencil.end_fill()

    
def drawStar(x, y, leng):
    areaPainting(x, y, "white")
    pencil.left(36)
    pencil.forward(leng/2)
    for i in range(6):
        if i == 0:
            angle = 160
        else:
            angle = 144
        if i == 5:
            angle = 189
            pencil.left(angle)
            pencil.penup()
            pencil.end_fill()
            return
        pencil.left(angle)
        pencil.forward(leng)
        
def drawFlag(x, y, g):
    areaPainting(x, y, "red")
    rectangle(g)
    pencil.end_fill()
    bPole = g/2 #  (x axis)
    bRadius = g/4 # radius of the great circle (y axis)
    bDistance = g/16 # distance between center of large circle and center of small circle
    sRadius = g/5 # radius of the small circle
    sDistance = g/3 # the distance between the center of the stars and the center of the small circle
    sRadius = g/8 # radius of stars
    
    
    
    #moondraw
    areaPainting(g/2 + x, g/4 + y, "white")
    drawMoon(g/4)
    areaPainting(g/2 + g/16 + x, g/2 - g/5 +y, "red") 
    drawMoon(g/5)
    
    
    
    # stardraw
    starX = (bPole + bDistance + sDistance - sRadius + sRadius)
    starY = g/2
    starLen = (sRadius + (cos(radians(36))*sRadius)/cos(radians(18)))
    drawStar(starX + x, starY + y, starLen)
    
drawFlag(0,0,100)    