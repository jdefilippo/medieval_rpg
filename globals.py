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
    P_DEAD = 5
    M_DEAD = 7
    B_DEAD = 8 
    G_DEAD = 9 

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
    # SWAP MONSTER TILES
    M_LOOK_SOUTH = 49
    M_LOOK_WEST  = 49+(12*1)
    M_LOOK_EAST  = 49+(12*2)
    M_LOOK_NORTH = 49+(12*3)
    M_MOVE_SOUTH   = 48 
    M_MOVE_WEST    = 48+(12*1) 
    M_MOVE_EAST    = 48+(12*2) 
    M_MOVE_NORTH   = 48+(12*3)
    M_MOVE_SOUTH2   = 50 
    M_MOVE_WEST2    = 50+(12*1) 
    M_MOVE_EAST2    = 50+(12*2) 
    M_MOVE_NORTH2   = 50+(12*3)
    # BAT TILES 
    B_LOOK_SOUTH = 52
    B_LOOK_WEST  = 52+(12*1)
    B_LOOK_EAST  = 52+(12*2)
    B_LOOK_NORTH = 52+(12*3)
    B_MOVE_SOUTH   = 51 
    B_MOVE_WEST    = 51+(12*1) 
    B_MOVE_EAST    = 51+(12*2) 
    B_MOVE_NORTH   = 51+(12*3)
    B_MOVE_SOUTH2   = 53 
    B_MOVE_WEST2    = 53+(12*1) 
    B_MOVE_EAST2    = 53+(12*2) 
    B_MOVE_NORTH2   = 53+(12*3)
    # GHOST TILES 
    G_LOOK_SOUTH = 55
    G_LOOK_WEST  = 55+(12*1)
    G_LOOK_EAST  = 55+(12*2)
    G_LOOK_NORTH = 55+(12*3)
    G_MOVE_SOUTH   = 54 
    G_MOVE_WEST    = 54+(12*1) 
    G_MOVE_EAST    = 54+(12*2) 
    G_MOVE_NORTH   = 54+(12*3)
    G_MOVE_SOUTH2   = 53 
    G_MOVE_WEST2    = 56+(12*1) 
    G_MOVE_EAST2    = 56+(12*2) 
    G_MOVE_NORTH2   = 56+(12*3)



class TileImg:
    """
    Mapping for art/basictiles.png
    """
    GRASS = 11
    ROAD  = 10
    BLACK  = 22
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
    EXIT_CAVE   = 99
    EXIT_HOME   = 100



g_item_tiles     = set([TileImg.ROCKS,TileImg.JEWELS, TileImg.ARMOR, TileImg.MAGIC_SPELL, TileImg.SWORD, TileImg.HEALTH_POTION, TileImg.MUSHROOMS])
g_blocked_tiles  = set([TileImg.WALL_1, TileImg.WALL_2, TileImg.WALL_3, TileImg.WALL_4,
                                TileImg.WALL_5, TileImg.WALL_6, TileImg.WALL_7, TileImg.WALL_8,
                                  TileImg.OCEAN, TileImg.EVERGREEN, TileImg.BASIC_TREE, 
                                  TileImg.SUCCULENT, TileImg.ROCK_FACE, TileImg.MONUMENT, TileImg.BLACK, TileImg.MOUNTAIN_1, TileImg.MOUNTAIN_2])
g_animated_tiles = set([TileImg.TORCH_1])
g_door_tiles     = set([TileImg.DOOR_CLOSED, TileImg.DOOR_OPENING_1, TileImg.DOOR_OPENING_2, TileImg.DOOR_OPENING_3])
      

def debug_log(s):
    """
    A simple function to control debugging throughout entire program
    """
    if DEBUG:
        debug_log(s)
