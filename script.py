import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns

data = pd.read_csv('/kaggle/input/lifeexpectancygdp/all_data.csv')
data.dropna()

plt.figure(figsize=(11,8))
ax = sns.barplot(data = data, x='Country', y='Life expectancy at birth (years)')
ax.set_title('Average life expectancy in each country')

plt.figure(figsize=(11,8))
ax = sns.boxplot(data = data, x='Country', y='Life expectancy at birth (years)')
ax.set_title('Average life expectancy in each country')

plt.figure(figsize=(11,8))
ax = sns.barplot(data = data, x='Country', y='GDP')
ax.set_title('Average GDP in each country')

plt.figure(figsize=(11,8))
sns.boxplot(data=data, x='Country', y='GDP')

chile = data[data['Country'] == 'Chile']
china = data[data['Country'] == 'China']
german = data[data['Country'] == 'Germany']
mexico = data[data['Country'] == 'Mexico']
usa = data[data['Country'] == 'United States of America']
zimbabwe = data[data['Country'] == 'Zimbabwe']

plt.figure(figsize=(10, 5))
ax1 = plt.subplot(2, 3, 1)
plt.scatter(chile['Life expectancy at birth (years)'], chile.GDP)
ax1.set_title('Chile')
plt.ylabel('GDP in Trillions of U.S. Dollars')
plt.subplots_adjust(wspace= .2, hspace= 0.5)

ax2 = plt.subplot(2, 3, 2)
plt.scatter(china['Life expectancy at birth (years)'], china.GDP, color='red')
ax2.set_title('China')

ax3 = plt.subplot(2, 3, 3)
plt.scatter(german['Life expectancy at birth (years)'], german.GDP, color='yellow')
ax3.set_title('Germany')

ax4 = plt.subplot(2, 3, 4)
plt.scatter(mexico['Life expectancy at birth (years)'], mexico.GDP, color='green')
ax4.set_title('Mexico')
plt.ylabel('GDP in Trillions of U.S. Dollars')
plt.xlabel('Life Expectancy at birth (years)')
plt.subplots_adjust(hspace= 0.5)

ax5 = plt.subplot(2, 3, 5)
plt.scatter(usa['Life expectancy at birth (years)'], usa.GDP, color='black')
ax5.set_title('United States of America')
plt.xlabel('Life Expectancy at birth (years)')

ax6 = plt.subplot(2, 3, 6)
plt.scatter(zimbabwe['Life expectancy at birth (years)'], zimbabwe.GDP, color='brown')
ax6.set_title('Zimbabwe')
plt.xlabel('Life Expectancy at birth (years)')
