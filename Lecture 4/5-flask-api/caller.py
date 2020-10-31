
import requests


# Endpoint 1
endpoint1 = "http://0.0.0.0:5000/math/2/4"
r = requests.get(endpoint1)
r.text



# Endpoint 2
endpoint2 = "http://0.0.0.0:5000/math2"
parameters = {"num1": 2, "num2": 4}
r = requests.get(endpoint2, params=parameters)
r.text
r.url

# Endpoint 3
endpoint3 = "http://0.0.0.0:5000/math3"
parameters = {"num1": 2, "num2": 5}
r = requests.get(endpoint3, params=parameters)
r.text
r.json()["sum"]


# Endpoint 4
endpoint4 = "http://0.0.0.0:5000/math4"
body = {"nums": [1, 3, 4, 5, 12]}
r = requests.post(endpoint4, json=body)
r.json()
