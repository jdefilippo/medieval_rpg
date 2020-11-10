import pygame as pg
from globals import *

from item_models import *
from character_models import * 


class ItemSprite(pg.sprite.Sprite):
    def __init__(self, x, y, img, item_model, used_img):
        super().__init__()
        self.width = TILE_SIZE
        self.height = TILE_SIZE
        self.image = img.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.item_model = item_model
        self.usedImage = used_img.convert_alpha()


class ImpassableTile(pg.sprite.Sprite):
    def __init__(self, x, y, tileImg):
        super().__init__()
        self.width = TILE_SIZE
        self.height = TILE_SIZE
        self.image = tileImg.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class DoorTile(pg.sprite.Sprite):
    def __init__(self, x, y, closeImg, openImg):
        super().__init__()
        self.width = TILE_SIZE
        self.height = TILE_SIZE
        self.image = closeImg.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.closeImg = closeImg
        self.openImg = openImg


class AnimationTile(pg.sprite.Sprite):
    def __init__(self, x, y, frames):
        super().__init__()
        self.width = TILE_SIZE
        self.height = TILE_SIZE
        self.image = frames[0].convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.frames = frames
        self.index = 0

    def animate(self):
        self.image = self.frames[self.index].convert_alpha()
        if self.index == len(self.frames) - 1:
            self.index = 0
        else:
            self.index += 1

    def update(self, *args):
        self.animate()