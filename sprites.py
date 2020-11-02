import pygame as pg
from globals import *
from items import *


class MerchantSprite(pg.sprite.Sprite):
    def __init__(self, x, y, char_set, screen_rec):
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
        self.first_loc_x = x
        self.first_loc_y = y
        self.second_loc_x = x - 64
        self.second_loc_y = y
        self.patrol_state = 1
        self.clock = None
        self.label = "Hello!"
        self.display_label = False
        self.start_display_time = None

    def set_clock(self, clock):
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

    def move_down(self, pixels):
        if self.last_move == 2:
            self.image = self.char_set[ChImg.T_MOVE_SOUTH2].convert_alpha()
        else:
            self.image = self.char_set[ChImg.T_MOVE_SOUTH].convert_alpha()
        self.prev_y = self.rect.y
        self.rect.y += pixels
        self.rect.clamp_ip(self.screen_rec)
        self.last_move = 2

    def move_up(self, pixels):
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
            # debug_log("Case1")
            self.move_left(1)
        elif(self.rect.x == self.second_loc_x and self.patrol_state == 1):
            # debug_log("Case2")
            self.patrol_state = 2
            # self.move_right(1)
        elif(self.rect.x < self.first_loc_x and self.patrol_state == 2):
            # debug_log("Case3")
            self.move_right(1)
        elif(self.rect.x == self.first_loc_x and self.patrol_state == 2):
            self.move_left(1)
            self.patrol_state = 1
        else:
            debug_log("lost")

    def update(self, *args):
        pass
        # self.patrol()


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

    def move_down(self, pixels):
        if self.last_move == 2:
            self.image = self.char_set[ChImg.P_MOVE_SOUTH2].convert_alpha()
        else:
            self.image = self.char_set[ChImg.P_MOVE_SOUTH].convert_alpha()
        self.prev_y = self.rect.y
        self.rect.y += pixels
        self.rect.clamp_ip(self.screen_rec)
        self.last_move = 2

    def move_up(self, pixels):
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