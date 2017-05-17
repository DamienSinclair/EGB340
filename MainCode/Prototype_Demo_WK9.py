#Import system libs
import sys
import os

#Import RFID Libs
import Adafruit_PN532 as PN532
sys.path.append('/home/pi/Desktop/EGB340/RFID')
from libRFID import *

#Import Database Libs
import MySQLdb
sys.path.append('/home/pi/Desktop/EGB340/Database')
from LibMySQL import*


os.system('clear')
ProductID = 0

#Configure the Reader
pn532 = initialise_RFID(6, 26, 13, 19)

while True :
    # Get the user to scan to borrow the Trolly
    print "Please scan your card to borrow a trolley"

    #Read Current Value
    CardID = read(pn532)

    Userdata = queryCardID(CardID)

    # the card is not registered to a user
    # user is prompted to register or leave
    while not Userdata:
        print "You dont have an account with use"
        print "Would you like to set one up and speed up your shopping experience today?"
        print "Type yes to register or no to leave"
        #get the user to either add there card or leave
        UserInput = raw_input()

        # User wants to add there card
        if UserInput == 'yes':
            print"Lets get started"
            FirstName = raw_input('Whats your firstname? ')
            LastName = raw_input('and lastname? ')
            addUser(CardID, FirstName, LastName)
            Userdata = Userdata = queryCardID(CardID)
            break

        #user wants to leave
        else:
            os.system('clear')
            print"Thanks anyways, checkout with us later"
            break

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
            if ProductID == CardID:
                os.system('clear')
                print("Thanks for shopping %s" %fname)
                print("Your total is $%d" %Total)
                break

            # the item being scanned is not a product, cdo nothing and continue scanning
            elif not ProductData:
                    bob = "do nothing and keep scanning"

            # a product was scanned so add it to the local total
            else:
                pname = ProductData[0]
                pprice = ProductData[1]

                Total = Total + pprice
                print("%s Costs $%s" % (pname, pprice))
                print("Total $%d" % Total)

        break
