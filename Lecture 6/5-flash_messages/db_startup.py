"""
We are working in a new folder with a new db, so we have to initialise our
database

Remember to drop all tables and rerun this command if you make a change to the
structure of your database in the code.
"""

from main import db

db.create_all()
