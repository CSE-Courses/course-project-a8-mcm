# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 16:46:41 2020

@author: Ralph
"""

import unittest
from webscrape import *

class TestCurrentPrice(unittest.TestCase):

    #Testing the get_url fucntion
    def test_url(self):
        self.assertEqual(get_url(),
                         'https://finance.yahoo.com/quote/csco/history?p=csco&tsrc=find-tre-srch')    
    
    #Testing the current_price function
    def test_current_price(self):
        self.assertEqual(current_price(
            "https://finance.yahoo.com/quote/csco/history?p=csco&tsrc=find-tre-srch"), '38.28')
        
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
            
if __name__ == '__main__':
    unittest.main()