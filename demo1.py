import json
from difflib import get_close_matches
data = json.load(open("data.json"))
print(get_close_matches("rainn", data.keys()))