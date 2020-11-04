# Lecture 9

## Content

1. Setting up a SQL Database in GCP
    1. Creating the SQL instance
    1. Connecting with Python and SQL Alchemy
1. BigQuery
1. SQL query language
    1. Basic queries
    1. Where statements
    1. Joins
    1. Exercise: running SQL like queries on BigQuery
1. DataStudio
    1. Intro to DataStudio
    1. Exercise: Connecting SQL and BigQuery
1. Cloud Storage
    1. Overview
    1. Adding files via gcloud command line
    1. Adding files with python
    1. Saving file paths in SQL
1. Some comments about the projects

## Extra content to cover if we have time
1. Qwiklabs
1. Cron Jobs
1. Running a Jupyter notebook on a GCP Server



## Working with google storage

### Overview

Google Cloud Storage is a online file storage system for storing data on GCP. Files are stored as so-called binary large objects (BLOBs) which can store any type of data and are especially suitable for large chunks of data and files like images, audio, media or other files.

While we could store images and videos in sql databases, it's better to as blob files rather than in a DB. This minimises the CPU usage and the number of input/output operations uploading/downloading images and videos and playing videos.

### Prerequisites

Install google cloud storage:

  `pip install google-cloud-storage`

Make sure you have credentials for your GCP project as a json file (see lecture 8 notes) and set the environment variable `GOOGLE_APPLICATION_CREDENTIALS`

### Usage

See the file `Code/1-gcs.py`

Read more in the documentation:
* https://cloud.google.com/storage/docs/
* https://googleapis.dev/python/storage/latest/buckets.html



## Cloud SQL - Running a SQL database on GCP

### Overview

We can choose between three types of SQL databases (1) MySQL (2) PostgreSQL and (3) SQL Server. The differences between these are minuscule and mostly relate to syntax or names of functions that do the same thing. We will use PostgreSQL as its general syntax which means that you can easily translate your skills to other database management systems. It is also very close to SQLite

### Creating a SQL database

1. Open the hamburger menu and select "SQL" from the databases group
1. Choose PostgreSQL
1. Set a name, a long and safe password, the latest version (currently this is PostrgreSQL 12) and set the region to be in Europe
1. Select "more options" and set the following
    * Cores: 2 cores with 3.75 gb in memory
    * Storage capacity: 10gb
    * Under Connectivity, click add network and enter your IP address followed by /32, e.g. 194.230.145.194/32. You can use google to get your IP address.
1. Click create, the creation of the sql instance can take a few minutes. Once its ready continue with the next steps
1. Go to "databases" on the right and create a new database, e.g. flaskapp_database

### Connecting to your SQL database with Flask

The only change we have to make is changing the connection string `SQLALCHEMY_DATABASE_URI` to point to our new cloud sql database. For this you will need (1) the public ip address, (2) the database name and (3) the password. Keep these in a secrets.py file (that is mentioned in the gitignore file) and import them to your app.

Also notice the following minor differences:

1. For encrypted password columns in the table definition, we use the column type db.Binary instead of db.String. See comment in `2-cloud-sql/main`
1. Some of you have relied on deleting your SQLite database during development when something went wrong, instead you should now use the command `db.drop_all()`. See `2-cloud-sql/db_startup.py`.


### Further Reading
* [SQL Server, PostgreSQL, MySQL... what's the difference? Where do I start? (Datacamp)](https://www.datacamp.com/community/blog/sql-differences)


## Working with Cloud SQL and Cloud Storage

So far, when we worked with images, we stored these in our application folder itself. This is not an ideal approach as we don't want to store any permanent data of the app on the server where the app is running. We separated the tabular data by using a SQL database, but as mentioned above, we should not be using it to store images, videos or other media. Instead, the best approach is to store this kind of data to cloud storage and store the link to the file in the SQL database. We will look at an implementation of this in `Code/3-cloud-sql-AND-cloud-storage`.

Note that you should create a separate database in your SQL server that is being referenced by the application. This is because we will be adding additional rows to our posts table and this will not be compatible anymore with the code in `2-cloud-sql/db_startup.py`. So remember to also adjust the secrets.py file to include the name of the second database.

Some important changes to note:

* We are adding our gcp credential key to the folder. The file is hidden from Github via .gitignore so remember to add your own key and change the link to it in `main.py`
* We adjust our PostForm in `forms.py` to include a file upload field, we also have to amend the `upload.html` to include the field
* We alter our Products table to contain the columns "img_public_url" and "img_gcs_path"
* We alter our upload route function


## Working with SQL

We can easily load data to and from sql with pandas. In our case we will use the `tamimimarkets` dataset, which contains the expenses of a Saudi Arabian supermarket in April of 2020.

We can connect to any sql server using a connection string that looks like this:

```
<dialect>+<driver>://<username>:<password>@<host>/<database-name>
```

* dialect - The type of the database e.g. mysql, postgres, sqlite
* driver - The name of the api to communicate with the database. There are default for each dialect, so you don't always have to enter this
* username - the username that is registered in the database. A database can have multiple users. In postgres there will always be the user "postgres"
* password - the password for the respective user account
* host - where the database is located. This is normally the ip address
* database name - The different collections of data

A connection string for our case could look like this:

`postgresql://postgres:mypassword@34.77.39.10/supermarket_data`

Besides the method we covered so far, we can connect to a database by using the create_engine command of the sql alchemy package:

`engine = create_engine(postgresql://postgres:mypassword@34.77.39.10/supermarket_data)`


Lets have a look at this in `Code/4-sql`

## BigQuery
BigQuery is a large-scale data warehouse for analysis of petabytes of data. It has a SQL like syntax which makes it very easy to work with!

https://www.qwiklabs.com/focuses/2802?parent=catalog


### Further resources on SQL

* [W3 Schools SQL Tutorial](https://www.w3schools.com/sql/sql_intro.asp)
* [Learn SQL](https://sqlzoo.net/wiki/SELECT_basics)
