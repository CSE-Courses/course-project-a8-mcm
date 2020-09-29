# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 16:46:41 2020

@author: Ralph
"""

import unittest
from webscrape import *

class TestWebScape(unittest.TestCase):

    # Testing the get_url fucntion
    def test_url(self):
        self.assertEqual(get_url("csco"),
                         'https://finance.yahoo.com/quote/csco/history?p=csco&tsrc=find-tre-srch')    
    
    # Testing the current_price function
    def test_current_price(self):
        self.assertEqual(current_price(
            "https://finance.yahoo.com/quote/csco/history?p=csco&tsrc=find-tre-srch"), '39.26')
        
    def test_not_current_price(self):
        self.assertNotEqual(current_price(
            "https://finance.yahoo.com/quote/csco/history?p=csco&tsrc=find-tre-srch"), '40')
        
    def test_current_price_error(self):
        self.assertEqual(current_price(
            "https://finance.yahoo.com/quote/agaij/history?p=agaij&tsrc=find-tre-srch"),
            "Error. Can't find stock name. Make sure name is correct.")
        
    def test_no_error_current_price(self):
        self.assertNotEqual(current_price(
            "https://finance.yahoo.com/quote/csco/history?p=csco&tsrc=find-tre-srch"),
            "Error. Can't find stock name. Make sure name is correct.")
    
    # Testing getting the header of a yahoo finance table    
    def test_get_header(self):
        self.assertEqual(get_header(
            "https://finance.yahoo.com/quote/csco/history?p=csco&tsrc=find-tre-srch"),
            ['Date', 'Open', 'High', 'Low', 'Close*', 'Adj Close**', 'Volume'])
        
    # Testing getting the data from the table by testing one row
    def test_get_data(self):
        data = get_data("https://finance.yahoo.com/quote/csco/history?p=csco&tsrc=find-tre-srch")
        self.assertEqual(data[2],
                         ['Sep 25, 2020', '37.76', '38.54', '37.62', '38.45', '38.45', '22,966,600'])
        
    # Testing data with no dividends
    # This test compares original data to a filtered one where it doesn't show dividends in table
    def test_og_to_nodivs(self):
        original_data = get_data("https://finance.yahoo.com/quote/csco/history?p=csco&tsrc=find-tre-srch")
        no_divs = get_data_nodiv("https://finance.yahoo.com/quote/csco/history?p=csco&tsrc=find-tre-srch")
        self.assertNotEqual(no_divs, original_data)
        
    def test_no_divs(self):
        no_divs = get_data_nodiv("https://finance.yahoo.com/quote/csco/history?p=csco&tsrc=find-tre-srch")
        self.assertEqual(no_divs[1],
                         ['Sep 28, 2020', '39.20', '39.29', '38.79', '39.13', '39.13', '24,239,500'])
        
    # Testing the dates
    def test_dates(self):
        dates = get_data_date("https://finance.yahoo.com/quote/csco/history?p=csco&tsrc=find-tre-srch")
        self.assertEqual(dates[0], 'Sep 29, 2020')
        
    # Testing opening prices
    def test_csco_open_prices(self):
        open_price = get_data_open("https://finance.yahoo.com/quote/csco/history?p=csco&tsrc=find-tre-srch")
        self.assertEqual(open_price[1], '39.20')
        
    def test_aapl_open_prices(self):
        open_price = get_data_open("https://finance.yahoo.com/quote/aapl/history?p=aapl&tsrc=find-tre-srch")
        self.assertEqual(open_price[1], '115.01')
        
    # Testing Closing Prices
    def test_csco_close_prices(self):
        close_price = get_data_close("https://finance.yahoo.com/quote/csco/history?p=csco&tsrc=find-tre-srch")
        self.assertEqual(close_price[1], '39.13')
        
    def test_aapl_close_price(self):
        close_price = get_data_close("https://finance.yahoo.com/quote/aapl/history?p=aapl&tsrc=find-tre-srch")
        self.assertEqual(close_price[1], '114.96')
        
    # Test getting the company name
    def test_csco_company_name(self):
        self.assertEqual(get_company_name(
            "https://finance.yahoo.com/quote/csco/history?p=csco&tsrc=find-tre-srch"), 
            "Cisco Systems, Inc. (CSCO)")
        
    def test_aapl_company_name(self):
        self.assertEqual(get_company_name(
            "https://finance.yahoo.com/quote/aapl/history?p=aapl&tsrc=find-tre-srch"), 
            "Apple Inc. (AAPL)")
        
    # Test getting the high prices
    def test_csco_high_prices(self):
        high = get_data_high("https://finance.yahoo.com/quote/csco/history?p=csco&tsrc=find-tre-srch")
        self.assertEqual(high[1], '39.29')
        
    def test_aapl_high_prices(self):
        high = get_data_high("https://finance.yahoo.com/quote/aapl/history?p=aapl&tsrc=find-tre-srch")
        self.assertEqual(high[1], '115.32')
        
    # Test getting the low prices
    def test_csco_low_prices(self):
        low = get_data_low("https://finance.yahoo.com/quote/csco/history?p=csco&tsrc=find-tre-srch")
        self.assertEqual(low[1], '38.79')
        
    def test_aapl_low_prices(self):
        low = get_data_low("https://finance.yahoo.com/quote/aapl/history?p=aapl&tsrc=find-tre-srch")
        self.assertEqual(low[1], '112.78')
        
    # Test getting adjclose prices
    def test_csco_adjprices(self):
        adj = get_data_adjclose("https://finance.yahoo.com/quote/csco/history?p=csco&tsrc=find-tre-srch")
        self.assertEqual(adj[1], '39.13')
        
    def test_aapl_adjprices(self):
        adj = get_data_adjclose("https://finance.yahoo.com/quote/aapl/history?p=aapl&tsrc=find-tre-srch")
        self.assertEqual(adj[1], '114.96')
        
            
if __name__ == '__main__':
    unittest.main()