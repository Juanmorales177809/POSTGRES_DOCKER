from sqlalchemy import create_engine
import pandas as pd


engine = create_engine('postgresql://admin:abcd1234@172.16.20.101:5432/admin')

query = 'SELECT * FROM "Port1" LIMIT 50'


df = pd.read_sql(query, con=engine)
print(df)
print("done")

engine.dispose()

