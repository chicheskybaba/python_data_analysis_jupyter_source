
# importing modules and libraries

from dateutil.parser import parse

import matplotlib as mpl

import matplotlib.pyplot as plt

import seaborn as sns

import numpy as np

import pandas as pd

plt.rcParams.update({'figure.figsize': (10, 7), 'figure.dpi': 120})



# Import as Dataframe

df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/a10.csv', parse_dates=['date'])

df.head()

print (df.head())





# dataset source: https://github.com/rouseguy

df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/MarketArrivals.csv')

df = df.loc[df.market=='MUMBAI', :]

df.head()

print (df.head())





# 1. Visualizing a time series with dataset residing on external server

df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/a10.csv', parse_dates=['date'], index_col='date')

# Draw Plot

def plot_df(df, x, y, title="", xlabel='Date', ylabel='Value', dpi=100):

    plt.figure(figsize=(16,5), dpi=dpi)

    plt.plot(x, y, color='tab:red')

    plt.gca().set(title=title, xlabel=xlabel, ylabel=ylabel)

    plt.show()


plot_df(df, x=df.index, y=df.value, title='Monthly anti-diabetic drug sales in Australia from 1992 to 2008.')






# 2. Visualizing another time series with dataset residing on local disk

# import data

df = pd.read_csv(r'C:\Users\Oluwaseun Alade\Documents\SOFTWARE\PYTHON\multiTimeline4.csv', parse_dates=['date'])

x = df['date'].values

y = df['value'].values



# Draw Plot

def plot_df(df, x, y, title="", xlabel='date', ylabel='value', dpi=100):

    plt.figure(figsize=(16,5), dpi=dpi)

    plt.plot(x, y, color='tab:blue')

    plt.gca().set(title=title, xlabel=xlabel, ylabel=ylabel)

    plt.show()


plot_df(df, x=df.index, y=df.value, title='Air Passengers (Two Side View.')





# 3. Seasonal Plot of a Time Series


# Import Data

df = pd.read_csv(r'C:\Users\Oluwaseun Alade\Documents\SOFTWARE\PYTHON\a12.txt', parse_dates=['date'], index_col='date')

df.reset_index(inplace=True)

df['year'] = [d.year for d in df.date]

df['month'] = [d.strftime('%b') for d in df.date]

years = df['year'].unique()


# Prep Colors

np.random.seed(100)

mycolors = np.random.choice(list(mpl.colors.XKCD_COLORS.keys()), len(years), replace=False)



# Draw Plot

plt.figure(figsize=(16,12), dpi= 80)

for i, y in enumerate(years):
    
    if i > 0:
        
        plt.plot('month', 'value', data=df.loc[df.year==y, :], color=mycolors[i], label=y)
        
        plt.text(df.loc[df.year==y, :].shape[0]-.9, df.loc[df.year==y, 'value'][-1:].values[0], y, fontsize=12, color=mycolors[i])


# Decoration

plt.gca().set(xlim=(-0.3, 11), ylim=(2, 30), ylabel='$Drug Sales$', xlabel='$Month$')

plt.yticks(fontsize=12, alpha=.7)

plt.title("Seasonal Plot of Drug Sales Time Series", fontsize=20)

plt.show()





# 4. Let Us do Boxplot of Month-wise (Seasonal) and Year-wise (trend) Distribution

# Import Data

df = pd.read_csv(r'C:\Users\Oluwaseun Alade\Documents\SOFTWARE\PYTHON\a12.txt', parse_dates=['date'], index_col='date')

df.reset_index(inplace=True)


# Prepare data

df['year'] = [d.year for d in df.date]

df['month'] = [d.strftime('%b') for d in df.date]

years = df['year'].unique()


# Draw Plot

fig, axes = plt.subplots(1, 2, figsize=(20,7), dpi= 80)

sns.boxplot(x='year', y='value', data=df, ax=axes[0])

sns.boxplot(x='month', y='value', data=df.loc[~df.year.isin([1991, 2008]), :])


# Set Title

axes[0].set_title('Year-wise Box Plot\n(The Trend)', fontsize=18);

axes[1].set_title('Month-wise Box Plot\n(The Seasonality)', fontsize=18)

plt.show()





# 5. Patterns in a time series


# Any time series may be split into the following components: Base Level + Trend + Seasonality + Error


# A trend is observed when there is an increasing or decreasing slope observed in the time series.

# Seasonality is observed when there is a distinct repeated pattern observed between regular intervals due to seasonal factors.

# Seasonality could be because of the month of the year, the day of the month, weekdays or even time of the day.

# However, It is not mandatory that all time series must have a trend and/or seasonality.

# A time series may not have a distinct trend but have a seasonality. The opposite can also be true.

# So, a time series may be imagined as a combination of the trend, seasonality and the error terms.



# Let us do patterns in a time series for dataset that resides on server

fig, axes = plt.subplots(1,3, figsize=(20,4), dpi=100)


pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/guinearice.csv', parse_dates=['date'], index_col='date').plot(title='Trend Only', legend=False, ax=axes[0])


pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/sunspotarea.csv', parse_dates=['date'], index_col='date').plot(title='Seasonality Only', legend=False, ax=axes[1])


pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/AirPassengers.csv', parse_dates=['date'], index_col='date').plot(title='Trend and Seasonality', legend=False, ax=axes[2])


plt.show()



# Let us do patterns in a time series for dataset that resides on local hard disk

fig, axes = plt.subplots(1,3, figsize=(20,4), dpi=100)


pd.read_csv(r'C:\Users\Oluwaseun Alade\Documents\SOFTWARE\PYTHON\a12.txt', parse_dates=['date'], index_col='date').plot(title='Trend Only', legend=False, ax=axes[0])


pd.read_csv(r'C:\Users\Oluwaseun Alade\Documents\SOFTWARE\PYTHON\a12.txt', parse_dates=['date'], index_col='date').plot(title='Seasonality Only', legend=False, ax=axes[1])


pd.read_csv(r'C:\Users\Oluwaseun Alade\Documents\SOFTWARE\PYTHON\a12.txt', parse_dates=['date'], index_col='date').plot(title='Trend and Seasonality', legend=False, ax=axes[2])


plt.show()


