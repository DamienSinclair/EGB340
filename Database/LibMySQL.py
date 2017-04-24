# Written by Damien Sinclair

import MySQLdb

# AWS Server Settings
ip = "34.209.19.53"
user = "root"
password = "Peanut"
database = "EGB340_AWS"


# Creating Commands


def addUser(userID, firstname, lastname):
        #Add a user to the database

        #Open Database Connection
        db = MySQLdb.connect(ip,user,password,database)
        # prepare a cursor object using cursor() method
        cursor = db.cursor()
        #Create New User
        cursor.execute("INSERT INTO userData (userID, firstname, lastname) VALUES(%s, %s, %s, %s, %s);",( userID, firstname, lastname))
        # disconnect from server
        db.close()

def queryCardID(userID):
        #Queries Database and returns fname, lname, credit and bottles
        #Must interpriate data using 'data[0]'
        
        #Open Database Connection
        db = MySQLdb.connect(ip,user,password,database)
        # prepare a cursor object using cursor() method
        cursor = db.cursor()
        #Quesy Database
        cursor.execute("SELECT firstname, lastname FROM %s WHERE cardid = %s;",(EGB340_AWS, userID))
        #Save Data
        data = cursor.fetchone()
        # disconnect from server
        db.close()
        return data