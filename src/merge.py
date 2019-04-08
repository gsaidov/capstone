import geopandas as gpd
import pandas as pd
import numpy as np
import json
from shapely.geometry import Point, LineString, Polygon
import pickle

# getting the geometry data from geopandas dataframes
def get_geom(df):
    return df.geometry



# function to find the minimum distance between each accident point 
# and traffic volume of road segments in the traffic volume data

def min_dist(points, linestrings):
    # points  is the series of geopandas dataframe geometry column
    # linestrings is the series of geopandas dataframe geometry column

    dist = []
    for point in points:
        dis = []
        for line in linestrings: # for each line find the closest point
            dis.append(line.distance(point))
        
        dist.append(np.array(dis).argmin()) # add the line with minimum distance to the distance array
    
    return np.array(dist)

# function to find the nearest road blocks in the road network data 
# to each road segment in traffic volume data to find annual daily traffic for each road block

def min_block(network, segments):
    dist = []
    for segment in segments.geometry:
        d = []
        for block in network.geometry:
            d.append(segment.distance(block))
    d = np.array(d)
    return dist.append(d.argmin())
    

# Joining two dataframes based on the same indices

def add_df(df1, df2):

    # df1 and df2 are two pandas dataframes

    # if the indices are different for two dataframes, make them same by setting the indices of 
    # one dataframe as the indices of another.

    df2['index'] = df1.index
    df2.set_index('index', inplace = True) # making the indices same for the two dataframes

    return df1.join(df2)



# We can save the dataframe as a csv file or pickle file

# accident.to_csv('data/accident.csv', index = False)
# accident.to_pickle('data/accident.pickle')

    