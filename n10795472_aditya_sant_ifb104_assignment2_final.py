
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
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  Submitted files will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Assignment Description-----------------------------------------#
#
#  Runners-Up
#
#  In this assignment you will combine your knowledge of HTMl
#  mark-up languages with your skills in Python scripting, pattern
#  matching, and Graphical User Interface design to produce a useful
#  application that allows the user to access online data.  See the
#  instruction sheet accompanying this file for full details.
#
#--------------------------------------------------------------------#



#-----Imported Functions---------------------------------------------#
#
# Below are various import statements for helpful functions.  You
# should be able to complete this assignment using these functions
# only.  You can import other functions provided they are standard
# ones that come with the default Python/IDLE implementation and NOT
# functions from modules that need to be downloaded and installed
# separately.  Note that not all of the imported functions below are
# needed to successfully complete this assignment.

# The function for accessing a web document given its URL.
# (You WILL need to use this function in your solution,
# either directly or via our "download" function.)
import urllib.request
from urllib.request import urlopen

# The function for displaying a web document in the host
# operating system's default web browser.  We have given
# the function a distinct name to distinguish it from the
# built-in "open" function for opening local files.
# (You WILL need to use this function in your solution.)
import webbrowser
from webbrowser import open as urldisplay

# Import some standard Tkinter functions. (You WILL need to use
# some of these functions in your solution.)  You may also
# import other widgets from the "tkinter" module, provided they
# are standard ones and don't need to be downloaded and installed
# separately.
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter.ttk import Progressbar
from tkinter.ttk import Combobox

# Functions for finding all occurrences of a pattern
# defined via a regular expression, as well as
# the "multiline" and "dotall" flags.  (You do NOT need to
# use these functions in your solution, because the problem
# can be solved with the string "find" function, but it will
# be difficult to produce a concise and robust solution
# without using regular expressions.)
from re import findall, finditer, MULTILINE, DOTALL

# Import the standard SQLite functions (just in case they're
# needed).
from sqlite3 import *

#
#--------------------------------------------------------------------#



#--------------------------------------------------------------------#
#
# A function to download and save a web document. If the
# attempted download fails, an error message is written to
# the shell window and the special value None is returned.
#
# Parameters:
# * url - The address of the web page you want to download.
# * target_filename - Name of the file to be saved (if any).
# * filename_extension - Extension for the target file, usually
#      "html" for an HTML document or "xhtml" for an XML
#      document.
# * save_file - A file is saved only if this is True. WARNING:
#      The function will silently overwrite the target file
#      if it already exists!
# * char_set - The character set used by the web page, which is
#      usually Unicode UTF-8, although some web pages use other
#      character sets.
# * lying - If True the Python function will try to hide its
#      identity from the web server. This can sometimes be used
#      to prevent the server from blocking access to Python
#      programs. However we do NOT encourage using this option
#      as it is both unreliable and unethical!
# * got_the_message - Set this to True once you've absorbed the
#      message above about Internet ethics.
#
def download(url = 'https://www.wikipedia.org',
             target_filename = 'download',
             filename_extension = 'html',
             save_file = True,
             char_set = 'UTF-8',
             lying = False,
             got_the_message = True):

    # Import the function for opening online documents and
    # the class for creating requests
    from urllib.request import urlopen, Request

    # Import an exception raised when a web server denies access
    # to a document
    from urllib.error import HTTPError

    # Open the web document for reading
    try:
        if lying:
            # Pretend to be something other than a Python
            # script (NOT RELIABLE OR RECOMMENDED!)
            request = Request(url)
            request.add_header('User-Agent', 'Mozilla/5.0')
            if not got_the_message:
                print("Warning - Request does not reveal client's true identity.")
                print("          This is both unreliable and unethical!")
                print("          Proceed at your own risk!\n")
        else:
            # Behave ethically
            request = url
        web_page = urlopen(request)
    except ValueError:
        print("Download error - Cannot find document at URL '" + url + "'\n")
        return None
    except HTTPError:
        print("Download error - Access denied to document at URL '" + url + "'\n")
        return None
    except Exception as message:
        print("Download error - Something went wrong when trying to download " + \
              "the document at URL '" + url + "'")
        print("Error message was:", message, "\n")
        return None

    # Read the contents as a character string
    try:
        web_page_contents = web_page.read().decode(char_set)
    except UnicodeDecodeError:
        print("Download error - Unable to decode document from URL '" + \
              url + "' as '" + char_set + "' characters\n")
        return None
    except Exception as message:
        print("Download error - Something went wrong when trying to decode " + \
              "the document from URL '" + url + "'")
        print("Error message was:", message, "\n")
        return None

    # Optionally write the contents to a local text file
    # (overwriting the file if it already exists!)
    if save_file:
        try:
            text_file = open(target_filename + '.' + filename_extension,
                             'w', encoding = char_set)
            text_file.write(web_page_contents)
            text_file.close()
        except Exception as message:
            print("Download error - Unable to write to file '" + \
                  target_filename + "'")
            print("Error message was:", message, "\n")

    # Return the downloaded document to the caller
    return web_page_contents

