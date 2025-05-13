import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Loading and examining data
lc_data = pd.read_csv('data_analyst_final_portfolio/LungCancerData.csv')
print(lc_data.head())
print(lc_data.columns)
#print(lc_data.isnull().sum())  #Checking for null values


# Asking: what perent of patients in this dataset have lung cancer?
non_lc_patients = lc_data.loc[lc_data.label == 0]
lc_patients = lc_data.loc[lc_data.label == 1]
prop_non_lc = len(non_lc_patients) / len(lc_data)
prop_lc = len(lc_patients) / len(lc_data)
print('{:.1%} of patients in this dataset have lung cancer, and {:.1%} do not.'.format(prop_lc, prop_non_lc))


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
plt.clf()


# Investiating BMI distribution of patients with and without lung cancer
plt.hist(non_lc_patients['Body Mass Index'], range=(20,50), bins=15, alpha=0.5)
plt.hist(lc_patients['Body Mass Index'], range=(20,50), bins=15, alpha=0.5)
plt.legend(['Non-LC', 'LC'])
plt.title('BMI Distribution of Patients With and Without Lung Cancer')
plt.ylabel('Patient Count')
plt.show()
plt.clf()

# Grouping BMI into weight categories
lc_data_copy = lc_data.copy(deep=True)
bins = [15, 18.5, 25, 30, 50]                                        #Weight class limits
labels = ['Underweight', 'Healthy Weight', 'Overweight', 'Obese']    #Weight class labels
lc_data_copy['BMI_group'] = pd.cut(lc_data_copy['Body Mass Index'], bins=bins, labels=labels)

sns.countplot(lc_data_copy, x='BMI_group', hue='label')
plt.legend(['Non-LC', 'LC'])
plt.title('BMI Classes of Patients With and Without Lung Cancer')
plt.xlabel('BMI Class')
plt.ylabel('Patient Count')
plt.show()
plt.clf()


# Investigating racial and ethnic makeup of the dataset
#print(lc_data['race'].unique())
white = lc_data.loc[lc_data.race == 'white']
asian = lc_data.loc[lc_data.race == 'asian']
black = lc_data.loc[lc_data.race == 'black']
hawaiian = lc_data.loc[lc_data.race == 'hawaiian']
native = lc_data.loc[lc_data.race == 'native']
other = lc_data.loc[lc_data.race == 'other']
racial_data = [len(white), len(asian), len(black), len(hawaiian), len(native), len(other)]
racial_cats =['White', 'Asian', 'Black', 'Hawaiian', 'Native', 'Other']
plt.pie(racial_data, autopct='%0.1f%%', pctdistance=1.2)
plt.legend(racial_cats)
plt.title('Racial Composition of Dataset')
plt.axis('Equal')
plt.show()
plt.clf()

#print(lc_data['ethnic'].unique())
hispanic = lc_data.loc[lc_data.ethnic == 'hispanic']
nonhispanic = lc_data.loc[lc_data.ethnic == 'nonhispanic']
ethnic_data = [len(hispanic), len(nonhispanic)]
ethnic_cats = ['Hispanic', 'Nonhispanic']
plt.pie(ethnic_data, autopct='%0.1f%%', pctdistance=1.2)
plt.legend(ethnic_cats)
plt.title('Ethnic Composition of Dataset')
plt.axis('Equal')
plt.show()
plt.clf()


# Investigating which sex has a higher percentage of lung cancer patients
male_lc_patients = lc_patients.loc[lc_patients.gender == 'm']
female_lc_patients = lc_patients.loc[lc_patients.gender == 'f']
prop_male_lc = len(male_lc_patients) / len(lc_patients)
prop_female_lc = len(female_lc_patients) / len(lc_patients)
print('{:.1%} of lung cancer patients in this dataset are male, and {:.1%} are female.'.format(prop_male_lc, prop_female_lc))


# Investigating whether or not LC patients have higher triglycerides than non-LC patients
lc_data_fewer_tri_outliers = lc_data[lc_data['Triglycerides'] < 250]
ax = sns.boxplot(x=lc_data_fewer_tri_outliers['label'], y=lc_data_fewer_tri_outliers['Triglycerides'])
ax.set_xticks(range(0,2))
ax.set_xticklabels(['Non-LC', 'LC'])
plt.title('Triglyceride Levels of Patients With and Without Lung Cancer')
plt.show()
plt.clf()


# Asking: do lung cancer patients have higher or lower leukocyte levels than non-LC patients?
ax = sns.boxplot(x=lc_data['label'], y=lc_data['Leukocytes [#/volume] in Blood by Automated count'])
ax.set_xticks(range(0,2))
ax.set_xticklabels(['Non-LC', 'LC'])
plt.title('Leukocyte Levels of Patients With and Without Lung Cancer')
plt.show()
plt.clf()


# Asking: do lung cancer patients have higher or lower platelet levels than non-LC patients?
ax = sns.boxplot(x=lc_data['label'], y=lc_data['Platelets [#/volume] in Blood by Automated count'])
ax.set_xticks(range(0,2))
ax.set_xticklabels(['Non-LC', 'LC'])
plt.title('Platelet Levels of Patients With and Without Lung Cancer')
plt.show()
plt.clf()


# Asking: do lung cancer patients have higher or lower erythrocyte levels than non-LC patients?
ax = sns.boxplot(x=lc_data['label'], y=lc_data['Erythrocytes [#/volume] in Blood by Automated count'])
ax.set_xticks(range(0,2))
ax.set_xticklabels(['Non-LC', 'LC'])
plt.title('Erythrocyte Levels of Patients With and Without Lung Cancer')
plt.show()
plt.clf()


# Investigating correlation between heart rate and respiratory rate for LC and non-LC patients
fig, ax = plt.subplots(1, 1)
sns.regplot(x=non_lc_patients['Respiratory rate'], y=non_lc_patients['Heart rate'],
            scatter_kws={'color': 'orange'}, line_kws={'color': 'red'}, label='Non-LC')
sns.regplot(x=lc_patients['Respiratory rate'], y=lc_patients['Heart rate'],
            scatter_kws={'color': 'green'}, line_kws={'color': 'blue'}, label='LC')
ax.legend()
ax.set(xlabel='Respiratory Rate', ylabel='Heart Rate')
plt.show()
plt.clf()
