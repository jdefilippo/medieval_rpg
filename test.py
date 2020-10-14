import pygame as pg
import random
import numpy as np




SCREEN_WIDTH  = 400
SCREEN_LENGTH = 400
TILE_SIZE = 16

pg.init()
done = False
screen = pg.display.set_mode((SCREEN_LENGTH,SCREEN_WIDTH))
screen_rect = screen.get_rect()

charSheet = pg.image.load('characters.png')
terrainSheet = pg.image.load('basictiles.png')
size = charSheet.get_size()


map = np.array([   [10, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11],
                   [10, 10,  11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11],
                   [11, 10,  11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11],
                   [11, 10,  11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11],
                   [11, 10,  11, 11,11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11],
                   [11, 10,  11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11],
                   [11, 10,  11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11],
                   [11, 10,  11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11],
                   [11, 10,  11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11],
                   [11, 10,  10,  10,  10,  11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11],
                   [11, 11, 11, 11, 11,10,  13, 13, 13, 13, 13, 13,  11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11],
                   [11, 11, 11, 11, 11, 11, 13,  13,  13,  13,  13,  13,  11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11],
                   [11, 11, 11, 11, 11, 13, 13,  13,  13,  11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11],
                   [11, 11, 11, 11, 11, 11, 13,  13,  11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11],
                   [11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11],
                   [11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11],
                   [11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11],
                   [11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11],
                   [11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11],
                   [11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11],
                   [11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11],
                   [11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11],
                   [11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11],
                   [11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11],
                   [11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11]])



WHITE = (255, 255, 255)
RED = (255, 0, 0)

#set(13,)
    #odd = False
    #for x in range(0,50):
    #    for y in range(0,37):
    #        if odd:
    #            screen.blit(basicTiles[11], (x*16,y*16))
    #            odd = False
    #        else:
    #            screen.blit(basicTiles[11], (x*16,y*16))
    #            odd = True

def drawMap():
    for x in range(0,SCREEN_LENGTH//TILE_SIZE):
        for y in range(0,SCREEN_WIDTH//TILE_SIZE):
            screen.blit(basicTiles[map[x,y]],(x*16,y*16))

    

def strip_from_sheet(sheet, start, size, columns, rows):
    frames = []
    for j in range(rows):
        for i in range(columns):
            location = (start[0]+size[0]*i, start[1]+size[1]*j)
            frames.append(sheet.subsurface(pg.Rect(location, size)))
    return frames

characters = strip_from_sheet(charSheet,(0,0),(16,16),12,8)
basicTiles = strip_from_sheet(terrainSheet,(0,0),(16,16),8,10)

class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = characterDict["PlayerLookEast"].convert_alpha()
        self.rect = self.image.get_rect()
        self.prevX = 0
        self.prevY = 0 
        self.lastMove = -1
    
    def moveRight(self, pixels):

        if self.lastMove == 0:
            self.image = characterDict["PlayerMoveEast2"].convert_alpha()
        else:
            self.image = characterDict["PlayerMoveEast"].convert_alpha()

        self.prevX = self.rect.x
        self.rect.x += pixels 
        self.rect.clamp_ip(screen_rect)  
        self.lastMove = 0

    def moveLeft(self, pixels):
        if self.lastMove == 1:
            self.image = characterDict["PlayerMoveWest2"].convert_alpha()
        else:
            self.image = characterDict["PlayerMoveWest"].convert_alpha()
        self.prevX = self.rect.x
        self.rect.x -= pixels
        self.rect.clamp_ip(screen_rect)
        self.lastMove = 1


    def moveDown(self,pixels):
        if self.lastMove == 2:
            self.image = characterDict["PlayerMoveSouth2"].convert_alpha()
        else:
            self.image = characterDict["PlayerMoveSouth"].convert_alpha()
        self.prevY = self.rect.y
        self.rect.y += pixels
        self.rect.clamp_ip(screen_rect)
        self.lastMove = 2


    def moveUp(self,pixels):
        if self.lastMove == 2:
            self.image = characterDict["PlayerMoveNorth2"].convert_alpha()
        else:
            self.image = characterDict["PlayerMoveNorth"].convert_alpha()
        self.prevY = self.rect.y
        self.rect.y -= pixels
        self.rect.clamp_ip(screen_rect)
        self.lastMove = 3


    def rest(self):
        if self.lastMove == 0:
            self.image = characterDict["PlayerLookEast"].convert_alpha()
        elif self.lastMove == 1:
            self.image = characterDict["PlayerLookWest"].convert_alpha()
        elif self.lastMove == 2:
            self.image = characterDict["PlayerLookSouth"].convert_alpha()        
        elif self.lastMove == 3:
            self.image = characterDict["PlayerLookNorth"].convert_alpha()






class Wall(pg.sprite.Sprite):
    def __init__(self,  width, height, x, y):
        super().__init__()
        self.width = width
        self.height = height
        #self.image = pg.Surface([self.width, self.height])
        #self.image.fill(RED)
        self.image = basicTiles[1].convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

#This will be a list that will contain all the sprites we intend to use in our game.
all_sprites_list = pg.sprite.Group()

terrain = {} 
terrain["Grass"] = basicTiles[11]
terrain["Flowers"] = basicTiles[12]
terrain["StoneFloor"] = basicTiles[1]

characterDict = {}
characterDict["PlayerLookSouth"] = characters[7]
characterDict["PlayerLookWest"] = characters[7+12]
characterDict["PlayerLookEast"]  = characters[7+12*2]
characterDict["PlayerLookNorth"] =  characters[7+12*3]

characterDict["PlayerMoveSouth"] = characters[6]
characterDict["PlayerMoveWest"] = characters[6+12]
characterDict["PlayerMoveEast"]  = characters[6+12*2]
characterDict["PlayerMoveNorth"] =  characters[6+12*3]


characterDict["PlayerMoveSouth2"] = characters[8]
characterDict["PlayerMoveWest2"] = characters[8+12]
characterDict["PlayerMoveEast2"]  = characters[8+12*2]
characterDict["PlayerMoveNorth2"] =  characters[8+12*3]


#for x in range(0,50):
#    for y in range(0,37):
#        screen.blit(basicTiles[11], (x*16,y*16))


player = Player()

#ghost = Ghost()

widthTile = 16
lenTile   = 16

#Wall(lenTile,TILE_SIZE,100,0)
#walls = [] 
#for i in range(0, 10):
#    walls.append(Wall(TILE_SIZE,TILE_SIZE,100, i*16))
#wallsRect = [i.rect for i in walls]



all_sprites_list.add(player)
###all_sprites_list.add(walls)


clock=pg.time.Clock()
step = 4


while not done:

    player.lastMove = -1 

    for event in pg.event.get(): 
        if event.type == pg.QUIT:
            done = True
        

    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT]:
            player.moveLeft(step)

    if keys[pg.K_RIGHT]:
            player.moveRight(step)

    if keys[pg.K_DOWN]:
            player.moveDown(step)

    if keys[pg.K_UP]:
            player.moveUp(step)

    #all_sprites_list.sprites()[1].collision(all_sprites_list.sprites()[0])
    

    ### WALL LOGIC
    #for wall in walls[:]: 
    #    if player.rect.colliderect(wall.rect):
    #        player.rect.x = player.prevX
    #        player.rect.y = player.prevY 

    drawMap()




    all_sprites_list.update()
    all_sprites_list.draw(screen)

    player.rest()

    #pg.display.update()
    pg.display.flip()

    clock.tick(30)


