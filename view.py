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
    def __init__(self,x,y, char_set, screen_rec):
        super().__init__() 
        self.char_set = char_set
        self.image = self.char_set[ChImg.T_LOOK_WEST].convert_alpha()
        self.rect = self.image.get_rect()
        self.prev_x = 0
        self.prev_y = 0 
        self.last_move = -1
        self.rect.x = x 
        self.rect.y = y
        self.screen_rec = screen_rec
        self.first_loc_x   = x 
        self.first_loc_y   = y 
        self.second_loc_x  = x-64
        self.second_loc_y  = y
        self.patrol_state = 1
        self.clock       = None

    def set_clock(self,clock):
        self.clock = clock



    
    def move_right(self, pixels):

        if self.last_move == 0:
            self.image = self.char_set[ChImg.T_MOVE_EAST2].convert_alpha()
        else:
            self.image = self.char_set[ChImg.T_MOVE_EAST].convert_alpha()

        self.prev_x = self.rect.x
        self.rect.x += pixels 
        self.rect.clamp_ip(self.screen_rec)  
        self.last_move = 0

    def move_left(self, pixels):
        if self.last_move == 1:
            self.image = self.char_set[ChImg.T_MOVE_WEST2].convert_alpha()
        else:
            self.image = self.char_set[ChImg.T_MOVE_WEST].convert_alpha()
        self.prev_x = self.rect.x
        self.rect.x -= pixels
        self.rect.clamp_ip(self.screen_rec)
        self.last_move = 1


    def move_down(self,pixels):
        if self.last_move == 2:
            self.image = self.char_set[ChImg.T_MOVE_SOUTH2].convert_alpha()
        else:
            self.image = self.char_set[ChImg.T_MOVE_SOUTH].convert_alpha()
        self.prev_y = self.rect.y
        self.rect.y += pixels
        self.rect.clamp_ip(self.screen_rec)
        self.last_move = 2


    def move_up(self,pixels):
        if self.last_move == 2:
            self.image = self.char_set[ChImg.T_MOVE_NORTH2].convert_alpha()
        else:
            self.image = self.char_set[ChImg.T_MOVE_NORTH].convert_alpha()
        self.prev_y = self.rect.y
        self.rect.y -= pixels
        self.rect.clamp_ip(self.screen_rec)
        self.last_move = 3


    def rest(self):
        if self.last_move == 0:
            self.image = self.char_set[ChImg.T_LOOK_EAST].convert_alpha()
        elif self.last_move == 1:
            self.image = self.char_set[ChImg.T_LOOK_WEST].convert_alpha()
        elif self.last_move == 2:
            self.image = self.char_set[ChImg.T_LOOK_SOUTH].convert_alpha()        
        elif self.last_move == 3:
            self.image = self.char_set[ChImg.T_LOOK_NORTH].convert_alpha()

    def patrol(self):
        if(self.rect.x <= self.first_loc_x and self.rect.x > self.second_loc_x and self.patrol_state == 1):
            #print("Case1")
            self.move_left(1)    
        elif(self.rect.x == self.second_loc_x and self.patrol_state == 1):
            #print("Case2")
            self.patrol_state = 2
            #self.move_right(1) 
        elif(self.rect.x < self.first_loc_x and self.patrol_state == 2):
            #print("Case3")
            self.move_right(1) 
        elif(self.rect.x == self.first_loc_x and self.patrol_state == 2):
            self.move_left(1)
            self.patrol_state = 1
        else:
            print("lost")

    def update(self, *args):
        pass
        #self.patrol()



    


