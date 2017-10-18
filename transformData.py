import helpers
import pandas as pd
import json
from collections import defaultdict


concatPolData = pd.read_csv('combinedPoliceData.csv')            

# Remove rows which do not have an LSOA
concatPolData = concatPolData[concatPolData["LSOA name"].notnull()]


LSOAs = list(concatPolData["LSOA name"].unique())
crimeTypes = list(concatPolData["Crime type"].unique())
months = sorted(list(concatPolData["Month"].unique()))

# initialise dictionary in the structure of the json
outputDict = defaultdict(dict)
for lsoa in LSOAs:
    for t in crimeTypes:
        outputDict[lsoa][t] = [0] * len(months)

# update count values in dictionary
for index, row in concatPolData.iterrows():
    outputDict[row["LSOA name"]][row["Crime type"]][months.index(row["Month"])] += 1

# write the dictionary to a json file
with open("policeCount.json", "w") as f:
    json.dump(outputDict, f, indent=2)






