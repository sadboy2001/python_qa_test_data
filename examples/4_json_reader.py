import json
from files import JSON_FILE_PATH


with open(JSON_FILE_PATH, "r") as f:
    users = json.loads(f.read())

users_list = users['users']

for user in users_list:
    print(user)
