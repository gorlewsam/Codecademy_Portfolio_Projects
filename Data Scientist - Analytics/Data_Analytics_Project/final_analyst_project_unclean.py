import pandas as pd
import numpy as np
np.set_printoptions(legacy='1.25')
from analyst_proj_funs import ReplaceColNames, DisplayCatValCounts, ObjectDtypeConvert

# Loading and examining data
lc_data1 = pd.read_csv('synthea-pt30k-lc-data-sel.csv', low_memory=False)
lc_data2 = pd.read_csv('synthea-pt30k1-lc-data-sel.csv', low_memory=False)
lc_data3 = pd.read_csv('synthea-pt30k2-lc-data-sel.csv', low_memory=False)
lc_data4 = pd.read_csv('synthea-pt30k3-lc-data-sel.csv', low_memory=False)
lc_data5 = pd.read_csv('synthea-pt30k4-lc-data-sel.csv', low_memory=False)

frames = [lc_data1, lc_data2, lc_data3, lc_data4, lc_data5]
lc_df = pd.concat(frames)
print(lc_df.head(10), "\n")
print(lc_df.shape, "\n")

# Loading in column name codes and corresponding labels
codes_file = pd.read_csv('synthea-lc-dataset-codes.csv')

# Replacing the coded column names with their corresponding labels
lc_df_rename = ReplaceColNames(lc_df, codes_file)
# print(lc_df_rename.head(10))


# Checking for repeat entries of individual patients
# print(df_['ptnum'].value_counts(dropna=False), "\n")

# When running print(df_['ptnum'].value_counts(dropna=False), "\n"), 
# some patient numbers are repeated, which skews data. Removing duplicate patients
lc_df_rename = lc_df_rename.copy().drop_duplicates(subset='ptnum')


# Checking for proportion of null values for each variable
print(lc_df_rename.isnull().sum()/len(lc_df_rename)) 

# Removing variables that are missing 60% or more of their data
lc_df_clean = lc_df_rename.dropna(axis=1, thresh=(len(lc_df_rename)*0.60))
print(lc_df_clean.shape)
print(lc_df_clean.isnull().sum()/len(lc_df_clean)) 
# print(lc_df_clean.columns, "\n")

# Variables with (procedure) only indicate whether a procedure was performed, not the results
# Filtering out variables with (procedure) in their name to evaluate relevance
# for col in lc_df_clean.columns:    
#     if "(procedure)" in col:
#         print(col)

# Procedures left after cleaning are not relevant to lung cancer diagnoses, removing them
lc_df_clean = lc_df_clean.copy()
for col in lc_df_clean.columns:    
    if "(procedure)" in col:
        lc_df_clean.drop(col, axis=1, inplace=True)

# print(lc_df_clean.columns, "\n")

# Remaining variables with (finding) indicate various social circumstances not relevant to lung cancer diagnosis
# Removing variables with (finding) in their name
lc_df_clean = lc_df_clean.copy()
for col in lc_df_clean.columns:    
    if "(finding)" in col:
        lc_df_clean.drop(col, axis=1, inplace=True)


print(lc_df_clean.shape, "\n")      # Left with 51 columns after cleaning
# print(lc_df_clean.columns, "\n")
# print(lc_df_clean.isnull().sum()/len(lc_df_clean), "\n") 
# print(lc_df_clean.dtypes)


# The "Influenza  seasonal  injectable  preservative free" variable
# is not relevant to lung cancer diagnoses, removing 
lc_df_clean = lc_df_clean.drop(['Influenza  seasonal  injectable  preservative free'], axis=1)


# Investingating categorical variables to evaluate answers and deal with NaNs
DisplayCatValCounts(lc_df_clean)

# The "Viral sinusitis (disorder)" variable has NaNs in place of 'False' values,
# replacing NaNs with False
lc_df_clean = lc_df_clean.copy()
lc_df_clean['Viral sinusitis (disorder)'] = lc_df_clean['Viral sinusitis (disorder)'].fillna(False)

# "Tobacco smoking status NHIS" variable has 11 NaNs, removing those patients
# DisplayCatValCounts(lc_df_clean)
lc_df_clean = lc_df_clean.dropna(subset=['Tobacco smoking status NHIS'])
# DisplayCatValCounts(lc_df_clean)


# Converting object dtype columns to string dtype
lc_df_clean = ObjectDtypeConvert(lc_df_clean)
# print("After conversion\n", lc_df_clean.dtypes, "\n")


# Writing cleaned dataframe to csv file for later visualization purposes
# lc_df_clean.to_csv('clean_df.csv', encoding='utf-8', index=False, header=True)