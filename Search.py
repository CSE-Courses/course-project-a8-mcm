#stockList=["GILD","WMT","UNP", "UTX","HPQ", "V", "CSCO", "SLB", "AMGN", "BA", "TGT", "COP", "CMCSA", "BMY", "CVX", "VZ", "BP", "T", "UNH", "MCD", "PFE", "ABT", "FB", "DIS", "MMM", "XOM", "ORCL", "PEP","HD", "JPM", "INTC", "WFC", "MRK", "KO", "AMZN", "PG", "BRKB","GOOGL", "GM", "JNJ", "MO", "IBM", "GE", "MSFT", "AAPL","NVDA", "AMD", "GE", "NTDOF", "SNE"]

from webscrape import *
import pygame
from pygame.locals import *
import time

"""

Input:stockName (string)

Return: bool

Given a stok name will attempt to webscrape to its page, if sucessfull
it will return True. If unsucessfull it will return false

"""
# Variable that holds stockName
# stkName = ""


def search(stockName):
    url = get_url(stockName.lower())
    print(url)
    price=current_price(url)
    if price == "Error. Can't find stock name. Make sure name is correct." or price==None:
        print("Stock not Found")
        return False
    else:
        print(current_price(url))
        print("THIS IS THECURRENT PRIce")
        print("Stock Full Name: " + get_company_name(url))
        # stockName = get_company_name(url)
        t = time.localtime()
        currentTime = time.strftime("%H:%M:%S", t)
        print(get_company_name(url) + "Stock Data Updated at " + currentTime)
        return True


"""

Return: Search Bar Button (pygame.Rect), Search Bar Font (pygame.font)

Initializes the GUI structures for the search bar

"""


def searchBarInitalize():
    searchBarButton = pygame.Rect(200, 10, 1000, 70)
    font = pygame.font.Font("../course-project-a8-mcm/Fonts/times.ttf", 50)
    timeFont = pygame.font.Font("../course-project-a8-mcm/Fonts/times.ttf", 30)
    favFont = pygame.font.Font("../course-project-a8-mcm/Fonts/times.ttf", 60)
    companyFont = pygame.font.Font(
        "../course-project-a8-mcm/Fonts/times.ttf", 50)
    t = time.localtime()
    currentTime = time.strftime("%H:%M:%S", t)
    updatedTime = "Stock Data Updated at " + currentTime
    return searchBarButton, font, updatedTime, timeFont, companyFont, favFont


"""

Event handler for Search bar. On key press will delete a char from search bar text if char was \b 
Otherwise will add char to the search bar text

"""


def updateSearchBarOnKeyPress(theGuiEvent, searchBarText):
    if theGuiEvent.unicode == "\b":
        return searchBarText[:-1]

    elif theGuiEvent.unicode.isalpha() and len(searchBarText) <= 5 or theGuiEvent.unicode.isdigit() and len(searchBarText) <= 5:
        return searchBarText+theGuiEvent.unicode
    else:
        if len(searchBarText) >= 5:
            print("max length of string reached")

        return searchBarText


def timeStamp():
    t = time.localtime()
    currentTime = time.strftime("%H:%M:%S", t)
    updatedTime = "Updated Stock Data at " + str(currentTime)
    return updatedTime
