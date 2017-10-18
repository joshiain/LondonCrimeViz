import helpers
import pandas as pd

concatPolData = helpers.concatPoliceFiles()            
concatPolData.to_csv('combinedPoliceData.csv')