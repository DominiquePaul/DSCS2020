import pandas as pd
from sqlalchemy import create_engine

from secrets import SQL_PASSWORD, SQL_PUBLIC_IP, SQL_DATABASE_NAME

# Google Cloud SQL settings
PASSWORD = SQL_PASSWORD
PUBLIC_IP_ADDRESS = SQL_PUBLIC_IP
DBNAME = SQL_DATABASE_NAME

# set up the engine connecting us with the database
connection_string = f"postgresql://postgres:{PASSWORD}@{PUBLIC_IP_ADDRESS}/{DBNAME}"
engine = create_engine(connection_string)

# we read in the data and send it to the sql database
df = pd.read_csv("data/tamimimarkets.csv")
df.to_sql("tamimimarkets", engine, if_exists="replace")


df.columns = [x.lower() for x in df.columns]
# we can determine what to do if a database exists
# Options: "append", "replace", "fail"
df.to_sql("tamimimarkets", engine, if_exists="replace")


# We can also load data like that from a sql database
# This is very useful if we just quickly want to grab some data for analysis
tamimi = pd.read_sql("tamimimarkets", engine)


# and also run sql commands
query1 = """
select *
from tamimimarkets
"""

pd.DataFrame(engine.execute(query1))
