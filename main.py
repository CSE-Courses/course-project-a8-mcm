import pygame
from pygame.locals import *
from stock_info_page import*
from Search import *
from LoadingScreen import *


"""
@Authors: Musaiyab Ali, David Forrest
The temporary main class and function that controls the entire program. The MainMenu class is used to create and hold certain
variables that will be used in multiple methods. For now, there's only one method that serves to display the UI and call the back-end
methods to add the functionalities.
"""

class MainRunner:
    #default sizes for screen resolution
    screenWid=1280
    screenLen=720 

    #checker variables to keep track of states
    insearchbar=0
    hamState=0

    #the text the user is inputing into the search bar
    searchbarText=""

    # Empty time string
    updatedTimeText = ""

    autoFill=""

    #favorited stocks
    fav1 = ""
    fav2 = ""
    fav3 = ""

    # The current tab the user is on
    currentPage=1
    didPageChange=True

    #the list of stocks
    stockList=["GILD","WMT","UNP", "GPRO","HPQ", "V", "CSCO", "SLB", "AMGN", "BA", "TGT", "COP", "CMCSA", "BMY", "CVX", "VZ", "BP", "T", "UNH", "MCD", "PFE", "ABT", "FB", "DIS", "MMM", "XOM", "ORCL", "PEP","HD", "JPM", "INTC", "WFC", "MRK", "KO", "AMZN", "PG", "BRKB","GOOGL", "GM", "JNJ", "MO", "IBM", "GE", "MSFT", "AAPL","NVDA", "AMD", "GE", "NTDOF", "SNE"]



    #function for initializing images
    def imgInit(self):
        #loading images
        loadImg1 = pygame.image.load("../course-project-a8-mcm/images/loadingScreen/load1.png")
        loadImg2 = pygame.image.load("../course-project-a8-mcm/images/loadingScreen/load2.png")
        #background image
        fillerImag=pygame.image.load("../course-project-a8-mcm/images/homepageFiles/white.png")
        #menu button image
        hamburgermenu=pygame.image.load("../course-project-a8-mcm/images/homepageFiles/burger.png")
        searchIcon = pygame.image.load("../course-project-a8-mcm/images/homepageFiles/searchy3.png")
        #favorites menu image
        favMenu=pygame.image.load("../course-project-a8-mcm/images/homepageFiles/favorites_background.png")
        #search bar image
        searchbar=pygame.image.load("../course-project-a8-mcm/images/homepageFiles/SearchBar.png")
        #homepage tab images
        hompeageIcons=pygame.image.load("../course-project-a8-mcm/images/homepageFiles/homePageIcons.png")

        return loadImg1, loadImg2, fillerImag, hamburgermenu, favMenu, searchbar, hompeageIcons,searchIcon

    def buttonInit(self):
        #render hidden buttons
        hamHidden=pygame.Rect(0,0,100,100)

        #render buttons for stocks
        stock1 = pygame.Rect(200, 145, 975, 50)
        stock2 = pygame.Rect(200, 240, 975, 70)
        stock3 = pygame.Rect(200, 355, 975, 65)
        stock4 = pygame.Rect(200, 470, 975, 60)
        stock5 = pygame.Rect(200, 580, 975, 60)

        #render buttons for switching between pages
        goback=pygame.Rect(20, 670, 30, 20)
        numb1=pygame.Rect(60, 670, 30, 20)
        numb2=pygame.Rect(100, 670, 30, 20)
        numb3=pygame.Rect(140, 670, 30, 20)
        numb4=pygame.Rect(180, 670, 30, 20)
        numb5=pygame.Rect(220, 670, 30, 20)
        goforward=pygame.Rect(260, 670, 30, 20)

        #render fav menu buttons
        fav1B=pygame.Rect(200, 325, 175, 100)
        fav2B=pygame.Rect(200, 450, 175, 100)
        fav3B=pygame.Rect(200, 575, 175, 100)

        #render delete fav buttons
        delFav1=pygame.Rect(400, 325, 100, 100)
        delFav2=pygame.Rect(400, 450, 100, 100)
        delFav3=pygame.Rect(400, 575, 100, 100)        

        return hamHidden, stock1, stock2, stock3, stock4, stock5, goback, numb1, numb2, numb3, numb4, numb5, goforward, fav1B,fav2B, fav3B, delFav1, delFav2, delFav3

    #function that reads settings file and saves the values to fav1, fav2, and fav3
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

    #function that writes to the settings file, updates fav1, fav2, and fav3
    #str is the stock that will be added to favorites
    def writeFile(self, str):
        if self.fav1 != "" and self.fav2 != "" and self.fav3 != "":
            print("Favorite list is full!")
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

    #str is either fav1, fav2, or fav3, will be deleted
    def delFav(self, str):
        if str == "fav1":
            self.fav1 = ""
        if str == "fav2":
            self.fav2 = ""
        if str == "fav3":
            self.fav3 = ""

        theFile= open("settings.txt", "w")
        theFile.write("fav1=" + self.fav1 + "=\n")
        theFile.write("fav2=" + self.fav2 + "=\n")
        theFile.write("fav3=" + self.fav3 + "=\n")

        theFile.close()

    def fontInit(self):
        pagenumber=pygame.font.Font("../course-project-a8-mcm/Fonts/times.ttf",25)
        stockfont=pygame.font.Font("../course-project-a8-mcm/Fonts/times.ttf",40)
        return pagenumber, stockfont

    def mainScreen(self):

        
        pygame.init()

        #name of the screen
        pygame.display.set_caption('MCM')
        
        # width then Height
        screen=pygame.display.set_mode((self.screenWid , self.screenLen))    
        
        #calls method to initialize all the images
        loadImg1, loadImg2, fillerImag, hamburgermenu, favMenu, searchbar, homepageIcons, searchIcon = self.imgInit()

        #calls method from Search to make button and font for search bar
        searchBarButton, searchBarFont, updatedTime, timeFont, companyFont, favFont = searchBarInitalize() 

        #calls method to initalize make the buttons
        hamHidden, stock1, stock2, stock3, stock4, stock5, goback, numb1, numb2, numb3, numb4, numb5, goforward, fav1B, fav2B, fav3B, delFav1, delFav2, delFav3 =self.buttonInit()
        searchBarButton = pygame.Rect(198, 17, 983, 56)
       #calls method to initalize fonts
        pagenumber, stockfont=self.fontInit()
        loadScreen(screen) 

        autoFillFont = pygame.font.Font("../course-project-a8-mcm/Fonts/times.ttf", 50)

        #screen while program is running
        while True:
            #clears the screen
            screen.fill(0) 

            #update fav variables by reading file
            self.readFile()

            #renders all of the hidden buttons
            
            pygame.draw.rect(screen, [225, 225, 225], stock1)
            pygame.draw.rect(screen, [225, 225, 225], stock2)
            pygame.draw.rect(screen, [0, 0, 0], stock3)
            pygame.draw.rect(screen, [0, 0, 0], stock4)
            pygame.draw.rect(screen, [0, 0, 0], stock5)


            #renders background and menu buttons
            screen.blit(fillerImag, (0,0))
            pygame.draw.rect(screen,[0,0,0],searchBarButton)
            screen.blit(searchbar,(0,0))
            screen.blit(searchIcon, (205, 28))
            screen.blit(hamburgermenu,(0,0))

            #render search bar text
            searchtext=searchBarFont.render(self.searchbarText,True,[0,0,0])
            screen.blit(searchtext,(250,15))
            if self.autoFill !="":
                autoFillText=autoFillFont.render((self.autoFill + "?"),True, [192,192,192])
                #renders hompage hiddenButtons
                screen.blit(autoFillText, (750,15))

            #renders hompage page switching buttons
            pygame.draw.rect(screen,[255,0,0],numb1)
            pygame.draw.rect(screen,[255,0,0],numb2)
            pygame.draw.rect(screen,[255,0,0],numb3)
            pygame.draw.rect(screen,[255,0,0],numb4)
            pygame.draw.rect(screen,[255,0,0],numb5)
            pygame.draw.rect(screen,[0,255,0],goback)
            pygame.draw.rect(screen,[0,255,0],goforward)
            screen.blit(homepageIcons,(0,0))

            #renders stock text for each stock on display
            firstStock=stockfont.render(self.stockList[self.currentPage*5-5], True,[0,0,0])
            secondStock=stockfont.render(self.stockList[self.currentPage*5-4], True,[0,0,0])
            thirdStock=stockfont.render(self.stockList[self.currentPage*5-3], True,[0,0,0])
            fourthStock=stockfont.render(self.stockList[self.currentPage*5-2], True,[0,0,0])
            fifthStock=stockfont.render(self.stockList[self.currentPage*5-1], True,[0,0,0])
            screen.blit(firstStock, (205, 155))
            screen.blit(secondStock, (205, 265))
            screen.blit(thirdStock, (205, 375))
            screen.blit(fourthStock, (205, 485))
            screen.blit(fifthStock, (205, 595))

            #handles page switching
            if self.currentPage<6:
                if self.currentPage==1:
                    one=pagenumber.render("1",True,[255,255,255])
                    two=pagenumber.render("2",True,[0,0,0])
                    three=pagenumber.render("3",True,[0,0,0])
                    four=pagenumber.render("4",True,[0,0,0])
                    five=pagenumber.render("5",True,[0,0,0])
                elif self.currentPage==2:
                    one=pagenumber.render("1",True,[0,0,0])
                    two=pagenumber.render("2",True,[255,255,255])
                    three=pagenumber.render("3",True,[0,0,0])
                    four=pagenumber.render("4",True,[0,0,0])
                    five=pagenumber.render("5",True,[0,0,0])
                elif self.currentPage==3:
                    one=pagenumber.render("1",True,[0,0,0])
                    two=pagenumber.render("2",True,[0,0,0])
                    three=pagenumber.render("3",True,[255,255,255])
                    four=pagenumber.render("4",True,[0,0,0])
                    five=pagenumber.render("5",True,[0,0,0])
                elif self.currentPage==4:
                    one=pagenumber.render("1",True,[0,0,0])
                    two=pagenumber.render("2",True,[0,0,0])
                    three=pagenumber.render("3",True,[0,0,0])
                    four=pagenumber.render("4",True,[255,255,255])
                    five=pagenumber.render("5",True,[0,0,0])
                else:
                    one=pagenumber.render("1",True,[0,0,0])
                    two=pagenumber.render("2",True,[0,0,0])
                    three=pagenumber.render("3",True,[0,0,0])
                    four=pagenumber.render("4",True,[0,0,0])
                    five=pagenumber.render("5",True,[255,255,255])
                screen.blit(one,(68,665))
                screen.blit(two,(108,665))
                screen.blit(three,(148,665))
                screen.blit(four,(188,665))
                screen.blit(five,(228,665))
            else:
                if self.currentPage==6:
                    one=pagenumber.render("6",True,[255,255,255])
                    two=pagenumber.render("7",True,[0,0,0])
                    three=pagenumber.render("8",True,[0,0,0])
                    four=pagenumber.render("9",True,[0,0,0])
                    five=pagenumber.render("10",True,[0,0,0])
                elif self.currentPage==7:
                    one=pagenumber.render("6",True,[0,0,0])
                    two=pagenumber.render("7",True,[255,255,255])
                    three=pagenumber.render("8",True,[0,0,0])
                    four=pagenumber.render("9",True,[0,0,0])
                    five=pagenumber.render("10",True,[0,0,0])
                elif self.currentPage==8:
                    one=pagenumber.render("6",True,[0,0,0])
                    two=pagenumber.render("7",True,[0,0,0])
                    three=pagenumber.render("8",True,[255,255,255])
                    four=pagenumber.render("9",True,[0,0,0])
                    five=pagenumber.render("10",True,[0,0,0])
                elif self.currentPage==9:
                    one=pagenumber.render("6",True,[0,0,0])
                    two=pagenumber.render("7",True,[0,0,0])
                    three=pagenumber.render("8",True,[0,0,0])
                    four=pagenumber.render("9",True,[255,255,255])
                    five=pagenumber.render("10",True,[0,0,0])
                else:
                    one=pagenumber.render("6",True,[0,0,0])
                    two=pagenumber.render("7",True,[0,0,0])
                    three=pagenumber.render("8",True,[0,0,0])
                    four=pagenumber.render("9",True,[0,0,0])
                    five=pagenumber.render("10",True,[255,255,255])
                screen.blit(one,(68,665))
                screen.blit(two,(108,665))
                screen.blit(three,(148,665))
                screen.blit(four,(188,665))
                screen.blit(five,(222,665))
                            
            # render updated time text
            timeText = timeFont.render(self.updatedTimeText, True, [0, 0, 0])
            screen.blit(timeText, (875, 670))
            # )

            #checks if fav menu button is clicked
            if self.hamState==1:
                screen.blit(favMenu, (0,0))
                #add any favorited stocks to menu
                if self.fav1 != "":
                    pygame.draw.rect(screen,[0,0,0],fav1B)
                    fav1Text = favFont.render(self.fav1, True, [255, 255, 255])
                    screen.blit(fav1Text, (200, 350))
                    pygame.draw.rect(screen,[255,0,0],delFav1)
                if self.fav2 != "":
                    pygame.draw.rect(screen,[0,0,0],fav2B)
                    fav2Text = favFont.render(self.fav2, True, [255, 255, 255])
                    screen.blit(fav2Text, (200, 475))
                    pygame.draw.rect(screen,[255,0,0],delFav2)
                if self.fav3 != "":
                    pygame.draw.rect(screen,[0,0,0],fav3B)
                    fav3Text = favFont.render(self.fav3, True, [255, 255, 255])
                    screen.blit(fav3Text, (200, 600))
                    pygame.draw.rect(screen,[255,0,0],delFav3)                               
            
            #updates the screen
            pygame.display.update()

            #event handler loop
            for event in pygame.event.get():
                #clicking X on window
                if event.type==pygame.QUIT:
                    print("Exiting Window")
                    pygame.quit() 
                    exit(0)

               #if user clicked left mouse button
                if event.type==pygame.MOUSEBUTTONDOWN:
                    pos= event.pos
                    if self.hamState==0:
                        #handle opening the info page when clicking on the stock
                        if stock1.collidepoint(event.pos):
                            newPage=InfoPage()
                            newPage.setStock(self.stockList[self.currentPage*5-5])
                            newPage.infoPgInit()
                        if stock2.collidepoint(event.pos):
                            newPage=InfoPage()
                            newPage.setStock(self.stockList[self.currentPage*5-4])
                            newPage.infoPgInit()
                        if stock3.collidepoint(event.pos):
                            newPage=InfoPage()
                            newPage.setStock(self.stockList[self.currentPage*5-3])
                            newPage.infoPgInit()
                        if stock4.collidepoint(event.pos):
                            newPage=InfoPage()
                            newPage.setStock(self.stockList[self.currentPage*5-2])
                            newPage.infoPgInit()
                        if stock5.collidepoint(event.pos):
                            newPage=InfoPage()
                            newPage.setStock(self.stockList[self.currentPage*5-1])
                            newPage.infoPgInit()
                            

                            #handles tabing between pages

                        if goback.collidepoint(pos) and self.currentPage > 1:
                            self.currentPage-=1
                            self.didPageChange=True
                            #print(str(self.currentPage))
                        if goforward.collidepoint(pos) and self.currentPage<10:
                            self.currentPage+=1
                            self.didPageChange=True
                        # print(str(self.currentPage))
                        if numb1.collidepoint(pos) and self.currentPage>5:
                            self.currentPage=6
                            self.didPageChange=True
                        # print(str(self.currentPage))
                        elif numb1.collidepoint(pos):
                            self.currentPage=1
                            self.didPageChange=True
                        #  print(str(self.currentPage))
                        if numb2.collidepoint(pos) and self.currentPage<=5:
                            self.currentPage=2
                            self.didPageChange=True
                            #print(str(self.currentPage))
                        elif numb2.collidepoint(pos):
                            self.currentPage=7
                            self.didPageChange=True
                            #print(str(self.currentPage))
                        if numb3.collidepoint(pos) and self.currentPage<=5:
                            self.currentPage=3
                            self.didPageChange=True
                            #print(str(self.currentPage))
                        elif numb3.collidepoint(pos):
                            self.currentPage=8
                            self.didPageChange=True
                        #  print(str(self.currentPage))
                        if numb4.collidepoint(pos) and self.currentPage<=5:
                            self.currentPage=4
                            self.didPageChange=True
                        # print(str(self.currentPage))
                        elif numb4.collidepoint(pos):
                            self.currentPage=9
                            self.didPageChange=True
                        # print(str(self.currentPage))
                        if numb5.collidepoint(pos) and self.currentPage<=5:
                            self.currentPage=5
                            self.didPageChange=True
                            #print(str(self.currentPage))
                        elif numb5.collidepoint(pos):
                            self.currentPage=10
                            self.didPageChange=True
                        #  print(str(self.currentPage))
                    if self.hamState == 1:
                        if fav1B.collidepoint(event.pos) and self.fav1 != "":
                            newPage=InfoPage()
                            newPage.setStock(self.fav1)
                            newPage.infoPgInit()
                        if fav2B.collidepoint(event.pos) and self.fav2 != "":
                            newPage=InfoPage()
                            newPage.setStock(self.fav2)
                            newPage.infoPgInit()
                        if fav3B.collidepoint(event.pos) and self.fav3 != "":
                            newPage=InfoPage()
                            newPage.setStock(self.fav3)
                            newPage.infoPgInit()
                        if delFav1.collidepoint(event.pos):
                            self.delFav("fav1") 
                        if delFav2.collidepoint(event.pos):
                            self.delFav("fav2")
                        if delFav3.collidepoint(event.pos):
                            self.delFav("fav3")

                    if hamHidden.collidepoint(event.pos):
                        if self.hamState==0:
                            self.hamState=1      
                        else: 
                            self.hamState=0                                        
                    elif searchBarButton.collidepoint(event.pos):
                        self.insearchbar=1 
                    else:
                        self.insearchbar=0               
                
                #if user typed into search bar
                if event.type==pygame.KEYDOWN and self.insearchbar==1:
                    if event.unicode=="\r":
                        if search(self.searchbarText):
                            newPage=InfoPage()
                            newPage.setStock(self.searchbarText)
                            newPage.infoPgInit()
                            self.searchbarText=""
                            self.autoFill=""
                            self.updatedTimeText = timeStamp()
                    elif event.unicode=="\t":
                        newPage=InfoPage()
                        newPage.setStock(self.autoFill)
                        newPage.infoPgInit()
                        self.searchbarText=""
                        self.autoFill=""
                        self.updatedTimeText = timeStamp()
                        
                    else:
                        self.searchbarText = updateSearchBarOnKeyPress(event, self.searchbarText)
                        for stockName in self.stockList:
                           # print(stockName)
                            if self.searchbarText.upper() in stockName:
                                print ("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
                                self.autoFill=stockName
                                break

                    
test=MainRunner()
test.readFile()
test.mainScreen()
