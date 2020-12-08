import pygame
import time
from pygame.locals import *
from tqdm import *
from Search import *

# method for running the loading screen/transition screen


def loadScreen(currentScreen):
    # declaring screen, and images used
    # pygame.init()
    screen = currentScreen
    bgIMG = pygame.image.load("../course-project-a8-mcm/images/loadingScreen/load0001.png")
    bgIMG2 = pygame.image.load("../course-project-a8-mcm/images/loadingScreen/load0002.png")
    bgIMG3 = pygame.image.load("../course-project-a8-mcm/images/loadingScreen/load0003.png")
    bgIMG4 = pygame.image.load("../course-project-a8-mcm/images/loadingScreen/load0004.png")
    bgIMG5 = pygame.image.load("../course-project-a8-mcm/images/loadingScreen/load0005.png")
    bgalt = pygame.image.load("../course-project-a8-mcm/images/loadingScreen/loaad0000.png")
    bgalt1 = pygame.image.load("../course-project-a8-mcm/images/loadingScreen/loaad0001.png")
    bgalt2 = pygame.image.load("../course-project-a8-mcm/images/loadingScreen/loaad0002.png")
    bgalt3 = pygame.image.load("../course-project-a8-mcm/images/loadingScreen/loaad0003.png")
    bgalt4 = pygame.image.load("../course-project-a8-mcm/images/loadingScreen/loaad0004.png")
    bgalt5 = pygame.image.load("../course-project-a8-mcm/images/loadingScreen/loaad0005.png")
    bgalt6 = pygame.image.load("../course-project-a8-mcm/images/loadingScreen/loaad0006.png")
    bgalt7 = pygame.image.load("../course-project-a8-mcm/images/loadingScreen/loaad0007.png")
    bgalt8 = pygame.image.load("../course-project-a8-mcm/images/loadingScreen/loaad0008.png")
    bgalt9 = pygame.image.load("../course-project-a8-mcm/images/loadingScreen/loaad0009.png")

    # status=0

    # loop for loading screen and animation, runs for ~10 seconds
    # loop = tqdm(total=10, position=0, leave=False)
    for k in range(5):
        for temp in range(10):
            # loop.set_description("Loading...".format(k))
            screen.fill(0)
            if temp==0:
                screen.blit(bgIMG, (0,0))
                screen.blit(bgalt,(0,0))
                pygame.display.update()
            elif temp==1:
                screen.blit(bgIMG2, (0,0))
                screen.blit(bgalt1,(0,0))
                pygame.display.update()
            elif temp==2:
                screen.blit(bgIMG3, (0,0))
                screen.blit(bgalt2,(0,0))
                pygame.display.update()
            elif temp==3:
                screen.blit(bgIMG4, (0,0))
                screen.blit(bgalt3,(0,0))
                pygame.display.update()
            elif temp==4:
                screen.blit(bgIMG5, (0,0))
                screen.blit(bgalt4,(0,0))
                pygame.display.update()
            elif temp==5:
                screen.blit(bgIMG, (0,0))
                screen.blit(bgalt5,(0,0))
                pygame.display.update()
            elif temp==6:
                screen.blit(bgIMG2, (0,0))
                screen.blit(bgalt6,(0,0))
                pygame.display.update()
            elif temp==7:
                screen.blit(bgIMG3, (0,0))
                screen.blit(bgalt7,(0,0))
                pygame.display.update()
            elif temp==8:
                screen.blit(bgIMG4, (0,0))
                screen.blit(bgalt8,(0,0))
                pygame.display.update()
            elif temp==9:
                screen.blit(bgIMG5, (0,0))
                screen.blit(bgalt9,(0,0))
                pygame.display.update()
            # print(status)
            # status+=1
            # if status>4:
            #     status=0
            

            # screen.blit(logo, (5, 5))
            # screen.blit(bgIMG, (0, 0))
            
            time.sleep(0.02)
        # screen.blit(bgIMG2, (0, 0))
        # pygame.display.update()
        # time.sleep(0.1)

    #     loop.update(1)
    # loop.close()


class MainMenu:
    # default sizes for screen resolution
    screenWid = 1280
    screenLen = 720

    # checker variables to keep track of states
    insearchbar = 0
    hamState = 0

    # the text the user is inputing into the search bar
    searchbarText = ""

    # Empty time string
    updatedTimeText = ""

    def menuInit(self):

        pygame.init()

        # name of the screen
        pygame.display.set_caption('MCM')

        # width then Height
        screen = pygame.display.set_mode((self.screenWid, self.screenLen))

        # background image
        fillerImag = pygame.image.load(
            "../course-project-a8-mcm/images/homepageFiles/white.png")

        # menu button
        hamburgermenu = pygame.image.load(
            "../course-project-a8-mcm/images/homepageFiles/HamburgerMenu.png")

        # search bar box
        searchbar = pygame.image.load(
            "../course-project-a8-mcm/images/homepageFiles/SearchBar.png")

        # button and font for search bar
        # searchBarButton, searchBarFont, updatedTime, timeFont = searchBarInitalize()

        # favorites menu
        favMenu = pygame.image.load(
            "../course-project-a8-mcm/images/homepageFiles/favorites_background.png")

        loadScreen(screen)

        # screen while program is running
        # while True:
        #     # clears the screen
        #     screen.fill(0)

        #     # renders all of the hidden buttons
        #     pygame.draw.rect(screen, [0, 0, 0], searchBarButton)

        #     # renders background and menu buttons
        #     screen.blit(fillerImag, (0, 0))
        #     screen.blit(searchbar, (0, 0))
        #     screen.blit(hamburgermenu, (0, 0))

        #     # render search bar text
        #     searchtext = searchBarFont.render(
        #         self.searchbarText, True, [0, 0, 0])
        #     screen.blit(searchtext, (200, 15))

        #     if self.hamState == 1:
        #         screen.blit(favMenu, (0, 0))

        #     # render hidden buttons
        #     hamHidden = pygame.Rect(0, 0, 100, 100)

        #     # render updated time text
        #     timeText = timeFont.render(self.updatedTimeText, True, [0, 0, 0])
        #     screen.blit(timeText, (875, 670))
        #     # )

        #     # updates the screen
        #     pygame.display.update()

        #     # event handler loop
        #     for event in pygame.event.get():
        #         # clicking X on window
        #         if event.type == pygame.QUIT:
        #             print("Exiting Window")
        #             pygame.quit()
        #             exit(0)

        #         # if user clicked hamburger icon
        #         if event.type == pygame.MOUSEBUTTONDOWN:
        #             if hamHidden.collidepoint(event.pos):
        #                 if self.hamState == 0:
        #                     self.hamState = 1
        #                 else:
        #                     self.hamState = 0

        #         # whether user clicked into search bar
        #         if event.type == pygame.MOUSEBUTTONDOWN:
        #             if searchBarButton.collidepoint(event.pos):
        #                 self.insearchbar = 1
        #             else:
        #                 self.insearchbar = 0

        #         # if user typed into search bar
        #         if event.type == pygame.KEYDOWN and self.insearchbar == 1:
        #             if event.unicode == "\r":
        #                 if search(self.searchbarText):
        #                     self.searchbarText = ""
        #                     self.updatedTimeText = timeStamp()
        #             else:
        #                 self.searchbarText = updateSearchBarOnKeyPress(
        #                     event, self.searchbarText)

# calls the method to run the program.
test=MainMenu()
test.menuInit()
