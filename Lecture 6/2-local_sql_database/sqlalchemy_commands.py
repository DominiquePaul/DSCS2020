
# 4. Initialise our database using `db.create_all()`.
#
# we import the database object itself
from main import db
# but we can also import the respective classes for each table
from main import User, Products

import pandas as pd

###############################################################################
# Most important commands
###############################################################################

# Creates the database or reads from an existing file at the path specified
# you just need to do this once. Ideally do so in another script than your
# flask app, so that it doesnt execute every time the app is loaded. In
# practice you will often have a "start-up" script for your database that
# initiates it and populates it with some first bits of data
db.create_all()

# Lets view all items in our User table
User.query.all()


a = Products.query.first()

dir(a.vendor)
a.vendor
a["vendor"]["email"]
a["price"]

# Its still empty, so lets add two new users
user1 = User(name="Dominique Paul",
             email="dominique.paul@unisg.ch",
             password="password")

user2 = User(name="test user",
             email="test@unisg.ch",
             password="test_password")


# Notice that the formatting printed out here is the one we created ourself in
# the __repr__ function
user1

# this places new objects in the session (but doesn't write them to the
# database yet)
db.session.add(user1)
db.session.add(user2)


# Now we write the objects to the actual database (in this case our file)
# notice how the objects now have an id assigned
db.session.commit()

# Lets also add some products
product1 = Products(name="Parke blazer",
                    description="""It doesn't get more classic than this
                    versatile layering piece. Not too big, not too small and
                    structured enough to wear over anything, anytime.""",
                    price=179.95,
                    user_id=1)
product2 = Products(name="Merino wool sweater",
                    description="""We blended soft, naturally breathable merino
                     wool with hardy nylon for sweaters that are as soft and
                     comfortable as they are durable.""",
                    price=89.95,
                    user_id=1)
product3 = Products(name="Veja V-10 LEATHER WHITE",
                    description="""The V-10 model made out of ecological and
                    sustainable materials stands for 10 years of love.""",
                    price=159.95,
                    user_id=2)

# we could also do this instead of adding the items one by one using the
# command db.session.add(product1)
db.session.add_all([product1, product2, product3])
db.session.commit()


###############################################################################
# Different methods for querying our database
###############################################################################

# The most general method to get the contents of a database
all_products = Products.query.all()


# Get the user with the ID "1"
my_product = Products.query.get(1)
my_product

my_product = Products.query.get(2)
my_product

# Get the first item
my_product = Products.query.first()
my_product

# apply a filter
my_product = Products.query.filter_by(name="Merino wool sweater").first()
my_product.description

# we can also count the results
Products.query.filter_by(name="Merino wool sweater").count()

if 1:
    print("Works")

# when we retrieve and store an object, then we can also access it attributes
# like this
my_user = User.query.first()
my_user.id
my_user.name
# we can also access all the items that we specified in the foreign relationship
# products isn't an actual column in the user table, but it allows us to access
# the associated objec
my_user.products

# we can do the same for the product
my_product.id
my_product.description
my_product.name
# we can also access the vendor information. This is what the "backref"
# attribute does in the db.relationship line of the user class
my_product.user_id
my_product.vendor


# We can also read files directly as pandas dataframes. For this we change the
# structure a bit to take advantage of a function that is already built into
# pandas.
# The statement (first argument) is just an sql query (you don't have to
# understand this yet)
print(Products.query.statement)

# The second argument just gives pandas the information to connect to the
# database itself

# Get the entire table as a dataframe:
df = pd.read_sql(Products.query.statement, db.session.bind)

# this also works with the filter method
df = pd.read_sql(Products.query.filter_by(name="Merino wool sweater").statement, db.session.bind)


# If you want to delete ALL tables and start from scratch you can run this:
# db.drop_all()


###############################################################################
# Errors and rollbacks
###############################################################################


# __Nullable__
# This doesn't work because we didnt specify a password although in our
# definition of the class we said that it has to have a value (nullable
# argument)
user3 = User(name="Johannes Binswanger", email="johannes.binswanger@unisg.ch")
db.session.add(user3)
db.session.commit()

# this now also throws an error
User.query.all()

# If an error happens, then we have to reset the current interaction session
# with the database. This resets to the last commit to the database
db.session.rollback()


# __More comments on rollbacks__
# Rolling back a session means that other changes that were added but not
# committed are also undone

User.query.all()

user4 = User(name="Richard Feynman",
             email="richard@feynman.com",
             password="mypassword")
db.session.add(user4)
# no commit

user3 = User(name="Johannes Binswanger", email="johannes.binswanger@unisg.ch")
db.session.add(user3)


db.session.commit()
db.session.rollback()

# Notice how user4 is not in the database
User.query.all()


# __unique__
# This doesn't work because the email already exists
user4 = User(name="Dominique Paul 2",
             email="dominique.paul@unisg.ch",
             password="mypassword2")
db.session.add(user4)
db.session.commit()
