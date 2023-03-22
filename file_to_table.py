import os
from datetime import date
from google.cloud import bigquery

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = './Credential/secret_key.json'
client = bigquery.Client()
table_id = 'cymbal-store-dev.PY_ETL.FILE_PR_T'
job_config = bigquery.LoadJobConfig(
    autodetect=True, source_format=bigquery.SourceFormat.CSV
)
source_file_name = 'demo.csv'
uri = 'gs://py_etl_file_tsfr/'+'dir/'+date.today().strftime("%Y")+'/' + \
    date.today().strftime("%Y%m")+"/"+date.today().strftime("%Y%m%d") + \
    "/"+source_file_name
load_job = client.load_table_from_uri(
    uri, table_id, job_config=job_config
)
load_job.result()
destination_table = client.get_table(table_id)
print("Loaded {} rows.".format(destination_table.num_rows))
