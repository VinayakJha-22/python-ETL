import os
from google.cloud import bigquery

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = './Credential/secret_key.json'
client = bigquery.Client()
#TABLE_NAME = input("Enter Table Name")

query = """
    CREATE TABLE `cymbal-store-dev.PY_ETL.FILE_PR_T_SCD1`
     (SNo INT64,
     Name STRING,
     Gender STRING,
     Age INT64,
     LOAD_DT date DEFAULT current_date
     ) 
     PARTITION BY LOAD_DT;
"""
results = client.query(query)

for row in results:
    print(row)
