import pygame as pg
from globals import *
from item_models import *
from item_sprites import *
from character_models import PlayerModel

class TraderSprite(pg.sprite.Sprite):
    def __init__(self, x1, y1, x2, y2, char_set, screen_rec, inventory={}):
        super().__init__()
        self.char_set = char_set
        self.image = self.char_set[ChImg.T_LOOK_WEST].convert_alpha()
        self.rect = self.image.get_rect()
        self.prev_x = 0
        self.prev_y = 0
        self.last_move = -1
        self.rect.x = x1
        self.rect.y = y1
        self.screen_rec = screen_rec
        self.first_loc_x = x1
        self.first_loc_y = y1
        self.second_loc_x = x2
        self.second_loc_y = y2
        self.patrol_state = 1
        self.clock = None
        self.label = "Hello!"
        self.display_label = False
        self.start_display_time = None
        self.trader_model = TraderModel()


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
        #pass
        self.patrol()


class PlayerSprite(pg.sprite.Sprite):
    def __init__(self, x, y, char_set, screen_rec):
        super().__init__()
        self.char_set = char_set
        self.image = self.char_set[ChImg.P_LOOK_EAST].convert_alpha()
        self.rect = self.image.get_rect()
        self.prev_x = 0
        self.prev_y = 0
        self.last_move = -1
        self.player_model = PlayerModel()
        self.screen_rec = screen_rec
        self.rect.x = x
        self.rect.y = y

    def teleport(self, x, y):
        self.rect.x = x 
        self.rect.y = y



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




class EnemySprite(pg.sprite.Sprite):
    def __init__(self, x1, y1, x2, y2, char_set, dead_set, screen_rec, inventory={}):
        super().__init__()
        self.char_set = char_set
        self.dead_set = dead_set
        self.image = self.char_set[ChImg.S_LOOK_WEST].convert_alpha()
        self.rect = self.image.get_rect()
        self.prev_x = 0
        self.prev_y = 0
        self.last_move = -1
        self.rect.x = x1
        self.rect.y = y1
        self.screen_rec = screen_rec
        self.first_loc_x = x1
        self.first_loc_y = y1
        self.second_loc_x = x2
        self.second_loc_y = y2
        self.patrol_state = 1
        self.clock = None
        self.label = "Hello!"
        self.display_label = False
        self.start_display_time = None
        self.enemy_model = EnemyModel()
        self.alive = True
        self.pause_patrol = False
        self.move_east_img = ChImg.S_MOVE_EAST
        self.move_east2_img = ChImg.S_MOVE_EAST2
        self.move_north_img = ChImg.S_MOVE_NORTH
        self.move_north2_img = ChImg.S_MOVE_NORTH2
        self.move_south_img = ChImg.S_MOVE_SOUTH
        self.move_south2_img = ChImg.S_MOVE_SOUTH
        self.move_west_img = ChImg.S_MOVE_WEST
        self.move_west2_img = ChImg.S_MOVE_WEST2
        self.look_east_img = ChImg.S_LOOK_EAST
        self.look_west_img = ChImg.S_LOOK_WEST
        self.look_north_img = ChImg.S_LOOK_NORTH
        self.look_south_img = ChImg.S_LOOK_SOUTH

    def express_defeat(self):
            self.image = self.dead_set[DeadImg.S_DEAD].convert_alpha()
            self.alive = False
            self.pause_patrol = True
            
    def move_right(self, pixels):

        if self.last_move == 0:
            self.image = self.char_set[self.move_east2_img].convert_alpha()
        else:
            self.image = self.char_set[self.move_east_img].convert_alpha()

        self.prev_x = self.rect.x
        self.rect.x += pixels
        self.rect.clamp_ip(self.screen_rec)
        self.last_move = 0

    def move_left(self, pixels):
        if self.last_move == 1:
            self.image = self.char_set[self.move_west2_img].convert_alpha()
        else:
            self.image = self.char_set[self.move_west_img].convert_alpha()
        self.prev_x = self.rect.x
        self.rect.x -= pixels
        self.rect.clamp_ip(self.screen_rec)
        self.last_move = 1

    def move_down(self, pixels):
        if self.last_move == 2:
            self.image = self.char_set[self.move_south2_img].convert_alpha()
        else:
            self.image = self.char_set[self.move_south_img].convert_alpha()
        self.prev_y = self.rect.y
        self.rect.y += pixels
        self.rect.clamp_ip(self.screen_rec)
        self.last_move = 2

    def move_up(self, pixels):
        if self.last_move == 2:
            self.image = self.char_set[self.move_north2_img].convert_alpha()
        else:
            self.image = self.char_set[self.move_north_img].convert_alpha()
        self.prev_y = self.rect.y
        self.rect.y -= pixels
        self.rect.clamp_ip(self.screen_rec)
        self.last_move = 3

    def rest(self):
        if self.last_move == 0:
            self.image = self.char_set[self.look_east_img].convert_alpha()
        elif self.last_move == 1:
            self.image = self.char_set[self.look_west_img].convert_alpha()
        elif self.last_move == 2:
            self.image = self.char_set[self.look_south_img].convert_alpha()
        elif self.last_move == 3:
            self.image = self.char_set[self.look_north_img].convert_alpha()

    def patrol_horizontal(self):
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

    def patrol_vertical(self):
        if(self.rect.y <= self.first_loc_y and self.rect.y > self.second_loc_y and self.patrol_state == 1):
            debug_log("Case1")
            self.move_up(1)
        elif(self.rect.y == self.second_loc_y and self.patrol_state == 1):
            debug_log("Case2")
            self.patrol_state = 2
        elif(self.rect.y < self.first_loc_y and self.patrol_state == 2):
            debug_log("Case3")
            self.move_down(1)
        elif(self.rect.y == self.first_loc_y and self.patrol_state == 2):
            self.patrol_state = 1
        else:
            debug_log("lost")

    def update(self, *args):
        if not self.pause_patrol:
            #self.patrol_horizontal()
            self.patrol_vertical()


