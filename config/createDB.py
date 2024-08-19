import mysql.connector as connection

class ConnectionDB:
    def __init__(self, user, host, passwd):
        self.user = user
        self.host = host
        self.passwd = passwd
        self.db = self.connect()
        self.cursor = self.db.cursor()
        self.createDB("companydata")
    
    def connect(self):
        mydb = connection.connect(
            host = self.host,
            user = self.user, 
            passwd = self.passwd
        )
        return mydb
    
    def createDB(self, name):
        self.cursor.execute(f"CREATE DATABASE IF NOT EXISTS {name};")
    
    def connectDB(self, name):
        self.cursor.execute(f"USE {name};")

    def executeQuery(self, query):
        self.cursor.execute(query)
    
    def close(self):
        self.db.close()
    
mydb = ConnectionDB("root", "localhost", "")