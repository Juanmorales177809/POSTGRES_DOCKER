import pandas as pd
import numpy as np

import psycopg2
from sqlalchemy import create_engine





def readData(text): #Read any cst Data
    df = pd.read_csv(text, sep = ';', decimal=",")
    df.columns=["Ang", "dBm"]
    return df


data = readData('https://firebasestorage.googleapis.com/v0/b/curso-pandas.appspot.com/o/port1_new.csv?alt=media&token=c0ac8ef3-88ea-438e-9231-68c45e6f3cd4')
engine = create_engine('postgresql://admin:abcd1234@172.16.20.101:5432/')
data.to_sql('tabla_ejemplo',engine, if_exists ='replace')
engine.dispose()

# def queryPerClass(clase, engine):
#         query = """
#         SELECT *
#         FROM "Port1"
#         WHERE "Class" = %(clase)s
#         """
#         queryParameters = {'clase': clase}
#         dataQuery = pd.read_sql_query(query, con = engine, params = queryParameters)
#         return(dataQuery)





# if __name__ == '__main__':
    
#     sql = """"
#         SELECT * FROM table;
#         """
#     with engine.connect().execution_options(autocommit=True) as conn:
#          query = conn.execute(text(sql))
#     df = pd.DataFrame(query.fetchall())
    
    





