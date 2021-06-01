# Stock-Market-Closing-Price-Prediction

We have used historical data of Reliance Industries Limited and Pfizer Inc. Stocks to predict the next day closing price of these Stocks.

# Data Preprocessing
We have used new variables from the existing variables to predict the price.
1. Open - Close (O - C)
2. High - Low (H - L)
3. Volume traded
4. 7 day Moving Average of Stock Price (7DMA)
5. 21 day Moving Average of Stock Price (21DMA)
6. 7 day Standard Deviation (7SD)

# Model Training
For comparative analysis we have used 3 regression techniques and evaluated them on the basis os R2, RMSE, MAPE and MBE.
1. Polynomial Regression
2. Support Vector Regression
3. Random Forest Regression

# Prediction
We have used an API of alphavantage to get the real time data and modify the data according to the requirements to get the new features for prediction

# Deployment
We have used Flask to deploy the project and saved the model in pkl file so that we don't need to run the model again and again.
