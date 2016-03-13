import pygame
from pygame.locals import *
import sys
import random

#Constants#
FPS = 30

#Map data#
MAPHEIGHT = 20
TILESIZE = 32
MAPWIDTH = 20
TREE_DENSITY = 10
#Tiles#
DIRT = 0
GRASS = 1
STONE = 3
WATER = 4
SAND = 5
WOOD = 6
METAL = 7

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


tilemap = []
i = 0


def read_file(f):
    ''' File reading function

    Function takes a string as name of file (f), opens, reads the contents and
    returns contents'''
    file_object = open(f, 'r')
    return file_object.read()

def parse_map(data):
    '''Parses map data into lists

    Takes characters and if matching tile types, builds a list within a list of
    entire map'''
    tilemap_tmp = []
    for line in data:
        if line == '#':
            tilemap_tmp.append(SAND)
        elif line == '~':
            tilemap_tmp.append(WATER)
        elif line == 'v':
            tilemap_tmp.append(SAND)
        elif line == '_':
            tilemap_tmp.append(GRASS)
        elif line == '"':
            tilemap_tmp.append(DIRT)
        elif line == '=':
            tilemap_tmp.append(WOOD)
        elif line == '/':
            tilemap.append(tilemap_tmp)
            #print tilemap_tmp
            tilemap_tmp = []
            


parse_map(read_file('map_data.txt'))

colors = {
        DIRT: pygame.image.load('assets/dirt.png'),
        GRASS: pygame.image.load('assets/grass.png'),
        WATER: pygame.image.load('assets/water2.png'),
        STONE: pygame.image.load('assets/stone.png'),
        SAND: pygame.image.load('assets/sand2.png'),
        WOOD: pygame.image.load('assets/wood.png'),
        METAL: pygame.image.load('assets/metal.png')
        }

playerPos = [0,0]

def display(item, location):
    '''Display assets

    Function takes a variable and a tuple as an asset and its location in order
    to display it on screen'''
    DISPLAYSURF.blit(item, (location[0] * TILESIZE, location[1] * TILESIZE))


pygame.init()
#Initialize pygame

#Set constants
FPSCLOCK = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((MAPWIDTH*TILESIZE, MAPHEIGHT*TILESIZE + 60))
INVFONT = pygame.font.SysFont("comicsansms",50)

#Load more assets

PLAYER = 1
TREE = 2
BONE = 3
COIN = 4

game_objects = {
    PLAYER: pygame.image.load('assets/player.png').convert_alpha(),
    TREE: pygame.image.load('assets/cactus.png').convert_alpha()
    }


game_items = {
    BONE: pygame.image.load('assets/bone.png').convert_alpha(),
    COIN: pygame.image.load('assets/coin.png').convert_alpha()
    }

inventory = {
    BONE: 0,
    COIN: 0
    }
TREE_LOCATIONS = []


for row in range(MAPHEIGHT):
    for column in range(MAPWIDTH):
        if tilemap[row][column] == 5:
            if random.randrange(100) < TREE_DENSITY:
                #Save all coordinates of tree locations into list
                TREE_LOCATIONS.append([column, row])


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        #Movement
        elif event.type == KEYDOWN:
            if (event.key == K_RIGHT) and ((playerPos[0] + 1) < MAPWIDTH) and tilemap[playerPos[1]][playerPos[0] + 1] != 4:
                playerPos[0] += 1
            elif (event.key == K_LEFT) and ((playerPos[0] - 1) >= 0) and tilemap[playerPos[1]][playerPos[0] - 1] != 4:
                playerPos[0] -= 1
            elif (event.key == K_DOWN) and ((playerPos[1] + 1) < MAPHEIGHT) and tilemap[playerPos[1] + 1][playerPos[0]] != 4:
                playerPos[1] += 1
            elif (event.key == K_UP) and ((playerPos[1] - 1) >= 0) and tilemap[playerPos[1] - 1][playerPos[0]] != 4:
                playerPos[1] -= 1
            #print tilemap[playerPos[1]][playerPos[0]]


    #Draw tiles
    for row in range(MAPHEIGHT):
        for column in range(MAPWIDTH):
            display(game_items[BONE], (3, 4))
            display(game_items[COIN], (12, 8))
            display(colors[tilemap[row][column]], (column, row))
            display(game_objects[PLAYER], (playerPos[0], playerPos[1]))
            if [row, column] in TREE_LOCATIONS:
                display(game_objects[TREE], (row, column))


    placePosition = 10
    for i in game_items:
        DISPLAYSURF.blit(game_items[i], (placePosition, MAPHEIGHT * TILESIZE + 20))
        placePosition += 40
        textObj = INVFONT.render(str(inventory[i]), True, WHITE, BLACK)
        DISPLAYSURF.blit(textObj, (placePosition, MAPHEIGHT*TILESIZE + 20))
        placePosition += 60
        

    pygame.display.update()
    pygame.display.flip()
    #FPSCLOCK.tick()
