import helpers
import pandas as pd


concatPolData = helpers.concatPoliceFiles()            

# Remove rows which do not have an LSOA
concatPolData = concatPolData[concatPolData["LSOA name"].notnull()]

LSOAs = list(concatPolData["LSOA name"].unique())
months = sorted(list(concatPolData["Month"].unique()))

# Generate dummy variables for the months, and concatenate this on to the combined dataframe
# This is required to get 0 values for months where no crime occurs
monthDummys = pd.get_dummies(concatPolData["Month"])
concatWithDummys = pd.concat([concatPolData,monthDummys], axis=1)


# aggregate the data by LSOA name and Crime type, summing the month dummy variables
aggData = concatWithDummys[['LSOA name', 'Crime type', 'Month'] + months].groupby(['LSOA name', 'Crime type'],as_index=False).sum()

aggDataLong = pd.melt(aggData, id_vars=['LSOA name', 'Crime type'], value_vars=months, var_name='Date', value_name='Count')

# Plot a time series for all LSOA names
for LSOA in LSOAs:
    helpers.crimeTimeSeries(aggDataLong,LSOA)


