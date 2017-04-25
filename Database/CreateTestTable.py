import MySQLdb


#Set Server Settings
ip = "34.209.19.53"
user = "root"
password = "Peanut"
database = "EGB340"

#Open Database Connection
db = MySQLdb.connect(ip,user,password,database)
# prepare a cursor object using cursor() method
cursor = db.cursor()
#Create New User
cursor.execute("CREATE TABLE `EGB340`.`Test` (`TestID` INT NOT NULL, `Test2` VARCHAR(45) NOT NULL, PRIMARY KEY (`TestID`))")
# disconnect from server
db.close()
print ("Created new Table")
