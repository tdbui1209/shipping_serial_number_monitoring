import cx_Oracle
import pandas as pd


class OracleDataframeQuery:
    '''
    This class is used to connect to Oracle database and query the data into a pandas dataframe.
    '''
    def __init__(self, username, password, dsn):
        self.username = username
        self.password = password
        self.dsn = dsn

    def query(self, query):
        conn = cx_Oracle.connect(self.username, self.password, self.dsn)
        cursor = conn.cursor()
        cursor.execute(query)

        rows = cursor.fetchall()
        descs = cursor.description

        df = pd.DataFrame(rows, columns=[d[0] for d in descs])
        cursor.close()
        conn.close()
        return df
