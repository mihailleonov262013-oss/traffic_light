from turtle import *

def circle1():
    color('red')
    penup()
    goto(0,100)
    pendown()
    circle(35)

def circle1_fill():
    color('red')
    penup()
    goto(0,100)
    pendown()
    begin_fill()
    circle(35)
    end_fill()

def circle2():
    color('yellow')
    penup()
    goto(0,0)
    pendown()
    circle(35)   

def circle2_fill():
    color('yellow')
    penup()
    goto(0,0)
    pendown()
    begin_fill()
    circle(35)
    end_fill()

def circle3():
    color('green')
    penup()
    goto(0,-100)
    pendown()
    circle(35)

def circle3_fill():
    color('green')
    penup()
    goto(0,-100)
    pendown()
    begin_fill()
    circle(35)
    end_fill()
color_of_light = input('Какой горит цвет красный/жёлтый/зелёный?')
circle1()
circle2()
circle3()
if color_of_light == 'красный':
    circle1_fill()
if color_of_light == 'жёлтый':
    circle2_fill()
if color_of_light == 'зелёный':
    circle3_fill()
exitonclick()
hideturtle()
