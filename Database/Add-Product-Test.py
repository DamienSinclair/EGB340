import sys

# Database library
import MySQLdb

# database library
sys.path.append('/home/pi/Desktop/EGB340/Database')
from LibMySQL import *

# RFID Library
#adafruit Library
import Adafruit_PN532 as PN532
#scanning library
sys.path.append('/home/pi/Desktop/EGB340/RFID')
from libRFID import *

#Configure the Reader
pn532 = initialise_RFID(18, 25, 23, 24)

# Setting up new product
while 1:
    # user scan new product to start
    print('Scan a new product')

    productID = read(pn532)

    #queryProductID working
    data = queryProductID(productID)

    if not data: #not working
        PDesc = raw_input('Enter Product Discription: ')
        PCost = raw_input('Enter Product Cost: ')

        print('Product ID = %s') %productID
        print('Product Description = %s') %PDesc
        print('Product Cost = %s') %PCost

        
        #add products is not coming up on the database
        addProduct(productID,PDesc,PCost)

        print('The product has been added')


    else: #working
        ProductDesc = data[0]
        ProductCost = data[1]
        print('The product you are scanning is already as...')
        print('Product Description = %s') %ProductDesc
        print('Product Cost = %s') %ProductCost
        print"Please scan another item"

