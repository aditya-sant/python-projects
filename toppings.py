#toppings
from turtle import *
from random import uniform, randint

#Define a function for drawing pepperoni
def pepperoni(edible_radius, extent = 359, how_many = 100):
    pencolor('black')
    fillcolor('brown')
    shape('circle')
    turtlesize(3, 3)
    for pepperoni_slice in range(how_many):
        # Choose a position
        home()
        setheading(randint(0, extent))
        forward(randint(edible_radius // 4, edible_radius // 1.2))
        #Stamp the image
        stamp()
        
#Define a function for drawing one piece of cheese
def cheese_bit(heading, distance):
    pencolor('orange red')
    fillcolor('yellow')
    shape('circle')
    #Choose how big a bit to add
    turtlesize(uniform(0.5, 3.0), uniform(0.5, 3.0))
    #Move to chosen position
    home()
    setheading(heading)
    forward(distance)
    #Insert shape on canvas
    stamp()
