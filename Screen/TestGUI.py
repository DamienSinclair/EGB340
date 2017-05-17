# import system libs
import sys
from Tkinter import *
import tkFont

#Import RFID Libs
import Adafruit_PN532 as PN532
sys.path.append('/home/pi/Desktop/EGB340/RFID')
from libRFID import *

#Import Database Libs
import MySQLdb
sys.path.append('/home/pi/Desktop/EGB340/Database')
from LibMySQL import*

#Configure the RFID Reader
RFIID = initialise_RFID(6, 26, 13, 19)


## GUI Definitions

# creating the object mGui
mGui = Tk()

myFont = tkinter.font.Font(family = 'Helvetica', size = 12, weight = "bold")

## action event

<<<<<<< HEAD
if not RFIID:
=======
if not RFID-ID:
>>>>>>> 7abd8afbafc0a8fa57a4f8c96c84988ad0dc47b9
    RFIDRead["text"] = "%s" % RFID-ID

## Widgets
RFIDRead = Button(mGui, text = 'Read RFID', font = myfont, command = readRFID, gb = 'bisque2', height = 1, width = 24)
RFIDRead.grid(row=0, column=1)

#setting up the screen size
mGui.title("RFID/Screen Test")
mGui.geometry('400x400')
