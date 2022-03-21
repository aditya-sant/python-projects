
#-----Statement of Authorship----------------------------------------#
#
#  By submitting this task I agree that it represents my own work.
#  I am aware of the University rule that a student must not
#  act in a manner which constitutes academic dishonesty as stated
#  and explained in QUT's Manual of Policies and Procedures,
#  Section C/5.3 "Academic Integrity" and Section E/2.1 "Student
#  Code of Conduct".
#
#  Student no:      n10795472
#  Student name:    Aditya Sant
#
#--------------------------------------------------------------------#



#-----Task Description-----------------------------------------------#




from turtle import *

setup()

pencolor('black') #Outline colour is black.

#Lime Square
fillcolor('lime')
pensize(5) #Visible outline
penup()

goto(-200,200)

pendown()
begin_fill()

#Code for drawing square
forward(100)
left(270)
forward(100)
left(270)
forward(100)
left(270)
forward(100)
left(270)
forward(100)

end_fill()
penup()

#Overlapped Red Square
fillcolor('red')
goto(-150, 150)

pendown()
begin_fill()

forward(100)
left(270)
forward(100)
left(270)
forward(100)
left(270)
forward(100)
left(270)
forward(100)

end_fill()
penup()

#Yellow Square
fillcolor('yellow')
goto(-150, 150)

pendown()
begin_fill()

forward(50)
left(270)
forward(50)
left(270)
forward(50)
left(270)
forward(50)
left(270)
forward(50)

end_fill()
penup()


hideturtle()
done()


