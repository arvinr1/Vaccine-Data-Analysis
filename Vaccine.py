import pandas as pd
import numpy as np

def make_subset(df, region = None, vaccine = None, year = None, additive = True):
    if additive == False:
        if region != None and vaccine != None and year != None:
            df_copy = df.loc[(df['Region'].isin(region)) | (df['Vaccine'].isin(vaccine)) | (df['Year'].isin(year))]
        else:
            df_copy = df.copy()
    elif additive == True:
        if region == None:
            region = df['Region'].values.tolist()
        if vaccine == None:
            vaccine = df['Vaccine'].values.tolist()
        if year == None:
            year = df['Year'].values.tolist()
        df_copy = df.loc[(df['Region'].isin(region)) & (df['Vaccine'].isin(vaccine)) & (df['Year'].isin(year))]
    return df_copy
