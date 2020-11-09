
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

df.head()

df.to_sql("tamimimarkets", engine, index=False,)

# we can determine what to do if a database exists
# Options: "append", "replace", "fail"
#
# By specifcing: method = "multi" we can also significantly speed up the upload
# process. By default, to_sql adds data row by row, but by method="multi" we
# tell pandas to write bigger chunks of data
df.to_sql("tamimimarkets", engine, if_exists="replace", method='multi')



# Same for the avocado dataset
df = pd.read_csv("data/avocado.csv")
df["Date"] = pd.to_datetime(df["Date"])
df.to_sql("avocado_sales",
          engine,
          index=False,
          if_exists="replace",
          method='multi')




# We can also load data like that from a sql database
# This is very useful if we just quickly want to grab some data for analysis
tamimi = pd.read_sql("tamimimarkets", engine)
tamimi


# We can also run sql commands
query1 = """
SELECT *
FROM tamimimarkets
"""

query2 = "select * from tamimimarkets"

pd.DataFrame(engine.execute(query1))


avo = pd.read_sql("avocado_sales", engine)
avo
