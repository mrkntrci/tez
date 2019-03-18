import json
from pprint import pprint
import time
start = time.time()
#from dataStructures import *

# Open the data set
with open('SampleDataset1.json') as f:
    data = json.load(f)

##pprint(data)

##for i in range(17):
##    print(data["rows"][i]["fromGlobalId"])

#print(data["rows"][1]["fromGlobalId"])

# How many edges are there?

entities = {}
#print(len(data['rows']))
for e in range(len(data["rows"])):
    # Check whether the entity has been created previously?
    fromID = data['rows'][e]['fromGlobalId']
    toID = data['rows'][e]['toGlobalId']
    viaID = data['rows'][e]['viaGlobalId'] # edge


    # WE HAVE NOT COVERED THE EDGES!
    # Do not add the entity itself as its own adjacent - hence the AND clause!
    if(fromID in entities):
        if( (not (toID in entities[fromID])) and fromID != toID):
            entities[fromID].append(toID)
    else:
        entities[fromID] = []
        entities[fromID].append(toID)

    # The adjacency is bidirectional! -->
    if(toID in entities):
        if( (not (fromID in entities[toID])) and toID != fromID):
            entities[toID].append(fromID)
    else:
        entities[toID] = []
        entities[toID].append(fromID)

def dfs_recursive(graph, vertex, path=[]):
    path += [vertex]

    for neighbor in graph[vertex]:
        if neighbor not in path:
            path = dfs_recursive(graph, neighbor, path)

    return path

print(dfs_recursive(entities, '{7FC28536-6F4A-4A9A-B439-1D87AE2D8871}'))

def dfs_iterative(graph, start):
    stack, path = [start], []

    while stack:
        vertex = stack.pop()
        if vertex in path:
            continue
        path.append(vertex)
        for neighbor in graph[vertex]:
            stack.append(neighbor)

    return path
#print(dfs_iterative(entities, '{7FC28536-6F4A-4A9A-B439-1D87AE2D8871}'))
end = time.time()
print(end - start)
