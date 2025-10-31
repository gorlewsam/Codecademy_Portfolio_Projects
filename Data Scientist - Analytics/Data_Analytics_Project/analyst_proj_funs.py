import numpy as np
import pandas as pd
np.set_printoptions(legacy='1.25')

# Replacing the coded column names with their corresponding labels
def ReplaceColNames(df, codes_file):
    modified_df = df.copy()
    codes = codes_file.iloc[:, 0].tolist() 
    labels = codes_file.iloc[:, 1].tolist()

    for col in modified_df.columns:
        if col in codes:
            modified_df = modified_df.rename(columns={col: labels[codes.index(col)]})

    return modified_df


# Displaying unique categories as well as how many entries each has
def DisplayCatValCounts(df):
    df_ = df.select_dtypes(exclude=['int', 'float'])
    for col in df_.columns:
        print(df_[col].unique())                            # Printing categories' names
        print(df_[col].value_counts(dropna=False), "\n")    # Printing number of patients in each category


# Converting object dtype columns to string dtype
def ObjectDtypeConvert(df):
    for col in df.columns:
        if df[col].dtype == 'object':
            if True in df[col].unique():
                df[col] = df[col].astype(bool)
            
            else:
                df[col] = df[col].astype(str)
    
    return df


# Looking at blood counts to investigate associations with lung cancer, excluding NaNs
def col_LC_nonLC_median(df, col):
    LC_vals = []
    nonLC_vals = []

    LC_vals = df.loc[df['label'] == 1, col].tolist()
    nonLC_vals = df.loc[df['label'] == 0, col].tolist()

    return np.nanmedian(LC_vals), np.nanmedian(nonLC_vals)