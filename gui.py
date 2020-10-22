import pygame_gui
import pygame as pg
from globals import * 

class TraderGUI(): 
    def __init__(self, player, trader):
        self.player = player
        self.trader = trader
        self.manager = pygame_gui.UIManager((SCREEN_WIDTH,SCREEN_LENGTH), pygame_gui.PackageResource(package='data.themes', resource='theme_2.json'))
        self.trading_title = pygame_gui.elements.UILabel(pg.Rect((75, 0), (250, 50)), "TRADING",
                                   manager=self.manager,
                                   object_id='#inventory')

    def hideAll(self): 
        self.trading_title.hide()

class MessageBoxGUI(): 
    def __init__(self):
        self.manager = pygame_gui.UIManager((SCREEN_WIDTH,SCREEN_LENGTH), pygame_gui.PackageResource(package='data.themes', resource='theme_2.json'))
        self.trading_title = pygame_gui.elements.UILabel(pg.Rect((75, 0), (250, 50)), "TRADING",
                                   manager=self.manager,
                                   object_id='#inventory')

    def hideAll(self): 
        self.trading_title.hide()

class InventoryGUI():
    def __init__(self, player):
        self.player  = player
        self.manager = pygame_gui.UIManager((SCREEN_WIDTH,SCREEN_LENGTH), pygame_gui.PackageResource(package='data.themes', resource='theme_2.json'))
        self.stats_title = pygame_gui.elements.UILabel(pg.Rect((75, 0), (250, 50)), "STATS",
                                   manager=self.manager,
                                   object_id='#inventory')

        self.coin_stat = pygame_gui.elements.UILabel(pg.Rect((-77, 75), (250, 25)), 'Coin: ' + str(self.player.player_model.money),
                                   manager=self.manager,
                                   object_id='#coin')

        self.hp_stat = pygame_gui.elements.UILabel(pg.Rect((-71, 50), (250, 25)), 'HP: ' + str(self.player.player_model.current_health) + '/' +  str(self.player.player_model.health_capacity),
                                   manager=self.manager,
                                   object_id='#coin')   

        self.strength_stat = pygame_gui.elements.UILabel(pg.Rect((-62, 100), (250, 25)), 'Strength: ' + str(self.player.player_model.strength),
                                   manager=self.manager,
                                   object_id='#coin')  

        self.inventory_title = pygame_gui.elements.UILabel(pg.Rect((75, 125), (250, 50)), "INVENTORY",
                                   manager=self.manager,
                                   object_id='#inventory')

        self.inventory = pygame_gui.elements.UILabel(pg.Rect((75, 175), (250, 50)), "No items in inventory", manager=self.manager, object_id="#coin")
    def update_inventory(self):
        newInventory = self.player.player_model.inventory
        newOptions = [i + " x " + str(newInventory[i][0]) for i in newInventory] 
        self.inventory.kill()
        self.inventory = pygame_gui.elements.UIDropDownMenu(relative_rect=pg.Rect((10, 200), (250, 50)), manager=self.manager, options_list=newOptions, starting_option=newOptions[0])
   
    def update_money(self): 
        self.coin_stat.set_text('Coin: ' + str(self.player.player_model.money))

    def hideAll(self):
        self.stats_title.hide()
        self.coin_stat.hide()
        self.hp_stat.hide()
        self.strength_stat.hide()
        self.inventory_title.hide()
        self.inventory.hide()
