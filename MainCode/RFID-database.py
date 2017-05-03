
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
    while not Userdata:
        print "You dont have an account with use"
        print "Would you like to set one up and speed up your shopping experience today?"

        #get the user to either add there card or leave
        UserInput = raw_input()

        # User wants to add there card
        if UserInput == 'yes':
            print"sweet bro, lets sign up"
            FirstName = raw_input('Whats your firstname? ')
            LastName = raw_input('and lastname? ')
            addUser(CardID, FirstName, LastName)
                        
        #user wants to leave
        else:
            print"Thanks anyways, checkout with us later"
        

    # The card has a user
    while Userdata:
        fname = Userdata[0]
        sname = Userdata[1] 
        print('Hi %s') %fname

        print "You're good to go"
        print "Start scanning products"

        k = 1
        Total = 0
        finished = 0
        while finished==0:

            ProductID = read(pn532)

            ProductData = queryProductID(ProductID)

            # whatever was just scanned isn't a product so just keep looking for products
            if not ProductData:
                    bob = "do nothing and keep scanning"

            # a product was scanned so add it to the tally
            else:
                pname = ProductData[0]
                pprice = ProductData[1]

                
                Total = Total + pprice
                print("%s Costs $%s" % (pname, pprice))

                print("Total $%d" % Total)

                

                




                
