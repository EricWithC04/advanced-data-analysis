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

def mean_median_std_performance_score ():
    groupby_department = result_dataFrame.groupby(by="department")

    ps_mean = groupby_department.mean()["performance_score"]
    ps_median = groupby_department.median()["performance_score"]
    ps_std = groupby_department.std()["performance_score"]

    return {
        "mean": ps_mean, # Media
        "median": ps_median, # Mediana
        "std": ps_std, # Desviación Estandar
    }