import turtle
import math


T = turtle.Turtle() 
T.speed(0)  
T.color("red")  
turtle.bgcolor("black")  


def corazon(n):
    x = 16 * math.sin(n)**3
    y = 13 * math.cos(n) - 5 * math.cos(2 * n) - 2 * math.cos(3 * n) - math.cos(4 * n)
    return x, y

T.penup() 
for i in range(1, 15): 
    T.goto(0, 0) 
    T.pendown()  
    for n in range(0, 100, 2):  
        x, y = corazon(n / 10) 
        T.goto(x * i, y * i) 
    T.penup()  

T.hideturtle()  
turtle.done()  
