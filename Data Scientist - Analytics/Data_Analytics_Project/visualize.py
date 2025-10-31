import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from analyst_proj_funs import col_LC_nonLC_median

lc_data = pd.read_csv('clean_df.csv')
print(lc_data.head(10))
print(lc_data.columns)

# Asking: what proportion of patients have lung cancer in this dataset?
non_lc_patients = lc_data.loc[lc_data.label == 0]
lc_patients = lc_data.loc[lc_data.label == 1]
prop_non_lc = len(non_lc_patients) / len(lc_data)
prop_lc = len(lc_patients) / len(lc_data)
print('{:.1%} of patients in this dataset have lung cancer, and {:.1%} do not.'.format(prop_lc, prop_non_lc), "\n")


# Investigating NHIS tobacco smoking status for LC and non-LC patients
ax = sns.countplot(x='label', hue='Tobacco smoking status NHIS', data=lc_data)
plt.xlabel('Lung Cancer Status')
ax.set_xticks(range(0,2))
ax.set_xticklabels(['Non-LC', 'LC'])
plt.title('Smoking Status of Patients With and Without Lung Cancer')
plt.show()
plt.close()


# Investigating age distribution of patients with and without lung cancer
# Adding age group to the dataframe
lc_data_copy = lc_data.copy(deep=True)
bins = [30, 40, 50, 60, 70, 80, 90]                                                     # Age group limits
labels = ['30 to 39', '40 to 49', '50 to 59', '60 to 69', '70 to 79', '80 and Older']   # Age group labels
lc_data_copy['age_group'] = pd.cut(lc_data_copy.age, bins=bins, labels=labels)

sns.countplot(lc_data_copy, x='age_group', hue='label')
plt.legend(['Non-LC', 'LC'])
plt.title('Age Distribution of Patients With and Without Lung Cancer')
plt.xlabel('Age Group')
plt.ylabel('Patient Count')
plt.show()
plt.close()


# Investigating racial and ethnic makeup of the dataset
# print(lc_data['race'].unique())
white = lc_data.loc[lc_data.race == 'white']
asian = lc_data.loc[lc_data.race == 'asian']
black = lc_data.loc[lc_data.race == 'black']
hawaiian = lc_data.loc[lc_data.race == 'hawaiian']
native = lc_data.loc[lc_data.race == 'native']
other = lc_data.loc[lc_data.race == 'other']
racial_data = [len(white), len(asian), len(black), len(hawaiian), len(native), len(other)]
racial_cats =['White', 'Asian', 'Black', 'Hawaiian', 'Native', 'Other']

plt.figure(figsize=(10,8))
plt.subplot(1, 2, 1)
plt.pie(racial_data, autopct='%0.1f%%', pctdistance=1.2)
plt.legend(racial_cats)
plt.title('Racial Composition of Dataset')
plt.axis('Equal')

white_lc = lc_data.loc[(lc_data.race == 'white') & (lc_data.label == 1)]
asian_lc = lc_data.loc[(lc_data.race == 'asian') & (lc_data.label == 1)]
black_lc = lc_data.loc[(lc_data.race == 'black') & (lc_data.label == 1)]
hawaiian_lc = lc_data.loc[(lc_data.race == 'hawaiian') & (lc_data.label == 1)]
native_lc = lc_data.loc[(lc_data.race == 'native') & (lc_data.label == 1)]
other_lc = lc_data.loc[(lc_data.race == 'other') & (lc_data.label == 1)]
racial_data_lc = [len(white_lc), len(asian_lc), len(black_lc), 
                  len(hawaiian_lc), len(native_lc), len(other_lc)]

plt.subplot(1, 2, 2)
plt.pie(racial_data_lc, autopct='%0.1f%%', pctdistance=1.2)
plt.legend(racial_cats)
plt.title('Racial Composition of Lung Cancer Patients')
plt.axis('Equal')
plt.show()
plt.close()

