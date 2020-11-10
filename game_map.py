import numpy as np
import pandas as pd
import pygame as pg

from item_models import *
from item_sprites import *
from character_models import *
from character_sprites import *


from globals import * 

class GameMap():
    '''
    GameMap is responsible for 1. generating the initial game map from a multi-sheet excel spreadsheet 2. interpreting that spreadsheet based on 
    a mapping from the spreadsheet elements to tile images 3. rendering the display of the map through pygame.

    :param screen: 
    :param screen_rect: 
    :param map_file: 
    :param char_file:
    :param basic_file:
    :param things_file:
    :param char_tile_set:
    :param basic_tile_set:
    :param things_tile_set:
    :param layer_1:
    :param layer_2:
    :param layer_3:
    :param layer_4:
    :param blocked_tiles
    :param item_tiles
    :param animated_tiles
    :param door_tiles
    :param blocked_sprites
    :param item_sprites
    :param friend_sprites
    :param door_sprites
    :param animated_sprites
    :param player_sprite
    '''
    def __init__(self, screen, map_file, char_file, basic_file, things_file, dead_file):
        self.screen          = screen
        self.screen_rect     = screen.get_rect()
        self.map_file         = map_file
        self.char_file        = char_file
        self.basic_file       = basic_file
        self.things_file      = things_file
        self.dead_file        = dead_file
        self.char_tile_set     = None
        self.basic_tile_set    = None
        self.things_tile_set   = None
        self.dead_tile_set     = None
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
        self.enemy_sprites    = [] 

    def get_enemy_sprites(self):
        return self.enemy_sprites

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
        self.dead_tile_set   = self.strip_from_sheet(pg.image.load(self.dead_file),(0,0),(TILE_SIZE,TILE_SIZE),3,4)


        self.item_tiles     = set([TileImg.ROCKS,TileImg.JEWELS, TileImg.ARMOR, TileImg.MAGIC_SPELL, TileImg.SWORD, TileImg.HEALTH_POTION, TileImg.MUSHROOMS])
        self.blocked_tiles  = set([TileImg.WALL_1, TileImg.WALL_2, TileImg.WALL_3, TileImg.WALL_4,
                                  TileImg.WALL_5, TileImg.WALL_6, TileImg.WALL_7, TileImg.WALL_8,
                                  TileImg.OCEAN, TileImg.EVERGREEN, TileImg.BASIC_TREE, 
                                  TileImg.SUCCULENT, TileImg.ROCK_FACE, TileImg.MONUMENT])
        self.animated_tiles = set([TileImg.TORCH_1])
        self.door_tiles     = set([TileImg.DOOR_CLOSED, TileImg.DOOR_OPENING_1, TileImg.DOOR_OPENING_2, TileImg.DOOR_OPENING_3])


      
        self.player_sprite    = PlayerSprite(self.char_tile_set, self.screen_rect)
        trader = TraderSprite(125,336, self.char_tile_set, self.screen_rect)
        self.friend_sprites = [trader]

        skeleton = EnemySprite(210, 100, 200, 90, self.char_tile_set, self.dead_tile_set, self.screen_rect)
        self.enemy_sprites = [skeleton]




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
                        pass

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
                    if ((x*TILE_SIZE, y*TILE_SIZE) not in usedSpritesLocs):
                        self.screen.blit(self.basic_tile_set[self.layer_2[x,y]],(x*TILE_SIZE,y*TILE_SIZE)) 
                if self.layer_3[x,y] != -1 and self.layer_3[x,y] < THINGS_TILE_OFFSET:                             
                    self.screen.blit(self.basic_tile_set[self.layer_3[x,y]],(x*TILE_SIZE,y*TILE_SIZE))         
                if self.layer_4[x,y] != -1 and self.layer_4[x,y] < THINGS_TILE_OFFSET:                             
                    self.screen.blit(self.basic_tile_set[self.layer_4[x,y]],(x*TILE_SIZE,y*TILE_SIZE))  


    def strip_from_sheet(self, sheet, start, size, columns, rows):
        """
        Utility function to divide tile sheets into equal chunks.
        """
        frames = []
        for j in range(rows):
            for i in range(columns):
                location = (start[0]+size[0]*i, start[1]+size[1]*j)
                frames.append(sheet.subsurface(pg.Rect(location, size)))
        return frames
