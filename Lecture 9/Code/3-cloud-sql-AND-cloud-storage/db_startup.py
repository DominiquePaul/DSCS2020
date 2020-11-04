from main import db, GC_BUCKET_NAME
from google.cloud import storage

db.create_all()

# create bucket
storage_client = storage.Client()
storage_client.create_bucket(GC_BUCKET_NAME)


# as completely deleting your database - which is an extreme way of resolving
# an error anyways - is no longer an option, you can instead resort to the
# drop_all() command if necessary
#
# db.drop_all()


# Delete bucket: Run this code to delete bucket from cloud storage. Note that
# while bucket is deleted, the files are not yet fully erased yet. Google holds
# on to the files in a bin and only deletes them after ~30 days. Images are not
# automatically overwritten and public urls will remain accessible until the
# files are fully deleted
#
# storage_client = storage.Client()
# bucket = storage_client.bucket(GC_BUCKET_NAME)
# bucket.delete(force=True)
