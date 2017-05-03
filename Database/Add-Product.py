# Database library
import MySQLdb
# RFID Library
from libRFID import *
import Adafruit_PN532 as PN532
#Configure the Reader
pn532 = initialise_RFID(18, 25, 23, 24)
#Set Server Settings
ip = "34.209.19.53"
user = "root"
password = "Peanut"
database = "EGB340"



# Setting up new product

# user scan new product to start
print('Scan a new product')
 = read(pn532)

P = raw_input('Enter Value: ')
