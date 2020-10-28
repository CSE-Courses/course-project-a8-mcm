import pygame
from pygame.locals import *
from Search import *
from LoadingScreen import *
from TempInfoPage import*

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
        fillerImag=pygame.image.load("../course-project-a8-mcm/images/homepageFiles/Background base.png")
        #menu button image
        hamburgermenu=pygame.image.load("../course-project-a8-mcm/images/homepageFiles/HamburgerMenu.png")
        #favorites menu image
        favMenu=pygame.image.load("../course-project-a8-mcm/images/homepageFiles/favorites_background.png")
        #search bar image
        searchbar=pygame.image.load("../course-project-a8-mcm/images/homepageFiles/SearchBar.png")
        #homepage tab images
        hompeageIcons=pygame.image.load("../course-project-a8-mcm/images/homepageFiles/hompage Icons.png")

        return loadImg1, loadImg2, fillerImag, hamburgermenu, favMenu, searchbar, hompeageIcons

    def buttonInit(self):
        #render hidden buttons
        hamHidden=pygame.Rect(0,0,100,100)

        #render buttons for stocks
        stock1=pygame.Rect(20, 110, 1240, 90)
        stock2=pygame.Rect(20, 220, 1240, 90)
        stock3=pygame.Rect(20, 330, 1240, 90)
        stock4=pygame.Rect(20, 440, 1240, 90)
        stock5=pygame.Rect(20, 550, 1240, 90)

        #render buttons for switching between pages
        goback=pygame.Rect(20, 670, 30, 20)
        numb1=pygame.Rect(60, 670, 30, 20)
        numb2=pygame.Rect(100, 670, 30, 20)
        numb3=pygame.Rect(140, 670, 30, 20)
        numb4=pygame.Rect(180, 670, 30, 20)
        numb5=pygame.Rect(220, 670, 30, 20)
        goforward=pygame.Rect(260, 670, 30, 20)

        return hamHidden, stock1, stock2, stock3, stock4, stock5, goback, numb1, numb2, numb3, numb4, numb5, goforward

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

    def fontInit(self):
        pagenumber=pygame.font.Font("../course-project-a8-mcm/Fonts/times.ttf",25)
        stockfont=pygame.font.Font("../course-project-a8-mcm/Fonts/times.ttf",65)
        return pagenumber, stockfont

    def mainScreen(self):
        
        pygame.init()

        #name of the screen
        pygame.display.set_caption('MCM')
        
        # width then Height
        screen=pygame.display.set_mode((self.screenWid , self.screenLen))    
        
        #calls method to initialize all the images
        loadImg1, loadImg2, fillerImag, hamburgermenu, favMenu, searchbar, homepageIcons = self.imgInit()

        #calls method from Search to make button and font for search bar
        searchBarButton, searchBarFont, updatedTime, timeFont, companyFont, favFont = searchBarInitalize() 

        #calls method to initalize make the buttons
        hamHidden, stock1, stock2, stock3, stock4, stock5, goback, numb1, numb2, numb3, numb4, numb5, goforward=self.buttonInit()
       
       #calls method to initalize fonts
        pagenumber, stockfont=self.fontInit()
        loadScreen(screen) 

        #screen while program is running
        while True:
            #clears the screen
            screen.fill(0) 

            #renders all of the hidden buttons
            pygame.draw.rect(screen,[0,0,0],searchBarButton)


            #renders background and menu buttons
            screen.blit(fillerImag, (0,0))
            screen.blit(searchbar,(0,0))
            screen.blit(hamburgermenu,(0,0))

            #render search bar text
            searchtext=searchBarFont.render(self.searchbarText,True,[0,0,0])
            screen.blit(searchtext,(200,15))

            #renders hompage hiddenButtons
            pygame.draw.rect(screen,[0,0,0],stock1)
            pygame.draw.rect(screen,[0,0,0],stock2)
            pygame.draw.rect(screen,[0,0,0],stock3)
            pygame.draw.rect(screen,[0,0,0],stock4)
            pygame.draw.rect(screen,[0,0,0],stock5)

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
            screen.blit(firstStock,(30, 110))
            screen.blit(secondStock,(30, 220))
            screen.blit(thirdStock,(30, 330))
            screen.blit(fourthStock,(30, 440))
            screen.blit(fifthStock,(30, 550))

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
                fav1Text = favFont.render(self.fav1, True, [0, 0, 0])
                screen.blit(fav1Text, (200, 350))
                fav2Text = favFont.render(self.fav2, True, [0, 0, 0])
                screen.blit(fav2Text, (200, 475))
                fav3Text = favFont.render(self.fav3, True, [0, 0, 0])
                screen.blit(fav3Text, (200, 600))
            
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
                            self.updatedTimeText = timeStamp()
                    else:
                        self.searchbarText = updateSearchBarOnKeyPress(event, self.searchbarText)

                    
test=MainRunner()
test.readFile()
test.mainScreen()
