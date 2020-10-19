import numpy as np
import enum
import pandas as pd
import pygame as pg

from model import *

SCREEN_WIDTH  = 400
SCREEN_LENGTH = 400
TILE_SIZE = 16
THINGS_TILE_OFFSET = 1000

class MerchantSprite(pg.sprite.Sprite):
    def __init__(self,x,y, charSet, screenRec):
        super().__init__() 
        self.charSet = charSet
        self.image = self.charSet[ChImg.tLookWest].convert_alpha()
        self.rect = self.image.get_rect()
        self.prevX = 0
        self.prevY = 0 
        self.lastMove = -1
        self.rect.x = x 
        self.rect.y = y
        self.screenRec = screenRec


    
    def move_right(self, pixels):

        if self.lastMove == 0:
            self.image = self.charSet[ChImg.pMoveEast2].convert_alpha()
        else:
            self.image = self.charSet[ChImg.pMoveEast].convert_alpha()

        self.prevX = self.rect.x
        self.rect.x += pixels 
        self.rect.clamp_ip(self.screenRec)  
        self.lastMove = 0

    def move_left(self, pixels):
        if self.lastMove == 1:
            self.image = self.charSet[ChImg.pMoveWest2].convert_alpha()
        else:
            self.image = self.charSet[ChImg.pMoveWest].convert_alpha()
        self.prevX = self.rect.x
        self.rect.x -= pixels
        self.rect.clamp_ip(self.screenRec)
        self.lastMove = 1


    def move_down(self,pixels):
        if self.lastMove == 2:
            self.image = self.charSet[ChImg.pMoveSouth2].convert_alpha()
        else:
            self.image = self.charSet[ChImg.pMoveSouth].convert_alpha()
        self.prevY = self.rect.y
        self.rect.y += pixels
        self.rect.clamp_ip(self.screenRec)
        self.lastMove = 2


    def move_up(self,pixels):
        if self.lastMove == 2:
            self.image = self.charSet[ChImg.pMoveNorth2].convert_alpha()
        else:
            self.image = self.charSet[ChImg.pMoveNorth].convert_alpha()
        self.prevY = self.rect.y
        self.rect.y -= pixels
        self.rect.clamp_ip(self.screenRec)
        self.lastMove = 3


    def rest(self):
        if self.lastMove == 0:
            self.image = self.charSet[ChImg.pLookEast].convert_alpha()
        elif self.lastMove == 1:
            self.image = self.charSet[ChImg.pLookWest].convert_alpha()
        elif self.lastMove == 2:
            self.image = self.charSet[ChImg.pLookSouth].convert_alpha()        
        elif self.lastMove == 3:
            self.image = self.charSet[ChImg.pLookNorth].convert_alpha()


    


class PlayerSprite(pg.sprite.Sprite):
    def __init__(self, charSet, screenRec):
        super().__init__() 
        self.charSet = charSet
        self.image = self.charSet[ChImg.pLookEast].convert_alpha()
        self.rect = self.image.get_rect()
        self.prevX = 0
        self.prevY = 0 
        self.lastMove = -1
        self.playerModel = PlayerModel()
        self.screenRec = screenRec

    
    def move_right(self, pixels):

        if self.lastMove == 0:
            self.image = self.charSet[ChImg.pMoveEast2].convert_alpha()
        else:
            self.image = self.charSet[ChImg.pMoveEast].convert_alpha()

        self.prevX = self.rect.x
        self.rect.x += pixels 
        self.rect.clamp_ip(self.screenRec)  
        self.lastMove = 0

    def move_left(self, pixels):
        if self.lastMove == 1:
            self.image = self.charSet[ChImg.pMoveWest2].convert_alpha()
        else:
            self.image = self.charSet[ChImg.pMoveWest].convert_alpha()
        self.prevX = self.rect.x
        self.rect.x -= pixels
        self.rect.clamp_ip(self.screenRec)
        self.lastMove = 1


    def move_down(self,pixels):
        if self.lastMove == 2:
            self.image = self.charSet[ChImg.pMoveSouth2].convert_alpha()
        else:
            self.image = self.charSet[ChImg.pMoveSouth].convert_alpha()
        self.prevY = self.rect.y
        self.rect.y += pixels
        self.rect.clamp_ip(self.screenRec)
        self.lastMove = 2


    def move_up(self,pixels):
        if self.lastMove == 2:
            self.image = self.charSet[ChImg.pMoveNorth2].convert_alpha()
        else:
            self.image = self.charSet[ChImg.pMoveNorth].convert_alpha()
        self.prevY = self.rect.y
        self.rect.y -= pixels
        self.rect.clamp_ip(self.screenRec)
        self.lastMove = 3


    def rest(self):
        if self.lastMove == 0:
            self.image = self.charSet[ChImg.pLookEast].convert_alpha()
        elif self.lastMove == 1:
            self.image = self.charSet[ChImg.pLookWest].convert_alpha()
        elif self.lastMove == 2:
            self.image = self.charSet[ChImg.pLookSouth].convert_alpha()        
        elif self.lastMove == 3:
            self.image = self.charSet[ChImg.pLookNorth].convert_alpha()


