# 1 
# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# load rankings data
wood_coasters = pd.read_csv('portfolio_roller_coaster_vis_starter_files/Golden_Ticket_Award_Winners_Wood.csv')
print(wood_coasters.head())

# load rankings data
steel_coasters = pd.read_csv('portfolio_roller_coaster_vis_starter_files/Golden_Ticket_Award_Winners_Steel.csv')
print(steel_coasters.head())

# 2
# Create a function to plot rankings over time for 1 roller coaster
def plot_coaster_rank(df, coaster_name, park_name):
  coaster_ranking = df[(df['Name'] == coaster_name) & (df['Park'] == park_name)]
  ax = plt.subplot()
  ax.plot(coaster_ranking['Year of Rank'], coaster_ranking['Rank'])
  ax.set_xticks(coaster_ranking['Year of Rank'].values)
  ax.set_yticks(coaster_ranking['Rank'].values)
  ax.invert_yaxis()
  plt.title("{} Ranking".format(coaster_name))
  plt.xlabel('Year')
  plt.ylabel('Ranking')
  plt.show()
  plt.close()
  return

# 3
# Create a plot of El Toro ranking over time
plot_coaster_rank(wood_coasters, 'El Toro', 'Six Flags Great Adventure')
plt.clf()

# Create a plot of El Toro and Boulder dash hurricanes
def plot_2_coaster_ranks(df, coaster_1_name, park_1_name, coaster_2_name, park_2_name):
  coaster_1_rankings = df[(df['Name'] == coaster_1_name) & (df['Park'] == park_1_name)]
  coaster_2_rankings = df[(df['Name'] == coaster_2_name) & (df['Park'] == park_2_name)]

  ax = plt.subplot()
  ax.plot(coaster_1_rankings['Year of Rank'], coaster_1_rankings['Rank'], color='green', label=coaster_1_name)
  ax.plot(coaster_2_rankings['Year of Rank'], coaster_2_rankings['Rank'], color='red', label=coaster_2_name)
  ax.invert_yaxis()
  plt.title("{} vs {} Rankings".format(coaster_1_name,coaster_2_name))
  plt.xlabel('Year')
  plt.ylabel('Ranking')
  plt.legend()
  plt.show()
  plt.close()
  return

plot_2_coaster_ranks(wood_coasters,'El Toro','Six Flags Great Adventure','Boulder Dash','Lake Compounce')
plt.clf()

# 4
# Create a function to plot top n rankings over time
def plot_top_n(df, n):
  top_n_rankings = df[df['Rank'] <= n]

  ax = plt.subplot()
  
  for coaster in set(top_n_rankings['Name']):
    coaster_ranking = top_n_rankings[top_n_rankings['Name'] == coaster]
    ax.plot(coaster_ranking['Year of Rank'], coaster_ranking['Rank'], label=coaster)

  ax.set_yticks([i for i in range(1,6)])
  ax.invert_yaxis()
  plt.title("Top {} Coaster Rankings".format(str(n)))
  plt.xlabel('Year')
  plt.ylabel('Ranking')
  plt.legend(loc=4)
  plt.show()
  plt.close()
  return

# Create a plot of top n rankings over time
plot_top_n(wood_coasters, 5)
plt.clf()

# 5
# load roller coaster data
coasters = pd.read_csv('portfolio_roller_coaster_vis_starter_files/roller_coasters.csv')
print(coasters.head())

# 6
# Create a function to plot histogram of column values
def plot_hist(df, col_name):
  plt.hist(df[col_name].dropna())
  plt.title('Histogram of Roller Coaster {}'.format(col_name))
  plt.xlabel(col_name)
  plt.ylabel('Count')
  plt.show()
  plt.close()
  return

# Create histogram of roller coaster speed
plot_hist(coasters, 'speed')

# Create histogram of roller coaster length
plot_hist(coasters, 'length')

# Create histogram of roller coaster number of inversions
plot_hist(coasters, 'num_inversions')

# Create a function to plot histogram of height values
def plot_hist_height(df):
  # Removing outliers and missing values
  heights = df[df['height'] <= 200]['height'].dropna()
  plt.hist(heights)
  plt.title('Histogram of Roller Coaster Height')
  plt.xlabel('Height')
  plt.ylabel('Count')
  plt.show()
  plt.close()
  return

# Create a histogram of roller coaster height
plot_hist_height(coasters)

# 7
# Create a function to plot inversions by coaster at park
def plot_num_inversions(df, park_name):
  park_coasters = df[df['park'] == park_name]
  coaster_names = park_coasters['name']
  num_invs = park_coasters['num_inversions']

  ax = plt.subplot()
  plt.bar(range(len(num_invs)), num_invs)
  ax.set_xticks(range(len(coaster_names)))
  ax.set_xticklabels(coaster_names, rotation=90)
  plt.title('Number of Inversions Per Coaster at {}'.format(park_name))
  plt.xlabel('Roller Coaster')
  plt.ylabel('Number of Inversions')
  plt.show()
  plt.close()
  return

# Create barplot of inversions by roller coasters
plot_num_inversions(coasters, 'Six Flags Great Adventure')
plt.clf()

# 8
# Create a function to plot a pie chart of status.operating
def plot_op_status(df):
  working_coasters = df[df['status'] == 'status.operating']
  nonfunc_coasters = df[df['status'] == 'status.closed.definitely']
  status_counts = [len(working_coasters), len(nonfunc_coasters)]

  plt.pie(status_counts, autopct='%0.1f%%', labels=['Operating', 'Closed'])
  plt.title('Roller Coaster Operating Status')
  plt.axis('Equal')
  plt.show()
  plt.close()
  return

# Create pie chart of roller coasters
plot_op_status(coasters)
plt.clf()

# 9
# Create a function to plot scatter of any two columns
def scatter_plot(df, col_x, col_y):
  plt.scatter(df[col_x], df[col_y])
  plt.title('Scatter Plot of {} vs. {}'.format(col_y, col_x))
  plt.xlabel(col_x)
  plt.ylabel(col_y)
  plt.show()
  plt.close
  return

# Create a function to plot scatter of speed vs height
def plot_speed_vs_height(df):
  # Removing outliers
  df = df[df['height'] <= 200]

  plt.scatter(df['height'], df['speed'])
  plt.title('Scatter Plot of Coaster Speed vs. Height')
  plt.xlabel('Height')
  plt.ylabel('Speed')
  plt.show()
  plt.clf()
  return

# Create a scatter plot of roller coaster height by speed
plot_speed_vs_height(coasters)
plt.clf()

# 10
# Create a pie chart of seating type popularity
def plot_seating(df):
  df = df.dropna(subset=['seating_type'])
  seats = df['seating_type'].value_counts()
  mask = df['seating_type'].isin(seats[seats < 50].index)
  df.loc[mask, 'seating_type'] = 'Other'
  print(df['seating_type'].value_counts())

  plt.pie(df.seating_type.value_counts(), autopct='%0.1f%%', labels=['Sit Down', 'Other', 'Spinning', 'Inverted', 'Suspended'])
  plt.title('Roller Coaster Seating Types')
  plt.axis('Equal')
  plt.show()
  plt.close()
  return

# Create pie chart of roller coasters
plot_seating(coasters)
plt.clf()