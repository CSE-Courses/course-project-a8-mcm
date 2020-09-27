# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 16:25:58 2020

@author: Ralph
Webscraping finance.yahoo.com
"""
import requests
from bs4 import BeautifulSoup

"""
    get_url():
        Asks user for stock they want to look up. Will return the url for 
        webscraping.
"""
def get_url():
    base_url = "https://finance.yahoo.com/quote/"
    # Get input of the stock that needs to be looked up
    stock = input("Type name of stock to look up: ")
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
        
print(current_price("https://finance.yahoo.com/quote/agaij/history?p=agaij&tsrc=find-tre-srch"))
        