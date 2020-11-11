# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 17:22:32 2020

@author: Ralph
"""
# Import webscraped data 
from webscrape import *

# Importing numpy and panda packages
import numpy as np
import pandas as pd

# Data Visualization
import matplotlib.pyplot as plt
import mplfinance as mpf

"""
    def readTable(string stock):
        Uses stock to get the url and write the data to csv. Reads all the headers and reverses the order to have newest at bottom
        and oldest data on top.
"""
def readTable(stock):
    url = get_url(stock)
    write_to_csv(url)
    
    df = pd.read_csv('output.csv', index_col=0, parse_dates=True)
    df = df.reindex(index=df.index[::-1])
    return df

"""
    def readTableClose(string stock):
        Uses the stock string to get the url to write data webscraped into a csv table. Reverses the csv table to have oldest
        date at top and newest date at bottom. Only reads the closing data.
"""
def readTableClose(stock):
    url = get_url(stock)
    write_to_csv(url)

    df = pd.read_csv('output.csv', index_col=0, parse_dates=True, usecols = ["Date", "Close"])
    df = df.reindex(index=df.index[::-1])
    return df

"""
    closeLine(stock):
        Converts the stock data into a csv file. Then read data into a dataframe using panda. It reverses the
        table data to have the oldest date at the top and newest at the bottom. Then it will save the line graph of close 
        as a line.png.
"""
def closeLine(stock):
    df = readTableClose(stock)
    df.plot(y="Close", ylabel="Price", figsize=(10,8), title = get_company_name(get_url(stock)), rot=90)
    plt.savefig("line.png")
    
"""
    candleStick(stock):
        Converts the stock data into a csv file. Then read data into a dataframe using panda. It reverses the
        table data to have the oldest date at the top and newest at the bottom. Then it will save the candlestick 
        graph as a candlestick.png.
"""
def candleStick(stock):
    df = readTable(stock)
    mpf.plot(df, type='candle', style='charles', title=get_company_name(get_url(stock)), ylabel="Price", savefig="candlestick.png")
    
"""
    def MACD(string stock):
        Takes in a string to be useds on the function read table which then can be used to calculations
        for MACD. It gets the exponential moving average and calculates the signal line and shows when to
        buy or put. When MACD line crosses over signal line than buy else put.
"""
def MACD(stock):
    df = readTableClose(stock)
    
    exp1 = df.ewm(span=12, adjust=False).mean()
    exp2 = df.ewm(span=26, adjust=False).mean()

    macd = exp1 - exp2
    exp3 = macd.ewm(span=9, adjust=False).mean()

    plt.figure(figsize=(10,8))
    plt.xticks(rotation=90)
    plt.plot(macd, label="MACD", color = '#DB33FF')
    plt.plot(exp3, label='Signal Line', color='#33DFFF')
    plt.legend(loc='upper left')
    plt.savefig("macd.png")
