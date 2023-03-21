import os
from google.cloud import bigquery

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = './Credential/secret_key.json'
client = bigquery.Client()

query = """
    select current_datetime;
"""
results = client.query(query)

for row in results:
    print(row)
