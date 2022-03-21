#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: n10795472
#    Student name: Aditya Sant
#
#--------------------------------------------------------------------#

# Import necessary functions
from sqlite3 import *
from random import choice
from os.path import isfile

# Connect to the phonetics database
db_file = 'military_phonetic_alphabets.db'
if isfile(db_file):
    db_connection = connect(database = db_file)
    db_cursor = db_connection.cursor()
else:
    raise Exception('Cannot find database file: ' + db_file)

# Select and print the question of interest
letter = choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
print('What are the original (World War I) and present day codewords ' + \
      'for the letter "' + letter + '"?')

#--------------------------------------------------------------------#

# Put your code here
random_letter = letter
db_cursor.execute("SELECT World_War_I,Present_Day FROM Military_Phonetic_Alphabets WHERE Letter = ?", (random_letter,))
print(db_cursor.fetchone())

#--------------------------------------------------------------------#

# Release the phonetics database
db_cursor.close()
db_connection.close()
