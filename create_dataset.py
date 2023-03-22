import os
from google.cloud import bigquery


os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = './Credential/secret_key.json'
dataset_id = 'cymbal-store-dev.PY_ETL'
client = bigquery.Client()
dataset = bigquery.Dataset(dataset_id)
dataset.location = "US"
dataset = client.create_dataset(dataset, timeout=30)  # Make an API request.
print("Created dataset {}.{}".format(client.project, dataset.dataset_id))
