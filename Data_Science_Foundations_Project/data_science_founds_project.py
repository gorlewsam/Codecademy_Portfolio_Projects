import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import chi2_contingency
from itertools import chain
import string
import seaborn as sns

species = pd.read_csv('portfolio_biodiversity_starter_files/species_info.csv', encoding='utf-8')
observs = pd.read_csv('portfolio_biodiversity_starter_files/observations.csv', encoding='utf-8')

print(species.head())
print(observs.head())

# Examining the species dataset
print(f"\nNumber of species:{species.scientific_name.nunique()}")
print(f"Number of categories:{species.category.nunique()}")
print(f"Categories:{species.category.unique()}")
print("Number of species in each category:", species.groupby("category").size())

print(f"\nNumber of conservation statuses:{species.conservation_status.nunique()}")
print(f"Unique conservation statuses:{species.conservation_status.unique()}")
print(f"Number of NaN values:{species.conservation_status.isna().sum()}")
print("Number of species under each conservation status:", species.groupby("conservation_status").size())

# Examining the observations dataset
print(f"\nNumber of parks:{observs.park_name.nunique()}")
print(f"Unique parks:{observs.park_name.unique()}")

print(f"\nNumber of observations:{observs.observations.sum()}")

# Replacing NaN values with "Least Concern"
species.fillna('Least Concern', inplace=True)
print("\nNumber of species under each conservation status:", species.groupby("conservation_status").size())

# Examining the categories of species that are not labeled "Least Concern"
conservationCat = species[species.conservation_status != "Least Concern"]\
    .groupby(["conservation_status", "category"])['scientific_name'].count().unstack()
print(conservationCat)

ax = conservationCat.plot(kind = 'bar', figsize=(8, 12), stacked=True)
ax.set_xlabel("Conservation Status")
ax.set_ylabel("Number of Species")
plt.show()
plt.clf()

# Examining if certain types of species are more likely to be in conservation
species['protected'] = species.conservation_status != 'Least Concern'

cat_counts = species.groupby(['category', 'protected']).scientific_name.nunique().reset_index()\
                        .pivot(columns='protected', index='category', values='scientific_name').reset_index()
cat_counts.columns = ['category', 'not_protected', 'protected']
print("\n", cat_counts)

cat_counts['percent_protected'] = cat_counts.protected / (cat_counts.protected + cat_counts.not_protected)*100
print("\n", cat_counts)

# Asking: Mammals and birds are most likely to be "Protected";
# Is there a statistically significant difference in conservation status rates between the two groups?

# Format of [[mammal_not_protected, mammal_protected], [bird_not_protected, bird_protected]]
mammal_bird_contingency = [[146, 30], 
                           [413, 75]]
print(chi2_contingency(mammal_bird_contingency))

# Amphibians are the next most likely to be "Protected" after mammals and birds;
# Is there a statistically significant difference in conservation status rates between amphibians and birds?

# Format of [[amphibian_not_protected, amphibian_protected], [bird_not_protected, bird_protected]]
amphibian_bird_contingency = [[72, 7], 
                              [413, 75]]
print(chi2_contingency(amphibian_bird_contingency))

# Examining which group of mammal species is most prevalent 
def remove_punc(str):
    for punctuation in string.punctuation:
        str = str.replace(punctuation, '')
    return str

# Removing all punctuation
commonNames = species[species.category == "Mammal"].common_names\
    .apply(remove_punc)\
    .str.split().tolist()

print(commonNames[:6])

# Removing duplicate words within each row
cleanRows = []
for item in commonNames:
    item = list(dict.fromkeys(item))
    cleanRows.append(item)
    
print(cleanRows[:6])

# Converting species list of lists into one single list
single_list = list(chain.from_iterable(i if isinstance(i, list) else [i] for i in cleanRows))
print(single_list[:6])

# Counting the occurrences of each type of animal
words_counted = []
for i in single_list:
    x = single_list.count(i)
    words_counted.append((i,x))

# Top 5 most observed species
print(pd.DataFrame(set(words_counted), columns =['Word', 'Count']).sort_values("Count", ascending = False).head())

# There are several different types of shrews;
# Identifying which rows in species refer to shrews
species['is_shrew'] = species.common_names.str.contains(r"\bShrew\b", regex = True)
print("\n", species.loc[species['is_shrew'] == True])

# Merging shrew observations with the observs df
shrew_observs = observs.merge(species[species.is_shrew])
print("\n", shrew_observs)

# Checking how many times shrews have been observed in each of the four parks
print("Number of shrew sightings for each park:\n", 
      shrew_observs.groupby('park_name').observations.sum().reset_index())

# Examining number of protected shrew sightings vs non-protected shrew sightings
protect_obs_by_park = shrew_observs.groupby(['park_name', 'protected']).observations.sum().reset_index()
print(protect_obs_by_park)

plt.figure(figsize=(15, 10))
sns.barplot(x=protect_obs_by_park.park_name, y= protect_obs_by_park.observations, hue=protect_obs_by_park.protected)
plt.xlabel('National Parks')
plt.ylabel('Number of Observations')
plt.title('Observations of Shrews per Week')
plt.show()
plt.clf()