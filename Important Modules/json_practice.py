#Python has a built-in module named json that provides functionalities for working 
# with JSON (JavaScript Object Notation) data. JSON is a lightweight data-interchange
#  format commonly used for transmitting data between a server and web application, 
# or for storing configuration information.

import json

# Dict → JSON
data = {"user": "Ali", "role": "admin"}
json_str = json.dumps(data)
print("JSON String:", json_str)

# JSON → Dict
parsed = json.loads(json_str)
print("User:", parsed["user"])

# Save JSON to file
with open("data.json", "w") as f:
    json.dump(data, f)

# Load JSON from file
with open("data.json") as f:
    loaded = json.load(f)
print("Loaded from file:", loaded)
