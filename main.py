#Current ouput should be the list of items in descending order
from functions import *
from classes import *
import pygame
from pygame.locals import *
import sys
import math
import random

#pygame dependent function
def sort_highlight(pX, pY, oX, oY):
    '''Function to highlight items being sorted

    Takes 4 integers, position of item, and position of player'''
    pygame.draw.line(DISPLAYSURF, BLUE, (pX, pY), (oX, oY), 1)
    
def start():
    #Initialize variables
    objs = []
    collected_items = []
    rock_locations = []
    bush_locations = []
    water_locations = []
    nextPos = []
    steps = 0
    count = 0
    value = 0
    ASCENDING = False
    WIDTH = 30
    HEIGHT = 20
    INV_WIDTH = 5
    TILESIZE = 32
    ROCK_DENSITY = 20
    WATER_DENSITY = 10
    BLUE = (0, 0, 255)
    GREEN = (0, 255, 0)
    TIME = 50000
    SAND = pygame.image.load('assets/sand-new.png')
    STONE = pygame.image.load('assets/stone.png')
    BUSH = pygame.image.load('assets/bush.png')
    WATER = pygame.image.load('assets/water32.png')
    BG = pygame.image.load('assets/bg.png')

    #Initialize items
    #Load image for items
    item_1 = pygame.image.load('assets/coin.png')
    item_2 = pygame.image.load('assets/crown.png')
    item_3 = pygame.image.load('assets/spearhead.png')
    item_4 = pygame.image.load('assets/bone2.png')
    item_5 = pygame.image.load('assets/key1.png')

    #Make items instances of classes
    game_items = {
        item_1: Item('coin', 2, gen_coordinates(0, WIDTH, 0, HEIGHT), 'treasure', 10, False),
        item_2: Item('crown', 200, gen_coordinates(0, WIDTH, 0, HEIGHT), 'treasure', 2, False),
        item_3: Item('spear', 30, gen_coordinates(0, WIDTH, 0, HEIGHT), 'weapon', 5, False),
        item_4: Item('bone', 5, gen_coordinates(0, WIDTH, 0, HEIGHT), 'remains', 4, False),
        item_5: Item('pot', 10, gen_coordinates(0, WIDTH, 0, HEIGHT), 'tool', 10, False)
        }

    #Sort the items
    items = [item_1, item_2, item_3, item_4, item_5]
    for i in range(len(game_items)):
        objs.append(game_items[items[i]])

    print("Sorting into order")
    if ASCENDING == True:
        sorted_list = sort_objects(objs)[::-1]
    else:
        sorted_list = sort_objects(objs)

    #INITIALIZE PYGAME
    #===============
    pygame.init()
    #pygame.mixer.init()
    #Initialize pygame dependent variables
    flags = DOUBLEBUF
    DISPLAYSURF = pygame.display.set_mode((INV_WIDTH * TILESIZE + WIDTH*TILESIZE, HEIGHT*TILESIZE), flags)
    clock = pygame.time.Clock()
    player = pygame.image.load('assets/player-idea.png')
    pygame.time.set_timer(USEREVENT, TIME)
    DISPLAYSURF.set_alpha(None)
    pygame.font.init()
    default_font = pygame.font.get_default_font()
    font_renderer = pygame.font.Font(default_font, 19)
    pygame.mixer.init()
    sound1 = pygame.mixer.Sound('smb3_coin.wav')
    sound2 = pygame.mixer.Sound('ijtheme.wav')
    sound2.play()

    inv_label = font_renderer.render("Inventory", 1, (255, 255, 255))

    #Build array of locations for randomly placed rocks and trees
    #Bulk of this code is to increase likelihood of clumping nature
    for rows in range(WIDTH):
        for columns in range(HEIGHT):
            if [rows + 1, columns] in water_locations or \
                    [rows - 1, columns] in water_locations or \
                    [rows, columns + 1] in water_locations or \
                    [rows, columns - 1] in water_locations:
                        if random.randrange(15) < WATER_DENSITY:
                            water_locations.append([rows, columns])

            elif (random.randrange(1000) > 1000 - WATER_DENSITY):
                water_locations.append([rows, columns])
            #water_locations = disperse(rows, columns, WATER_DENSITY, 15, water_locations) 

            if [rows + 1, columns] in rock_locations or \
                    [rows - 1, columns] in rock_locations or \
                    [rows, columns + 1] in rock_locations or \
                    [rows, columns - 1] in rock_locations:
                        if random.randrange(80) < ROCK_DENSITY:
                            rock_locations.append([rows, columns])

            elif random.randrange(1000) < ROCK_DENSITY: rock_locations.append([rows, columns])

            if [rows + 1, columns] in bush_locations or \
                    [rows - 1, columns] in bush_locations or \
                    [rows, columns + 1] in bush_locations or \
                    [rows, columns - 1] in bush_locations:
                        if random.randrange(80) < ROCK_DENSITY:
                            bush_locations.append([rows, columns])
            elif (random.randrange(1000) > 1000 - ROCK_DENSITY):
                bush_locations.append([rows, columns])


    #place player in the middle of the screen
    playerPos = [WIDTH / 2, HEIGHT / 2]
    first_it = True #Variable to keep track of first iteration
    game_running = True
    searchingFor = 1
    inv_count = 0

    print(nextPos)
    print(playerPos)

    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit
            elif (event.type == USEREVENT):
                print("GAME END")
                game_running = False

        #run scoreboard code
        if (game_running):
            value_label = font_renderer.render("Value: " + str(value), 1, (255, 255, 255))
            #steps_label = font_renderer.render("Steps: " + str(value), 1, (255, 255, 255))
            pX = playerPos[0]
            pY = playerPos[1]
            #Code that gets coordinates for object being searched for
            for i in range(1, len(game_items) + 1):
                if searchingFor == i:
                    oX = sorted_list[i - 1].location[0]
                    oY = sorted_list[i - 1].location[1]
                elif (i > len(game_items)):
                    game_running = False

            #Generate random direction, move, calculate if closer, move again.
            if (pX == oX and pY == oY):
                #Collect item
                for i in game_items:
                    if (pX == game_items[i].location[0] and \
                            pY == game_items[i].location[1] and \
                            game_items[i].hidden == False):
                        game_items[i].hidden = True
                        DISPLAYSURF.blit(i, (WIDTH * 37, HEIGHT))
                        value += game_items[i].value
                        print(value)
                        print("FOUND ITEM")
                        sound1.play()
                searchingFor += 1
            if searchingFor > len(game_items):
                getScore(value)
                game_running = False
                print("END IT NOW!")
                pygame.quit()
                sys.exit

            #Searching algorithm
            if (pX < oX):
                playerPos[0] += 1
            elif (pX > oX):
                playerPos[0] -= 1
            if (pY < oY):
                playerPos[1] += 1
            elif (pY > oY):
                playerPos[1] -= 1
            steps += 1
        
        for row in range(HEIGHT):
            for column in range(WIDTH + INV_WIDTH * TILESIZE):
                DISPLAYSURF.blit(BG, (column * TILESIZE, row * TILESIZE))
        DISPLAYSURF.blit(inv_label, (WIDTH * TILESIZE + 5, TILESIZE / 2))
        DISPLAYSURF.blit(value_label, (WIDTH * TILESIZE, TILESIZE * HEIGHT / 2))
        #Display player, sand, rocks and bushes
        for row in range(HEIGHT):
            for column in range(WIDTH):
                DISPLAYSURF.blit(SAND, (column * TILESIZE, row * TILESIZE))
                DISPLAYSURF.blit(player, (playerPos[0] * TILESIZE,(playerPos[1]) * TILESIZE))
                if [column, row] in rock_locations:
                    DISPLAYSURF.blit(STONE, (column * TILESIZE, row * TILESIZE))
                if [column, row] in bush_locations:
                    DISPLAYSURF.blit(BUSH, (column * TILESIZE, row * TILESIZE))
                if [column, row] in water_locations:
                    DISPLAYSURF.blit(WATER, (column * TILESIZE, row * TILESIZE))

        for row in range(HEIGHT):
            for row in range(WIDTH, WIDTH + INV_WIDTH * TILESIZE):
                DISPLAYSURF.blit(WATER, (column * TILESIZE, row * TILESIZE))
        
        #Display items if not already collected
        inv_count = 0
        for i in game_items:
            if (game_items[i].hidden != True):
                DISPLAYSURF.blit(i, (game_items[i].location[0] * TILESIZE, game_items[i].location[1] * TILESIZE))
                #Draw blue lines
                pygame.draw.line(DISPLAYSURF, BLUE, (playerPos[0] * TILESIZE,
                    playerPos[1] * TILESIZE), (game_items[i].location[0] *
                        TILESIZE, game_items[i].location[1] * TILESIZE), 2)
            else:
                inv_count += 1
                DISPLAYSURF.blit(i, (WIDTH * TILESIZE + 32, 5 + inv_count * TILESIZE))

        pygame.display.update()
        clock.tick(60)