#
#--------------------------------------------------------------------#



#--------------------------------------------------------------------#
#
# A function to open a local HTML file in your operating
# system's default web browser.  (Note that Python's "webbrowser"
# module does not guarantee to open local files, even if you use a
# 'file://..." address).  The file to be opened must be in the same
# folder as this module.
#
# Since this code is platform-dependent we do NOT guarantee that it
# will work on all systems.
#
def open_html_file(file_name):
    
    # Import operating system functions
    from os import system
    from os.path import isfile
    
    # Remove any platform-specific path prefixes from the
    # filename
    local_file = file_name[file_name.rfind('/') + 1:] # Unix
    local_file = local_file[local_file.rfind('\\') + 1:] # DOS
    
    # Confirm that the file name has an HTML extension
    if not local_file.endswith('.html'):
        raise Exception("Unable to open file " + local_file + \
                        " in web browser - Only '.html' files allowed")
    
    # Confirm that the file is in the same directory (folder) as
    # this program
    if not isfile(local_file):
        raise Exception("Cannot find file " + local_file + \
                        " in the same folder as this program")
    
    # Collect all the exit codes for each attempt
    exit_codes = []
    
    # Microsoft Windows: Attempt to "start" the web browser
    code = system('start ' + local_file)
    if code != 0:
        exit_codes.append(code)
    else:
        return 0
    
    # Apple macOS: Attempt to "open" the web browser
    code = system("open './" + local_file + "'")
    if code != 0:
        exit_codes.append(code)       
    else:
        return 0
    
    # Linux: Attempt to "xdg-open" the local file in the
    # web browser
    code = system("xdg-open './" + local_file + "'")
    if code != 0:
        exit_codes.append(code)       
    else:
        return 0
    
    # Give up!
    raise Exception('Unable to open file ' + local_file + \
                    ' in web browser - Exit codes: ' + \
                    str(exit_codes))

#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
# Put your solution at the end of this file.
#

##### DEVELOP YOUR SOLUTION HERE #####

website_list = ['https://www.marketwatch.com/story/these-are-the-10-top-grossing-films-of-2018-2018-12-18',
                'https://www.alexa.com/topsites',
                'https://www.centralcharts.com/en/price-list-ranking/ALL/asc/ts_29-us-nyse-stocks--qc_1-alphabetical-order',
                'https://earthquaketrack.com/']

runnerup_lists =['Daily Earthquake Tracker', 'See runner up stocks',
                 'Alexa runner up websites', 'Highest grossing movies (static)']

def open_source():
    #selected_source = Label(the_window, text = clicked.get()).grid()
    if clicked.get() == 'Highest grossing movies (static)':
        urldisplay('https://www.marketwatch.com/story/these-are-the-10-top-grossing-films-of-2018-2018-12-18')
    if clicked.get() == 'Daily Earthquake Tracker':
        urldisplay('https://earthquaketrack.com/')
    if clicked.get() == 'Alexa runner up websites':
        urldisplay('https://www.alexa.com/topsites')
    if clicked.get() == 'See runner up stocks':
        urldisplay('https://www.centralcharts.com/en/price-list-ranking/ALL/desc/ts_29-us-nyse-stocks--qc_2-daily-change')

