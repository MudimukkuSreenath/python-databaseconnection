import mysql.connector
mydb=mysql.connector.connect('sreenath@localhost')
mycusor=mydb.cursor()
mycursor.execute("show databases")
