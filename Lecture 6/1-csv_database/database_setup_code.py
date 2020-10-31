import pandas as pd

post_data = pd.DataFrame(columns=["name", "description", "price"])
post_data.to_csv("data/product_data.csv", index=False)

user_data = pd.DataFrame(columns=["name", "email", "password"])
user_data.to_csv("data/user_data.csv", index=False)
