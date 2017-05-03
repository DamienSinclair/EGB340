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

def addProduct(ProductID, ProductName, ProductPrice):
        #Add a product to the database

        #Open Database Connection
        db = MySQLdb.connect(ip,user,password,database)
        # prepare a cursor object using cursor() method
        cursor = db.cursor()
        #Create New Product
        cursor.execute("INSERT INTO Products (ProductCode, ProductName, ProductPrice) VALUES (%s, %s, %s);",(ProductID, ProductName, ProductPrice))
        # Commit changes???
        db.commit()
        # disconnect from server
        
        db.close()
        print "added"

def queryCardID(userID):
        #Queries Database and returns fname, lname, credit and bottles
        #Must interpriate data using 'data[0]'

        #Open Database Connection
        db = MySQLdb.connect(ip,user,password,database)
        # prepare a cursor object using cursor() method
        cursor = db.cursor()
        #Quesy Database
        cursor.execute("SELECT firstname, lastname FROM Users WHERE cardid = %s;",(userID))
        #Save Data
        data = cursor.fetchone()
        # disconnect from server
        db.close()
        return data

def queryProductID(productID):
        #Queries Database and returns
        #Must interpriate data using 'data[0]'

        #Open Database Connection
        db = MySQLdb.connect(ip,user,password,database)
        # prepare a cursor object using cursor() method
        cursor = db.cursor()
        #Quesy Database
        cursor.execute("SELECT ProductName, ProductPrice FROM Products WHERE ProductCode = %s;",(productID))
        #Save Data
        gdata = cursor.fetchone()
        # disconnect from server
        db.close()
        return gdata

## Cost Calculator:

#from re import findall
#def totalCost(items):
 #       #Open Database Connection
  #      db = MySQLdb.connect(ip,user,password,database)
   #     data1=[]
    #    data2=[]
     #   cost = 0
      #  cursor = db.cursor()
       # for item in items:
        #        cursor.execute("SELECT ProductPrice FROM Products WHERE ProductCode = %s;", (item))
         #       data1 = [cursor.fetchone()]
          #      data2 = data2 + findall('\(\'(.+)\',\)', str(data1))
     #   cost = sum(float(i) for i in data2)
      #  return cost
       # db.close()

#lists = ['def1f6b5','def1f6b5']
#print totalCost(lists)