class ItemSprite(pg.sprite.Sprite): 
    def __init__(self, x, y, img, itemModel, usedImg):
        super().__init__()
        self.width =  TILE_SIZE
        self.height = TILE_SIZE
        self.image = img.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.itemModel = itemModel
        self.usedImage = usedImg.convert_alpha()
        print("Made")
        print(self.rect.x, self.rect.y)

class ImpassableTile(pg.sprite.Sprite):
    def __init__(self, x, y, tileImg ):
        super().__init__()
        self.width =  TILE_SIZE
        self.height = TILE_SIZE
        self.image = tileImg.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class DoorTile(pg.sprite.Sprite):
    def __init__(self, x, y, closeImg, openImg ):
        super().__init__()
        self.width =  TILE_SIZE
        self.height = TILE_SIZE
        self.image = closeImg.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.closeImg = closeImg
        self.openImg = openImg

class AnimationTile(pg.sprite.Sprite):
    def __init__(self, x, y, frames ):
        super().__init__()
        self.width =  TILE_SIZE
        self.height = TILE_SIZE
        self.image = frames[0].convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.frames = frames 
        self.index  = 0 

    def animate(self):
        self.image = self.frames[self.index].convert_alpha()
        if self.index == len(self.frames)-1:
            self.index = 0
        else:
            self.index += 1 

    def update(self, *args):
        self.animate()


    
    
    #def animate(self):
    #    while True:
    #        for frame in self.frames[0]:
    #            self.image = frame
    #            yield None
    #            yield None

    #def update(self, *args):
    #    self.animate.next()

class ChImg: 
    pLookNorth  = 43
    pLookSouth  = 7
    pLookEast   = 31
    pLookWest   = 19
    pMoveNorth  = 42
    pMoveSouth  = 6   
    pMoveEast   = 30
    pMoveWest   = 18
    pMoveNorth2 = 44
    pMoveSouth2 = 8
    pMoveEast2  = 32
    pMoveWest2  = 20
    tLookSouth  = 4
    tLookWest   = 16
    tLookEast   = 28
    tLookNorth  = 40

class TileImg:
    wall1  = 0
    wall2  = 1
    wall3  = 2
    wall4  = 3
    wall5  = 4
    wall6  = 5
    wall7  = 6
    wall8  = 7
    rocks  = 68
    jewels = 69
    water  = 13 
    evergreen = 30
    basictree = 38
    rockface  = 15
    succulent = 20
    ocean = 13
    monument = 47
    doorClosed   = THINGS_TILE_OFFSET
    doorOpening1 = THINGS_TILE_OFFSET + 12 
    doorOpening2 = THINGS_TILE_OFFSET + 24 
    doorOpening3 = THINGS_TILE_OFFSET + 36 
    torch1       = THINGS_TILE_OFFSET + 48 
    torch2       = THINGS_TILE_OFFSET + 49 
    torch3       = THINGS_TILE_OFFSET + 50 
    torch4       = THINGS_TILE_OFFSET + 51 
    '''
    torch1       = 1048
    torch2       = 1060
    torch3       = 1072 
    torch4       = 1084
    '''


