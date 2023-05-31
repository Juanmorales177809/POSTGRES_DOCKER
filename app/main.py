from typing import Union
from fastapi import FastAPI
from sqlalchemy import create_engine
import pandas as pd


engine = create_engine('postgresql://admin:abcd1234@172.16.20.101:5432/admin')

query = 'SELECT * FROM "Port1" LIMIT 50'
query1 = 'SELECT MAX("Ang") FROM "Port1"'


engine.dispose()
# Creación de una aplicación FastAPI:
app = FastAPI()

@app.get('/')
def read_root():
    return {'Prueba': 'Puerto!!!'}


@app.get('/max')
def max():
   df = pd.read_sql(query1, con=engine)
   json_data = df.to_json(orient='records')
   return json_data

@app.get('/port')
def data():
    query1 = 'SELECT * FROM "Port1" LIMIT 50'
    df = pd.read_sql(query1, con=engine)
    json_data = df.to_json(orient='records')
    return json_data

