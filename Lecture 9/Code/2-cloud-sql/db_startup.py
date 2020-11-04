
from main import db

# as completely deleting your database - which is an extreme way of resolving
# an error anyways - is no longer an option, you can instead resort to the
# drop_all() command if necessary
#
# db.drop_all()

db.create_all()
