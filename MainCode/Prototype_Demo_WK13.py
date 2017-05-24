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

   
def main():
    Waiting_for_user()
    os.system('clear')

    global pressed
    global finished_pay_button

    pressed = False
    
    print "tests"

    while True:
        # Get the user to scan to borrow the Trolly
        print "Please scan your card to borrow a trolley"
        
        #Read Current Value
        CardID = read(pn532)

        # test line
        print CardID + "5"

        Total = 0
        finished = 0
        Userdata = queryCardID(CardID)

        # test line
        print CardID + "4"
      
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
                    print 'Product Data is in MySQL Database'
                    print ProductData
                            
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

                    # test line
                    print 'ProductID is CardID'
                    print ProductData
                    
                    Check_out(Products, Prices, Total)
                    
                    # test line
                    print"2Thanks anyways, checkout with us later"
                    print CardID + "2"
                    finished_pay_button=Button(window, text="Finish and pay", width=30, relief="groove", fg="black",
                                               command= finish_pay)
                    finished_pay_button.grid(row=4, sticky = W + E)

                    while pressed == False:
                        finished_pay_button.update()

                    # Reset all variable used
                    pressed = False
                    CardID = None
                    Userdata = []
                    ProductData = []
                    ProductID = None
                    pname = None
                    pprice = None
                    fname = None
                    finished = 1
                    finished_pay_button.grid_forget()

                    print ProductData
            
                    print"RESET"

                    Waiting_for_user()

            print"end of first loop"

def Check_out(Products, Prices, Total):
    global frame2
    global list_box
    global scroll

    product_label.grid_forget()
    price_label.grid_forget()
    
    frame2=Frame(window, bd=2, relief=SUNKEN)
    scroll = Scrollbar(frame2, orient=VERTICAL)
    scroll.pack(side=RIGHT,fill=Y)
    list_box = Listbox(frame2, bd=0, height = 5)
    list_box.pack()
    scroll.configure(command=list_box.yview)
    list_box.configure(yscrollcommand=scroll.set)

    for i in range(0,len(Products)):
        x=i+1
        list_box.insert(END,"%s:   %s   $%s" % (x, Products[i], Prices[i]))
        list_box.config(font=("Times New Roman", 15))

    frame2.grid(row=5, sticky = W + E, columnspan=100)

    total_label.config(text='Your total is $%s' % Total)

    total_label.update()

    print "2lease scan your card to borrow a trolley"
 

def finish_pay():
    
    total_label.grid_forget()

    global pressed
    global finished_pay_button
    global frame2
    global list_box
    global scroll

    pressed = True
    finished_pay_button.grid_forget()
    list_box.pack_forget()
    scroll.grid_forget()
    frame2.grid_forget()

main()
window.mainloop()
