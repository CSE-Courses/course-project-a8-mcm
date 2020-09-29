# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 16:25:58 2020

@author: Ralph
Webscraping finance.yahoo.com
"""
import requests
import csv
from bs4 import BeautifulSoup

"""
    get_url(stock):
        Looks up the url that was given as an arugment. The argument has to be a string.
        Will return the url for webscraping.
"""
def get_url(stock):
    base_url = "https://finance.yahoo.com/quote/"
    # Get input of the stock that needs to be looked up. Most likely will be changed
    url = base_url + stock + "/history?p=" + stock + "&tsrc=find-tre-srch"
    return url.lower()

"""
    current_price(url):
        Checks yahoo finance for current price of desired stock.
"""
def current_price(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'lxml')
    results = soup.find('span', class_ = 'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)')
    if results is None:
        return "Error. Can't find stock name. Make sure name is correct."
    else:
        for price in results:
            return price
        
"""
    history_data(url):
        Requests access to yahoo finance history table and returns the table in
        text. This function is used for table manipulations.
"""
def history_data(url):
    page = requests.get(url).text
    soup = BeautifulSoup(page, 'lxml')
    history_table = soup.find('table', class_='W(100%) M(0)')
    
    return history_table

"""
    get_header(url):
        Uses history_data(url) function and return a list of headers.
"""
def get_header(url):
    history_table = history_data(url)
    history_table_heading = history_table.thead.find_all("tr")
    
    headings = []
    for heading in history_table_heading:
        headings.append(heading.get_text(separator='| '))
    headings = headings[0].split('| ')
    return headings

"""
    get_data(url):
        Uses history_data(url) function to get the body data and store each 
        row as a sublist. Returns a list.
"""
def get_data(url):
    history_table = history_data(url)
    history_table_data = history_table.tbody.find_all("tr")
    datas = []
    nice_data = []
    
    for data in history_table_data:
        datas.append(data.get_text(separator='| '))
    for data in datas:
        nice_data.append(data.split('| '))
    return nice_data

"""
    get_data_nodiv(url):
        Returns a list of data that doesn't include dividends.
"""
def get_data_nodiv(url):
    nice_data = get_data(url)
    no_div = []
    
    for data in nice_data:
        if (data[3] =='Dividend'):
            continue
        else:
            no_div.append(data)
    return no_div

"""
    get_data_date(url):
        Uses get_data_nodiv(url) function to get all the dates the data 
        provides from get_data_nodiv(url). Returns a list of date prices.
"""
def get_data_date(url):
    nice_data = get_data_nodiv(url)
    dates = []
    
    for data in nice_data:
        dates.append(data[0])
    return dates

"""
    get_data_open(url):
        Uses get_data_nodiv(url) function to get all the open prices of the data 
        provided. Returns a list of open prices.
"""
def get_data_open(url):
    nice_data = get_data_nodiv(url)
    open_price = []
    
    for data in nice_data:
        open_price.append(data[1])
    return open_price

"""
    get_data_close(url):
        Uses get_data_nodiv(url) function to get all the close prices of the data 
        provided. Returns a list of closing prices.
"""
def get_data_close(url):
    nice_data = get_data_nodiv(url)
    close_price = []
    
    for data in nice_data:
        close_price.append(data[4])
    return close_price

"""
    get_data_high(url):
        Uses get_data_nodiv(url) function to get all the high open prices of the data 
        provided. Returns a list of high prices.
"""
def get_data_high(url):
    nice_data = get_data_nodiv(url)
    high_price = []
    
    for data in nice_data:
        high_price.append(data[2])
    return high_price

"""
    get_data_low(url):
        Uses get_data_nodiv(url) function to get all the low prices of the data 
        provided. Returns a list of low prices.
"""
def get_data_low(url):
    nice_data = get_data_nodiv(url)
    low_price = []
    
    for data in nice_data:
        low_price.append(data[3])
    return low_price

"""
    get_data_adjclose(url):
        Uses get_data_nodiv(url) function to get all the adjclose prices of the data 
        provided. Returns a list of adjusted closing prices.
"""
def get_data_adjclose(url):
    nice_data = get_data_nodiv(url)
    adjclose = []
    
    for data in nice_data:
        adjclose.append(data[5])
    return adjclose

"""
    get_data_vol(url):
        Uses get_data_nodiv(url) function to get all the volumes of the data 
        provided. Returns a list of volume prices.
"""
def get_data_vol(url):
    nice_data = get_data_nodiv(url)
    vol_price = []
    
    for data in nice_data:
        vol_price.append(data[6])
    return vol_price

"""
    get_company_name(url):
        Will return the company name of the stock that was searched in url.
"""
def get_company_name(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'lxml')
    results = soup.find('h1', class_ = 'D(ib) Fz(18px)')
    for name in results:
        return name
    