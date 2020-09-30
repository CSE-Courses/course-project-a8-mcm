#stockList=["GILD","WMT","UNP", "UTX","HPQ", "V", "CSCO", "SLB", "AMGN", "BA", "TGT", "COP", "CMCSA", "BMY", "CVX", "VZ", "BP", "T", "UNH", "MCD", "PFE", "ABT", "FB", "DIS", "MMM", "XOM", "ORCL", "PEP","HD", "JPM", "INTC", "WFC", "MRK", "KO", "AMZN", "PG", "BRKB","GOOGL", "GM", "JNJ", "MO", "IBM", "GE", "MSFT", "AAPL","NVDA", "AMD", "GE", "NTDOF", "SNE"]

from webscrape import *
import pygame
from pygame.locals import *

"""

Input:stockName (string)

Return: bool

Given a stok name will attempt to webscrape to its page, if sucessfull
it will return True. If unsucessfull it will return false

"""
def search(stockName):
    url = get_url(stockName.lower())
    print(url)
    if current_price(url) == "Error. Can't find stock name. Make sure name is correct.":
        print("Stock not Found")
        return False
    else:
        print("Stock Full Name: " + get_company_name(url))
        return True

"""

Return: Search Bar Button (pygame.Rect), Search Bar Font (pygame.font)

Initializes the GUI structures for the search bar

"""
def searchBarInitalize():
    searchBarButton=pygame.Rect(200,10,1000,70)
    font=pygame.font.Font("../course-project-a8-mcm/Fonts/times.ttf",50)
    return searchBarButton,font



"""

Event handler for Search bar. On key press will delete a char from search bar text if char was \b 
Otherwise will add char to the search bar text

"""
def updateSearchBarOnKeyPress(theGuiEvent, searchBarText ):
    if theGuiEvent.unicode=="\b":
        return searchBarText[:-1]
        
    elif theGuiEvent.unicode.isalpha()  and len(searchBarText)<=10 or theGuiEvent.unicode.isdigit() and len(searchBarText)<=10 :
        return searchBarText+theGuiEvent.unicode
    else:
        if len(searchBarText)>=10:
            print("max length of string reached")

        return searchBarText


