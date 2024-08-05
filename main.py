import mysql.connector as connection
import pandas as pd
from matplotlib import pyplot as plt

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

def mean_median_std_salary ():
    groupby_department = result_dataFrame.groupby(by="department")

    s_mean = groupby_department.mean()["salary"]
    s_median = groupby_department.median()["salary"]
    s_std = groupby_department.std()["salary"]

    return {
        "mean": s_mean, # Media
        "median": s_median, # Mediana
        "std": s_std, # Desviación Estandar
    }

def correlation_year_performance():
    correlation = pd.DataFrame()

    correlation["department"] = result_dataFrame["department"]
    correlation["years_with_company"] = result_dataFrame["years_with_company"]
    correlation["performance_score"] = result_dataFrame["performance_score"]
    
    return correlation.groupby(by="department").corr()["years_with_company"].unstack()["performance_score"]

def correlation_salary_performance():
    correlation = pd.DataFrame()

    correlation["department"] = result_dataFrame["department"]
    correlation["salary"] = result_dataFrame["salary"]
    correlation["performance_score"] = result_dataFrame["performance_score"]
    
    return correlation.groupby(by="department").corr()["salary"].unstack()["performance_score"]

def hist_performance_per_department ():
    department_performance = result_dataFrame.groupby(by="department").mean()
    
    plt.bar(department_performance.index, department_performance["performance_score"])

    plt.xticks(rotation=45, ha='right')

    plt.show()

hist_performance_per_department()