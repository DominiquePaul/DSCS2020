"""
Make sure you have google the cloud storage package installed:

    pip install google-cloud-storage

________________________

Functions covered here:

    * list_buckets - List buckets in your project
    * create_bucket - Create a new bucket
    * upload_file - Upload a new file to a bucket
    * list_blobs - List all files in a bucket
    * download_file - Download a file from the bucket
________________________

Documentation for google cloud storage:
https://cloud.google.com/storage/docs
https://googleapis.dev/python/storage/latest/buckets.html
"""

import os
import io

from PIL import Image
from google.cloud import storage

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "../gcp_credentials/dscs2020-b20a630b58a2.json"

###############################################################################
# Introduction
###############################################################################

storage_client = storage.Client()

# get all buckets in your project
buckets = storage_client.list_buckets()
bucket_names = [bucket.name for bucket in buckets]
bucket_names


# create a bucket
bucket_name = "bucket1"
bucket = storage_client.create_bucket(bucket_name)  # doesn't work

# Bucket names have to be unique
bucket_name = "mynewbucket-dscs2"
bucket = storage_client.create_bucket(bucket_name)

dir(bucket)

bucket.time_created

bucket.location  # buckets are per default created in the US multiregion
bucket.location_type

# we can also create a bucket in a specific location
# have a look at locations here
# https://cloud.google.com/storage/docs/bucket-locations
bucket_name = "mynewbucket-dscs-europe2"
location = "EUROPE-WEST1"
bucket = storage_client.create_bucket(bucket_name, location=location)

bucket.location
bucket.location_type


# get a single bucket by its name the bucket by name
bucket_name = "mynewbucket-dscs-europe2"
bucket = storage_client.bucket(bucket_name)


# upload a file

# first upload
destination_blob_name = "myfile.txt"
source_file_name = "../example_files/example.txt"

# this creates the blob object in python but does not upload anything
blob = bucket.blob(destination_blob_name)
# upload the file
blob.upload_from_filename(source_file_name)

# second upload
destination_blob_name = "subfolder/campus.jpg"
source_file_name = "../example_files/campus.jpg"

# this creates the blob object in python but does not upload anything
blob = bucket.blob(destination_blob_name)
# upload the file
blob.upload_from_filename(source_file_name)



# show all files in a bucket
bucket_name = "mynewbucket-dscs-europe2"
blobs = storage_client.list_blobs(bucket_name)
file_names = [blob.name for blob in blobs]
file_names

# get a file from a bucket
blob_name = "subfolder/campus.jpg"
blob = bucket.blob(blob_name)

dir(blob)

# lets have a look at the file in our browser
blob.public_url

# lets make it public
blob.make_public()

# and turn it into a private file again
blob.make_private()

# download the file
blob.download_to_filename("../example_files/downloads/st_gallen.jpg")


# We can also load a file into memory without saving it to the disk first
myfile = blob.download_as_string()  # this loads the file as a bytes string

# We need to know what kind of file type it is to know which function to apply
# to the bytes string. In this case I knew it was an image file so I took the
# code from here:
# https://stackoverflow.com/questions/32908639/open-pil-image-from-byte-file
image = Image.open(io.BytesIO(myfile))
image


###############################################################################
# Overview of usage by function
###############################################################################

def list_buckets():

    storage_client = storage.Client()

    buckets = storage_client.list_buckets()

    bucket_names = [bucket.name for bucket in buckets]

    return bucket_names


def create_bucket(bucket_name, location="EUROPE-WEST1"):
    """
    Have a look at locations here
    https://cloud.google.com/storage/docs/bucket-locations
    """

    storage_client = storage.Client()

    # Creates the new bucket
    bucket = storage_client.create_bucket(bucket_name, location=location)

    print(f"Bucket {bucket_name} created in location {location}.")


def delete_bucket(bucket_name, force=False):
    """
    The bucket must be empty in order to submit a delete request. If
    force=True is passed, this will first attempt to delete all the
    objects / blobs in the bucket (i.e. try to empty the bucket).
    """

    storage_client = storage.Client()

    bucket = storage_client.bucket(bucket_name)

    bucket.delete(force=force)


def list_blobs(bucket_name):

    storage_client = storage.Client()

    blobs = storage_client.list_blobs(bucket_name)

    file_names = [blob.name for blob in blobs]

    return file_names


def upload_file(bucket_name, source_file_name, destination_blob_name):

    storage_client = storage.Client()

    # get the bucket by name
    bucket = storage_client.bucket(bucket_name)

    # this creates the blob object in python but does not upload anything
    blob = bucket.blob(destination_blob_name)

    # upload the file
    blob.upload_from_filename(source_file_name)


def download_file(bucket_name, source_blob_name, destination_file_name):

    storage_client = storage.Client()

    bucket = storage_client.bucket(bucket_name)

    blob = bucket.blob(source_blob_name)

    blob.download_to_filename(destination_file_name)


def delete_file(bucket_name, source_blob_name):

    storage_client = storage.Client()

    bucket = storage_client.bucket(bucket_name)

    blob = bucket.blob(source_blob_name)

    blob.delete()


###############################################################################
# Applying the functions
###############################################################################


list_buckets()

create_bucket(bucket_name="mybucket-dscs")

list_blobs(bucket_name="mybucket-dscs")

upload_file(bucket_name="mybucket-dscs",
            source_file_name="../example_files/example.txt",
            destination_blob_name="subfolder/example.txt")

upload_file(bucket_name="mybucket-dscs",
            source_file_name="../example_files/campus.jpg",
            destination_blob_name="campus.jpg")

download_file(bucket_name="mybucket-dscs",
              source_blob_name="campus.jpg",
              destination_file_name="../example_files/downloads/campus.jpg")


create_bucket(bucket_name="mybucket-dscs3")

delete_bucket(bucket_name="mybucket-dscs3")

# this does not work because the bucket is not empty
delete_bucket(bucket_name="mybucket-dscs")

# we can override this, but be careful as you might delete an important folder
# with a lot of files by accident
delete_bucket(bucket_name="mybucket-dscs", force=True)
