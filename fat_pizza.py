#Fat pizza main program

#Import necessary functions
from turtle import *
from random import uniform, randint
from toppings import cheese_bit, pepperoni

#Create drawing canvas
setup(900, 700)
title('Fat Pizza')
tablecloth = 'sea green'
bgcolor(tablecloth)

#Draw
penup()
speed('fastest')

#Define useful constants
diameter = 600
radius = diameter // 2
crust = 50

#Draw pizza base
pencolor('tan')
dot(diameter)

#Draw tomato paste
pencolor('orange red')
dot(diameter - crust)

#Mozzarella cheese
tracer(False)
for bits in range(300):
    cheese_bit(randint(0, 359), randint(0, radius - crust))

#Add slices of pepperoni to pizza
pepperoni(radius, how_many = 40)
    
#Pizza slices
tracer(True)
pencolor(tablecloth)
width(8)
home()
pendown()
for portion in range(6):
    forward(radius)
    goto(0, 0)
    left(60)

#Hide the turtle and release the window
hideturtle()
done()