class GhostSprite(EnemySprite):
    def __init__(self, x1, y1, x2, y2, char_set, dead_set, screen_rec, inventory={}):
        super().__init__(x1, y1, x2, y2, char_set, dead_set, screen_rec, inventory={})
        self.image = self.char_set[ChImg.G_LOOK_WEST].convert_alpha()
        self.enemy_model = GhostModel()
        self.move_east_img = ChImg.G_MOVE_EAST
        self.move_east2_img = ChImg.G_MOVE_EAST2
        self.move_north_img = ChImg.G_MOVE_NORTH
        self.move_north2_img = ChImg.G_MOVE_NORTH2
        self.move_south_img = ChImg.G_MOVE_SOUTH
        self.move_south2_img = ChImg.G_MOVE_SOUTH
        self.move_west_img = ChImg.G_MOVE_WEST
        self.move_west2_img = ChImg.G_MOVE_WEST2
        self.look_east_img = ChImg.G_LOOK_EAST
        self.look_west_img = ChImg.G_LOOK_WEST
        self.look_north_img = ChImg.G_LOOK_NORTH
        self.look_south_img = ChImg.G_LOOK_SOUTH

    
    def express_defeat(self):
            self.image = self.dead_set[DeadImg.G_DEAD].convert_alpha()
            self.alive = False
            self.pause_patrol = True

class BatSprite(EnemySprite):
    def __init__(self, x1, y1, x2, y2, char_set, dead_set, screen_rec, inventory={}):
        super().__init__(x1, y1, x2, y2, char_set, dead_set, screen_rec, inventory={})
        self.image = self.char_set[ChImg.G_LOOK_WEST].convert_alpha()
        self.enemy_model = BatModel()
        self.move_east_img = ChImg.B_MOVE_EAST
        self.move_east2_img = ChImg.B_MOVE_EAST2
        self.move_north_img = ChImg.B_MOVE_NORTH
        self.move_north2_img = ChImg.B_MOVE_NORTH2
        self.move_south_img = ChImg.B_MOVE_SOUTH
        self.move_south2_img = ChImg.B_MOVE_SOUTH
        self.move_west_img = ChImg.B_MOVE_WEST
        self.move_west2_img = ChImg.B_MOVE_WEST2
        self.look_east_img = ChImg.B_LOOK_EAST
        self.look_west_img = ChImg.B_LOOK_WEST
        self.look_north_img = ChImg.B_LOOK_NORTH
        self.look_south_img = ChImg.B_LOOK_SOUTH

    

    
    def express_defeat(self):
            self.image = self.dead_set[DeadImg.B_DEAD].convert_alpha()
            self.alive = False
            self.pause_patrol = True


class SkeletonSprite(EnemySprite):
    def __init__(self, x1, y1, x2, y2, char_set, dead_set, screen_rec, inventory={}):
        super().__init__(x1, y1, x2, y2, char_set, dead_set, screen_rec, inventory={})
        self.image = self.char_set[ChImg.S_LOOK_WEST].convert_alpha()
        self.enemy_model = SkeletonModel()
        self.move_east_img = ChImg.S_MOVE_EAST
        self.move_east2_img = ChImg.S_MOVE_EAST2
        self.move_north_img = ChImg.S_MOVE_NORTH
        self.move_north2_img = ChImg.S_MOVE_NORTH2
        self.move_south_img = ChImg.S_MOVE_SOUTH
        self.move_south2_img = ChImg.S_MOVE_SOUTH
        self.move_west_img = ChImg.S_MOVE_WEST
        self.move_west2_img = ChImg.S_MOVE_WEST2
        self.look_east_img = ChImg.S_LOOK_EAST
        self.look_west_img = ChImg.S_LOOK_WEST
        self.look_north_img = ChImg.S_LOOK_NORTH
        self.look_south_img = ChImg.S_LOOK_SOUTH

    

    
    def express_defeat(self):
            self.image = self.dead_set[DeadImg.S_DEAD].convert_alpha()
            self.alive = False
            self.pause_patrol = True
