import pandas as pd

user_data = pd.read_csv("data/user_data.csv")

email = "dominique.paul@unisg.ch"
password = "password"

is_email_in_database = email in list(user_data["email"])

if is_email_in_database:

    passwords_bool_mask = user_data.loc[user_data["email"] == email,
                                            "password"] == password
    is_password_correct = passwords_bool_mask.any()

    if is_password_correct:
        return True

return False


passwords_bool_mask.any()



user_data.loc[user_data["email"] == email, "password"] == password
