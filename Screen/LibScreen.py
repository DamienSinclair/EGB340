import os
from Tkinter import *

## Create the window
window=Tk()
window.title("Waiting Screen")
window.geometry('480x320')
window.grid_columnconfigure(0, weight=1)
window.grid_rowconfigure(4, weight=1)


# GUI Definitions
    # Welcome to Wollies Label
main_label=Label(window, text="Welcome to Woolworths", fg="green", font=("Times New Roman", 30, 'bold'), justify=CENTER)
    # Start to scan label
start_label=Label(window, text="Please scan your card to borrow a trolley", fg="black", font=("Times New Roman", 15), justify=CENTER)
    # Product Label
product_label=Label(window, fg="black", font=("Times New Roman", 20, 'bold'), justify=CENTER)
# Product1 Label
product1_label=Label(window, fg="black", font=("Times New Roman", 20, 'bold'), justify=CENTER)
    
    # Price
price_label=Label(window,  fg="black", font=("Times New Roman", 20, 'bold'), justify=CENTER)
    # Total
total_label=Label(window, fg="black", font=("Times New Roman", 20, 'bold'), justify=CENTER)

def Waiting_for_user():
        # Text Defs
    main_label.config(text="Welcome to Woolworths", fg="green", font=("Times New Roman", 30, 'bold'), justify=CENTER)
    start_label.config(text="Please scan your card to borrow a trolley", fg="black", font=("Times New Roman", 15), justify=CENTER)
        # Grid Defs
    main_label.grid(row=0, sticky = W + E)
    start_label.grid(row=1, sticky = W + E)
        # Push to Window
    main_label.update()
    start_label.update()
    
# A user has scanned there Card and is starting to shop
def welcome_user(ffname, ssname):
        # Text Defs
    main_label.config(text = 'Welcome %s %s' % (ffname, ssname), fg='black', font=("Times New Roman", 30))
    start_label.config(text = 'You\'re good to go, start scanning products')
        # Push to Window
    main_label.update()
    start_label.update()

# User wants additional information to be displayed about the item
def product_info():
    info_label=Label(window, text='Product info comming soon', fg="black",
                  font=("Times New Roman", 20, 'bold'), justify=CENTER)
    info_label.grid(row=5, sticky = W + E)
    print 'Product info comming soon'
def Remove_Cart(pname, pprice, Total, fname):
    # Forget Unused 
    start_label.grid_forget()
        # Text Defs
    product_label.config(text='Product removed')
    product1_label.config(text='%s' % pname)
    #price_label.config(text='The price is $%s' % pprice)
    total_label.config(text='Your current running total is $%s' % Total)
    main_label.config(text = '%s current shopping - Scan your card to finish' % fname, fg='black', font=("Times New Roman", 10))
        # Grid Defs
    product_label.grid(row=5, sticky = W + E)
    product1_label.grid(row=6, sticky = W + E)
    price_label.grid(row=7, sticky = W + E)
    total_label.grid(row=8, sticky = W + E)
        # Push to Window
    product_label.update()
    price_label.update()
    total_label.update()
    main_label.update()   
    
def Update_Cart(pname, pprice, Total, fname):
        # Forget Unused 
    start_label.grid_forget()
        # Text Defs
    product_label.config(text='Latest product added')
    product1_label.config(text='%s' % pname)
    price_label.config(text='The price is $%s' % pprice)
    total_label.config(text='Your current running total is $%s' % Total)
    main_label.config(text = '%s current shopping - Scan your card to finish' % fname, fg='black', font=("Times New Roman", 10))
        # Grid Defs
    product_label.grid(row=5, sticky = W + E)
    product1_label.grid(row=6, sticky = W + E)
    price_label.grid(row=7, sticky = W + E)
    total_label.grid(row=8, sticky = W + E)
        # Push to Window
    product_label.update()
    price_label.update()
    total_label.update()
    main_label.update()   
   


           

