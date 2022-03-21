#Percentage calculator with interface

#Import the user interface functions
from tkinter import *

def percentage(numerator, denominator):
    result = round((numerator * 100) / denominator)
    return str(result) + '%'

def calculate_and_display():
    num = int(numerator.get())
    den = int(denominator.get())
    answer = percentage(num, den)
    display['text'] = answer

#Front end

big_font = ('Arial', 34)

calculator = Tk()
calculator.title('Percentages')

#Create widgets
numerator = Entry(calculator, font = big_font, width =5)
numerator.pack()

denominator = Entry(calculator, font = big_font, width = 5)
denominator.pack()

display = Label(calculator, font = big_font, text = '???')
display.pack()

start_button = Button(calculator, font = big_font, text = 'Calculate')
start_button.pack()

calculator.mainloop()
