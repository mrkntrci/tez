import json
from pprint import pprint
from dataStructures import *


def findPaths(entityID, adjacencies, previousEntities, controllerIDs, paths):
    print("\n\nEntity ID: ", entityID)
    print("Adjacents: ", adjacencies[entityID])
    print("Previous: ", previousEntities)

    if(entityID in controllerIDs):
        # FOUND A PATH
        print("\n\n\n***************       PATH      ********************\n")
        previousEntities.append(entityID)
        paths.append(previousEntities)

        print("PATH: ", paths)
        return paths

    try:
        # Find the adjacencies of the entity ID
        for i in range(len(adjacencies[entityID])):
            print("----- i: ", i)
            if(adjacencies[entityID][i] in previousEntities):
                print("A")
                continue
            else:
                print("\t\tB")
                print("E -ID: ", entityID)

                if(entityID not in previousEntities):
                    previousEntities.append(entityID)

                print("Siradaki: ", adjacencies[entityID][i])
                findPaths(adjacencies[entityID][i],
                          adjacencies,
                          previousEntities,
                          controllerIDs,
                          paths)

    except:
        print("Girdi")
        return
    finally:
        return paths


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
    viaID = data['rows'][e]['viaGlobalId']
##    print("From: ", fromID)
##    print("To: ", toID)
##    print("Via: ", viaID)

    # WE HAVE NOT COVERED THE EDGES!
    # Do not add the entity itself as its own adjacent - hence the AND clause!
    if(fromID in entities):
        if( (not (toID in entities[fromID])) and fromID != toID):
            entities[fromID].append(toID)
##        if( (not (viaID in entities[fromID])) and fromID != viaID):
##            entities[fromID].append(viaID)
    else:
        entities[fromID] = []
        entities[fromID].append(toID)
##        entities[fromID].append(viaID)

    # The adjacency is bidirectional! -->
    if(toID in entities):
        if( (not (fromID in entities[toID])) and toID != fromID):
            entities[toID].append(fromID)
##        if( (not (viaID in entities[toID])) and toID != viaID):
##            entities[toID].append(viaID)
    else:
        entities[toID] = []
        entities[toID].append(fromID)
##        entities[toID].append(viaID)

inputEntity = '{2B6225F3-6544-4995-BA7D-7908113B5E87}'



# controllers IDs
numControllers = len(data["controllers"])
#print("Number of controllers: ", numControllers)

#print("Controller IDs: ")
controllerIDs = []
for c in range(numControllers):
    controllerIDs.append(data['controllers'][c]['globalId'])

previousEntities = findPaths(inputEntity, entities, [], controllerIDs, [[]])




print(controllerIDs)
