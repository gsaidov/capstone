import json
import geopandas as gpd
import numpy as np


# Import necessary data in geopandas format

def get_geo_data(filepath):
    df = gpd.read_file(filepath)

    return df # returns a geopandas dataframe





