import os
import logging
import mysql.connector


class DBConnection():

    def __init__(self,user,passwd):
        self.conn = None
        self.get_connection(user,passwd)
        self.__initialize__()

    def get_connection(self,user,passwd,new=False):
        """Creates return new Singleton database connection"""
        if new or not self.conn:
            self.conn = self.__create_connection__(user,passwd)
        return self.conn

    def __initialize__(self):
        curr = conn.cursor()
        curr.execute("CREATE DATABASE Split_Tip")
        curr.execute("CREATE DATABASE BMI")


    # Function to establish a database connection
    def __create_connection__(self,user='user',passwd='password'):
        try:
            self.conn = mysql.connector.connect(
                host="localhost",
                user=user,
                passwd=passwd,
            )
            return self.conn
        except Error as e:
            logging.error(e)

        return None

    # # Returns a Class object based on the specified name from the database
    # def select_class_by_name(self,name):
    #     cur = self.conn.cursor()
    #     cur.execute("SELECT * FROM CLASSES where Name = '"+name+"';")

    #     results = []
    #     rows = cur.fetchall()
    #     logging.debug(rows[0])
    #     for i,row in enumerate(rows):
    #         growthRates = [(rows[i][4],rows[i][5],rows[i][6]),(rows[i][7],rows[i][8],rows[i][9]),(rows[i][10],rows[i][11],rows[i][12]),(rows[i][13],rows[i][14],rows[i][15]),(rows[i][16],rows[i][17],rows[i][18]),(rows[i][19],rows[i][20],rows[i][21])]
    #         unitClass = UNIT_CLASS.UnitClass(name=rows[i][0],desc=rows[i][1],maxLevel=rows[i][2],movement=rows[i][3],growthRates=growthRates)

    #     return unitClass