def see_list():
    #Show runner up and other items(movies) on static list
    if clicked.get() == 'Highest grossing movies (static)':
        runner_up_label['text'] = '2nd movie on the list: '
        others_label['text'] = 'Other movies on the list: '
        
        #download and open web document for static list
        download(url = 'https://www.marketwatch.com/story/these-are-the-10-top-grossing-films-of-2018-2018-12-18', target_filename = '2018')
        retrieve_list = open('2018.html', 'r', encoding='utf-8')
        retrieve_list_bytes = retrieve_list.read()

        #Find runner up on static list (Expected output should be 2. Avengers: Infinity War)
        global runnerup_movie, boxoffice
        runnerup_movie = re.findall('(2\.) <a href="https:\/\/www.boxofficemojo.com\/movies\/\?id=marvel0518.htm" target="_blank" class="icon none" >([A-Za-z: ]+)', retrieve_list_bytes) #Correct
        boxoffice = re.findall('ar<\/a> - (\$[0-9,]+)', retrieve_list_bytes)

        #Find other movies on the list
        global othermovies
        othermovies = re.findall('none" >([A-Za-z:\- ]+)', retrieve_list_bytes) #Complete

        #Paste runner up as a label inside the runner up label frame
        runnerup_name_label['text'] = runnerup_movie, boxoffice
        

        #Paste other movies into other items label frame (Expected output should be movie names and if preceded by numbers)
        other_items_label['text'] = othermovies
    
    if clicked.get() == 'Daily Earthquake Tracker':
        runner_up_label['text'] = '2nd most recent earthquake today: '
        others_label['text'] = 'Other earthquakes today: '

        #Download and open web document for updated list
        download(url = 'https://earthquaketrack.com/', target_filename = 'earthquake')
        retrieve_list2 = open('earthquake.html', 'r', encoding='utf-8')
        retrieve_list2_bytes = retrieve_list2.read()

        #Runner up earthquake on updated list
        recent_earthquake = re.findall("""1">\n  <h4 class='title text-warning'>([0-9\.]+ magnitude earthquake)<""", retrieve_list2_bytes) #Correct but two additional earthquakes are shown
        earthquake_location = re.findall('<a href="\/r\/([a-z-]+)\/recent">([A-Za-z ]+)<\/a>\n\n<\/div>\n<div class="quake-info-window" data-quakeIndex="1">\n  <[^<]+', retrieve_list2_bytes)

        #Paste runner up earthquake
        runnerup_name_label['wraplength'] = 350
        runnerup_name_label['text'] = recent_earthquake, earthquake_location
        
        #Other earthquakes on updated list (Expected output should be a location)
        other_earthquakes = re.findall('[0-9\.\s]+ magnitude earthquake', retrieve_list2_bytes) #Complete

        #Paste other earthquakes
        other_items_label['wraplength'] = 175 #Complete
        other_items_label['text'] = other_earthquakes
        
    if clicked.get() == 'See runner up stocks':
        runner_up_label['text'] = '2nd stock with most %change: '
        others_label['text'] = 'Other stocks: '

        #Download and open web document
        download(url = 'https://www.centralcharts.com/en/price-list-ranking/ALL/desc/ts_29-us-nyse-stocks--qc_2-daily-change', target_filename = 'stocks')
        retrieve_list3 = open('stocks.html', 'r', encoding='utf-8')
        retrieve_list3_bytes = retrieve_list3.read()

        #Find runner up today
        second_stock = re.search("alt='([A-Z \.])+", retrieve_list3_bytes) #Incomplete, FIND the second stock (not SEARCH)

        #Paste runner up
        runnerup_name_label['text'] = second_stock

        #Find other stocks on updated list
        other_stocks = re.findall("\=\'[A-Z\s]+", retrieve_list3_bytes) #Correct, change design and remove tags

        #Paste other stocks
        other_items_label['wraplength'] = 217 #Change
        other_items_label['text'] = other_stocks
        
    if clicked.get() == 'Alexa runner up websites':
        runner_up_label['text'] = '2nd most visited website: '
        others_label['text'] = 'Other websites: '

        #Download and open web document
        download(url = 'https://www.alexa.com/topsites', target_filename = 'alexa')
        retrieve_list4 = open('alexa.html', 'r', encoding = 'utf-8')
        retrieve_list4_bytes = retrieve_list4.read()

        #Find runner up website
        second_website = re.findall('(>2<)\/div>\n\s+<div class="td DescriptionCell">\n\s+<p class="">\n\s+<a href="\/siteinfo\/([a-z\.]+)', retrieve_list4_bytes)
        second_website_property = re.findall('>2<\/div>\n\s+<div class="td DescriptionCell">\n\s+<p class="">\n\s+<a href="\/siteinfo\/[a-z\.]+">[A-Za-z\.]+<\/a>\s+<\/p>\n\s+<\/div>\n\s+<div class="td right"><p>([0-9\:]+)'
                                            , retrieve_list4_bytes)

        #Paste runner up website
        runnerup_name_label['text'] = second_website, second_website_property, 'daily hours spent'

        #Find other websites on updated list
        other_websites = re.findall('info/([a-z\.]+)', retrieve_list4_bytes) #Complete
        website_property = re.findall('info\/[a-z\.]+">[A-Za-z\.]+<\/a>\s+<\/p>?\n\s+<\/div>\n\s+<div class="td right"><p>([0-9\:]+)', retrieve_list4_bytes)

        #paste other websites
        other_items_label['wraplength'] = 100
        other_items_label['text'] = other_websites
