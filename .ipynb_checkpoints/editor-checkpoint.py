import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt


# import Training Dataset

df = pd.read_csv (r'C:\Users\Oluwaseun Alade\Documents\SOFTWARE\PYTHON\carstraining.csv')

# print Training Dataset

print (df)


# Develop Regression Model (Linear Regression in this case)

X = df[['Weight', 'Volume']]

y = df['CO2']


regr = linear_model.LinearRegression()
regr.fit(X, y)


# Predict Data based on Testing Dataset

predicted1_CO2 = regr.predict([[1523, 1600]])

print (predicted1_CO2)


predicted2_CO2 = regr.predict([[1705, 2000]])

print (predicted2_CO2)


predicted3_CO2 = regr.predict([[1605, 2100]])

print (predicted3_CO2)


predicted4_CO2 = regr.predict([[1746, 2000]])

print (predicted4_CO2)


predicted5_CO2 = regr.predict([[1235, 1600]])

print (predicted5_CO2)


predicted6_CO2 = regr.predict([[1390, 1600]])

print (predicted6_CO2)


predicted7_CO2 = regr.predict([[1405, 1600]])

print (predicted7_CO2)


predicted8_CO2 = regr.predict([[1395, 2500]])

print (predicted8_CO2)


# import Testing Dataset

dt = pd.read_csv (r'C:\Users\Oluwaseun Alade\Documents\SOFTWARE\PYTHON\carstesting.csv')

print (dt)


# import Combined Dataset

dc = pd.read_csv (r'C:\Users\Oluwaseun Alade\Documents\SOFTWARE\PYTHON\combined.csv')

print (dc)


# Let us calculate the r-squared, mean_absolute_error, and mean_squared_error


from sklearn.metrics import r2_score , mean_absolute_error, mean_squared_error


y = [109, 114, 115, 117, 104, 108, 109, 120]

ypred = [108.333469, 112.600589, 113.284153, 117.567681, 100.56463, 107.44022, 109.42818, 121.86591]

r2 = r2_score(y,ypred)

print ("r_squared = " , r2)









