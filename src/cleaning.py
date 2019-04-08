import geopandas as gpd
import pandas as pd
import numpy as np


# Convert date and time columns to pandas date and time 

def convert_date(df, column):
    # df is the pandas or geopandas dataframe
    # column is the name of the column (string)
    df.loc[:, 'new_column_name'] = pd.to_datetime(df[column])


# Create a year, month, day, and dayofweek columns

def create_time(df, , date_col, length_of_time):
    # df is the pandas or geopandas dataframe
    # length_of_time is the name of time length (string) : year, month, day, dayofweek
    # date_col is the datetime column of the dataframe (string)
    new_df.loc[:, length_of_time] = pd.DatetimeIndex(new_df[date_col]).length_of_time






