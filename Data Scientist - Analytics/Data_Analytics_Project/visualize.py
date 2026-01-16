import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from analyst_proj_funs import remove_outliers

lc_data = pd.read_csv('clean_df.csv')
print(lc_data.head(10))
print(lc_data.columns)


# Investigating NHIS tobacco smoking status for LC and non-LC patients
smoke_never = lc_data.loc[(lc_data['Tobacco smoking status NHIS'] == 'never') & (lc_data['label'] == 0)]
smoke_former = lc_data.loc[(lc_data['Tobacco smoking status NHIS'] == 'former') & (lc_data['label'] == 0)]
smoke_data = [len(smoke_never), len(smoke_former)]
smoke_cats = ['Never', 'Former']

plt.figure(figsize=(12,8))
plt.subplot(1, 2, 1)
plt.pie(smoke_data, autopct='%0.1f%%', pctdistance=1.2)
plt.legend(smoke_cats)
plt.title('Smoking Status of Patients Without Lung Cancer')
plt.axis('Equal')

smoke_never_lc = lc_data.loc[(lc_data['Tobacco smoking status NHIS'] == 'never') & (lc_data['label'] == 1)]
smoke_former_lc = lc_data.loc[(lc_data['Tobacco smoking status NHIS'] == 'former') & (lc_data['label'] == 1)]
smoke_data_lc = [len(smoke_never_lc), len(smoke_former_lc)]

plt.subplot(1, 2, 2)
plt.pie(smoke_data_lc, autopct='%0.1f%%', pctdistance=1.2)
plt.legend(smoke_cats)
plt.title('Smoking Status of Patients With Lung Cancer')
plt.axis('Equal')
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
plt.title('Ages of Patients With and Without Lung Cancer')
plt.xlabel('Age Group')
plt.ylabel('Patient Count')
plt.show()
plt.close()

ax = sns.violinplot(x=lc_data['label'], y=lc_data['age'])
plt.xlabel('Lung Cancer Status')
ax.set_xticks(range(0,2))
ax.set_xticklabels(['Non-LC', 'LC'])
plt.title('Age Distribution of Patients With and Without Lung Cancer')
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


# Asking: how does lung cancer patients' platelet count distribution compare to non-LC patients?
platelet_df = remove_outliers(lc_data, 'Platelets [#/volume] in Blood by Automated count')

ax = sns.violinplot(x=platelet_df['label'], y=platelet_df['Platelets [#/volume] in Blood by Automated count'])
plt.xlabel('Lung Cancer Status')
ax.set_xticks(range(0,2))
ax.set_xticklabels(['Non-LC', 'LC'])
plt.title('Platelet Levels of Patients With and Without Lung Cancer')
plt.show()
plt.close()


# Asking: how does lung cancer patients' leukocyte count distribution compare to non-LC patients?
leuk_df = remove_outliers(lc_data, 'Leukocytes [#/volume] in Blood by Automated count')

ax = sns.violinplot(x=leuk_df['label'], y=leuk_df['Leukocytes [#/volume] in Blood by Automated count'])
plt.xlabel('Lung Cancer Status')
ax.set_xticks(range(0,2))
ax.set_xticklabels(['Non-LC', 'LC'])
plt.title('Leukocyte Levels of Patients With and Without Lung Cancer')
plt.show()
plt.close()


# Asking: how does lung cancer patients' RDW distribution compare to non-LC patients?
rdw_df = remove_outliers(lc_data, 'Erythrocyte distribution width [Entitic volume] by Automated count')

plt.figure(figsize=(10,8))
ax = sns.violinplot(x=rdw_df['label'], y=rdw_df['Erythrocyte distribution width [Entitic volume] by Automated count'])
plt.xlabel('Lung Cancer Status')
ax.set_xticks(range(0,2))
ax.set_xticklabels(['Non-LC', 'LC'])
plt.title('Erythrocyte Distribution Width of Patients With and Without Lung Cancer')
plt.show()
plt.close()