# print(lc_data['ethnic'].unique())
hispanic = lc_data.loc[lc_data.ethnic == 'hispanic']
nonhispanic = lc_data.loc[lc_data.ethnic == 'nonhispanic']
ethnic_data = [len(hispanic), len(nonhispanic)]
ethnic_cats = ['Hispanic', 'Nonhispanic']

plt.figure(figsize=(10,8))
plt.subplot(1, 2, 1)
plt.pie(ethnic_data, autopct='%0.1f%%', pctdistance=1.2)
plt.legend(ethnic_cats)
plt.title('Ethnic Composition of Dataset')
plt.axis('Equal')

hispanic_lc = lc_data.loc[(lc_data.ethnic == 'hispanic') & (lc_data.label == 1)]
nonhispanic_lc = lc_data.loc[(lc_data.ethnic == 'nonhispanic') & (lc_data.label == 1)]
ethnic_data_lc = [len(hispanic_lc), len(nonhispanic_lc)]

plt.subplot(1, 2, 2)
plt.pie(ethnic_data_lc, autopct='%0.1f%%', pctdistance=1.2)
plt.legend(ethnic_cats)
plt.title('Ethnic Composition of Lung Cancer Patients')
plt.axis('Equal')
plt.show()
plt.close()


# Asking: do lung cancer patients have higher or lower platelet levels than non-LC patients?
ax = sns.violinplot(x=lc_data['label'], y=lc_data['Platelets [#/volume] in Blood by Automated count'])
plt.xlabel('Lung Cancer Status')
ax.set_xticks(range(0,2))
ax.set_xticklabels(['Non-LC', 'LC'])
plt.title('Platelet Levels of Patients With and Without Lung Cancer')
plt.show()
plt.close()


# Asking: do lung cancer patients have higher or lower leukocyte levels than non-LC patients?
ax = sns.violinplot(x=lc_data['label'], y=lc_data['Leukocytes [#/volume] in Blood by Automated count'])
plt.xlabel('Lung Cancer Status')
ax.set_xticks(range(0,2))
ax.set_xticklabels(['Non-LC', 'LC'])
plt.title('Leukocyte Levels of Patients With and Without Lung Cancer')
plt.show()
plt.close()


# Asking: do lung cancer patients have higher or lower RDW levels than non-LC patients?
plt.figure(figsize=(10,8))
ax = sns.violinplot(x=lc_data['label'], y=lc_data['Erythrocyte distribution width [Entitic volume] by Automated count'])
plt.xlabel('Lung Cancer Status')
ax.set_xticks(range(0,2))
ax.set_xticklabels(['Non-LC', 'LC'])
plt.title('Erythrocyte Distribution Width of Patients With and Without Lung Cancer')
plt.show()
plt.close()


# Asking: do lung cancer patients have higher or lower hemoglobin levels than non-LC patients?
ax = sns.violinplot(x=lc_data['label'], y=lc_data['Hemoglobin [Mass/volume] in Blood'])
plt.xlabel('Lung Cancer Status')
ax.set_xticks(range(0,2))
ax.set_xticklabels(['Non-LC', 'LC'])
plt.title('Hemoglobin Levels of Patients With and Without Lung Cancer')
plt.show()
plt.close()


# Asking: do lung cancer patients have higher or lower carbon dioxide levels than non-LC patients?
ax = sns.violinplot(x=lc_data['label'], y=lc_data['Carbon Dioxide'])
plt.xlabel('Lung Cancer Status')
ax.set_xticks(range(0,2))
ax.set_xticklabels(['Non-LC', 'LC'])
plt.title('Carbon Dioxide Levels of Patients With and Without Lung Cancer')
plt.show()
plt.close()