class PlayerSprite(pg.sprite.Sprite):
    def __init__(self, char_set, screen_rec):
        super().__init__() 
        self.char_set = char_set
        self.image = self.char_set[ChImg.P_LOOK_EAST].convert_alpha()
        self.rect = self.image.get_rect()
        self.prev_x = 0
        self.prev_y = 0 
        self.last_move = -1
        self.player_model = PlayerModel()
        self.screen_rec = screen_rec

    
    def move_right(self, pixels):

        if self.last_move == 0:
            self.image = self.char_set[ChImg.P_MOVE_EAST2].convert_alpha()
        else:
            self.image = self.char_set[ChImg.P_MOVE_EAST].convert_alpha()

        self.prev_x = self.rect.x
        self.rect.x += pixels 
        self.rect.clamp_ip(self.screen_rec)  
        self.last_move = 0

    def move_left(self, pixels):
        if self.last_move == 1:
            self.image = self.char_set[ChImg.P_MOVE_WEST2].convert_alpha()
        else:
            self.image = self.char_set[ChImg.P_MOVE_WEST].convert_alpha()
        self.prev_x = self.rect.x
        self.rect.x -= pixels
        self.rect.clamp_ip(self.screen_rec)
        self.last_move = 1


    def move_down(self,pixels):
        if self.last_move == 2:
            self.image = self.char_set[ChImg.P_MOVE_SOUTH2].convert_alpha()
        else:
            self.image = self.char_set[ChImg.P_MOVE_SOUTH].convert_alpha()
        self.prev_y = self.rect.y
        self.rect.y += pixels
        self.rect.clamp_ip(self.screen_rec)
        self.last_move = 2


    def move_up(self,pixels):
        if self.last_move == 2:
            self.image = self.char_set[ChImg.P_MOVE_NORTH2].convert_alpha()
        else:
            self.image = self.char_set[ChImg.P_MOVE_NORTH].convert_alpha()
        self.prev_y = self.rect.y
        self.rect.y -= pixels
        self.rect.clamp_ip(self.screen_rec)
        self.last_move = 3


    def rest(self):
        if self.last_move == 0:
            self.image = self.char_set[ChImg.P_LOOK_EAST].convert_alpha()
        elif self.last_move == 1:
            self.image = self.char_set[ChImg.P_LOOK_WEST].convert_alpha()
        elif self.last_move == 2:
            self.image = self.char_set[ChImg.P_LOOK_SOUTH].convert_alpha()        
        elif self.last_move == 3:
            self.image = self.char_set[ChImg.P_LOOK_NORTH].convert_alpha()


class ItemSprite(pg.sprite.Sprite): 
    def __init__(self, x, y, img, item_model, used_img):
        super().__init__()
        self.width =  TILE_SIZE
        self.height = TILE_SIZE
        self.image = img.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.item_model = item_model
        self.usedImage = used_img.convert_alpha()
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
    P_LOOK_NORTH  = 43
    P_LOOK_SOUTH  = 7
    P_LOOK_EAST   = 31
    P_LOOK_WEST   = 19
    P_MOVE_NORTH  = 42
    P_MOVE_SOUTH  = 6   
    P_MOVE_EAST   = 30
    P_MOVE_WEST   = 18
    P_MOVE_NORTH2 = 44
    P_MOVE_SOUTH2 = 8
    P_MOVE_EAST2  = 32
    P_MOVE_WEST2  = 20
    T_LOOK_SOUTH  = 4
    T_LOOK_WEST   = 16
    T_LOOK_EAST   = 28
    T_LOOK_NORTH  = 40
    T_MOVE_SOUTH  = 6
    T_MOVE_SOUTH2 = 2 
    T_MOVE_WEST   = 15 
    T_MOVE_WEST2  = 17
    T_MOVE_EAST   = 27
    T_MOVE_EAST2  = 29
    T_MOVE_NORTH  = 39
    T_MOVE_NORTH2 = 41


class TileImg:
    WALL_1  = 0
    WALL_2  = 1
    WALL_3  = 2
    WALL_4  = 3
    WALL_5  = 4
    WALL_6  = 5
    WALL_7  = 6
    WALL_8  = 7
    ROCKS  = 68
    JEWELS = 69
    ARMOR  = 70
    MAGIC_SPELL = 71
    SWORD  = 78
    HEALTH_POTION = 79
    MUSHROOMS = 44
    WATER  = 13 
    EVERGREEN = 30
    BASIC_TREE = 38
    ROCK_FACE  = 15
    SUCCULENT = 20
    OCEAN = 13
    MONUMENT = 47
    MOUNTAIN_1 = 62
    MOUNTAIN_2 = 63
    DOOR_CLOSED   = THINGS_TILE_OFFSET
    DOOR_OPENING_1 = THINGS_TILE_OFFSET + 12 
    DOOR_OPENING_2 = THINGS_TILE_OFFSET + 24 
    DOOR_OPENING_3 = THINGS_TILE_OFFSET + 36 
    TORCH_1       = THINGS_TILE_OFFSET + 48 
    TORCH_2       = THINGS_TILE_OFFSET + 49 
    TORCH_3       = THINGS_TILE_OFFSET + 50 
    TORCH_4       = THINGS_TILE_OFFSET + 51 
    '''
    TORCH_1       = 1048
    TORCH_2       = 1060
    TORCH_3       = 1072 
    TORCH_4       = 1084
    '''


