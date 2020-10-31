from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

password_hash = bcrypt.generate_password_hash("test")
# This is a bytes string
password_hash

# We can convert it to a regular string using .decode("utf-8")
# utf8 is the standard encoding method for text on your computer.
password_hash.decode("utf-8")


# Every time we run this the output is different
for i in range(3):
    print(bcrypt.generate_password_hash("test"))


# So how do we check if a user enters the correct password?
# We use a different function called
bcrypt.check_password_hash(password_hash, "mypassword")  # returns False
bcrypt.check_password_hash(password_hash, "test")  # returns True
