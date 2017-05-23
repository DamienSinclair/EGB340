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
main_label.grid(row=0, sticky = W + E)
    # Start to scan label
start_label=Label(window, text="Please scan your card to borrow a trolley", fg="black", font=("Times New Roman", 15), justify=CENTER)
start_label.grid(row=1, sticky = W + E)
    # Product Label
product_label=Label(window, fg="black", font=("Times New Roman", 20, 'bold'), justify=CENTER)
    # Price
price_label=Label(window,  fg="black", font=("Times New Roman", 20, 'bold'), justify=CENTER)
    # Total
total_label=Label(window, fg="black", font=("Times New Roman", 20, 'bold'), justify=CENTER)

    
# A user has scanned there Card and is starting to shop
def welcome_user(ffname, ssname):
    main_label.config(text = 'Welcome %s %s' % (ffname, ssname), fg='black', font=("Times New Roman", 30))
    start_label.config(text = 'You\'re good to go, start scanning products')
    main_label.update()
    start_label.update()

# User wants additional information to be displayed about the item
def product_info():
    info_label=Label(window, text='Product info comming soon', fg="black",
                  font=("Times New Roman", 20, 'bold'), justify=CENTER)
    info_label.grid(row=5, sticky = W + E)
    print 'Product info comming soon'



##def Waiting_for_user():
##    main_label.config(text="Welcome to Woolworths", fg="green", font=("Times New Roman", 30, 'bold'), justify=CENTER)
##    start_label.config(text="Please scan your card to borrow a trolley", fg="black", font=("Times New Roman", 15), justify=CENTER)
##    main_label.update()
##    start_label.update()

# User confirms order and pays



def Check_out(Products, Prices, Total):
    product_label.forget()
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
 

def finished_pay_button():
    pressed = True    


def finish_pay():
    print"Thanks for shopping"
    finished=1
    CardID = 0
    Userdata = []
    ProductID = 0
    x = 2

    total_label.destroy()

    window.update()

    main_label.config(text="Welcome to Woolworths", fg="green", font=("Times New Roman", 30, 'bold'), justify=CENTER)
    start_label.config(text="Please scan your card to borrow a trolley", fg="black", font=("Times New Roman", 15), justify=CENTER)
    main_label.update()
    start_label.update()
    return x, finished, CardID, Userdata, ProductID
            

