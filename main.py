import pandas as pd
from matplotlib import pyplot as plt
from config.connection_db import ConnectionDB
from config.alchemy_connection import AlchemyConnection
from classes.sql_data import data_sql

user = "root"
password = ""
host = "localhost"

result_dataFrame = None

try:
    mydb = ConnectionDB(user, host, password)

    mydb.createDB("companydata")

    mydb.connectDB("companydata")

    mydb.execute_query(
'''
CREATE TABLE IF NOT EXISTS employeeperformance (
    id INT AUTO_INCREMENT PRIMARY KEY,
    employee_id INT NOT NULL,
    department VARCHAR(255) NOT NULL,
    performance_score DECIMAL(10, 2) NOT NULL,
    years_with_company INT NOT NULL,
    salary DECIMAL(10, 2) NOT NULL
);
'''
    )

    alchemy_connect = AlchemyConnection(user, host, password)

    bd_data = alchemy_connect.get_employees_pd()

    result_dataFrame = data_sql(bd_data)

    if (len(result_dataFrame.data) == 0):
        data = pd.read_csv("data.csv")

        data.to_sql('employeeperformance', con=alchemy_connect.engine, if_exists='append', index=False)

        bd_data = alchemy_connect.get_employees_pd()

        result_dataFrame = data_sql(bd_data)
except Exception as e:
    print(str(e))

print(result_dataFrame.total_employees_per_department())