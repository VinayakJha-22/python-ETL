import os
from google.cloud import storage

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = './Credential/secret_key.json'

storage_client = storage.Client()
bucket_name = 'py_etl_file_tsfr'


def create_bucket_class_location(bucket_name):
    bucket = storage_client.bucket(bucket_name)
    bucket.storage_class = "NEARLINE"
    new_bucket = storage_client.create_bucket(bucket, location="us")
    print(
        "Created bucket {} in {} with storage class {}".format(
            new_bucket.name, new_bucket.location, new_bucket.storage_class
        )
    )
    return new_bucket


create_bucket_class_location(bucket_name)
