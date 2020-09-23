import pygame
from pygame.locals import *

class MainMenu:
    #default sizes for screen resolution
    screenWid=1280
    screenLen=720

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

        #screen while program is running
        while True:
            #clears the screen
            screen.fill(0)

            #renders background and menu buttons
            screen.blit(fillerImag, (0,0))
            screen.blit(searchbar,(0,0))
            screen.blit(hamburgermenu,(0,0))
            pygame.display.update()

            #event handler loop
            for event in pygame.event.get():
                #clicking X on window
                if event.type==pygame.QUIT:
                    print("Exiting Window")
                    pygame.quit() 
                    exit(0)


test=MainMenu()
test.menuInit()
