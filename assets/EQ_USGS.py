#!/usr/bin/env python
# coding: utf-8

# Written by Saied Mighani
#Latest update 20-07-19


#imports

import requests
import json
import pandas as pd
import numpy as np
import pandas as pd


# - Function for EQ json reading


def get_EQ_USGS_API(Params):
    """
    This function inputs the required details for pulling API's from USGS using requests library. Parameters are taken through {params_diction}
    """
    baseurl = 'https://earthquake.usgs.gov/fdsnws/event/1/query?'
    
    params_diction={}
    
    params_diction['format'] = Params["get_format"] # Format for importing data
    
    params_diction['starttime'] = Params["min_date"] # Minimum date for reporting the data
    params_diction['endtime'] = Params["max_date"] # Maximum date for reporting the data
    
    params_diction['minmagnitude'] = Params["min_magnitude"] # Minimum magnitude of the reporting data
    params_diction['maxmagnitude'] = Params["max_magnitude"] # Maximum magnitude of the reporting data
    
    params_diction['minlatitude'] = Params["min_latitude"] # Minimum latitude
    params_diction['maxlatitude'] = Params["max_latitude"] # Maximum latitude
    params_diction['minlongitude'] = Params["min_longitude"] # Minimum longitude
    params_diction['maxlongitude'] = Params["max_longitude"] # Maximum longitude
    
    params_diction['orderby'] = Params["order_by"] # Ordering the data by parameters
    
    params_diction['limit'] = Params["limit_data"] # Maximum number of data
    
    resp = requests.get(baseurl, params=params_diction)
    
    if resp.status_code == 200: 
        print("API status code: ", resp.status_code)
        return resp.json()
    
    else:
        print("An error occured while pulling API, please revisit parameters; status code: ", resp.status_code)




def get_EQ_USGS_df(Params):
    """
    This function inputs the converted DataFrame from USGS pulled API
    """
    USGS_EQ_data_pull = get_EQ_USGS_API(Params)
    # #### Step 1: Converting the imported "feature" json data into pandas dataframe
    USGS_EQ_features = USGS_EQ_data_pull["features"]
    df_eq = pd.DataFrame(USGS_EQ_features)
    
    df_4 = pd.DataFrame()


    for i in range(df_eq.shape[0]):
        H = df_eq["properties"][i]
        df_1 = pd.DataFrame.from_dict(H, orient='index').T
        df_1["index"] = i

        H = df_eq["geometry"][i]
        df_2 = pd.DataFrame.from_dict(H, orient='index').T
        df_2["index"] = i

        df_3 = pd.concat([df_1, df_2], axis=1)

        df_4= df_4.append(df_3)

    df_eq_parsed_properties = df_4
    
    print(len(df_4), " number of earthquakes were pulled")
    
    return df_eq_parsed_properties


def clean_EQ_USGS_df(df):
    """
    This function cleans the pulled DataFrames
    """

    # Getting only the useful columns
    df_clean = df[['type', "time", "coordinates", "mag", "place", "status", "tsunami", "sig", "net", 
                     "nst", "dmin", "rms", "gap", "magType"]].copy()

    # Parsing the coordinates

    long = [] 
    lat =[] 
    dep = []

    for i in range(len(df_clean)):

        coord_values = df_clean["coordinates"][i].replace("[", "").replace("]", "").replace(",", "").split()

        try:
            long.append(float(coord_values[0]))
        except:
            long.append(float("NaN"))
        
        try:
            lat.append(float(coord_values[1]))
        except:
            lat.append(float("NaN"))
            
        try:
            dep.append(float(coord_values[2]))
        except:
            dep.append(float("NaN"))
            
            
        

    df_clean["longitude"] = long
    df_clean["latitude"] = lat
    df_clean["depth"] = dep

    #Fixing time
    time = pd.to_datetime(df_clean["time"], unit="ms") 

    df_clean["time"] = time


    #Droppinguseless coordinate column

    df_clean.drop(columns = "coordinates", inplace = True)

    return df_clean