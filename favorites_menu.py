import pygame
from pygame.locals import *
from Search import *

class MainMenu:
    #default sizes for screen resolution
    screenWid=1280
    screenLen=720

    #whether user clicked in the search bar or not
    insearchbar=0

    #the text the user is inputing into the search bar
    searchbarText=""

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
        searchBarButton, searchBarFont = searchBarInitalize()

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
            pygame.display.update()

            #event handler loop
            for event in pygame.event.get():
                #clicking X on window
                if event.type==pygame.QUIT:
                    print("Exiting Window")
                    pygame.quit() 
                    exit(0)
                
                #whether user clicked into search bar
                if event.type== pygame.MOUSEBUTTONDOWN:
                    if searchBarButton.collidepoint(event.pos):
                        self.insearchbar=1
                    else:
                        self.insearchbar=0
                
                #if user typed into search bar
                if event.type==pygame.KEYDOWN and self.insearchbar==1:
                    if event.unicode=="\r":
                        if search(self.searchbarText):
                            self.searchbarText=""
                    else:
                        self.searchbarText = updateSearchBarOnKeyPress(event, self.searchbarText)
            



test=MainMenu()
test.menuInit()
