from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('/home/samorc/anaconda3/envs/codecademy/portfolio_data_vis_project_starter_files/Life-Expectancy-and-GDP-Starter/all_data.csv')
print(df.head())
df = df.rename(columns={"Life expectancy at birth (years)":"LEABY"})
print(df.head())

# Finding mean life expectancy and GDP for each country for the period between 2000 - 2015
df_Means = df.drop('Year', axis = 1).groupby('Country').mean().reset_index()
print(df_Means)
sns.barplot(x='GDP', y='Country', data=df_Means)
plt.xlabel("GDP in U.S. Dollars")
plt.show()
plt.clf()

sns.barplot(x='LEABY', y='Country', data=df_Means)
plt.xlabel("Life Expectancy at Birth (years)")
plt.show()
plt.clf()

# Showing the relationship between life expectancy and time for the countries in the dataset
sns.lineplot(data=df, x='Year', y='LEABY', hue='Country', marker='o')
plt.xlabel("Year")
plt.ylabel("Life Expectancy at Birth (years)")
ax = plt.subplot()
ax.set_xticks(range(2000, 2016))
plt.show()
plt.clf()

# Showing the relationship between GDP and time for the countries in the dataset
sns.lineplot(data=df, x='Year', y='GDP', hue='Country', marker='o')
plt.xlabel("Year")
plt.ylabel("GDP in U.S. Dollars")
ax = plt.subplot()
ax.set_xticks(range(2000, 2016))
plt.show()
plt.clf()

# Showing the relationship between GDP and life expectancy for each country
graph = sns.FacetGrid(df, col='Country', col_wrap=3, hue = 'Country', sharey = False, sharex = False)
graph = (graph.map(sns.scatterplot, 'LEABY', 'GDP') .add_legend() .set_axis_labels("Life Expectancy at Birth (years)", "GDP in U.S. Dollars"))
plt.show()
plt.clf()