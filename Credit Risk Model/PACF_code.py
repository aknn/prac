import pandas as pd
from sklearn import linear_model


#Read the data into a pandas DataFrame
df = pd.read_csv('southern_osc.csv', header=0, infer_datetime_format=True, parse_dates=[0], index_col=[0])

#add two columns containing the LAG=1 and LAG=2 version of the data to the DataFrame
df['T_(i-1)'] = df['T_i'].shift(1)
df['T_(i-2)'] = df['T_i'].shift(2)
#drop the top two rows as they contain NaNs after shifting
df = df.drop(df.index[[0,1]])

#fit a linear regression model on T_i and T_i-1 and add it's predictions to the DataFrame as a new column
lm = linear_model.LinearRegression()
df_X = df[['T_(i-1)']] #Note the double brackets! [[]]
df_y = df['T_i'] #Note the single brackets! []
model = lm.fit(df_X,df_y)
df['Predicted_T_i|T_(i-1)'] = lm.predict(df_X)

#create the time series of residuals corresponding to the predictions of this model and add it to the DataFrame.
# This gives us the first one of the two time series we need for calculating the PACF for X at LAG=2
#Observed minus predicted
df['Residual_T_i|T_(i-1)'] = df['T_i'] – df['Predicted_T_i|T_(i-1)']

#repeat the above procedure to calculate the second time series of residuals
lm = linear_model.LinearRegression()
df_X = df[['T_(i-1)']] #Note the double brackets! [[]]
df_y = df['T_(i-2)'] #Note the single brackets! []
model = lm.fit(df_X,df_y)
df['Predicted_T_(i-2)|T_(i-1)'] = lm.predict(df_X)
#Observed minus predicted
df['Residual_T_(i-2)|T_(i-1)'] = df['T_(i-2)'] – df['Predicted_T_(i-2)|T_(i-1)']

#Finally, apply the formula for Pearson's r to the two time series of residuals to get the value of the PACF at LAG=2
print(df.corr(method='pearson')['Residual_T_i|T_(i-1)']['Residual_T_(i-2)|T_(i-1)'])
#prints: 0.29612303554627606

#or cheat, like so:
from statsmodels.tsa.stattools import pacf
print(pacf(df['T_i'], nlags=2)[2])
#prints: 0.2996545841351261