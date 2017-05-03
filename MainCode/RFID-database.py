
import sys

#import RFID Libs
import Adafruit_PN532 as PN532
sys.path.append('/home/pi/Desktop/EGB340/RFID')
from libRFID import *

#Import Database Libs
import MySQLdb
sys.path.append('/home/pi/Desktop/EGB340/Database')
from LibMySQL import*


#Configure the Reader
pn532 = initialise_RFID(18, 25, 23, 24)

while True :
    # Get the user to scan to borrow the Trolly
    print "Please scan your card to borrow a trolly"

    #Read Current Value
    CardID = read(pn532)

    Userdata = queryCardID(CardID)

    # the card is not registered to a user
    if not Userdata:
        print "You dont have an account with use"
        print "Would you like to set one up and speed up your shopping experience today?"

        UserInput = raw_input()

        if UserInput == 'yes':
            print"sweet as bro"
            end

    # The card has a user
    else:
        fname = Userdata[0]
        sname = Userdata[1] 
        print('Hi %s') %fname

        print "You're good to go"
        print "Start scanning products"

        k = 1
        
        while k==1:

            ProductID = read(pn532)

            ProductData = queryProductID(ProductID)

            pname = ProductData[0]
            pprice = ProductData[1]

            print("%s Costs %s" % (pname, pprice))
