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
    closeLine(stock):
        Converts the stock data into a csv file. Then read data into a dataframe using panda. It reverses the
        table data to have the oldest date at the top and newest at the bottom. Then it will save the line graph of close 
        as a line.png.
"""

def closeLine(stock):
    url = get_url(stock)
    write_to_csv(url)
    df = pd.read_csv('output.csv', index_col=0, parse_dates=True)
    df = df.reindex(index=df.index[::-1])
    df.plot(y="Close", ylabel="Price", figsize=(10,8), title=get_company_name(url), rot=90)
    plt.savefig("line.png")
    
"""
    candleStick(stock):
        Converts the stock data into a csv file. Then read data into a dataframe using panda. It reverses the
        table data to have the oldest date at the top and newest at the bottom. Then it will save the candlestick 
        graph as a candlestick.png.
"""
def candleStick(stock):
    url = get_url(stock)
    write_to_csv(url)
    df = pd.read_csv('output.csv', index_col=0, parse_dates=True)
    df = df.reindex(index=df.index[::-1])
    mpf.plot(df, type='candle', style='charles', title=get_company_name(url), ylabel="Price", savefig="candlestick.png")
    