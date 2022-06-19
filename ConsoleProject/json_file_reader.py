import json


fhand=open("resources/blocks.json")

jhand=json.load(fhand)
for keys in jhand:
    print(keys)

