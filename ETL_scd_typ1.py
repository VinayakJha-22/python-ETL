import os
from google.cloud import bigquery

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = './Credential/secret_key.json'
client = bigquery.Client()
TABLE_NAME = input("Enter Table Name: ")

query1 = """
    DELETE FROM `cymbal-store-dev.PY_ETL."""+TABLE_NAME+"""_SCD1` WHERE SNo IN (SELECT SNo FROM `cymbal-store-dev.PY_ETL."""+TABLE_NAME+"""` WHERE LOAD_DT = current_date);
"""
results = client.query(query1)
for row in results:
    print(row)

query2 = """
    INSERT INTO `cymbal-store-dev.PY_ETL."""+TABLE_NAME+"""_SCD1` SELECT * FROM `cymbal-store-dev.PY_ETL."""+TABLE_NAME+"""` WHERE LOAD_DT = current_date;
"""
results = client.query(query2)

for row in results:
    print(row)
