import pygame
from pygame.locals import *
from Search2 import *
from webscrape import *
from graphs import *
import futureGraphs as fg
import asyncio

"""
@Authors: Musaiyab Ali, David Forrest, Sean Brasse
The class that displays stock information when a stock is clicked on. This will mimic
the favorites menu, but will display the line graph and company name
"""


class InfoPage:
    # default sizes for screen resolution
    screenWid = 1280
    screenLen = 720

    # checker variables to keep track of states
    insearchbar = 0
    hamState = 0

    #fav stocks
    fav1 = ""
    fav2 = ""
    fav3 = ""

    #verify favorited state
    verState = 2

    # the text the user is inputing into the search bar
    searchbarText = ""

    # Empty time string
    updatedTimeText = ""

    # Empty company name
    companyInitials = ""

    # Company name
    companyName = ""

    # stock to display
    stockToDisplay = ""

    # Labels
    currentTrend = "Stock Data"
    ai = "Projected Growth"

    # wheather user inputted a new stock
    updatedStock = 1

    stockList = ["GILD", "WMT", "UNP", "GPRO", "HPQ", "V", "CSCO", "SLB", "AMGN", "BA", "TGT", "COP", "CMCSA", "BMY", "CVX", "VZ", "BP", "T", "UNH", "MCD", "PFE", "ABT", "FB", "DIS", "MMM",
                 "XOM", "ORCL", "PEP", "HD", "JPM", "INTC", "WFC", "MRK", "KO", "AMZN", "PG", "BRKB", "GOOGL", "GM", "JNJ", "MO", "IBM", "GE", "MSFT", "AAPL", "NVDA", "AMD", "GE", "NTDOF", "SNE"]

    def setStock(self, stock):
        self.stockToDisplay = stock
        temp = get_url(stock)
        self.companyName = get_company_name(temp)
        self.updatedTimeText = timeStamp()

    def readFile(self):
        theFile= open("settings.txt")
        lineArray= theFile.readlines()
        for line in lineArray:
            if "fav1" in line:
                tmp= line.split("=")
                self.fav1 = tmp[1]
            if "fav2" in line:
                tmp= line.split("=")
                self.fav2 = tmp[1]
            if "fav3" in line:
                tmp= line.split("=")
                self.fav3 = tmp[1]
            
        theFile.close()

    def writeFile(self, str):
        if self.fav1 != "" and self.fav2 != "" and self.fav3 != "":
            print("Favorite list is full")
            return 1
        elif self.fav1 == "":
            self.fav1 = str
        elif self.fav2 == "":
            self.fav2 = str
        elif self.fav3 == "":
            self.fav3 = str            

        theFile= open("settings.txt", "w")
        theFile.write("fav1=" + self.fav1 + "=\n")
        theFile.write("fav2=" + self.fav2 + "=\n")
        theFile.write("fav3=" + self.fav3 + "=\n")

        theFile.close()
        return 0

    async def infoPgInit(self):

        pygame.init()

        # scroll = pygame.image.load("../course-project-a8-mcm/images/homepageFiles/scrollButtons.png")

        # name of the screen
        pygame.display.set_caption('MCM')

        # width then Height
        screen = pygame.display.set_mode((self.screenWid, self.screenLen))

        # background image
        fillerImag = pygame.image.load(
            "../course-project-a8-mcm/images/homepageFiles/white.png")

        # menu button
        hamburgermenu = pygame.image.load(
            "../course-project-a8-mcm/images/homepageFiles/burger.png")

        # search bar box
        searchbar = pygame.image.load(
            "../course-project-a8-mcm/images/homepageFiles/SearchBar.png")

        # search icon
        searchIcon = pygame.image.load(
            "../course-project-a8-mcm/images/homepageFiles/searchy3.png")

        # back button
        backButton = pygame.image.load(
            "../course-project-a8-mcm/images/homepageFiles/back2.png")

        # button and font for search bar
        searchBarButton, searchBarFont, updatedTime, timeFont, companyFont, favFont, verFont = searchBarInitalize()

        # CandlestickGraph
        candleStickGraph = pygame.image.load(
            "../course-project-a8-mcm/FUBUKIv2.png")
        mcdonaldsGraph = pygame.image.load(
            "../course-project-a8-mcm/FUBUKIv2.png")

        # leftHidden = pygame.Rect(1100, 600 ,1110, 610)
        # rightHidden = pygame.Rect(985, 520, 15, 16)
        backHidden = pygame.Rect(0, 650, 60, 720)
        # leftBorder = pygame.Rect(30, 210, 630 ,610)

        # favorites menu and button
        favMenu = pygame.image.load("../course-project-a8-mcm/images/homepageFiles/favorites_background.png")
        addFav=pygame.Rect(60, 678, 50, 25)

        # screen while program is running
        while True:
            # clears the screen
            screen.fill(0)

            self.readFile()

            #await asyncio.sleep(0.005)

            # renders background and menu buttons
            pygame.draw.rect(screen, [255, 0, 0], backHidden)
            screen.blit(fillerImag, (0, 0))
            # renders all of the hidden buttons
            pygame.draw.rect(screen, [0, 0, 0], searchBarButton)

            screen.blit(searchbar, (0, 0))
            screen.blit(searchIcon, (205, 28))
            # screen.blit(hamburgermenu, (10, 15))
            screen.blit(backButton, (15, 675))
            # screen.blit(rightScroll, (985, 520))
            # screen.blit(leftScroll, (955, 520))
            # pygame.draw.rect(screen,[255,0,0],leftHidden)
            # screen.blit(scroll, (0,0))

            # render search bar text
            searchtext = searchBarFont.render(
                self.searchbarText, True, [0, 0, 0])
            screen.blit(searchtext, (250, 15))

            # #render Company Name
            compName = companyFont.render(
                self.companyName, True, [0, 0, 0])

            current = timeFont.render(
                self.currentTrend, True, [0, 0, 0]
            )
            predict = timeFont.render(
                self.ai, True, [0, 0, 0]
            )

            # render hidden buttons
            # hamHidden = pygame.Rect(10, 10, 65, 65)

            timeFont2 = pygame.font.Font(
                "../course-project-a8-mcm/Fonts/times.ttf", 20)
            # render updated time text
            timeText = timeFont2.render(
                self.updatedTimeText, True, [0, 0, 0])
            # )

            # renders line graph box
            # lineGraphBox = pygame.Rect(300, 250, 700, 250)
            # pygame.draw.rect(screen, [0, 0, 0], lineGraphBox)

            # updates the screen

            if self.updatedStock == 0:
                tempgraph = pygame.transform.scale(
                    candleStickGraph, (600, 432))
                tempgraph2 = pygame.transform.scale(mcdonaldsGraph, (600, 432))
                leftBorder = pygame.Rect(35, 195, 705, 442)
                pygame.draw.rect(screen, [0, 0, 0], leftBorder)
                screen.blit(tempgraph, (40, 200))
                rightBorder = pygame.Rect(620, 195, 610, 442)
                pygame.draw.rect(screen, [0, 0, 0], rightBorder)
                screen.blit(tempgraph2, (625, 200))
                screen.blit(current, (290, 640))
                screen.blit(predict, (830, 640))
                screen.blit(compName, (20, 120))
                screen.blit(timeText, (1000, 690))

            #await asyncio.sleep(0.005)

            # if self.hamState == 1:
            #     screen.blit(favMenu, (0, 0))

            pygame.draw.rect(screen,[0,255,0],addFav)

            if self.verState == 1:
                verText = verFont.render("Favorite list is full", True, [0, 0, 0])
                screen.blit(verText, (150, 678))
            elif self.verState == 0:
                verText = verFont.render(self.stockToDisplay + " has been added to favorite list", True, [0, 0, 0])
                screen.blit(verText, (150, 678))

            #await asyncio.sleep(0.005)

            pygame.display.update()

            # event handler loop
            for event in pygame.event.get():
                # clicking X on window
                if event.type == pygame.QUIT:
                    print("Exiting Window")
                    pygame.quit()
                    exit(0)

                # if user clicked hamburger icon
                # if event.type == pygame.MOUSEBUTTONDOWN:
                    # if hamHidden.collidepoint(event.pos):
                    #     if self.hamState == 0:
                    #         self.hamState = 1
                    #     else:
                    #         self.hamState = 0

                # whether user clicked into search bar
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if searchBarButton.collidepoint(event.pos):
                        self.insearchbar = 1
                    else:
                        self.insearchbar = 0

                    if backHidden.collidepoint(event.pos):
                        return 0
                    if addFav.collidepoint(event.pos):
                        self.verState = self.writeFile(self.stockToDisplay)                        

                # if user typed into search bar
                if event.type == pygame.KEYDOWN and self.insearchbar == 1:
                    if event.unicode == "\r":
                        if search(self.searchbarText):
                            temp = get_url(self.searchbarText)
                            self.companyName = get_company_name(temp)
                            self.stockToDisplay = self.searchbarText
                            self.searchbarText = ""
                            self.updatedTimeText = timeStamp()
                            self.updatedStock = 1
                    else:
                        self.searchbarText = updateSearchBarOnKeyPress(
                            event, self.searchbarText)

            if self.updatedStock == 1:
                self.updatedStock = 0
                if self.stockToDisplay!="":
                    candleStick(self.stockToDisplay)
                    fg.futureLine(self.stockToDisplay)
                    candleStickGraph = pygame.image.load(
                        "../course-project-a8-mcm/candlestick.png")
                    mcdonaldsGraph = pygame.image.load(
                        "../course-project-a8-mcm/lstm.png")


# calls the method to run the program
# test = InfoPage()
# test.infoPgInit()
