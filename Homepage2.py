import pygame
from pygame.locals import *
from Search2 import *
from TempInfoPage import*
from LoadingScreen import *

"""
@Authors: Musaiyab Ali, David Forrest
The temporary main class and function that controls the entire program. The MainMenu class is used to create and hold certain
variables that will be used in multiple methods. For now, there's only one method that serves to display the UI and call the back-end
methods to add the functionalities.
"""


def make_buttons_for_stocks():
    stock1 = pygame.Rect(200, 145, 975, 50)
    stock2 = pygame.Rect(200, 240, 975, 70)
    stock3 = pygame.Rect(200, 355, 975, 65)
    stock4 = pygame.Rect(200, 470, 975, 60)
    stock5 = pygame.Rect(200, 580, 975, 60)
    return stock1, stock2, stock3, stock4, stock5


def make_buttons_for_page_switching():
    goback = pygame.Rect(20, 670, 30, 20)
    numb1 = pygame.Rect(60, 670, 30, 20)
    numb2 = pygame.Rect(100, 670, 30, 20)
    numb3 = pygame.Rect(140, 670, 30, 20)
    numb4 = pygame.Rect(180, 670, 30, 20)
    numb5 = pygame.Rect(220, 670, 30, 20)
    goforward = pygame.Rect(260, 670, 30, 20)
    return goback, numb1, numb2, numb3, numb4, numb5, goforward


