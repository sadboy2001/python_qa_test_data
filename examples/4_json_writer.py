import json

data = {
    "users": [
        {'name': 'Doomguy', 'skill': 100, 'gold': '99999', "weapons": ['Sword', 'Atomic Laser'], 'alive': True},
        {'name': 'Looser', 'skill': 1, 'gold': '-100000', "weapons": [None, None, None], 'alive': False},
    ]
}

with open("example.json", "w") as f:
    s = json.dumps(data, indent=4)
    f.write(s)
