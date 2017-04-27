from libRFID import *
import Adafruit_PN532 as PN532

#Configure the Reader
pn532 = initialise_RFID(18, 25, 23, 24)


while True :

    #Read Current Value
    r = read(pn532)

    #Print Current Value
    print "Card ID %s" % r
