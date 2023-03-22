import os
from google.cloud import storage
from datetime import date

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = './Credential/secret_key.json'
bucket_name = 'py_etl_file_tsfr'
source_file_name = 'demo.csv'
destination_blob_name = 'dir/'+date.today().strftime("%Y")+'/' + \
    date.today().strftime("%Y%m")+"/"+date.today().strftime("%Y%m%d")+"/"+source_file_name


def list_blobs(bucket_name):
    storage_client = storage.Client()
    blobs = storage_client.list_blobs(bucket_name)
    for blob in blobs:
        print(blob.name)


def upload_blob(bucket_name, source_file_name, destination_blob_name):

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    if(list_blobs(bucket_name) == destination_blob_name):
        generation_match_precondition = 0
        blob.upload_from_filename(
            source_file_name, if_generation_match=generation_match_precondition)
        print(
            f"File {source_file_name} uploaded to {destination_blob_name}."
        )
    else:
        print("File Already Exists !")


upload_blob(bucket_name, source_file_name, destination_blob_name)
