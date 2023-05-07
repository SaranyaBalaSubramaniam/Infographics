# -*- coding: utf-8 -*-
"""
Created on Thu May  4 21:04:10 2023

@author: ADMIN
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from matplotlib import gridspec

df = pd.read_csv("Weather_data.csv")
# Set seaborn style
sns.set(style="whitegrid")

# Creating a GridSpec layout
fig = plt.figure(figsize=(20, 15))
my_grid = gridspec.GridSpec(4, 2, figure=fig)

# Plot 1: Lineplot of AvgTemperature by Year (with error bands)
df_line = fig.add_subplot(my_grid[0, 0])
sns.lineplot(data=df, x='year', y='AvgTemperature',
             ci='sd', ax=df_line)
df_line.set_xlabel('Years', fontsize=15, fontfamily='serif')
df_line.set_ylabel('Temperature', fontsize=15, fontfamily='serif')
df_line.set_title('Average Temperature by Years with error',
                  fontsize=16, fontfamily='serif')

# Plot 1: Density plot of Avgerage Temperature by state
df_den = fig.add_subplot(my_grid[0, 1])
for state in df['state'].unique():
    sns.kdeplot(df[df['state'] == state]
                ['AvgTemperature'], label=state, ax=df_den)
df_den.set_xlabel('Avg Temp', fontsize=15, fontfamily='serif')
df_den.set_ylabel('Density', fontsize=15, fontfamily='serif')
df_den.set_title('State-wise climate dispersion',
                 fontsize=16, fontfamily='serif')
df_den.legend()

# Plot 3: Barplot of Average Temperature by state
df_bar = fig.add_subplot(my_grid[1, 0])
county_temp = df.groupby('state')['AvgTemperature'].mean().reset_index()
sns.barplot(data=county_temp, x='state',
            y='AvgTemperature', palette='RdYlBu', ax=df_bar, edgecolor='black')
df_bar.set_xlabel('States in USA', fontsize=15, fontfamily='serif')
df_bar.set_ylabel('Temperature', fontsize=15, fontfamily='serif')
df_bar.set_title('State-wise Average Temperature',
                 fontsize=16, fontfamily='serif')
df_bar.set_xticklabels(df_bar.get_xticklabels(), fontfamily='serif')

# Plot 4 Scatter plot of Average Temperature by month of year (colored by year)
df_scat = fig.add_subplot(my_grid[1, 1])
sns.scatterplot(data=df, x='month', y='AvgTemperature',
                palette='RdYlBu', hue='year', ax=df_scat)
df_scat.set_xlabel('Months', fontsize=15, fontfamily='serif')
df_scat.set_ylabel('Temperature', fontsize=15, fontfamily='serif')
df_scat.set_title('Temperature by month of year',
                  fontsize=16, fontfamily='serif')

# Plot 5: Boxplot of Avgerage Temperature by Month
df_box = fig.add_subplot(my_grid[2, :])
sns.boxplot(data=df, x='month', y='AvgTemperature',
            palette='RdYlBu', ax=df_box)
df_box.set_xlabel('Months', fontsize=15, fontfamily='serif')
df_box.set_ylabel('Temperature', fontsize=15, fontfamily='serif')
df_box.set_title('Monthly Average Temperature',
                 fontsize=16, fontfamily='serif')

fig.suptitle(
    'Weather Report of USA\nStudent Name : Saranya Bala Subramaniam\nID : 22033095',
    fontsize=22, fontfamily='serif')

# Adding textbox for explaination
explanation = '''
The climate's variation and fluctuations over the states, months, and years are shown on this report:
 Plot 1 - Average Temperature by Year with Error: The line graph displays the average temperature trends by year and 
          has error bands that illustrate the standard deviation.
 Plot 2 - State-level Weather Variance: This density map displays the temperature dispersion at the region- level.
 Plot 3 - Average Temperature for the State: The average temperature for the counties is displayed in this bar graph.
 Plot 4 - The average temperature for each month of the year is shown on this scatter plot, which is color-coded according to the year.
 Plot 5 - Monthly Average Temperature: This box plot illustrates the variation in monthly average temperatures.
'''

# Setting position of the textbox
textbox = plt.figtext(0.2, 0.05, explanation, fontsize=16, wrap=True, bbox=dict(
    facecolor='beige', edgecolor='black', boxstyle='sawtooth,pad=1'))

plt.tight_layout()
plt.subplots_adjust(top=0.9)
plt.savefig('22033095.png', dpi=300)
