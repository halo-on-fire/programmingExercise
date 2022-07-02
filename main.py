from sqlite3 import connect
from unittest import result
from venv import create
import mysql.connector

employees = []


# Duplicate Check ------------------------------------------------------------------------------>
def checkIfDuplicates(listOfElems):
    for elem in listOfElems:
        if listOfElems.count(elem) > 1:
            return True 
    return False

# Creating database ------------------------------------------------------------------------------->
def create_database():
    try:
        connection = mysql.connector.connect(host = 'localhost', user = 'root', password = 'hossein')
        mysql_Create_Database = """CREATE DATABASE IF NOT EXISTS Company"""

        cursor = connection.cursor()
        result = cursor.execute(mysql_Create_Database)
        print("Company Database created successfully")

    except mysql.connector.Error as error:
        print("Faild to create Databse in Mysql : {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

create_database()

#CreateTable Function() ----------------------------------------------------------------------->
def createTable():
    try:
        connection = mysql.connector.connect(host = 'localhost', database = 'Company', user = 'root', password  = 'hossein')

        mysql_Create_Table = """CREATE TABLE IF NOT EXISTS employees(Id INT(2) NOT NULL,Name VARCHAR(10) NOT NULL,Weight INT(3) NOT NULL, Height INT(3) NOT NULL , PRIMARY KEY(Id))"""

        cursor = connection.cursor()
        result = cursor.execute(mysql_Create_Table)
        print("Employees table was created....")

    except mysql.connector.Error as error:
        print("Faild to create table in MySQL: {}".format(error))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL conection is closed")

createTable()

#InsertIntoTable ---------------------------------------------------------------------------------->
def insert_variables_into_table (id, name, weight, height):
    try: 
        connection = mysql.connector.connect(host = 'localhost', database = 'Company', user = 'root', password = 'hossein')

        cursor = connection.cursor()
        mysql_insert_query = """INSERT INTO Employees (id,name, weight, height) VALUES (%s, %s, %s, %s)"""

        record = (id, name, weight, height)
        cursor.execute(mysql_insert_query, record)
        connection.commit()
        print("Record inserted successfully into employees")

    except mysql.connector.Error as error:
        print("Faild to insert into MySQL table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")



#selectFromTable Function ----------------------------------------------------------------->
def SelectFromTable():
    try: 
        connection = mysql.connector.connect(host = 'localhost', database = 'Company', user = 'root', password = 'hossein')
        sql_select_query = 'SELECT * FROM Employees'
        cursor = connection.cursor()
        cursor.execute(sql_select_query)
        #get all records
        records = cursor.fetchall()
        print("Total number of rows in table:", cursor.rowcount)
        print(" \n Printing each row : ")

        
        for row in records:
            employee = []
            employee.append(row[0])
            employee.append(row[1])
            employee.append(row[2])
            employee.append(row[3])

            employees.append(employee)
        
        result = sorted(employees, key = lambda x:(-x[3], x[2]))

        for i in result:
            print("id: ",i[0], i[1], i[2], i[3])

    except mysql.connector.Error as e:
        print("Error readin data from MySQL table", e)
    finally:
        if connection.is_connected():
            connection.close()
            cursor.close()
            print("MySQL connection is closed")


SelectFromTable()