import enum

""" global variables used throughout program """
SCREEN_WIDTH = 400
SCREEN_LENGTH = 400
TILE_SIZE = 16
THINGS_TILE_OFFSET = 1000
DEBUG = 0




player_inventory_item_selected = {}
trader_inventory_item_selected = {} 
player_inventory_item_objects  = {} 
trader_inventory_item_objects  = {} 

class DeadImg: 
    S_DEAD = 6

class ChImg:
    """
    Mapping for art/characters.png
    """
    # PLAYER TILES
    P_LOOK_NORTH = 43
    P_LOOK_SOUTH = 7
    P_LOOK_EAST = 31
    P_LOOK_WEST = 19
    P_MOVE_NORTH = 42
    P_MOVE_SOUTH = 6
    P_MOVE_EAST = 30
    P_MOVE_WEST = 18
    P_MOVE_NORTH2 = 44
    P_MOVE_SOUTH2 = 8
    P_MOVE_EAST2 = 32
    P_MOVE_WEST2 = 20
    # TRADER TILES
    T_LOOK_SOUTH = 4
    T_LOOK_WEST = 16
    T_LOOK_EAST = 28
    T_LOOK_NORTH = 40
    T_MOVE_SOUTH = 6
    T_MOVE_SOUTH2 = 2
    T_MOVE_WEST = 15
    T_MOVE_WEST2 = 17
    T_MOVE_EAST = 27
    T_MOVE_EAST2 = 29
    T_MOVE_NORTH = 39
    T_MOVE_NORTH2 = 41
    # SKELETON TILES
    S_LOOK_NORTH = 43+3
    S_LOOK_SOUTH = 7+3
    S_LOOK_EAST = 31+3
    S_LOOK_WEST = 19+3
    S_MOVE_NORTH = 42+3
    S_MOVE_SOUTH = 6+3
    S_MOVE_EAST = 30+3
    S_MOVE_WEST = 18+3
    S_MOVE_NORTH2 = 44+3
    S_MOVE_SOUTH2 = 8+3
    S_MOVE_EAST2 = 32+3
    S_MOVE_WEST2 = 20+3



class TileImg:
    """
    Mapping for art/basictiles.png
    """
    WALL_1 = 0
    WALL_2 = 1
    WALL_3 = 2
    WALL_4 = 3
    WALL_5 = 4
    WALL_6 = 5
    WALL_7 = 6
    WALL_8 = 7
    ROCKS = 68
    JEWELS = 69
    ARMOR = 70
    MAGIC_SPELL = 71
    SWORD = 78
    HEALTH_POTION = 79
    MUSHROOMS = 44
    WATER = 13
    EVERGREEN = 30
    BASIC_TREE = 38
    ROCK_FACE = 15
    SUCCULENT = 20
    OCEAN = 13
    MONUMENT = 47
    MOUNTAIN_1 = 62
    MOUNTAIN_2 = 63
    DOOR_CLOSED = THINGS_TILE_OFFSET
    DOOR_OPENING_1 = THINGS_TILE_OFFSET + 12
    DOOR_OPENING_2 = THINGS_TILE_OFFSET + 24
    DOOR_OPENING_3 = THINGS_TILE_OFFSET + 36
    TORCH_1 = THINGS_TILE_OFFSET + 48
    TORCH_2 = THINGS_TILE_OFFSET + 49
    TORCH_3 = THINGS_TILE_OFFSET + 50
    TORCH_4 = THINGS_TILE_OFFSET + 51


def debug_log(s):
    """
    A simple function to control debugging throughout entire program
    """
    if DEBUG:
        debug_log(s)
