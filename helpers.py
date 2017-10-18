import os
import pandas as pd
import matplotlib.pyplot as plt


def concatPoliceFiles(string='PoliceData'):
    concatPolData = pd.DataFrame([])

    # Navigate through police data files and combine in to one dataframe
    for root, dirs, files in os.walk(string):
        for file in (f for f in files if f.endswith(".csv")): 
            filePath = os.path.join(root,file)
            tempdf = pd.read_csv(filePath)
            tempdf['Month'] = root.replace(string+"/","")
            concatPolData = concatPolData.append(tempdf)
    
    return concatPolData

def df_to_geojson(df, parameters, lat='Latitude', lon='Longitude'):
    # define a function to convert a dataframe to GeoJSON. This was pulled from the internet and modified slightly
    geojson = {'type':'FeatureCollection', 'features':[]}
    for index, row in df.iterrows():
        if ((not pd.isnull(row[lon])) and (not pd.isnull(row[lat]))):
            feature = {'type':'Feature',
                       'properties':{},
                       'geometry':{'type':'Point',
                                   'coordinates':[]}}
            feature['geometry']['coordinates'] = [row[lon],row[lat]]
            for prop in parameters:
                feature['properties'][prop.replace(" ", "")] = row[prop]
            geojson['features'].append(feature)
    return geojson

def crimeTimeSeries(df,LSOA):
    # plot a time series and save in plots folder _ = is to supress the output in my console
    currentCrimes = df[df["LSOA name"]==LSOA].groupby('Crime type')['Crime type']
    numColours = len(currentCrimes)
    cm = plt.get_cmap('gist_rainbow')
    fig, ax = plt.subplots(1,1)
    _ = ax.set_title(LSOA)
    _ = ax.set_ylabel('Date')
    _ = ax.set_ylabel('Crime Count')
    _ = ax.set_prop_cycle('color',[cm(1.*i/numColours) for i in range(numColours)])
    _ = df[df["LSOA name"]==LSOA].groupby("Crime type").plot(x='Date', y='Count', ax=ax);
    _ = plt.legend([v[0] for v in currentCrimes], bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    plt.savefig('plots/'+LSOA+'_time_series.pdf',bbox_inches='tight')
    plt.close()