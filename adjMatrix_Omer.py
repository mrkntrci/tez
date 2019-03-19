import json
from pprint import pprint

# Open the data set
with open('SampleDataset1.json') as f:
    data = json.load(f)

##pprint(data)

##for i in range(17):
##    print(data["rows"][i]["fromGlobalId"])

#print(data["rows"][1]["fromGlobalId"])

# How many edges are there?
numEdges = len(data["rows"])

entities = {}

for e in range(numEdges):
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

# controllers IDs
numControllers = len(data["controllers"])
#print("Number of controllers: ", numControllers)

#print("Controller IDs: ")
controllerIDs = []
for c in range(numControllers):
    controllerIDs.append(data['controllers'][c]['globalId'])

ids = {}

c = 0
# Print the nodes and their adjacents
for k, v in entities.items():
	#print(k, ":\t", v)
	ids[k] = c
	c += 1

#print("IDs: \n", ids, "\n\n")

# Obtain from the dictionary
w = 17
adjacencyMatrix = [[0 for x in range(w)] for y in range(w)]

for k,v in entities.items():
    print(k, ": \t", v)
    numAdjacents = len(v)
    print("Num adjacents: ", numAdjacents)
    for i in range(numAdjacents):
        print("ID: ", ids[k], "Neighbour ID: ", ids[v[i]])
        adjacencyMatrix[ids[k]][ids[v[i]]] = 1
