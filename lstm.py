# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 16:09:53 2020

@author: Ralph
"""
# Importing libraries
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, Dropout, LSTM
from graphs import readTableDate
import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create Dataframe
def dataFunc(stock):
    df = readTableDate(stock)
    data = df.sort_index(ascending=False, axis=0)
    return data

def newDataFunc(stock):
    df = dataFunc(stock)
    newData = pd.DataFrame(index=range(0, len(df)), columns=["Date", "Close"])

    for i in range(0, len(df)):
        newData["Date"][len(df)-i-1] = df["Date"][i]
        newData["Close"][len(df)-i-1] = df["Close"][i]
    
    # Setting Index
    newData.index = newData.Date
    newData.drop("Date", axis=1, inplace=True)
    
    return newData

def lstmForecast(stock):
    df = readTableDate(stock)
    data = dataFunc(stock)
    # Creating train and test sets
    newData = newDataFunc(stock)
    dataset = newData.values

    train = dataset

    # Convert dataset into xTrain and yTrain
    lookBack= 30
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaledData = scaler.fit_transform(dataset)

    xTrain, yTrain = [], []
    for i in range(lookBack, len(train)):
        xTrain.append(scaledData[i-lookBack:i,0])
        yTrain.append(scaledData[i,0])
    xTrain, yTrain = np.array(xTrain), np.array(yTrain)

    xTrain = np.reshape(xTrain, (xTrain.shape[0], xTrain.shape[1], 1))

    # Create and fit the LSTM network
    model = Sequential()
    model.add(LSTM(units=50, return_sequences=True, input_shape=(xTrain.shape[1],1)))
    model.add(LSTM(units=50))
    model.add(Dense(1))

    model.compile(loss='mean_squared_error', optimizer='adam')
    model.fit(xTrain, yTrain, epochs=1, batch_size=1, verbose=2) 
    
    # Predict new data
    days = 7
    predictionList = dataset[-lookBack:]
    for i in range(days):
        x = predictionList[-lookBack:]
        x = np.array(x).astype('float64')
        x = x.reshape((1, lookBack, 1))
        out = model.predict(x)
        out = scaler.inverse_transform(out)
        predictionList = np.append(predictionList, out)
    predictionList = predictionList[lookBack-1:]

    # Prediction Dates
    lastDate = df['Date'].values[-1]
    predictionDates = pd.date_range(lastDate, periods=8).tolist()
    i=0
    for date in predictionDates:
        dateTimeObj = datetime.datetime.strptime(str(date), '%Y-%m-%d %H:%M:%S')
        predictionDates[i] = str(dateTimeObj.date())
        i+=1

    # Prediction Dataframe
    prediction = pd.DataFrame(index=range(0, len(predictionDates)-1), columns=["Date", "Close"])
    for i in range(0,days):
        prediction["Date"][i] = predictionDates[i+1]
        prediction["Close"][i] = predictionList[i+1]

    data = data.append(prediction, ignore_index=True)
    data.index = data.Date
    data.drop("Date", axis=1, inplace=True)
    
    return data