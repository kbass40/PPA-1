import os
import logging
import mysql.connector


class DBConnection():

    def __init__(self,user='user',passwd='password'):
        self.conn = None
        self.get_connection(user,passwd)
        self.__initialize__()

    def get_connection(self,user='user',passwd='password',new=False):
        """Creates return new Singleton database connection"""
        if new or not self.conn:
            self.conn = self.__create_connection__(user,passwd)
        return self.conn

    # Function to initialize the table schemas
    def __initialize__(self):
        curr = self.conn.cursor()
        curr.execute("CREATE TABLE IF NOT EXISTS db.EmailVerifier(time TIMESTAMP, emailInput VARCHAR(255), output VARCHAR(5), PRIMARY KEY (time, emailInput));")
        curr.execute("CREATE TABLE IF NOT EXISTS db.BMI(time TIMESTAMP, feet INT, inches INT, pounds FLOAT, output VARCHAR(100), PRIMARY KEY (time, feet, inches, pounds));")


    # Function to establish a database connection
    def __create_connection__(self,user='user',passwd='password'):
        try:
            self.conn = mysql.connector.connect(
                host="localhost",
                user=user,
                passwd=passwd,
                db="db"
            )
            return self.conn
        except Error as e:
            logging.error(e)

        return None

    def print_db(self):
        curr = self.conn.cursor(buffered=True)
        curr.execute("SHOW TABLES")

        tables = []
        for tup in curr:
            tables.append(tup)

        for x in tables:
            print("For Table: "+str(x[0]))
            query = "SELECT * FROM "+str(x[0])+";"
            curr.execute(query)
            for data in curr:
                print(data)

    def insert_into_Email_Verifier(self, timestamp, email, output):
        curr = self.conn.cursor()
        curr.execute("INSERT INTO EmailVerifier (time, emailInput, output) VALUES (%s, %s, %s)", (timestamp, email, output))
        self.conn.commit()
        print("Executed successfully")

    def insert_into_BMI(self, timestamp, feet, inches, pounds, output):
        curr = self.conn.cursor()
        curr.execute("INSERT INTO BMI (time, feet, inches, pounds, output) VALUES (%s, %s, %s, %s, %s)", (timestamp, feet, inches, pounds, output))
        self.conn.commit()
        print("Executed successfully")


def readBMI():
        db = DBConnection()
        conn =  db.get_connection()

        curr = conn.cursor()
        curr.execute("SELECT * FROM BMI")

        json = {}

        for i,tup in enumerate(curr):
            call = {
                "Timestamp" : str(tup[0]),
                "Feet" : str(tup[1]),
                "Inches" : str(tup[2]),
                "Pounds" : str(tup[3]),
                "Classification" : str(tup[4])
            }
            json[i+1] = call

        return json

def readEmailVerifier():
    db = DBConnection()
    conn =  db.get_connection()

    curr = conn.cursor()
    curr.execute("SELECT * FROM EmailVerifier")

    json = {}

    for i,tup in enumerate(curr):
        call = {
            "Timestamp" : str(tup[0]),
            "Input Email" : str(tup[1]),
            "Valid" : str(tup[2]),
        }
        json[i+1] = call

    return json 