#Save data into sql
def connect_db():
    connection = connect('runners_up.db')
    c = connection.cursor()
    if clicked.get() == 'Highest grossing movies (static)':
        c.execute("INSERT INTO runner_up VALUES (:competitor, :property)", {'competitor': runnerup_movie, 'property': boxoffice})
        connection.commit
        c.execute("INSERT INTO others VALUES(:competitor, :property)", {'competitor': other_movies, 'property': 'box office'})
    if clicked.get() == 'Daily Earthquake Tracker':
        c.execute("INSERT INTO runner_up VALUES (:competitor, :property)", {'competitor': recent_earthquake, 'property': 'magnitude'})
        connection.commit
    if clicked.get() == 'See runner up stocks':
        c.execute("INSERT INTO runner_up VALUES (:competitor, :property)", {'competitor': second_stock, 'property': 'gain'})
        connection.commit
    if clicked.get() == 'Alexa runner up websites':
        c.execute("INSERT INTO runner_up VALUES (:competitor, :property)", {'competitor': second_website, 'property': second_website_property})
        connection.commit
        c.execute("INSERT INTO others VALUES(:competitor, property)", {'competitor': other_websites, 'property': website_property})
        connection.commit
    connection.close
# GUI code
# Create a window
the_window = Tk()

# Give the window a title
the_window.title('Runners Up')

#Window elements
the_window['bg'] = ('slate blue')
the_window.geometry('900x500')

#Menubox Details
clicked = StringVar()
list_options = OptionMenu(the_window, clicked, *runnerup_lists)

#Label frame for image
image_frame = LabelFrame(the_window, bg = 'slate blue')
image_frame.grid(row = 0, column = 0, sticky = N)

#Image to indicate Runner's up program
display_image = PhotoImage(file = 'runners_up.gif')
display_image = display_image.subsample(5)
Label(image_frame, image = display_image).\
                 grid(row = 0, column = 0, sticky = W)

#Runner up indicator
runner_up_frame = LabelFrame(the_window, text = 'Runner up on selected list', bg = 'slate blue')
runner_up_label = Label(runner_up_frame, text = 'Nothing selected yet', font = ('Arial', 15), bg = 'slate blue')

runnerup_name_label = Label(runner_up_frame, text = ' ', font = ('Arial', 10), bg = 'slate blue', wraplength = 250)
runnerup_name_label.grid(row = 1, column = 0, sticky = W)

#Other items on the list
others_frame = LabelFrame(the_window, text = 'Other items on the selected list', bg = 'slate blue')
others_label = Label(others_frame, text = 'Nothing selected yet', font = ('Arial', 15), bg = 'slate blue')

other_items_label = Label(others_frame, text = 'Press Update button', font = ('Arial', 10), bg = 'slate blue', wraplength = 150)
other_items_label.grid(row = 1, column = 0, sticky = W)

#Save button
save_button = Button(the_window, text = 'Save', font = ('Arial', 15), command = connect_db)

#Open website source
source_button = Button(the_window, text = 'Open Source', font = ('Arial', 15), command = open_source)

#Update list button
update_button = Button(the_window, text = 'Update', font = ('Arial', 15), command = see_list)

#Instructions to run program
instructions = Label(the_window, text = '1. select list from option menu (under image)\n 2. press update button to display/change list\n 3. press open source button to see original site', font = ('Arial', 10), bg = 'slate blue')

#Paste buttons, labels, menus, etc. onto window
#Paste option menu and instructions
list_options.grid(row = 1, column = 0, sticky = W)
instructions.grid(row = 1, column = 1, sticky = W)

#Paste open source button
source_button.grid(row = 0, column = 1, sticky = N)

#Paste update button and save button
update_button.grid(row = 3, column = 0, sticky = NW)
save_button.grid(row = 2, column = 0, sticky = W)

runner_up_label.grid(row = 0, column = 0, sticky = S)
runner_up_frame.grid(row = 3, column = 1, sticky = N, padx = 15, pady = 15)

others_label.grid(row = 0, column = 0, sticky = S)
others_frame.grid(row = 3, column = 2, sticky = N, padx = 15, pady = 15)
