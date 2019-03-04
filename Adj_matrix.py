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

edges = zip(from_vertices,to_vertices)

matrix = []
matrix.append(from_vertices)
matrix.append(to_vertices)

for i in matrix:
    print(i)

empty_list =  []
for  i in range(len(from_vertices)):
    if from_vertices[i] not in empty_list:
        empty_list.append(from_vertices[i])
        from_vertices[i] = i
    elif from_vertices[i]  in empty_list:
        same_one = from_vertices[i]
        from_vertices[i] = empty_list.index(same_one)
print(from_vertices)
