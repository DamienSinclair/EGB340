#EGB340 DATABASE Commands
import MySQLdb

#Set Server Settings for AWS Server
ip = "34.209.19.53"
user = "root"
password = "Peanut"
database = "EGB340"

# Creating Commands
def addUser(userID, firstname, lastname):
        #Add a user to the database

        #Open Database Connection
        db = MySQLdb.connect(ip,user,password,database)
        # prepare a cursor object using cursor() method
        cursor = db.cursor()
        #Create New User
        cursor.execute("INSERT INTO userData (userID, firstname, lastname) VALUES(%s, %s, %s);",(userID, firstname, lastname))
        # disconnect from server
        db.close()

def addProduct(productID, ProductName, ProductPrice):
        #Add a user to the database

        #Open Database Connection
        db = MySQLdb.connect(ip,user,password,database)
        # prepare a cursor object using cursor() method
        cursor = db.cursor()
        #Create New User
        cursor.execute("INSERT INTO `EGB340`.`Products` (`ProductCode`, `ProductName`, `ProductPrice`) VALUES (%s, %s, %s);",(productID, ProductName, ProductPrice))
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
        cursor.execute("SELECT firstname, lastname FROM %s WHERE cardid = %s;",(fname, lname))
        #Save Data
        data = cursor.fetchone()
        # disconnect from server
        db.close()
        return data

## Cost Calculator:

from re import findall
def totalCost(items):
        #Open Database Connection
        db = MySQLdb.connect(ip,user,password,database)
        data1=[]
        data2=[]
        cost = 0
        cursor = db.cursor()
        for item in items:
                cursor.execute("SELECT ProductPrice FROM Products WHERE ProductCode = %s;", (item))
                data1 = [cursor.fetchone()]
                data2 = data2 + findall('\(\'(.+)\',\)', str(data1))
        cost = sum(float(i) for i in data2)
        return cost
        db.close()

lists = ['def1f6b5','def1f6b5']
print totalCost(lists)
