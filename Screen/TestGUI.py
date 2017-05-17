# import system libs
import sys
from tkinter import *
import tkinter.font

#Import RFID Libs
import Adafruit_PN532 as PN532
sys.path.append('/home/pi/Desktop/EGB340/RFID')
from libRFID import *

#Import Database Libs
import MySQLdb
sys.path.append('/home/pi/Desktop/EGB340/Database')
from LibMySQL import*

#Configure the RFID Reader
RFID-ID = initialise_RFID(6, 26, 13, 19)


## GUI Definitions

# creating the object mGui
mGui = Tk()
mGui.title("RFID/Screen Test")
myFont = tkinter.font.Font(family = 'Helvetica', size = 12, weight = "bold")

## action event

if not RFID-ID
    RFIDRead["text"] = "%s" % RFID-ID

## Widgets
RFIDRead = Button(mGui, text = 'Read RFID', font = myfont, command = readRFID, gb = 'bisque2', height = 1, width = 24)
RFIDRead.grid(row=0, column=1)

#setting up the screen size
mGui.geometry('400x400')