class GameMap():
    def __init__(self, screen, map_file, char_file, basic_file, things_file):
        self.screen          = screen
        self.screen_rect     = screen.get_rect()
        self.map_file         = map_file
        self.char_file        = char_file
        self.basic_file       = basic_file
        self.things_file      = things_file
        self.char_tile_set     = None
        self.basic_tile_set    = None
        self.things_tile_set   = None
        self.layer_1          = np.empty(1)
        self.layer_2          = np.empty(1)
        self.layer_3          = np.empty(1)
        self.layer_4          = np.empty(1)
        self.blocked_tiles    = None
        self.item_tiles       = None 
        self.animated_tiles   = None   
        self.door_tiles       = None
        self.blocked_sprites  = []
        self.item_sprites     = []
        self.friend_sprites   = [] 
        self.door_sprites     = [] 
        self.animated_sprites = [] 
        self.player_sprite    = None

    def get_friend_sprites(self):
        return self.friend_sprites

    def get_player_sprites(self):
        return self.player_sprite

    def get_blocked_sprites(self):
        return self.blocked_sprites 

    def get_item_sprites(self):
        return self.item_sprites

    def get_door_sprites(self):
        return self.door_sprites

    def get_animated_sprites(self):
        return self.animated_sprites

    def initialize(self):        
        df = pd.read_excel(self.map_file, sheet_name="L1", header=None)
        self.layer_1 = np.transpose(df.to_numpy())

        df = pd.read_excel(self.map_file, sheet_name="L2", header=None)
        self.layer_2 = np.transpose(df.to_numpy())

        df = pd.read_excel(self.map_file, sheet_name="L3", header=None)
        self.layer_3 = np.transpose(df.to_numpy())

        df = pd.read_excel(self.map_file, sheet_name="L4", header=None)
        self.layer_4 = np.transpose(df.to_numpy())
      
        self.char_tile_set   = self.strip_from_sheet(pg.image.load(self.char_file),(0,0),(TILE_SIZE,TILE_SIZE),12,8)
        self.basic_tile_set  = self.strip_from_sheet(pg.image.load(self.basic_file),(0,0),(TILE_SIZE,TILE_SIZE),8,10)
        self.things_tile_set = self.strip_from_sheet(pg.image.load(self.things_file),(0,0),(TILE_SIZE,TILE_SIZE),12,8)

        self.item_tiles     = set([TileImg.ROCKS,TileImg.JEWELS, TileImg.ARMOR, TileImg.MAGIC_SPELL, TileImg.SWORD, TileImg.HEALTH_POTION, TileImg.MUSHROOMS])
        self.blocked_tiles  = set([TileImg.WALL_1, TileImg.WALL_2, TileImg.WALL_3, TileImg.WALL_4,
                                  TileImg.WALL_5, TileImg.WALL_6, TileImg.WALL_7, TileImg.WALL_8,
                                  TileImg.OCEAN, TileImg.EVERGREEN, TileImg.BASIC_TREE, 
                                  TileImg.SUCCULENT, TileImg.ROCK_FACE, TileImg.MONUMENT])
        self.animated_tiles = set([TileImg.TORCH_1])
        self.door_tiles     = set([TileImg.DOOR_CLOSED, TileImg.DOOR_OPENING_1, TileImg.DOOR_OPENING_2, TileImg.DOOR_OPENING_3])


      
        self.player_sprite    = PlayerSprite(self.char_tile_set, self.screen_rect)
        merchant = MerchantSprite(125,336, self.char_tile_set, self.screen_rect)
        self.friend_sprites = [merchant]



        for x in range(0,SCREEN_LENGTH//TILE_SIZE):
            for y in range(0,SCREEN_WIDTH//TILE_SIZE):
                ### Basic Tile Set 
                if self.layer_1[x,y] in self.blocked_tiles:
                    self.blocked_sprites.append(ImpassableTile(x*TILE_SIZE, y*TILE_SIZE,self.basic_tile_set[self.layer_1[x,y]])) 
                if self.layer_2[x,y] in self.blocked_tiles:
                    self.blocked_sprites.append(ImpassableTile(x*TILE_SIZE, y*TILE_SIZE,self.basic_tile_set[self.layer_2[x,y]])) 
                if self.layer_2[x,y] in self.item_tiles:
                    if self.layer_2[x,y] == TileImg.ROCKS:
                        self.item_sprites.append(ItemSprite(x*TILE_SIZE, y*TILE_SIZE,self.basic_tile_set[self.layer_2[x,y]], Coin(), self.basic_tile_set[self.layer_1[x,y]] )) 
                    elif self.layer_2[x,y] == TileImg.JEWELS: 
                        self.item_sprites.append(ItemSprite(x*TILE_SIZE, y*TILE_SIZE,self.basic_tile_set[self.layer_2[x,y]], Jewel(), self.basic_tile_set[self.layer_1[x,y]] )) 
                    elif self.layer_2[x,y] == TileImg.ARMOR:
                        print("MADE IT")
                        self.item_sprites.append(ItemSprite(x*TILE_SIZE, y*TILE_SIZE,self.basic_tile_set[self.layer_2[x,y]], Armor(), self.basic_tile_set[self.layer_1[x,y]] )) 
                    elif self.layer_2[x,y] == TileImg.MAGIC_SPELL:
                        self.item_sprites.append(ItemSprite(x*TILE_SIZE, y*TILE_SIZE,self.basic_tile_set[self.layer_2[x,y]], MagicSpell(), self.basic_tile_set[self.layer_1[x,y]] )) 
                    elif self.layer_2[x,y] == TileImg.SWORD:
                        self.item_sprites.append(ItemSprite(x*TILE_SIZE, y*TILE_SIZE,self.basic_tile_set[self.layer_2[x,y]], Sword(), self.basic_tile_set[self.layer_1[x,y]] )) 
                    elif self.layer_2[x,y] == TileImg.HEALTH_POTION:
                        self.item_sprites.append(ItemSprite(x*TILE_SIZE, y*TILE_SIZE,self.basic_tile_set[self.layer_2[x,y]], HealthPotion(), self.basic_tile_set[self.layer_1[x,y]] )) 
                    elif self.layer_2[x,y] == TileImg.MUSHROOMS:
                        self.item_sprites.append(ItemSprite(x*TILE_SIZE, y*TILE_SIZE,self.basic_tile_set[self.layer_2[x,y]], Mushrooms(), self.basic_tile_set[self.layer_1[x,y]] ))
                    else:
                        print("Not handled!") 







                ### Things Tile Set
                if self.layer_2[x,y] in self.door_tiles:
                    self.door_sprites.append(DoorTile(x*TILE_SIZE, y*TILE_SIZE,self.things_tile_set[self.layer_2[x,y]-THINGS_TILE_OFFSET],self.things_tile_set[self.layer_2[x,y]-1000+36] ))  
                if self.layer_2[x,y] in self.animated_tiles:
                    self.animated_sprites.append(AnimationTile(x*TILE_SIZE, y*TILE_SIZE,[self.things_tile_set[self.layer_2[x,y]-THINGS_TILE_OFFSET],
                                                                                    self.things_tile_set[self.layer_2[x,y]-THINGS_TILE_OFFSET+1],
                                                                                    self.things_tile_set[self.layer_2[x,y]-THINGS_TILE_OFFSET+2]]))



    def render_display(self, usedSpritesLocs=None):
        for x in range(0,SCREEN_LENGTH//TILE_SIZE):
            for y in range(0,SCREEN_WIDTH//TILE_SIZE):                      
                if self.layer_1[x,y] != -1 and self.layer_1[x,y] < THINGS_TILE_OFFSET:   
                    self.screen.blit(self.basic_tile_set[self.layer_1[x,y]],(x*TILE_SIZE,y*TILE_SIZE))
                if self.layer_2[x,y] != -1 and self.layer_2[x,y] < THINGS_TILE_OFFSET:                    
                    #hideTile = False
                    if ((x*TILE_SIZE, y*TILE_SIZE) not in usedSpritesLocs):
                        self.screen.blit(self.basic_tile_set[self.layer_2[x,y]],(x*TILE_SIZE,y*TILE_SIZE)) 


                    '''
                    if len(usedSpritesLocs)>0:
                        for loc in usedSpritesLocs:  
                            if loc[0] == x*TILE_SIZE and loc[1] == y*TILE_SIZE: 
                                hideTile = True
                                break
                    if not hideTile: 
                        self.screen.blit(self.basic_tile_set[self.layer_2[x,y]],(x*TILE_SIZE,y*TILE_SIZE)) 
                    '''
                if self.layer_3[x,y] != -1 and self.layer_3[x,y] < THINGS_TILE_OFFSET:                             
                    self.screen.blit(self.basic_tile_set[self.layer_3[x,y]],(x*TILE_SIZE,y*TILE_SIZE))         
                if self.layer_4[x,y] != -1 and self.layer_4[x,y] < THINGS_TILE_OFFSET:                             
                    self.screen.blit(self.basic_tile_set[self.layer_4[x,y]],(x*TILE_SIZE,y*TILE_SIZE))  

                #if self.layer_4[x,y] != -1 and self.layer_4[x,y] >= 1000:    ### TODO: make this more elegant
                #    self.screen.blit(self.things_tile_set[self.layer_4[x,y]-1000],(x*TILE_SIZE,y*TILE_SIZE))



    def strip_from_sheet(self, sheet, start, size, columns, rows):
        frames = []
        for j in range(rows):
            for i in range(columns):
                location = (start[0]+size[0]*i, start[1]+size[1]*j)
                frames.append(sheet.subsurface(pg.Rect(location, size)))
        return frames
