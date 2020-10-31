# You can also import the 'app' object from another script if you want to keep
# things clean. You only need two lines then: the import and the execution.

# Here we are using a different way of importing code from another script, but
# only because in this case the name of the script starts with a number which
# is a forbidden starting character for a object in python
other_script = __import__("1-basic_flask")

other_script.app.run()
