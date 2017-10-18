# LondonCrimeViz

Access the heatmap visualisation [here](https://joshiain.github.io/LondonCrimeViz/).

Note: Only access this in Chrome for the best experience, the dropdown checkboxes are buggy in other browsers.

This was written on MacOS, as a result if using another operating system, file directory and instances in the code with '/' will need to be replaced with your system equivalent.

The data used for this is contained in the "PoliceData" folder.

## Python Scripts

The python scripts are in python3. The three main python scripts `transformData.py`, `crimeTimeSeries.py`, and `setupHeatmap.py` are written so that they can be run independently without requiring any of the other scripts to be run.

### helpers.py

`helpers.py` is a script containing helper functions that are used in the other three main scripts. It requires the packages matplotlib and pandas to be installed in your version of python.

It contains a function called `concatPoliceFiles` to concatenate the police data files in the folder 'PoliceData'. If your police files with the 'YYYY-MM' name format are in a different folder, input the folder root string as an input to this function.

Other functions include `df_to_geojson` a function that converts a dataframe in to GeoJSON, and `crimeTimeSeries` that plots a time series of the count of crime types for a particular LSOA over the time period of the input dataframe.

### transformData.py

Run this script by navigating to the folder that contains it in your terminal, and executing the command `python3 transformData.py`.

This python script generates an output csv with all of the csv's inside the PoliceData folder concatenated in a new file called `combinedPoliceData.csv`. It is important the folders within "PoliceData" follow the 'YYYY-MM' name format.

This script generates a second output file called `policeCount.json` which represents the concatenated police crime data as a JSON time series in the form:

```json
 {
    "LSOA name1": {
        "crime_type_1": [count month 1 year 1, count month 2 year 1, ..., count month 12 year 3],
        "crime_type_2": [count month 1 year 1, count month 2 year 2, ..., count month 12 year 3]
        },
    "LSOA name2": {
        "crime_type _1": [...],
        ...
        }
    ...
}
```

### crimeTimeSeries.py

Run this script by navigating to the folder that contains it in your terminal, and executing the command `python3 crimeTimeSeries.py`.

This script generates a timeseries plot for each LSOA of the count of crime occurences, by crime type. The plots generated are in the 'plots' folder.

As we plot a different subset of crime types for each plot (some crime types don't occur in a particular area at all in our time period), the colour assigned to a crime type line in the legend isn't consistent between plots.

#### Time Series Exploratory Summary

Particular areas in the City of London such as 001b, 001c, and 001e appear to have an increasing trend in the anti social behaviour crime count.

### setupHeatmap.py

Run this script by navigating to the folder that contains it in your terminal, and executing the command `python3 setupHeatmap.py`.

This script sets up the data to be used in the webapp with the heatmap visualisation. It generates GeoJSON from the crime data, and outputs a javascript file with the GeoJSON wrapped in a javascript function that is used in the google maps webapp called `policeGeoJSON.js`.

It also generates two other javascript files `lsoa.js` and `crimetypes.js`. These are simply assigning the unique values of the LSOA names, and the Crime types to a javascript array.

## Javascript webapp

Please view the visualisation in Google Chrome.

[Heatmap Visualisation](https://joshiain.github.io/LondonCrimeViz/).

This is the interactive heatmap visualisation of the crime counts in London. The heatmap can be filtered by LSOA name, and Crime type in the dropdown checkbox filters at the top of the webapp.

Note: Due to the limitations of the Google Maps API, a colour legend couldn't be generated. You may see more intense colours in areas when you filter and less crime points are plotted. This is because when filtering, the colour intensity of the heatmap is relative to counts of what is currently being displayed on the map.

### index.html

This contains the html and javascript used to create the heatmaps visualisation on Google Maps. It makes use of a jquery package called SumoSelect to create a dropdown checkbox to allow easy filtering of the LSOA names and Crime types. However SumoSelect is buggy in some browsers, so it is recommended to use Chrome.

It also loads the javascript file `policeGeoJSON.js` containing the GeoJSON generated from `setupHeatmap.py`.