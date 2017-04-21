import MySQLdb


#Set Server Settings
ip = "58.162.145.26"
user = "root"
password = "M2M"
database = "userData"


def addUser(cardid, firstname, lastname, credit, bottles):
        #Add a user to the database

        #Open Database Connection
        db = MySQLdb.connect(ip,user,password,database)
        # prepare a cursor object using cursor() method
        cursor = db.cursor()
        #Create New User
        cursor.execute("INSERT INTO userData (cardid, firstname, lastname, credit, bottles) VALUES(%s, %s, %s, %s, %s);",( cardid, firstname, lastname, credit, bottles))
        # disconnect from server
        db.close()

def queryCardID(cardid):
        #Queries Database and returns fname, lname, credit and bottles
        #Must interpriate data using 'data[0]'
        
        #Open Database Connection
        db = MySQLdb.connect(ip,user,password,database)
        # prepare a cursor object using cursor() method
        cursor = db.cursor()
        #Quesy Database
        cursor.execute("SELECT firstname, lastname, credit, bottles FROM %s WHERE cardid = %s;",(database, cardid))
        #Save Data
        data = cursor.fetchone()
        # disconnect from server
        db.close()
        return data

def updateData(cardid, credit, bottles):
        #Update the credit and bottles values

        #Open Database Connection
        db = MySQLdb.connect(ip,user,password,database)
        # prepare a cursor object using cursor() method
        cursor = db.cursor()
        #Quesy Database
        cursor.execute("UPDATE %s SET credit = %s, bottles = %s WHERE cardid = %s",(database,credit, bottles, cardid))
        #Save Data
        data = cursor.fetchone()
        # disconnect from server
        db.close()
        
def resetDatabase():
	#Update the credit and bottles values

        #Open Database Connection
        db = MySQLdb.connect(ip,user,password,database)
        # prepare a cursor object using cursor() method
        cursor = db.cursor()
        #Quesy Database
        cursor.execute("DROP TABLE userData")
        #Save Data
        data = cursor.fetchone()
        # disconnect from server
        db.close()

