import pygame
import main
import graphics
import GuiBase
from constants import *
import sys
from pygame.locals import *


class SceneBase():

    def __init__(self):
        self.next = self

    def process_input(self):
        pass

    def update(self):
        pass

    def render(self):
        pass

    def termianate(self):
        pygame.quit()

class Environment(SceneBase):

    def __init__(self):
        SceneBase.__init__(self)
        self.surface = graphics.SCREEN
        self.gui_group = pygame.sprite.Group()
        bckImg = pygame.image.load('map1.png') # loading an image of the map
        pygame.font.init()   # font initialisation
        myfont = pygame.font.Font('font1.ttf', 65)  # choosing the font
        myfont1 = pygame.font.Font('font1.ttf', 40)
        myfont2 = pygame.font.Font('font1.ttf', 30)
        title = myfont.render("IT BELONGS IN THE MUSEUM !", 1, (0,0,0))
        startTheGame = myfont1.render("PRESS 'ENTER' TO START", 1, (0,200,0))
        closeTheMenu = myfont2.render("PRESS 'Q' TO QUIT", 1, (180,0,0))
        self.surface.blit(bckImg, (0,0))  #blitting the background
        self.surface.blit(title, (375,80)) #blitting the title
        self.surface.blit(startTheGame, ((500),700))
        self.surface.blit(closeTheMenu, ((649),800))

    def process_input(self):
        for event in pygame.event.get(): # Menu control
            if event.type == pygame.KEYDOWN: 
                if (event.key == K_RETURN):
                    print("START GAME")
                    main.start()
                    #if (event.key == K_RETURN) == True:
                    # Code block to start game here
                elif (event.key == K_q): # Quit game
                    pygame.display.quit()
                    pygame.quit()
                    sys.exit()
                    
    def update(self):
        pass

    def render(self):
        self.gui_group.draw(self.surface)
        pygame.display.flip()
