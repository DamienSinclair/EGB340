#Import system libs
import sys
import os

#Import RFID Libs
sys.path.append('/home/pi/Desktop/EGB340/RFID')
from libRFID import *
import Adafruit_PN532 as PN532
    #Configure the Reader
pn532 = initialise_RFID(6, 26, 13, 19)

#Import Database Libs
sys.path.append('/home/pi/Desktop/EGB340/Database')
from LibMySQL import*
import MySQLdb

#Import GUI Libs
    # Import the Tkinter functions
from Tkinter import *
sys.path.append('/home/pi/Desktop/EGB340/Screen')
from LibScreen import*


#Import Live Date & Time Libs
from urllib import urlopen
from re import findall
from StringIO import StringIO
    # Required Variables
date_and_time_url = 'http://www.timeanddate.com/worldclock/australia/brisbane'
    ## Date and Time
date_and_time_web_page_contents = urlopen(date_and_time_url).read()
date=findall('ctdat>([A-Za-z, 0-9]*)',date_and_time_web_page_contents)
time=findall('class=h1>(.*)</span> <span id=cta',date_and_time_web_page_contents)
    # Date and time add to the same string
date_and_time=date[0]+" " + time[0]


# Global Variables
Products=[]
Prices = []


# GUI Definitions
    # Date and time
date_label=Label(window, text=date_and_time, fg="black", font=("Times New Roman", 10), justify=CENTER)
date_label.grid(row=3, sticky = W + E)
    # Initial button - to start everything 
main_button=Button(window, text="main", width=30, relief="groove", fg="black",
                      command= lambda: main())
main_button.grid(row=4, sticky = W + E)

#Button Definitions
    # Finish and Pay
##finished_pay_button=Button(window, text="Finish and pay", width=30, relief="groove", fg="black", command= lambda: finished_pay_button())
##finished_pay_button.grid(row=4, sticky = W + E)



##part_label=Label(window, fg="black", font=("Times New Roman", 20, 'bold'), justify=CENTER)
##price_label=Label(window,  fg="black", font=("Times New Roman", 20, 'bold'), justify=CENTER)
##total_label=Label(window, fg="black", font=("Times New Roman", 20, 'bold'), justify=CENTER)

    
def Update_Cart(pname, pprice, Total, fname):
    product_label.config(text='Latest product added: %s' % pname)
    price_label.config(text='Price of %s is %s' % (pname, pprice))
    total_label.config(text='Your current running total is $%s' % Total)
    start_label.forget()
    main_label.config(text = '%s current shopping' % fname, fg='black', font=("Times New Roman", 10))
    product_label.grid(row=5, sticky = W + E)
    price_label.grid(row=6, sticky = W + E)
    total_label.grid(row=7, sticky = W + E)

    product_label.update()
    price_label.update()
    total_label.update()
    main_label.update()
   
   
def main():
    os.system('clear')   
    main_button.destroy()
    pressed = False
    print "tests"
##    information.grid(row=10, sticky = W + E)
    while True:
        # Get the user to scan to borrow the Trolly
        print "Please scan your card to borrow a trolley"

        
        #Read Current Value
        CardID = read(pn532)

        # test line
        print CardID + "5"
        main_button.destroy()
        Total = 0
        finished = 0
        Userdata = queryCardID(CardID)

        # test line
        print CardID + "4"
        print Userdata[0]
              
        # The card has a user
        while Userdata:
            # test line
            print CardID + "1"
            print Userdata
            
            fname = Userdata[0]
            sname = Userdata[1]

            # Welcome User and start shopping
            welcome_user(fname, sname)

            # test line
            print"22Thanks anyways, checkout with us later"
                
            while finished==0:
                
                # test line
                print CardID + "3"
                print Userdata[1]

                ProductID = read(pn532)
                ProductData = queryProductID(ProductID)
                

                # a product was scanned so add it to the local total
                if ProductData:

                    # test line
                    print '2Product info comming soon'

                    pname = ProductData[0]
                    pprice = ProductData[1]

                    # add new items and price to Python Lists
                    Products.append(pname)
                    Prices.append(pprice)

                    Total = Total + pprice

                    # Update Screen
                    Update_Cart(pname, pprice, Total, fname)
                    
                # The item is product
                elif ProductID == CardID:

                    Check_out(Products, Prices, Total)

                    # test line
                    print"2Thanks anyways, checkout with us later"
                    print CardID + "2"
                    finished_pay_button=Button(window, text="Finish and pay", width=30, relief="groove", fg="black", command= lambda: finished_pay_button())
                    finished_pay_button.grid(row=4, sticky = W + E)

                    finished_pay_button.update()
##                    while ProductID == CardID:

                    print"Stuck in loop"
                    if pressed:
                        finish_pay()

                        
##                    if not finished_pay_button:
##                        finish_pay()

##                    finished_pay_button.update()
##                    x=1
##                    while x==1:
##                        print"Stuck in loop"
                    

            # test line
            print"end of first loop"
            



window.mainloop()
