# How the modules were setup
# from libRFID import *
# import Adafruit_PN532 as PN532
# import MySQLdb
# from LibMySQL import *
# import time
# import sys
# import os

import sys

sys.path.append('/home/pi/Desktop/EGB340/RFID')
from libRFID import *
import Adafruit_PN532 as PN532

sys.path.append('/home/pi/Desktop/EGB340/Database')
import MySQLdb
from LibMySQL import *

#Configure the Reader
pn532 = initialise_RFID(18, 25, 23, 24)

while True :

    #Read Current Value
    CardID = read(pn532)

    Userdata = queryCardID(CardID)

    fname = Userdata[0]
    sname = Userdata[1]

    print "Hello", (fname, sname)

    print "scan a product"

    while CardID != None:

        ProductID = read(pn532)

        ProductData = queryProductID(ProductID)

        pname = ProductData[0]
        pprice = ProductData[1]

        print "shit", (pname, pprice)