# Asking: how does lung cancer patients' hemoglobin level distribution compare to non-LC patients?
hemoglobin_df = remove_outliers(lc_data, 'Hemoglobin [Mass/volume] in Blood')

ax = sns.violinplot(x=hemoglobin_df['label'], y=hemoglobin_df['Hemoglobin [Mass/volume] in Blood'])
plt.xlabel('Lung Cancer Status')
ax.set_xticks(range(0,2))
ax.set_xticklabels(['Non-LC', 'LC'])
plt.title('Hemoglobin Levels of Patients With and Without Lung Cancer')
plt.show()
plt.close()


# Asking: how does lung cancer patients' carbon dioxide level distribution compare to non-LC patients?
co2_df = remove_outliers(lc_data, 'Carbon Dioxide')

ax = sns.violinplot(x=co2_df['label'], y=co2_df['Carbon Dioxide'])
plt.xlabel('Lung Cancer Status')
ax.set_xticks(range(0,2))
ax.set_xticklabels(['Non-LC', 'LC'])
plt.title('Carbon Dioxide Levels of Patients With and Without Lung Cancer')
plt.show()
plt.close()


# Asking: how does lung cancer patients' bilirubin level distribution compare to non-LC patients?
bilirubin_df = remove_outliers(lc_data, 'Bilirubin.total [Mass/volume] in Serum or Plasma')

ax = sns.violinplot(x=bilirubin_df['label'], y=bilirubin_df['Bilirubin.total [Mass/volume] in Serum or Plasma'])
plt.xlabel('Lung Cancer Status')
ax.set_xticks(range(0,2))
ax.set_xticklabels(['Non-LC', 'LC'])
plt.ylabel('Total Bilirubin [Mass/volume in Serum or Plasma]')
plt.title('Bilirubin Levels of Patients With and Without Lung Cancer')
plt.show()
plt.close()


# Asking: how does lung cancer patients' albumin level distribution compare to non-LC patients?
albumin_df = remove_outliers(lc_data, 'Albumin')

ax = sns.violinplot(x=albumin_df['label'], y=albumin_df['Albumin'])
plt.xlabel('Lung Cancer Status')
ax.set_xticks(range(0,2))
ax.set_xticklabels(['Non-LC', 'LC'])
plt.title('Albumin Levels of Patients With and Without Lung Cancer')
plt.show()
plt.close()


# Chronic viral sinusitis has been previously correlated with lung cancer incidence,
# actue, viral sinusitis can cause chronic sinusitis
# Asking: what proportions of LC and non-LC patients have had viral sinusitis?
vs_pos = lc_data['Viral sinusitis (disorder)'].loc[(lc_data['Viral sinusitis (disorder)'] == True) & (lc_data['label'] == 0)]
vs_neg = lc_data['Viral sinusitis (disorder)'].loc[(lc_data['Viral sinusitis (disorder)'] == False) & (lc_data['label'] == 0)]
vs_data = [len(vs_pos), len(vs_neg)]
vs_cats = ['Positive', 'Negative']

plt.figure(figsize=(12,8))
plt.subplot(1, 2, 1)
plt.pie(vs_data, autopct='%0.1f%%', pctdistance=1.2)
plt.legend(vs_cats)
plt.title('Viral Sinusitis Status of Patients Without Lung Cancer')
plt.axis('Equal')

vs_pos_lc = lc_data['Viral sinusitis (disorder)'].loc[(lc_data['Viral sinusitis (disorder)'] == True) & (lc_data['label'] == 1)]
vs_neg_lc = lc_data['Viral sinusitis (disorder)'].loc[(lc_data['Viral sinusitis (disorder)'] == False) & (lc_data['label'] == 1)]
vs_data_lc = [len(vs_pos_lc), len(vs_neg_lc)]

plt.subplot(1, 2, 2)
plt.pie(vs_data_lc, autopct='%0.1f%%', pctdistance=1.2)
plt.legend(vs_cats)
plt.title('Viral Sinusitis Status of Patients With Lung Cancer')
plt.axis('Equal')
plt.show()
plt.close()