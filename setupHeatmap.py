import helpers
import pandas as pd
import json


concatPolData = pd.read_csv('combinedPoliceData.csv')            

# Remove rows which do not have an LSOA
concatPolData = concatPolData[concatPolData["LSOA name"].notnull()]

LSOAs = list(concatPolData["LSOA name"].unique())
crimeTypes = list(concatPolData["Crime type"].unique())


crimeGeoJson = helpers.df_to_geojson(concatPolData,["LSOA name", "Crime type"])

# write the json as an input in to a javascript function used in the webapp
with open("policeGeoJSON.js", "w") as f:
    f.write('crime_callback(')
    json.dump(crimeGeoJson, f, indent=2)
    f.write(');')

# write the LSOA names to a javascript file that will define the list as a variable in JS
with open("lsoa.js", "w") as f:
    f.write('var LSOAs = ')
    f.write(str(list(LSOAs)).replace("'",'"'))
    f.write(';')

# write the crime types to a javascript file that will define the list as a variable in JS
with open("crimetypes.js", "w") as f:
    f.write('var crimeTypes = ')
    f.write(str(list(crimeTypes)).replace("'",'"'))
    f.write(';')