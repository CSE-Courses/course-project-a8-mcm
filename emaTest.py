# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 13:55:06 2020

@author: Ralph
"""
from graphs import *
import pandas as pd
import unittest

class TestEMA(unittest.TestCase):    
    #Test span of 12 for 2 days
    def testspan12days2(self):
        df = readTable("csco")
        self.assertEqual(round(df.ewm(span=12, adjust=False).mean()["Close"][1], 5), 45.38769)
        
    #test span of 12 for 3 days
    def testspan12days3(self):
        df = readTable("csco")
        self.assertEqual(round(df.ewm(span=12, adjust=False).mean()["Close"][2], 5), 45.50497)
    
    #Test span of 26 for 2 days
    def testspan26days2(self):
        df = readTable("csco")
        self.assertEqual(round(df.ewm(span=26, adjust=False).mean()["Close"][1], 5), 45.30074)
        
    #Test span of 26 for 3 days
    def testspan26days3(self):
        df = readTable("csco")
        self.assertEqual(round(df.ewm(span=26, adjust=False).mean()["Close"][2], 5), 45.36365)
    
if __name__ == '__main__':
    unittest.main()
