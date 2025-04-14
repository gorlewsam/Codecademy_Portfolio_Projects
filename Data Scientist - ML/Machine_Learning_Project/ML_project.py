import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from collections import Counter
from imblearn.over_sampling import RandomOverSampler
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix 
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score

profiles = pd.read_csv('/portfolio_ML_project_starter/profiles.csv')
print(profiles.head())
print(profiles.columns)

# End Goal: Predicting a user's smoking status based on other variables

######### Investigating distribution of responses for the 'smokes' column #########
print("Number of Categories:",profiles.smokes.nunique())
print("Categories:", profiles.smokes.unique())
print(profiles.smokes.value_counts())
print("Number of NaN values:", profiles.smokes.isna().sum())


######### Investigating distribution of variables, namely age, income, sex, body type, diet, religion,
# drinking status, pet ownership status, and zodiac sign #########
# Cleaning religion and zodiac sign categories
profiles['religionCleaned'] = profiles.religion.str.split().str.get(0)
profiles['signCleaned'] = profiles.sign.str.split().str.get(0)

# Age broken down by sex
sns.displot(data=profiles, x="age", hue="sex", kind="hist", binwidth = 5, multiple = "stack")
plt.title("Distribution of Users' Ages, Broken Down by Sex")
plt.show()
plt.close()

# Income broken down by sex
sns.displot(data=profiles, x="income", hue="sex", kind="hist", binwidth = 50000, multiple = "stack")
plt.title("Distribution of Users' Incomes, Broken Down by Sex")
plt.show()
plt.close()

# Number of people belonging to each sex
sns.countplot(data=profiles, y="sex")
plt.title("Number of Users Belonging to Each Sex")
plt.show()
plt.close()

# Distribution of users' body types
sns.countplot(data=profiles, y="body_type")
plt.title("Distribution of Users' Body Types")
plt.show()
plt.close()

# Ditribution of users' diets
sns.countplot(data=profiles, y="diet")
plt.title("Distribution of Users' Diets")
plt.show()
plt.close()

# Distribution of users' religions
sns.countplot(data=profiles, y="religionCleaned")
plt.title("Distribution of Users' Religions")
plt.show()
plt.close()

# Distribution of drinking status
sns.countplot(data=profiles, y="drinks")
plt.title("Distribution of Users' Drinking Status")
plt.show()
plt.close()

# Distribution of pet ownership status
sns.countplot(data=profiles, y="pets")
plt.title("Distribution of Users' Pet Ownership Status")
plt.show()
plt.close()

# Distribution of users' zodiac signs
sns.countplot(data=profiles, y='signCleaned')
plt.title("Distribution of Users' Zodiac Signs")
plt.show()
plt.close()

# Distribution of smoking status
sns.countplot(data=profiles, y="smokes")
plt.title("Distribution of Users' Smoking Status")
plt.show()
plt.close()


######### Preprocessing data #########
cols = ['sex', 'body_type', 'diet', 'religionCleaned', 'drinks', 'pets', 'signCleaned', 'smokes']
df = profiles[cols].dropna()
print(df.shape)

# Encoding categorical variables
for col in cols[:-1]:
    df = pd.get_dummies(df, columns=[col], prefix = [col])
print(df.head())

X = df.iloc[:, 1:]
y = df.iloc[:, 0:1]

# Label encoding so y can be undersampled to deal with class imbalance
le = LabelEncoder()
y = le.fit_transform(y)
labels = le.classes_

# Printing how many samples there are for each class after the NaN removal
counter = Counter(y)
for k,v in counter.items():
	per = v / len(y) * 100
	print('Class=', k, 'n=', v)

# Oversampling to deal with class imbalance
strategy = {0:12892, 1:12892, 2:12892, 3:12892, 4:12892}
undersample = RandomOverSampler(sampling_strategy=strategy, random_state=0)
X, y = undersample.fit_resample(X, y)

# Ensuring that the class distributions are equal
counter = Counter(y)
for k,v in counter.items():
	per = v / len(y) * 100
	print('Class=', k, 'n=', v)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state = 0)


######### Model building #########
dt = DecisionTreeClassifier()

model = dt.fit(X_train, y_train)
print("\nDecision Tree Depth:", model.get_depth())

y_pred = dt.predict(X_test)

print("\n", classification_report(y_test, y_pred))

# Plotting confusion matrix of test set and predicted classes
cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(14,14))
ax= plt.subplot()
sns.heatmap(cm, annot=True, ax=ax, fmt="d")

ax.set_xlabel('Predicted labels')
ax.set_ylabel('True labels')
ax.set_title('Confusion Matrix for Smoker Status Classification')
ax.yaxis.set_tick_params(rotation=360)
ax.xaxis.set_tick_params(rotation=90)
ax.xaxis.set_ticklabels(labels)
ax.yaxis.set_ticklabels(labels)

plt.show()
plt.close()

# Performing a 5-fold CV to test how well the decision tree model generalizes to other datasets
kfold = KFold(n_splits=5, shuffle=True, random_state=0)
results = cross_val_score(model, X_test, y_test, cv=kfold, scoring='accuracy')

print(results)
print("Baseline accuracy: %.2f%% (%.2f%%)" % (results.mean()*100, results.std()*100))