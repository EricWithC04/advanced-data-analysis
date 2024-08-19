from sqlalchemy import create_engine
import pandas as pd

class AlchemyConnection:
    def __init__(self, user, host, passwd):
        self.user = user
        self.host = host
        self.passwd = passwd
        self.engine = create_engine(f'mysql+mysqlconnector://{self.user}:{self.passwd}@{self.host}/companydata')

    def get_employees_pd(self):
        df = pd.read_sql("SELECT * FROM employeeperformance;", con=self.engine)
        return df