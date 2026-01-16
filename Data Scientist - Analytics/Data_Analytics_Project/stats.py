import pandas as pd
from scipy.stats import ttest_ind, chi2_contingency
from analyst_proj_funs import col_LC_nonLC_mean, age_ranges_LC_nonLC, remove_outliers
import numpy as np
np.set_printoptions(legacy='1.25')

lc_data = pd.read_csv('clean_df.csv')
#print(lc_data.head(10))
#print(lc_data.columns)


# Asking: what proportion of patients have lung cancer in this dataset?
non_lc_patients = lc_data.loc[lc_data.label == 0]
lc_patients = lc_data.loc[lc_data.label == 1]
prop_non_lc = len(non_lc_patients) / len(lc_data)
prop_lc = len(lc_patients) / len(lc_data)
print('{:.1%} of patients in this dataset have lung cancer, and {:.1%} do not.'.format(prop_lc, prop_non_lc), "\n")


# Looking at mean ages and age ranges for LC and non-LC patients
print("Mean Ages for LC and non-LC Patients:", 
      col_LC_nonLC_mean(lc_data, 'age'))

print(age_ranges_LC_nonLC(lc_data), "\n")


# Investigating whether there are significant differences between blood counts
# of LC and non-LC patients, removing outliers that are >Q3+1.5*IQR and <Q1-1.5*IQR
# Platelet count
platelet_df = remove_outliers(lc_data, 'Platelets [#/volume] in Blood by Automated count')
platelets_lc = platelet_df['Platelets [#/volume] in Blood by Automated count'].loc[(lc_data['label'] == 1)]
platelets_non_lc = platelet_df['Platelets [#/volume] in Blood by Automated count'].loc[(lc_data['label'] == 0)]
tstat, pval = ttest_ind(platelets_lc, platelets_non_lc, nan_policy='omit')
print("Platelet Count p-val: ", pval)

#Leukocyte count
leuk_df = remove_outliers(lc_data, 'Leukocytes [#/volume] in Blood by Automated count')
leukocyte_lc = leuk_df['Leukocytes [#/volume] in Blood by Automated count'].loc[(lc_data['label'] == 1)]
leukocyte_non_lc = leuk_df['Leukocytes [#/volume] in Blood by Automated count'].loc[(lc_data['label'] == 0)]
tstat, pval = ttest_ind(leukocyte_lc, leukocyte_non_lc, nan_policy='omit')
print("Leukocyte Count p-val: ", pval)

#Erythrocyte distribution width (RDW-SD)
rdw_df = remove_outliers(lc_data, 'Erythrocyte distribution width [Entitic volume] by Automated count')
rdw_lc = rdw_df['Erythrocyte distribution width [Entitic volume] by Automated count'].loc[(lc_data['label'] == 1)]
rdw_non_lc = rdw_df['Erythrocyte distribution width [Entitic volume] by Automated count'].loc[(lc_data['label'] == 0)]
tstat, pval = ttest_ind(rdw_lc, rdw_non_lc, nan_policy='omit')
print("Erythrocyte Distribution Width p-val: ", pval)

#Hemoglobin
hemoglobin_df = remove_outliers(lc_data, 'Hemoglobin [Mass/volume] in Blood')
hemoglob_lc = hemoglobin_df['Hemoglobin [Mass/volume] in Blood'].loc[(lc_data['label'] == 1)]
hemoglob_non_lc = hemoglobin_df['Hemoglobin [Mass/volume] in Blood'].loc[(lc_data['label'] == 0)]
tstat, pval = ttest_ind(hemoglob_lc, hemoglob_non_lc, nan_policy='omit')
print("Hemoglobin Level p-val: ", pval)

#Carbon dioxide
co2_df = remove_outliers(lc_data, 'Carbon Dioxide')
co2_lc = co2_df['Carbon Dioxide'].loc[(lc_data['label'] == 1)]
co2_non_lc = co2_df['Carbon Dioxide'].loc[(lc_data['label'] == 0)]
tstat, pval = ttest_ind(co2_lc, co2_non_lc, nan_policy='omit')
print("Carbon Dioxide Level p-val: ", pval)

#Total bilirubin
bilirubin_df = remove_outliers(lc_data, 'Bilirubin.total [Mass/volume] in Serum or Plasma')
tot_bilirubin_lc = bilirubin_df['Bilirubin.total [Mass/volume] in Serum or Plasma'].loc[(lc_data['label'] == 1)]
tot_bilirubin_non_lc = bilirubin_df['Bilirubin.total [Mass/volume] in Serum or Plasma'].loc[(lc_data['label'] == 0)]
tstat, pval = ttest_ind(tot_bilirubin_lc, tot_bilirubin_non_lc, nan_policy='omit')
print("Total Bilirubin Level p-val: ", pval)

#Albumin
albumin_df = remove_outliers(lc_data, 'Albumin')
albumin_lc = lc_data['Albumin'].loc[(lc_data['label'] == 1)]
albumin_non_lc = lc_data['Albumin'].loc[(lc_data['label'] == 0)]
tstat, pval = ttest_ind(albumin_lc, albumin_non_lc, nan_policy='omit')
print("Albumin Level p-val: ", pval, "\n")

