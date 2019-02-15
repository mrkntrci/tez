import json
from pprint import pprint
###open file
with open('SampleDataset1.json') as file:
    data = json.load(file)

###find the from vertices anc append them in a list
from_vertices = []
for i in range(0,len(data['rows'])):
    from_vertices.append(data["rows"][i]["fromGlobalId"])
#for item in from_vertices:
#    print(item)


###find to receiving vertices and append them in a list

to_vertices= []
for i in range(0,len(data['rows'])):
    to_vertices.append(data["rows"][i]["toGlobalId"])

#for item in to_vertices:
#    print(item)

edges = []
matrix =[from_vertices,to_vertices]
#for i in matrix:
#    print(i[1])

for i in matrix:
    for j in range(16):
        edges.append(i[j])
for item in edges:
    print(item)
print(len(edges))

rows = data['rows']
