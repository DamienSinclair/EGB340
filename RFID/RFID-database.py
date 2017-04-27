from libRFID import *
import Adafruit_PN532 as PN532
import MySQLdb
from LibMySQL import *



#Configure the Reader
pn532 = initialise_RFID(18, 25, 23, 24)


while True :

    #Read Current Value
    CardID = read(pn532)

    data = queryCardID(CardID)

    fname = data[0]
    sname = data[1]
    
    print "Hello", (fname, sname)