#Viral sinusitis 
vs_pos_nonlc = lc_data['Viral sinusitis (disorder)'].loc[(lc_data['Viral sinusitis (disorder)'] == True) & (lc_data['label'] == 0)]
vs_neg_nonlc = lc_data['Viral sinusitis (disorder)'].loc[(lc_data['Viral sinusitis (disorder)'] == False) & (lc_data['label'] == 0)]
nonlc_sinus = pd.concat([vs_pos_nonlc, vs_neg_nonlc], ignore_index=True, axis=0)
nonlc_sinus = pd.DataFrame({'Viral sinusitis (disorder)': nonlc_sinus})
nonlc_sinus['label'] = 0

vs_pos_lc = lc_data['Viral sinusitis (disorder)'].loc[(lc_data['Viral sinusitis (disorder)'] == True) & (lc_data['label'] == 1)]
vs_neg_lc = lc_data['Viral sinusitis (disorder)'].loc[(lc_data['Viral sinusitis (disorder)'] == False) & (lc_data['label'] == 1)]
lc_sinus = pd.concat([vs_pos_lc, vs_neg_lc], ignore_index=True, axis=0)
lc_sinus = pd.DataFrame({'Viral sinusitis (disorder)': lc_sinus})
lc_sinus['label'] = 1

sinus_df = pd.concat([nonlc_sinus, lc_sinus], ignore_index=True, axis=0)
obs = pd.crosstab(sinus_df['Viral sinusitis (disorder)'], sinus_df['label'])
print(obs)
chi2, pval, dof, expected = chi2_contingency(obs)
print("Viral Sinusitis and Lung Cancer chi^2 p-val:", pval, "\n")

#Smoking status
smoke_former_nonlc = lc_data['Tobacco smoking status NHIS'].loc[(lc_data['Tobacco smoking status NHIS'] == 'former') & (lc_data['label'] == 0)]
smoke_never_nonlc = lc_data['Tobacco smoking status NHIS'].loc[(lc_data['Tobacco smoking status NHIS'] == 'never') & (lc_data['label'] == 0)]
nonlc_smoke = pd.concat([smoke_former_nonlc, smoke_never_nonlc], ignore_index=True, axis=0)
nonlc_smoke = pd.DataFrame({'Tobacco smoking status NHIS': nonlc_smoke})
nonlc_smoke['label'] = 0

smoke_former_lc = lc_data['Tobacco smoking status NHIS'].loc[(lc_data['Tobacco smoking status NHIS'] == 'former') & (lc_data['label'] == 1)]
smoke_never_lc = lc_data['Tobacco smoking status NHIS'].loc[(lc_data['Tobacco smoking status NHIS'] == 'never') & (lc_data['label'] == 1)]
lc_smoke = pd.concat([smoke_former_lc, smoke_never_lc], ignore_index=True, axis=0)
lc_smoke = pd.DataFrame({'Tobacco smoking status NHIS': lc_smoke})
lc_smoke['label'] = 1

smoke_df = pd.concat([nonlc_smoke, lc_smoke], ignore_index=True, axis=0)
obs = pd.crosstab(smoke_df['Tobacco smoking status NHIS'], smoke_df['label'])
print(obs)
chi2, pval, dof, expected = chi2_contingency(obs)
print("Smoking Status and Lung Cancer chi^2 p-val:", pval, "\n")

# Looking at blood counts to investigate associations with lung cancer, excluding NaNs and outliers
print("Mean Platelet Counts for LC and non-LC Patients, With Outliers Filtered:", 
      col_LC_nonLC_mean(lc_data, 'Platelets [#/volume] in Blood by Automated count'))

print("Mean Leukocyte Counts for LC and non-LC Patients, With Outliers Filtered:",
      col_LC_nonLC_mean(lc_data, 'Leukocytes [#/volume] in Blood by Automated count'))

print("Mean Erythrocyte Distribution Width for LC and non-LC Patients, With Outliers Filtered:",
      col_LC_nonLC_mean(lc_data, 'Erythrocyte distribution width [Entitic volume] by Automated count'))

print("Mean Hemoglobin Levels for LC and non-LC Patients, With Outliers Filtered:",
      col_LC_nonLC_mean(lc_data, 'Hemoglobin [Mass/volume] in Blood'))

print("Mean Carbon Dioxide Levels for LC and non-LC Patients, With Outliers Filtered:", 
      col_LC_nonLC_mean(lc_data, 'Carbon Dioxide'))

print("Mean Bilirubin Levels for LC and non-LC Patients, With Outliers Filtered:", 
      col_LC_nonLC_mean(lc_data, 'Bilirubin.total [Mass/volume] in Serum or Plasma'))

print("Mean Albumin Levels for LC and non-LC Patients, With Outliers Filtered:", 
      col_LC_nonLC_mean(lc_data, 'Albumin'))