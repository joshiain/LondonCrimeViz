# LondonCrimeViz

The data used for this is contained in the "PoliceData" folder.

## Python Scripts

The python scripts are in python3. The three main python scripts `transformData.py`, `crimeTimeSeries.py`, and `setupHeatmap.py` are written so that they can be run independently.

### helpers.py

`helpers.py` is a script containing helper functions that are used in the other three main scripts. It requires the packages matplotlib and pandas to be installed in your version of python.

It contains a function called `concatPoliceFiles` to concatenate the police data files in the folder 'PoliceData'. If your police files with the 'YYYY-MM' name format are in a different folder, input the folder root string as an input to this function.

Other functions include `df_to_geojson` a function that converts a dataframe in to GeoJSON, and `crimeTimeSeries` that plots a time series of the count of crime types for a particular LSOA over the time period of the input dataframe.

### transformData.py

This python script generates an output csv with all of the csv's inside the PoliceData folder concatenated in a new file called `combinedPoliceData.csv`. It is important the folders within "PoliceData" follow the 'YYYY-MM' name format.

This script generates a second output file called `policeCount.json` which represents the concatenated police crime data as a JSON time series in the form:

```json
 {
    "LSOA name1": {
        "crime_type_1": \[count\_month\_1\_year\_1, count\_ month\_2\_year\_1, \.\.\., count\_month\_12\_year_3\],
        "crime_type_2": \[count\_month\_1\_year\_1, count\_month\_2\_year\_2, \.\.\., count\_month\_12\_year\_3\]
        },
    "LSOA name2": {
        "crime_type _1": \[\.\.\.\],
        \.\.\.
        }
    \.\.\.
}
```

### crimeTimeSeries.py

