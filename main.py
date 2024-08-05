import mysql.connector as connection
import pandas as pd

try:
    mydb = connection.connect(
        host = "localhost", 
        database = 'companydata',
        user="root", 
        passwd="")

    query = "SELECT * FROM employeeperformance;"
    result_dataFrame = pd.read_sql(query, mydb)

    mydb.close() #close the connection
except Exception as e:
    mydb.close()
    print(str(e))

def total_employees_per_department ():
    employees_by_department = result_dataFrame.groupby(by="department").count()["employee_id"]

    return employees_by_department