class GameMap():
    def __init__(self, screen, mapFile, charFile, basicFile, thingsFile):
        self.screen          = screen
        self.screen_rect     = screen.get_rect()
        self.mapFile         = mapFile
        self.charFile        = charFile
        self.basicFile       = basicFile
        self.thingsFile      = thingsFile
        self.charTileSet     = None
        self.basicTileSet    = None
        self.thingsTileSet   = None
        self.layer1          = np.empty(1)
        self.layer2          = np.empty(1)
        self.layer3          = np.empty(1)
        self.layer4          = np.empty(1)
        self.blockedTiles    = None
        self.itemTiles       = None 
        self.animatedTiles   = None   
        self.doorTiles       = None
        self.blockedSprites  = []
        self.itemSprites     = []
        self.friendSprites   = [] 
        self.doorSprites     = [] 
        self.animatedSprites = [] 
        self.playerSprite    = None

    def get_friend_sprites(self):
        return self.friendSprites

    def get_player_sprites(self):
        return self.playerSprite

    def get_blocked_sprites(self):
        return self.blockedSprites 

    def get_item_sprites(self):
        return self.itemSprites

    def get_door_sprites(self):
        return self.doorSprites

    def get_animated_sprites(self):
        return self.animatedSprites

    def initialize(self):        
        df = pd.read_excel(self.mapFile, sheet_name="L1", header=None)
        self.layer1 = np.transpose(df.to_numpy())

        df = pd.read_excel(self.mapFile, sheet_name="L2", header=None)
        self.layer2 = np.transpose(df.to_numpy())

        df = pd.read_excel(self.mapFile, sheet_name="L3", header=None)
        self.layer3 = np.transpose(df.to_numpy())

        df = pd.read_excel(self.mapFile, sheet_name="L4", header=None)
        self.layer4 = np.transpose(df.to_numpy())
      
        self.charTileSet   = self.strip_from_sheet(pg.image.load(self.charFile),(0,0),(TILE_SIZE,TILE_SIZE),12,8)
        self.basicTileSet  = self.strip_from_sheet(pg.image.load(self.basicFile),(0,0),(TILE_SIZE,TILE_SIZE),8,10)
        self.thingsTileSet = self.strip_from_sheet(pg.image.load(self.thingsFile),(0,0),(TILE_SIZE,TILE_SIZE),12,8)

        self.itemTiles     = set([TileImg.rocks,TileImg.jewels])
        self.blockedTiles  = set([TileImg.wall1, TileImg.wall2, TileImg.wall3, TileImg.wall4,
                                  TileImg.wall5, TileImg.wall6, TileImg.wall7, TileImg.wall8,
                                  TileImg.ocean, TileImg.evergreen, TileImg.basictree, 
                                  TileImg.succulent, TileImg.rockface, TileImg.monument])
        self.animatedTiles = set([TileImg.torch1])
        self.doorTiles     = set([TileImg.doorClosed, TileImg.doorOpening1, TileImg.doorOpening2, TileImg.doorOpening3])


      
        self.playerSprite    = PlayerSprite(self.charTileSet, self.screen_rect)
        merchant = MerchantSprite(125,336, self.charTileSet, self.screen_rect)
        self.friendSprites = [merchant]



        for x in range(0,SCREEN_LENGTH//TILE_SIZE):
            for y in range(0,SCREEN_WIDTH//TILE_SIZE):
                ### Basic Tile Set 
                if self.layer1[x,y] in self.blockedTiles:
                    self.blockedSprites.append(ImpassableTile(x*TILE_SIZE, y*TILE_SIZE,self.basicTileSet[self.layer1[x,y]])) 
                if self.layer2[x,y] in self.blockedTiles:
                    self.blockedSprites.append(ImpassableTile(x*TILE_SIZE, y*TILE_SIZE,self.basicTileSet[self.layer2[x,y]])) 
                if self.layer2[x,y] in self.itemTiles:
                    if self.layer2[x,y] == TileImg.rocks:
                        self.itemSprites.append(ItemSprite(x*TILE_SIZE, y*TILE_SIZE,self.basicTileSet[self.layer2[x,y]], Coin(), self.basicTileSet[self.layer1[x,y]] )) 
                    elif self.layer2[x,y] == TileImg.jewels: 
                        self.itemSprites.append(ItemSprite(x*TILE_SIZE, y*TILE_SIZE,self.basicTileSet[self.layer2[x,y]], Jewel(), self.basicTileSet[self.layer1[x,y]] )) 

                ### Things Tile Set
                if self.layer2[x,y] in self.doorTiles:
                    self.doorSprites.append(DoorTile(x*TILE_SIZE, y*TILE_SIZE,self.thingsTileSet[self.layer2[x,y]-THINGS_TILE_OFFSET],self.thingsTileSet[self.layer2[x,y]-1000+36] ))  
                if self.layer2[x,y] in self.animatedTiles:
                    self.animatedSprites.append(AnimationTile(x*TILE_SIZE, y*TILE_SIZE,[self.thingsTileSet[self.layer2[x,y]-THINGS_TILE_OFFSET],
                                                                                    self.thingsTileSet[self.layer2[x,y]-THINGS_TILE_OFFSET+1],
                                                                                    self.thingsTileSet[self.layer2[x,y]-THINGS_TILE_OFFSET+2]]))



    def render_display(self, usedSpritesLocs=None):
        for x in range(0,SCREEN_LENGTH//TILE_SIZE):
            for y in range(0,SCREEN_WIDTH//TILE_SIZE):                      
                if self.layer1[x,y] != -1 and self.layer1[x,y] < THINGS_TILE_OFFSET:   
                    self.screen.blit(self.basicTileSet[self.layer1[x,y]],(x*TILE_SIZE,y*TILE_SIZE))
                if self.layer2[x,y] != -1 and self.layer2[x,y] < THINGS_TILE_OFFSET:                    
                    #hideTile = False
                    if ((x*TILE_SIZE, y*TILE_SIZE) not in usedSpritesLocs):
                        self.screen.blit(self.basicTileSet[self.layer2[x,y]],(x*TILE_SIZE,y*TILE_SIZE)) 


                    '''
                    if len(usedSpritesLocs)>0:
                        for loc in usedSpritesLocs:  
                            if loc[0] == x*TILE_SIZE and loc[1] == y*TILE_SIZE: 
                                hideTile = True
                                break
                    if not hideTile: 
                        self.screen.blit(self.basicTileSet[self.layer2[x,y]],(x*TILE_SIZE,y*TILE_SIZE)) 
                    '''
                if self.layer3[x,y] != -1 and self.layer3[x,y] < THINGS_TILE_OFFSET:                             
                    self.screen.blit(self.basicTileSet[self.layer3[x,y]],(x*TILE_SIZE,y*TILE_SIZE))         
                if self.layer4[x,y] != -1 and self.layer4[x,y] < THINGS_TILE_OFFSET:                             
                    self.screen.blit(self.basicTileSet[self.layer4[x,y]],(x*TILE_SIZE,y*TILE_SIZE))  

                #if self.layer4[x,y] != -1 and self.layer4[x,y] >= 1000:    ### TODO: make this more elegant
                #    self.screen.blit(self.thingsTileSet[self.layer4[x,y]-1000],(x*TILE_SIZE,y*TILE_SIZE))



    def strip_from_sheet(self, sheet, start, size, columns, rows):
        frames = []
        for j in range(rows):
            for i in range(columns):
                location = (start[0]+size[0]*i, start[1]+size[1]*j)
                frames.append(sheet.subsurface(pg.Rect(location, size)))
        return frames