class MainMenu2:
    # default sizes for screen resolution
    screenWid = 1280
    screenLen = 720

    # checker variables to keep track of states
    insearchbar = 0
    hamState = 0
    loadState = 1

    # the text the user is inputing into the search bar
    searchbarText = ""

    inStockInfoPage = 0

    # Empty time string
    updatedTimeText = ""
    currentPage = 1
    didPageChange = True

    stockList = ["GILD", "WMT", "UNP", "GPRO", "HPQ", "V", "CSCO", "SLB", "AMGN", "BA", "TGT", "COP", "CMCSA", "BMY", "CVX", "VZ", "BP", "T", "UNH", "MCD", "PFE", "ABT", "FB", "DIS", "MMM",
                 "XOM", "ORCL", "PEP", "HD", "JPM", "INTC", "WFC", "MRK", "KO", "AMZN", "PG", "BRKB", "GOOGL", "GM", "JNJ", "MO", "IBM", "GE", "MSFT", "AAPL", "NVDA", "AMD", "GE", "NTDOF", "SNE"]

    def menuInit2(self):

        pygame.init()

        # name of the screen
        pygame.display.set_caption('MCM')

        # width then Height
        screen = pygame.display.set_mode((self.screenWid, self.screenLen))

        # loading images
        loadImg1 = pygame.image.load(
            "../course-project-a8-mcm/images/loadingScreen/load1.png")
        loadImg2 = pygame.image.load(
            "../course-project-a8-mcm/images/loadingScreen/load2.png")

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

        # # search bar box
        hompeageIcons = pygame.image.load(
            "../course-project-a8-mcm/images/homepageFiles/homePageIcons.png")

        # button and font for search bar
        searchBarButton, searchBarFont, updatedTime, timeFont, irrellavant, trash = searchBarInitalize()
        searchBarButton = pygame.Rect(198, 17, 983, 56)
        # favorites menu
        favMenu = pygame.image.load(
            "../course-project-a8-mcm/images/homepageFiles/favorites_background.png")

        stock1, stock2, stock3, stock4, stock5 = make_buttons_for_stocks()
        goback, numb1, numb2, numb3, numb4, numb5, goforward = make_buttons_for_page_switching()

        pagenumber = pygame.font.Font(
            "../course-project-a8-mcm/Fonts/times.ttf", 25)
        stockfont = pygame.font.Font(
            "../course-project-a8-mcm/Fonts/times.ttf", 40)

        # screen while program is running
        while True:
            # clears the screen
            screen.fill(0)

            if self.loadState == 1:
                self.loadState = 0
                loadScreen(screen)

            # renders all of the hidden buttons

            # renders background and menu buttons
            pygame.draw.rect(screen, [225, 225, 225], stock1)
            pygame.draw.rect(screen, [225, 225, 225], stock2)
            pygame.draw.rect(screen, [0, 0, 0], stock3)
            pygame.draw.rect(screen, [0, 0, 0], stock4)
            pygame.draw.rect(screen, [0, 0, 0], stock5)
            screen.blit(fillerImag, (0, 0))
            pygame.draw.rect(screen, [0, 0, 0], searchBarButton)
            screen.blit(searchbar, (0, 0))

            screen.blit(searchIcon, (205, 28))
            screen.blit(hamburgermenu, (10, 15))

            # render search bar text
            searchtext = searchBarFont.render(
                self.searchbarText, True, [0, 0, 0])
            screen.blit(searchtext, (250, 15))

            # render hidden buttons
            hamHidden = pygame.Rect(0, 0, 100, 100)

            # render updated time text
            timeText = timeFont.render(self.updatedTimeText, True, [0, 0, 0])
            screen.blit(timeText, (875, 670))
            # )

            pygame.draw.rect(screen, [255, 0, 0], numb1)
            pygame.draw.rect(screen, [255, 0, 0], numb2)
            pygame.draw.rect(screen, [255, 0, 0], numb3)
            pygame.draw.rect(screen, [255, 0, 0], numb4)
            pygame.draw.rect(screen, [255, 0, 0], numb5)
            pygame.draw.rect(screen, [0, 255, 0], goback)
            pygame.draw.rect(screen, [0, 255, 0], goforward)
            screen.blit(hompeageIcons, (0, 0))

            firstStock = stockfont.render(
                self.stockList[self.currentPage*5-5], True, [0, 0, 0])
            secondStock = stockfont.render(
                self.stockList[self.currentPage*5-4], True, [0, 0, 0])
            thirdStock = stockfont.render(
                self.stockList[self.currentPage*5-3], True, [0, 0, 0])
            fourthStock = stockfont.render(
                self.stockList[self.currentPage*5-2], True, [0, 0, 0])
            fifthStock = stockfont.render(
                self.stockList[self.currentPage*5-1], True, [0, 0, 0])
            screen.blit(firstStock, (205, 155))
            screen.blit(secondStock, (205, 265))
            screen.blit(thirdStock, (205, 375))
            screen.blit(fourthStock, (205, 485))
            screen.blit(fifthStock, (205, 595))
            if self.currentPage < 6:
                if self.currentPage == 1:
                    wan = pagenumber.render("1", True, [255, 255, 255])
                    two = pagenumber.render("2", True, [0, 0, 0])
                    three = pagenumber.render("3", True, [0, 0, 0])
                    four = pagenumber.render("4", True, [0, 0, 0])
                    five = pagenumber.render("5", True, [0, 0, 0])
                elif self.currentPage == 2:
                    wan = pagenumber.render("1", True, [0, 0, 0])
                    two = pagenumber.render("2", True, [255, 255, 255])
                    three = pagenumber.render("3", True, [0, 0, 0])
                    four = pagenumber.render("4", True, [0, 0, 0])
                    five = pagenumber.render("5", True, [0, 0, 0])
                elif self.currentPage == 3:
                    wan = pagenumber.render("1", True, [0, 0, 0])
                    two = pagenumber.render("2", True, [0, 0, 0])
                    three = pagenumber.render("3", True, [255, 255, 255])
                    four = pagenumber.render("4", True, [0, 0, 0])
                    five = pagenumber.render("5", True, [0, 0, 0])
                elif self.currentPage == 4:
                    wan = pagenumber.render("1", True, [0, 0, 0])
                    two = pagenumber.render("2", True, [0, 0, 0])
                    three = pagenumber.render("3", True, [0, 0, 0])
                    four = pagenumber.render("4", True, [255, 255, 255])
                    five = pagenumber.render("5", True, [0, 0, 0])
                else:
                    wan = pagenumber.render("1", True, [0, 0, 0])
                    two = pagenumber.render("2", True, [0, 0, 0])
                    three = pagenumber.render("3", True, [0, 0, 0])
                    four = pagenumber.render("4", True, [0, 0, 0])
                    five = pagenumber.render("5", True, [255, 255, 255])
                screen.blit(wan, (68, 665))
                screen.blit(two, (108, 665))
                screen.blit(three, (148, 665))
                screen.blit(four, (188, 665))
                screen.blit(five, (228, 665))
            else:
                if self.currentPage == 6:
                    wan = pagenumber.render("6", True, [255, 255, 255])
                    two = pagenumber.render("7", True, [0, 0, 0])
                    three = pagenumber.render("8", True, [0, 0, 0])
                    four = pagenumber.render("9", True, [0, 0, 0])
                    five = pagenumber.render("10", True, [0, 0, 0])
                elif self.currentPage == 7:
                    wan = pagenumber.render("6", True, [0, 0, 0])
                    two = pagenumber.render("7", True, [255, 255, 255])
                    three = pagenumber.render("8", True, [0, 0, 0])
                    four = pagenumber.render("9", True, [0, 0, 0])
                    five = pagenumber.render("10", True, [0, 0, 0])
                elif self.currentPage == 8:
                    wan = pagenumber.render("6", True, [0, 0, 0])
                    two = pagenumber.render("7", True, [0, 0, 0])
                    three = pagenumber.render("8", True, [255, 255, 255])
                    four = pagenumber.render("9", True, [0, 0, 0])
                    five = pagenumber.render("10", True, [0, 0, 0])
                elif self.currentPage == 9:
                    wan = pagenumber.render("6", True, [0, 0, 0])
                    two = pagenumber.render("7", True, [0, 0, 0])
                    three = pagenumber.render("8", True, [0, 0, 0])
                    four = pagenumber.render("9", True, [255, 255, 255])
                    five = pagenumber.render("10", True, [0, 0, 0])
                else:
                    wan = pagenumber.render("6", True, [0, 0, 0])
                    two = pagenumber.render("7", True, [0, 0, 0])
                    three = pagenumber.render("8", True, [0, 0, 0])
                    four = pagenumber.render("9", True, [0, 0, 0])
                    five = pagenumber.render("10", True, [255, 255, 255])
                screen.blit(wan, (68, 665))
                screen.blit(two, (108, 665))
                screen.blit(three, (148, 665))
                screen.blit(four, (188, 665))
                screen.blit(five, (222, 665))

            if self.hamState == 1:
                screen.blit(favMenu, (0, 0))
            # updates the screen
            pygame.display.update()

            # event handler loop
            for event in pygame.event.get():
                # clicking X on window
                if event.type == pygame.QUIT:
                    print("Exiting Window")
                    pygame.quit()
                    exit(0)

                # if user clicked hamburger icon
                if event.type == pygame.MOUSEBUTTONDOWN:

                    if stock1.collidepoint(event.pos):
                        newPage = InfoPage()
                        newPage.setStock(self.stockList[self.currentPage*5-5])
                        newPage.infoPgInit()
                    if stock2.collidepoint(event.pos):
                        newPage = InfoPage()
                        newPage.setStock(self.stockList[self.currentPage*5-4])
                        newPage.infoPgInit()
                        # temps=InfoPage(self.stockList[self.currentPage*5-4])
                    if stock3.collidepoint(event.pos):
                        newPage = InfoPage()
                        newPage.setStock(self.stockList[self.currentPage*5-3])
                        newPage.infoPgInit()
                        # temps=TempInfoPage.InfoPage(self.stockList[self.currentPage*5-3])
                    if stock4.collidepoint(event.pos):
                        newPage = InfoPage()
                        newPage.setStock(self.stockList[self.currentPage*5-2])
                        newPage.infoPgInit()
                        # temps=InfoPage(self.stockList[self.currentPage*5-2])
                    if stock5.collidepoint(event.pos):
                        newPage = InfoPage()
                        newPage.setStock(self.stockList[self.currentPage*5-1])
                        newPage.infoPgInit()
                        # temps=InfoPage(self.stockList[self.currentPage*5-1])

                    if hamHidden.collidepoint(event.pos):
                        if self.hamState == 0:
                            self.hamState = 1
                        else:
                            self.hamState = 0
                    pos = event.pos
                    if goback.collidepoint(pos) and self.currentPage > 1:
                        self.currentPage -= 1
                        self.didPageChange = True
                        print(str(self.currentPage))
                    if goforward.collidepoint(pos) and self.currentPage < 10:
                        self.currentPage += 1
                        self.didPageChange = True
                        print(str(self.currentPage))
                    if numb1.collidepoint(pos) and self.currentPage > 5:
                        self.currentPage = 6
                        self.didPageChange = True
                        print(str(self.currentPage))
                    elif numb1.collidepoint(pos):
                        self.currentPage = 1
                        self.didPageChange = True
                        print(str(self.currentPage))
                    if numb2.collidepoint(pos) and self.currentPage <= 5:
                        self.currentPage = 2
                        self.didPageChange = True
                        print(str(self.currentPage))
                    elif numb2.collidepoint(pos):
                        self.currentPage = 7
                        self.didPageChange = True
                        print(str(self.currentPage))
                    if numb3.collidepoint(pos) and self.currentPage <= 5:
                        self.currentPage = 3
                        self.didPageChange = True
                        print(str(self.currentPage))
                    elif numb3.collidepoint(pos):
                        self.currentPage = 8
                        self.didPageChange = True
                        print(str(self.currentPage))
                    if numb4.collidepoint(pos) and self.currentPage <= 5:
                        self.currentPage = 4
                        self.didPageChange = True
                        print(str(self.currentPage))
                    elif numb4.collidepoint(pos):
                        self.currentPage = 9
                        self.didPageChange = True
                        print(str(self.currentPage))
                    if numb5.collidepoint(pos) and self.currentPage <= 5:
                        self.currentPage = 5
                        self.didPageChange = True
                        print(str(self.currentPage))
                    elif numb5.collidepoint(pos):
                        self.currentPage = 10
                        self.didPageChange = True
                        print(str(self.currentPage))

                # whether user clicked into search bar
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if searchBarButton.collidepoint(event.pos):
                        self.insearchbar = 1
                    else:
                        self.insearchbar = 0

                # if user typed into search bar
                if event.type == pygame.KEYDOWN and self.insearchbar == 1:
                    if event.unicode == "\r":
                        if search(self.searchbarText):
                            newPage = InfoPage()
                            newPage.setStock(self.searchbarText)
                            newPage.infoPgInit()
                            self.searchbarText = ""
                            self.updatedTimeText = timeStamp()
                    else:
                        self.searchbarText = updateSearchBarOnKeyPress(
                            event, self.searchbarText)


# calls the method to run the program
test = MainMenu2()
test.menuInit2()
