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


## IMPORTS

# Import the Tkinter functions
from Tkinter import *
# Import the function for downloading web pages
from urllib import urlopen

# Import the regular expression function
from re import findall

# Import a constructor for converting byte data to character strings
from StringIO import StringIO
# Import the Python Imaging Library module (comment this line out
# if you do not intend to use PIL in your solution)
#from PIL import Image, ImageTk



## Required Variables
image_url='https://upload.wikimedia.org/wikipedia/en/thumb/0/0b/Woolworths_Stacked_Tag_RGB_Positive_HR.png/220px-Woolworths_Stacked_Tag_RGB_Positive_HR.png'
date_and_time_url = 'http://www.timeanddate.com/worldclock/australia/brisbane'

Products=[]
Prices = []

## Create the window
window=Tk()
window.title("Waiting Screen")
window.geometry('480x320')
window.grid_columnconfigure(0, weight=1)
window.grid_rowconfigure(4, weight=1)

## Background Image
# Download inital image, resize it to fit the screen and place it into the GUI
# Open image from website
# original_image=Image.open(StringIO(urlopen(image_url).read()))
# required_height=300 # required pixel height of image
# # Find the ratio of the new height from the original height
# height_percentage=(required_height/float(original_image.size[1]))
# # Create a variable of the new width from the ratio of the original width
# image_width=int((float(original_image.size[0])*float(height_percentage)))
# #resize the image with the new size values and import the image into the window
# resized_image=original_image.resize((image_width, required_height),Image.ANTIALIAS)
# background_image=ImageTk.PhotoImage((resized_image))
# background_label = Label(window, image=background_image)
# background_label.place(x=0, y=30, relwidth=1, relheight=1)


## Main Headings
main_label=Label(window, text="Welcome to Woolworths", fg="green",
                 font=("Times New Roman", 30, 'bold'), justify=CENTER)
start_label=Label(window, text="Please scan your card to borrow a trolley", fg="black",
                 font=("Times New Roman", 15), justify=CENTER)
main_label.grid(row=0, sticky = W + E)
start_label.grid(row=1, sticky = W + E)

## Date and Time
date_and_time_web_page_contents = urlopen(date_and_time_url).read()
date=findall('ctdat>([A-Za-z, 0-9]*)',date_and_time_web_page_contents)
time=findall('class=h1>(.*)</span> <span id=cta',date_and_time_web_page_contents)
# Final string of the current date and time to be used in the GUI
date_and_time=date[0]+" " + time[0]
date_label=Label(window, text=date_and_time, fg="black",
                 font=("Times New Roman", 10), justify=CENTER)
date_label.grid(row=3, sticky = W + E)

part_label=Label(window, fg="black",
                  font=("Times New Roman", 20, 'bold'), justify=CENTER)
price_label=Label(window,  fg="black",
                  font=("Times New Roman", 20, 'bold'), justify=CENTER)
total_label=Label(window, fg="black",
                  font=("Times New Roman", 20, 'bold'), justify=CENTER)

    
def restart():
    main_label=Label(window, text="Welcome to Woolworths", fg="green",
                 font=("Times New Roman", 30, 'bold'), justify=CENTER)
    start_label=Label(window, text="Please scan your card to borrow a trolley", fg="black",
                 font=("Times New Roman", 15), justify=CENTER)
    main_label.grid(row=0, sticky = W + E)
    start_label.grid(row=1, sticky = W + E)
    ## Date and Time
    date_and_time_web_page_contents = urlopen(date_and_time_url).read()
    date=findall('ctdat>([A-Za-z, 0-9]*)',date_and_time_web_page_contents)
    time=findall('class=h1>(.*)</span> <span id=cta',date_and_time_web_page_contents)
    # Final string of the current date and time to be used in the GUI
    date_and_time=date[0]+" " + time[0]
    date_label=Label(window, text=date_and_time, fg="black",
                     font=("Times New Roman", 10), justify=CENTER)
    date_label.grid(row=3, sticky = W + E)

    part_label=Label(window, fg="black",
                      font=("Times New Roman", 20, 'bold'), justify=CENTER)
    price_label=Label(window,  fg="black",
                      font=("Times New Roman", 20, 'bold'), justify=CENTER)
    total_label=Label(window, fg="black",
                      font=("Times New Roman", 20, 'bold'), justify=CENTER)
    main_button=Button(window, text="main", width=30, relief="groove", fg="black",
                      command= lambda: main())
    main_button.grid(row=4, sticky = W + E)
    window.after(1000, lambda: main())
        

