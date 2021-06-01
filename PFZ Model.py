import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
# from sklearn.metrics import r2_score,mean_squared_error


#Data Preprocessing -- Turning data into required useful data

df = pd.read_csv("C:\\Users\\user\\Desktop\\Projects\\Minor Project - 2\\Dataset\PFE.csv")
df= df[df.Volume!=0]
df = df.reset_index(drop=True)
df = df.drop(np.where(np.isnan(df['Volume'].to_numpy().astype('float32')))[0])
df = df.reset_index(drop=True)

rows = df.shape[0]
columns = df.shape[1]

df["Open-Close"] = df["Open"] - df["Close"]   # Open - Close
df["High-Low"] = df["High"] - df["Low"]       # High - Low

# 7 day Moving Average
df["7DMA"]=0.000000
for i in range(6,rows):
    df["7DMA"][i] = (df["Close"][i]+df["Close"][i-1]+df["Close"][i-2]+df["Close"][i-3]+df["Close"][i-4]+df["Close"][i-5]+df["Close"][i-6])/7

#21 Day Moving Average
df["21DMA"]=0.000000
for i in range(20,rows):
    df["21DMA"][i] = (df["Close"][i]+df["Close"][i-1]+df["Close"][i-2]+df["Close"][i-3]+df["Close"][i-4]+df["Close"][i-5]+df["Close"][i-6]+df["Close"][i-7]+df["Close"][i-8]+df["Close"][i-9]+df["Close"][i-10]+df["Close"][i-11]+df["Close"][i-12]+df["Close"][i-13]+df["Close"][i-14]+df["Close"][i-15]+df["Close"][i-16]+df["Close"][i-17]+df["Close"][i-18]+df["Close"][i-19]+df["Close"][i-20])/21
    
# 7 day Standard Deviation
import math
df["7DSD"]=0.000000
for i in range(6,rows):
    sum = 0.000000
    for j in range(7):
        sum = sum + (df["Close"][i-j] - df["7DMA"][i])**2
    df["7DSD"][i] = math.sqrt(sum/7)

ndf = df.copy()
ndf = ndf.drop(0)
ndf = ndf.reset_index(drop=True)
df["Next"] = ndf.Close

df = df.drop(columns=['Open','High','Close','Adj Close','Low'])
ndf = df[df['21DMA']!=0]
ndf = ndf.drop(rows-1)
ndf = ndf.reset_index(drop=True)


# Forming Dependent and Independent variables x and y

X = ndf[['Date','Volume','Open-Close','High-Low','7DMA','21DMA','7DSD']].to_numpy()
y = ndf['Next'].to_numpy()
x = X[:,1:]

# Data Splitting into Training and Testing data

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.1, random_state = 0)
x_train = X_train[:,1:]
x_test = X_test[:,1:]

# Regression Model

regressor = RandomForestRegressor(n_estimators = 500, random_state = 0)
regressor.fit(x_train, y_train)

#saving model to disk
import pickle

pickle.dump(regressor,open('C:\\Users\\user\\Desktop\\Projects\\Minor Project - 2\\Deployment\PFZ model.pkl','wb'))