#--------------------------------------------------------------------
#
# Fun With Flags
#
# In the lecture demonstration program "stars and stripes" we saw
# how function definitions allowed us to reuse code that drew a
# star and a rectangle (stripe) multiple times to create a copy of
# the United States flag.
#
# As a further example of the way functions allow us to reuse code,
# in this exercise we will import the flag_elements module into
# this program and create a different flag.  In the PDF document
# accompanying this file you will find several flags which can be
# constructed easily using the "star" and "stripe" functions already
# defined.  Choose one of these and try to draw it.
#

# First we import the two functions we need (make sure a copy of file
# flag_elements.py is in the same folder as this one)
from flag_elements import star, stripe

# Import the turtle graphics functions
from turtle import *

# Set up the drawing environment
setup(600, 400)

##### PUT YOUR CODE FOR DRAWING THE FLAG HERE
penup()
goto(-300, 200)
stripe(600, 400 / 3, 'red')

goto(-300, -200 / 3)
stripe(600, 400 / 3, 'black')

goto(-300 / 2, 20)
star(50, 'green')

goto(300 / 2, 20)
star(50, 'green')


# Exit gracefully
hideturtle()
done()