def id_scan(ffname, ssname):
    main_label.config(text = 'Welcome %s %s' % (ffname, ssname), fg='black', font=("Times New Roman", 30))
    start_label.config(text = 'You\'re good to go, start scanning products')
    main_label.update()
    start_label.update()

##def product_info():
##    info_label=Label(window, text='Product info comming soon', fg="black",
##                  font=("Times New Roman", 20, 'bold'), justify=CENTER)
##    info_label.grid(row=5, sticky = W + E)
##    print 'Product info comming soon'
##

def finish_pay():
    print"Thanks for shopping"
    finished=1
    CardID = 0
    Userdata = []
    x = 2
   # window.after(10000, lambda: os.execv(sys.executable, [sys.executable] + sys.argv))
    window.after(1000, lambda: restart())
    return x, finished, CardID, Userdata
    
    

        

def clear(pname, pprice, Total, fname):
    part_label.config(text='Latest product added: %s' % pname)
    price_label.config(text='Price of %s is %s' % (pname, pprice))
    total_label.config(text='Your current running total is $%s' % Total)
    start_label.forget()
    main_label.config(text = '%s current shopping' % fname, fg='black', font=("Times New Roman", 10))
    part_label.grid(row=5, sticky = W + E)
    price_label.grid(row=6, sticky = W + E)
    total_label.grid(row=7, sticky = W + E)
    part_label.update()
    price_label.update()
    total_label.update()
    main_label.update()
    
##    information.update()
##information=Button(window, text="Information", width=30, relief="groove", fg="black",
##                      command= lambda: product_info())    
global frame2
def done(Products, Prices, Total):
    part_label.forget()
    price_label.forget()
    total_label.forget()
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
##    total_label.grid(row=6, sticky = W + E, columnspan=100)
    total_label.update()
##    frame2.update()
    print "2lease scan your card to borrow a trolley"
    
def main():
    os.system('clear')
    ProductID = 0
    main_button.destroy()
    
##    information.grid(row=10, sticky = W + E)
    while True:
        # Get the user to scan to borrow the Trolly
        print "Please scan your card to borrow a trolley"

        


        #Read Current Value
        CardID = read(pn532)
        print CardID + "5"
        Total = 0
        finished = 0
        Userdata = queryCardID(CardID)


##        # the card is not registered to a user
##        # user is prompted to register or leave
##        while not Userdata:
##            print "You dont have an account with use"
##            print "Would you like to set one up and speed up your shopping experience today?"
##            print "Type yes to register or no to leave"
##            #get the user to either add there card or leave
##            UserInput = raw_input()
##
##            # User wants to add there card
##            if UserInput == 'yes':
##                print"Lets get started"
##                FirstName = raw_input('Whats your firstname? ')
##                LastName = raw_input('and lastname? ')
##                addUser(CardID, FirstName, LastName)
##                Userdata = Userdata = queryCardID(CardID)
##                
##
##            #user wants to leave
##            else:
##                os.system('clear')
##                print"Thanks anyways, checkout with us later"     
        print CardID + "4"
        print Userdata[0]
        # The card has a user
        while Userdata:
            print CardID + "1"
            print Userdata
            fname = Userdata[0]
            sname = Userdata[1]
            id_scan(fname, sname)
            print"22Thanks anyways, checkout with us later"
                
            while finished==0:
                print CardID + "3"
                print Userdata[1]
                ProductID = read(pn532)
                ProductData = queryProductID(ProductID)
                
                # whatever was just scanned isn't a product so just keep looking for products
                if ProductID == CardID:
                    done(Products, Prices, Total)
                    print"2Thanks anyways, checkout with us later"
                    
                    print CardID + "2"
                    
                    
                    finished_pay_button=Button(window, text="Finish and pay", width=30, relief="groove", fg="black",
                                                command= lambda: finish_pay())
                    finished_pay_button.grid(row=4, sticky = W + E)
                    finished_pay_button.update()
                    x=1
                    while x==1:
                        finished_pay_button.update()
                    

                # the item being scanned is not a product, cdo nothing and continue scanning
                elif not ProductData:
                        bob = "do nothing and keep scanning"

                # a product was scanned so add it to the local total
                else:
                    print '2Product info comming soon'
                    pname = ProductData[0]
                    pprice = ProductData[1]
                    Products.append(pname)
                    Prices.append(pprice)
                    print Products
                    print Prices
                    Total = Total + pprice
                    clear(pname, pprice, Total, fname)
                    
##                    information.update()
    ##                print("%s Costs $%s" % (pname, pprice))
    ##                print("Total $%d" % Total)
            print"end of first loop"
            
    
main_button=Button(window, text="main", width=30, relief="groove", fg="black",
                      command= lambda: main())
main_button.grid(row=4, sticky = W + E)

window.mainloop()