# Asking: do lung cancer patients have higher or lower bilirubin levels than non-LC patients?
# Anomalous outliers for non-LC patients that don't make logical sense, need to filter extreme outliers
bilirubin = lc_data['Bilirubin.total [Mass/volume] in Serum or Plasma'].to_numpy()
q1 = np.nanquantile(bilirubin, 0.25)
q3 = np.nanquantile(bilirubin, 0.75)
iqr = q3 - q1
lc_data.loc[(lc_data['Bilirubin.total [Mass/volume] in Serum or Plasma']>q3+1.5*iqr),'Bilirubin.total [Mass/volume] in Serum or Plasma']=np.nan
lc_data.loc[(lc_data['Bilirubin.total [Mass/volume] in Serum or Plasma']<q1-1.5*iqr),'Bilirubin.total [Mass/volume] in Serum or Plasma']=np.nan
ax = sns.violinplot(x=lc_data['label'], y=lc_data['Bilirubin.total [Mass/volume] in Serum or Plasma'])
plt.xlabel('Lung Cancer Status')
ax.set_xticks(range(0,2))
ax.set_xticklabels(['Non-LC', 'LC'])
plt.ylabel('Total Bilirubin [Mass/volume in Serum or Plasma]')
plt.title('Bilirubin Levels of Patients With and Without Lung Cancer')
plt.show()
plt.close()


# Asking: do lung cancer patients have higher or lower albumin levels than non-LC patients?
ax = sns.violinplot(x=lc_data['label'], y=lc_data['Albumin'])
plt.xlabel('Lung Cancer Status')
ax.set_xticks(range(0,2))
ax.set_xticklabels(['Non-LC', 'LC'])
plt.title('Albumin Levels of Patients With and Without Lung Cancer')
plt.show()
plt.close()


# Chronic viral sinusitis has been previously correlated with lung cancer incidence
# Asking: what proportions of LC and non-LC patients have had viral sinusitis?
vs_pos = lc_data.loc[(lc_data['Viral sinusitis (disorder)'] == True) & (lc_data['label'] == 0)]
vs_neg = lc_data.loc[(lc_data['Viral sinusitis (disorder)'] == False) & (lc_data['label'] == 0)]
vs_data = [len(vs_pos), len(vs_neg)]
vs_cats = ['Positive', 'Negative']

plt.figure(figsize=(12,8))
plt.subplot(1, 2, 1)
plt.pie(vs_data, autopct='%0.1f%%', pctdistance=1.2)
plt.legend(vs_cats)
plt.title('Viral Sinusitis Status of Patients Without Lung Cancer')
plt.axis('Equal')

vs_pos_lc = lc_data.loc[(lc_data['Viral sinusitis (disorder)'] == True) & (lc_data['label'] == 1)]
vs_neg_lc = lc_data.loc[(lc_data['Viral sinusitis (disorder)'] == False) & (lc_data['label'] == 1)]
vs_data_lc = [len(vs_pos_lc), len(vs_neg_lc)]

plt.subplot(1, 2, 2)
plt.pie(vs_data_lc, autopct='%0.1f%%', pctdistance=1.2)
plt.legend(vs_cats)
plt.title('Viral Sinusitis Status of Patients With Lung Cancer')
plt.axis('Equal')
plt.show()
plt.close()


# Looking at blood counts to investigate associations with lung cancer, excluding NaNs
print("Median Platelet Counts for LC and non-LC Patients:", 
      col_LC_nonLC_median(lc_data, 'Platelets [#/volume] in Blood by Automated count'))

print("Median Leukocyte Counts for LC and non-LC Patients:",
      col_LC_nonLC_median(lc_data, 'Leukocytes [#/volume] in Blood by Automated count'))

print("Median Erythrocyte Distribution Width for LC and non-LC Patients:",
      col_LC_nonLC_median(lc_data, 'Erythrocyte distribution width [Entitic volume] by Automated count'))

print("Median Hemoglobin Levels for LC and non-LC Patients:",
      col_LC_nonLC_median(lc_data, 'Hemoglobin [Mass/volume] in Blood'))

print("Median Carbon Dioxide Levels for LC and non-LC Patients:", 
      col_LC_nonLC_median(lc_data, 'Carbon Dioxide'))

print("Median Bilirubin Levels for LC and non-LC Patients, With Outliers Filtered:", 
      col_LC_nonLC_median(lc_data, 'Bilirubin.total [Mass/volume] in Serum or Plasma'))

print("Median Albumin Levels for LC and non-LC Patients:", 
      col_LC_nonLC_median(lc_data, 'Albumin'))
