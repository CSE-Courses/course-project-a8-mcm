# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 16:46:41 2020

@author: Ralph
"""

import unittest
from webscrape import *

class TestCurrentPrice(unittest.TestCase):

    def test_url(self):
        self.assertEqual(get_url(),
                         'https://finance.yahoo.com/quote/csco/history?p=csco&tsrc=find-tre-srch')    
        
    
    def test_current_price(self):
        self.assertEqual(current_price(
            "https://finance.yahoo.com/quote/csco/history?p=csco&tsrc=find-tre-srch"), '39.04')
        
    def test_not_current_price(self):
        self.assertNotEqual(current_price(
            "https://finance.yahoo.com/quote/csco/history?p=csco&tsrc=find-tre-srch"), '40')
            
if __name__ == '__main__':
    unittest.main()