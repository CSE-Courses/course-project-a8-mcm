# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 16:34:20 2020

@author: Ralph
"""
from lstm import lstmForecast, newDataFunc
import matplotlib.pyplot as plt

"""
    def MACD(string stock):
        Takes in a string to be useds on the function read table which then can be used to calculations
        for MACD. It gets the exponential moving average and calculates the signal line and shows when to
        buy or put. When MACD line crosses over signal line than buy else put.
"""
def MACD(stock):
    df = lstmForecast(stock)
    
    exp1 = df.ewm(span=12, adjust=False).mean()
    exp2 = df.ewm(span=26, adjust=False).mean()

    macd = exp1 - exp2
    exp3 = macd.ewm(span=9, adjust=False).mean()

    plt.figure(figsize=(16,8))
    plt.xticks(rotation=90)
    plt.plot(macd, label="MACD", color = '#DB33FF')
    plt.plot(exp3, label='Signal Line', color='#33DFFF')
    plt.legend(loc='upper left')
    return(plt.savefig("macd.png"))

def futureLine(stock):
    newData = newDataFunc(stock)
    data = lstmForecast(stock)
    old = len(newData) - 1
    prev = data[:old]
    pred = data[old:]
    plt.figure(figsize=(16,8))
    plt.xticks(rotation=90)
    plt.plot(prev['Close'])
    plt.plot(pred['Close'])
    return(plt.savefig("lstm.png"))