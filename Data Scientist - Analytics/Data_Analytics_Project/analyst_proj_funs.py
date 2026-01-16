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
def col_LC_nonLC_mean(df, col):
    LC_vals = []
    nonLC_vals = []

    LC_vals = df.loc[df['label'] == 1, col].to_numpy()
    nonLC_vals = df.loc[df['label'] == 0, col].to_numpy()
    
    
    lc_q1 = np.nanquantile(LC_vals, 0.25)
    lc_q3 = np.nanquantile(LC_vals, 0.75)
    nonlc_q1 = np.nanquantile(nonLC_vals, 0.25)
    nonlc_q3 = np.nanquantile(nonLC_vals, 0.75)
    lc_iqr = lc_q3 - lc_q1   
    nonlc_iqr = nonlc_q3 - nonlc_q1

    LC_vals = pd.DataFrame({col: LC_vals})
    nonLC_vals = pd.DataFrame({col: nonLC_vals})

    LC_vals.loc[(LC_vals[col]>lc_q3+1.5*lc_iqr),col]=np.nan
    LC_vals.loc[(LC_vals[col]<lc_q1-1.5*lc_iqr),col]=np.nan
    nonLC_vals.loc[(nonLC_vals[col]>nonlc_q3+1.5*nonlc_iqr),col]=np.nan
    nonLC_vals.loc[(nonLC_vals[col]<nonlc_q1-1.5*nonlc_iqr),col]=np.nan

    return round(np.nanmean(LC_vals), 2), f"+/-", round(np.nanstd(LC_vals),2), round(np.nanmean(nonLC_vals), 2), f"+/-", round(np.nanstd(nonLC_vals),2)

def age_ranges_LC_nonLC(df):
    LC_vals = []
    nonLC_vals = []

    LC_vals = df.loc[df['label'] == 1, 'age'].tolist()
    nonLC_vals = df.loc[df['label'] == 0, 'age'].tolist()

    min_LC = np.min(LC_vals)
    max_LC = np.max(LC_vals)
    min_nonLC = np.min(nonLC_vals)
    max_nonLC = np.max(nonLC_vals)
    return f"Age range of LC Patients: [{min_LC}, {max_LC}], Age Range of Non-LC Patients: [{min_nonLC}, {max_nonLC}]"

def remove_outliers(df, col):
    LC_vals = []
    nonLC_vals = []

    LC_vals = df.loc[df['label'] == 1, col].to_numpy()
    nonLC_vals = df.loc[df['label'] == 0, col].to_numpy()

    lc_q1 = np.nanquantile(LC_vals, 0.25)
    lc_q3 = np.nanquantile(LC_vals, 0.75)
    nonlc_q1 = np.nanquantile(nonLC_vals, 0.25)
    nonlc_q3 = np.nanquantile(nonLC_vals, 0.75)
    lc_iqr = lc_q3 - lc_q1   
    nonlc_iqr = nonlc_q3 - nonlc_q1

    LC_vals = pd.DataFrame({col: LC_vals})
    nonLC_vals = pd.DataFrame({col: nonLC_vals})

    LC_vals.loc[(LC_vals[col]>lc_q3+1.5*lc_iqr),col]=np.nan
    LC_vals.loc[(LC_vals[col]<lc_q1-1.5*lc_iqr),col]=np.nan
    nonLC_vals.loc[(nonLC_vals[col]>nonlc_q3+1.5*nonlc_iqr),col]=np.nan
    nonLC_vals.loc[(nonLC_vals[col]<nonlc_q1-1.5*nonlc_iqr),col]=np.nan

    LC_vals['label']=1
    nonLC_vals['label']=0

    df_cols = [nonLC_vals, LC_vals]
    col_vals = pd.concat(df_cols, ignore_index=True)

    return col_vals