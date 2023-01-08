# check prophet version

import prophet as fbprophet

# print version number

print ('prophet %s' % fbprophet.__version__)



# load the car sales dataset

from pandas import read_csv

# load data

path = 'https://raw.githubusercontent.com/jbrownlee/Datasets/master/monthly-car-sales.csv'

df = read_csv(path, header=0)

# summarize shape

print(df.shape)

# show first few rows

print(df.head(10))



# load and plot the car sales dataset

from pandas import read_csv

from matplotlib import pyplot

# load data

path = 'https://raw.githubusercontent.com/jbrownlee/Datasets/master/monthly-car-sales.csv'

df = read_csv(path, header=0)

# plot the time series

df.plot()

pyplot.show()



# fit prophet model on the car sales dataset

from pandas import read_csv
from pandas import to_datetime


# load data

path = 'https://raw.githubusercontent.com/jbrownlee/Datasets/master/monthly-car-sales.csv'

df = read_csv(path, header=0)

# prepare expected column names

df.columns = ['ds', 'y']

df['ds']= to_datetime(df['ds'])

# define the model

model = prophet()

# fit the model

model.fit(df)


