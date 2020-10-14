import pygame
import time
from pygame.locals import *
from tqdm import *
from Search import *

#method for running the loading screen/transition screen
def loadScreen(currentScreen):
    #declaring screen, and images used
    #pygame.init()
    screen = currentScreen
    bgIMG = pygame.image.load("../course-project-a8-mcm/images/loadingScreen/load1.png")
    bgIMG2 = pygame.image.load("../course-project-a8-mcm/images/loadingScreen/load2.png")
    
    #loop for loading screen and animation, runs for ~10 seconds
    loop = tqdm(total = 10, position = 0, leave = False)
    for k in range(10):
        loop.set_description("Loading...".format(k))
        #screen.fill(0)
        screen.blit(bgIMG, (0, 0))
        pygame.display.update()
        time.sleep(0.1)
        screen.blit(bgIMG2, (0, 0))
        pygame.display.update() 
        time.sleep(0.1)       
        
        loop.update(1)
    loop.close()

class MainMenu:
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
 
    def menuInit(self):
        
        pygame.init()

        #name of the screen
        pygame.display.set_caption('MCM')
        
        # width then Height
        screen=pygame.display.set_mode((self.screenWid , self.screenLen))
        
        #background image
        fillerImag=pygame.image.load("../course-project-a8-mcm/images/homepageFiles/Background base.png")

        #menu button
        hamburgermenu=pygame.image.load("../course-project-a8-mcm/images/homepageFiles/HamburgerMenu.png")
        
        #search bar box
        searchbar=pygame.image.load("../course-project-a8-mcm/images/homepageFiles/SearchBar.png")
        
        #button and font for search bar
        searchBarButton, searchBarFont, updatedTime, timeFont = searchBarInitalize()

        #favorites menu
        favMenu=pygame.image.load("../course-project-a8-mcm/images/homepageFiles/favorites_background.png")

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
            
            if self.hamState==1:
                screen.blit(favMenu, (0,0))
                
            #render hidden buttons
            hamHidden=pygame.Rect(0,0,100,100)

            # render updated time text
            timeText = timeFont.render(self.updatedTimeText, True, [0, 0, 0])
            screen.blit(timeText, (875, 670))
            # )


            #updates the screen
            pygame.display.update()

            #event handler loop
            for event in pygame.event.get():
                #clicking X on window
                if event.type==pygame.QUIT:
                    print("Exiting Window")
                    pygame.quit() 
                    exit(0)

                #if user clicked hamburger icon
                if event.type==pygame.MOUSEBUTTONDOWN:
                    if hamHidden.collidepoint(event.pos):
                        if self.hamState==0:
                            self.hamState=1
                        else:
                            self.hamState=0
 
                #whether user clicked into search bar
                if event.type==pygame.MOUSEBUTTONDOWN:
                    if searchBarButton.collidepoint(event.pos):
                        self.insearchbar=1
                    else:
                        self.insearchbar=0  
                
                #if user typed into search bar
                if event.type==pygame.KEYDOWN and self.insearchbar==1:
                    if event.unicode=="\r":
                        if search(self.searchbarText):
                            self.searchbarText=""
                            self.updatedTimeText = timeStamp()
                    else:
                        self.searchbarText = updateSearchBarOnKeyPress(event, self.searchbarText)

#calls the method to run the program.
test=MainMenu()
test.menuInit()