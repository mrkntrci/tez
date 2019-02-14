import json
from pprint import pprint

with open('SampleDataset1.json') as file:
    data = json.load(file)

from_vertices = []
for i in range(17):
    from_vertices.append(data["rows"][i]["toGlobalId"])

to_vertices= []
for i in range(17):
    to_vertices.append(data["rows"][i]["toGlobalId"])
