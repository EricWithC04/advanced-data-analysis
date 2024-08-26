import pandas as pd
from matplotlib import pyplot as plt

class data_sql():

    def __init__(self, data: pd.DataFrame):
        self.data: pd.DataFrame = data

    def total_employees_per_department (self):
        employees_by_department = self.data.groupby(by="department").count()["employee_id"]

        return employees_by_department

    def mean_median_std_performance_score (self):
        groupby_department = self.data.groupby(by="department")

        ps_mean = groupby_department.mean()["performance_score"]
        ps_median = groupby_department.median()["performance_score"]
        ps_std = groupby_department.std()["performance_score"]

        return {
            "mean": ps_mean, # Media
            "median": ps_median, # Mediana
            "std": ps_std, # Desviación Estandar
        }
    
    def mean_median_std_salary (self):
        groupby_department = self.data.groupby(by="department")

        s_mean = groupby_department.mean()["salary"]
        s_median = groupby_department.median()["salary"]
        s_std = groupby_department.std()["salary"]

        return {
            "mean": s_mean, # Media
            "median": s_median, # Mediana
            "std": s_std, # Desviación Estandar
        }
    
    def correlation_year_performance(self):
        correlation = pd.DataFrame()

        correlation["department"] = self.data["department"]
        correlation["years_with_company"] = self.data["years_with_company"]
        correlation["performance_score"] = self.data["performance_score"]

        return correlation.groupby(by="department").corr()["years_with_company"].unstack()["performance_score"]
    
    def correlation_salary_performance(self):
        correlation = pd.DataFrame()

        correlation["department"] = self.data["department"]
        correlation["salary"] = self.data["salary"]
        correlation["performance_score"] = self.data["performance_score"]

        return correlation.groupby(by="department").corr()["salary"].unstack()["performance_score"]
    
    def hist_performance_per_department (self):
        department_performance = self.data.groupby(by="department").mean()

        plt.bar(department_performance.index, department_performance["performance_score"])

        plt.xticks(rotation=45, ha='right')

        plt.show()

    def scatter_years_performance(self):
        plt.scatter(self.data["years_with_company"], self.data["performance_score"])
        plt.xlabel("Años en la compañia")
        plt.ylabel("Rendimiento")
        plt.show()

    def scatter_salary_performance(self):
        plt.scatter(self.data["performance_score"], self.data["salary"])
        plt.xlabel("Rendimiento")
        plt.ylabel("Salario")
        plt.show()