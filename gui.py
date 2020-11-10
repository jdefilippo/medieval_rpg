import pygame_gui
import pygame as pg
from globals import * 


import sgc
from sgc.locals import *


class InventoryRadio(sgc.Radio):
    def __init__(self,group, label, item_name, item_object=None, stats_label=None):
        sgc.Radio.__init__(self,group=group, label=label)
        self.item_name   = item_name
        self.group       = group
        self.item_object = item_object
        self.stats_label = stats_label

        if self.group=="player":
            player_inventory_item_selected[self.item_name] = False
            player_inventory_item_objects[self.item_name]  = self.item_object
        if self.group == "trader":
            trader_inventory_item_selected[self.item_name] = False
            trader_inventory_item_objects[self.item_name]  = self.item_object



    def on_select(self):
        if self.group == "player":
            global player_inventory_item_selected
            global player_inventory_item_objects
            player_inventory_item_selected = dict.fromkeys(player_inventory_item_selected, False)
            player_inventory_item_selected[self.item_name] = True      
            if self.stats_label: 
                self.stats_label.config(text=player_inventory_item_objects[self.item_name].print_stats())
                self.stats_label.add()

        if self.group == "trader":
            global trader_inventory_item_selected
            global trader_inventory_item_objects
            trader_inventory_item_selected = dict.fromkeys(trader_inventory_item_selected, False)
            trader_inventory_item_selected[self.item_name] = True
            trader_inventory_item_objects[self.item_name].print_stats()
            if self.stats_label: 
                self.stats_label.config(text=trader_inventory_item_objects[self.item_name].print_stats())
                self.stats_label.add()

class TraderGUI: 
    def __init__(self,screen,font, player):
        self.player = player
        self.screen = screen 
        self.font   = font         
        self.playerTitle = sgc.Label(text="Player Inventory", font=self.font)
        self.playerTitle.rect.center = (self.screen.rect.centerx-100, 40)
        #self.playerTitle.add()

        self.traderTitle = sgc.Label(text="Trader Inventory", font=self.font)
        self.traderTitle.rect.center = (self.screen.rect.centerx+100, 40)
        #self.traderTitle.add()       
        
        self.sell_button = sgc.Button(label="Sell\nItem", pos=(self.screen.rect.centerx-160,300))
        #self.sell_button.add(order=3)

        self.buy_button = sgc.Button(label="Buy\nItem", pos=(self.screen.rect.centerx,300))
        #self.buy_button.add(order=3)

        self.money_label = sgc.Label(text="Money: " + str(player.player_model.money), font=self.font)
        self.money_label.rect.center = (self.screen.rect.centerx-30, 275)
        #self.money_label.add()

        self.stats = sgc.Label(text="", font=pg.font.SysFont("Arial", 15))
        self.stats.rect.center = (self.screen.rect.centerx-160, 375)
        self.stats.config(text="")
        self.stats.add()

        self.player_radio_box = None
        self.player_radios    = []

        self.trader_radio_box = None
        self.trader_radios    = []

    def update_stats(self):        
        self.money_label.remove()
        self.money_label = sgc.Label(text="Money: " + str(self.player.player_model.money), font=self.font)
        self.money_label.rect.center = (self.screen.rect.centerx-30, 275)
        self.money_label.add()
        
    def update_player_inventory_gui(self, player_inventory):
        radios = []
        for item in player_inventory: 
            name     = item
            newDesc  = item + " x " + str(player_inventory[item][0])
            radios.append(InventoryRadio(group="player", label=newDesc, item_name=name, item_object=player_inventory[item][1], stats_label=self.stats))

        
        if self.player_radio_box: 
            self.player_radio_box.remove()

        self.player_radios = radios
        if radios != []: # if inventory is empty, do nothing
            self.player_radio_box = sgc.VBox(widgets=radios, pos=(40,40+40))       
            self.player_radio_box.add(order=2) 


    def update_trader_inventory_gui(self, trader_inventory):
        radios = []
        for item in trader_inventory: 
            name     = item
            newDesc  = item + " x " + str(trader_inventory[item][0])
            radios.append(InventoryRadio(group="trader", label=newDesc, item_name=name, item_object=trader_inventory[item][1], stats_label=self.stats))

        
        if self.trader_radio_box: 
            self.trader_radio_box.remove()

        self.trader_radios = radios
        if radios != []: # if inventory is empty, do nothing
            self.trader_radio_box = sgc.VBox(widgets=radios, pos=(40+200,40+40))       
            self.trader_radio_box.add(order=2)     

    def sell_item(self):
        pass

    def buy_item(self):
        pass


    def hide(self):
        self.traderTitle.remove()
        self.playerTitle.remove()
        if self.player_radio_box is not None: 
            self.player_radio_box.remove()
        if self.trader_radio_box is not None: 
            self.trader_radio_box.remove()
        self.buy_button.remove()
        self.sell_button.remove()
        self.money_label.remove()



    def show(self):
        self.traderTitle.add()
        self.playerTitle.add()
        if self.player_radio_box is not None: 
            self.player_radio_box.add()
        if self.player_radio_box is not None: 
            self.trader_radio_box.add()
        self.buy_button.add()
        self.sell_button.add()
        self.money_label.add()

class InventoryGUI: 
    def __init__(self, screen, font):
        self.screen = screen
        self.font   = font
        self.radio_box = None
        self.radios    = []

        self.title = sgc.Label(text="Inventory", font=self.font)
        self.title.rect.center = (self.screen.rect.centerx, 40)
        #self.title.add()

        self.drop_button = sgc.Button(label="Drop\nItem", pos=(self.screen.rect.centerx-160,300))
        #self.drop_button.add()

        self.quit_button = sgc.Button(label="Quit", pos=(self.screen.rect.centerx,300))
        #self.quit_button.add()
        
        self.stats = sgc.Label(text="", font=pg.font.SysFont("Arial", 15))
        self.stats.rect.center = (self.screen.rect.centerx-160, 375)
        self.stats.config(text="")
        #self.stats.add()

    
    def hide(self):
        self.title.remove()
        self.drop_button.remove()
        self.quit_button.remove()
        if self.radio_box is not None: 
            self.radio_box.remove()
        self.stats.remove()


    def show(self):
        self.title.add()
        self.drop_button.add()
        self.quit_button.add()
        if self.radio_box is not None: 
            self.radio_box.add()
        self.stats.add()



    def update_inventory_gui(self, player_inventory):
        radios = []
        for item in player_inventory: 
            name     = item
            newDesc  = item + " x " + str(player_inventory[item][0])
            radios.append(InventoryRadio(group="player", label=newDesc, item_name=name, item_object=player_inventory[item][1], stats_label=self.stats))

        
        if self.radio_box: 
            self.radio_box.remove()

        self.radios = radios
        if radios != []: # if inventory is empty, do nothing
            self.radio_box = sgc.VBox(widgets=radios, pos=(40,40+40))       
            self.radio_box.add(order=2)

class BattleGUI: 
    def __init__(self, screen, font, player, enemy):
        self.player = player
        self.enemy  = enemy
        self.screen = screen
        self.font   = font
        self.title = sgc.Label(text="Battle", font=self.font)

        self.title.rect.center = (self.screen.rect.centerx, 40)

        player_image_zoomed = pg.transform.rotozoom(player.image, 0, 3)
        self.player_img = sgc.Simple(surf=player_image_zoomed, pos=(self.screen.rect.centerx-160,75))

        enemy_image_zoomed = pg.transform.rotozoom(enemy.image, 0, 3)
        self.enemy_img = sgc.Simple(surf=enemy_image_zoomed, pos=(self.screen.rect.centerx+120,75))

        self.player_hp_label = sgc.Label(text="HP: " + str(self.player.player_model.current_health) + " / " + str(self.player.player_model.health_capacity), font=pg.font.SysFont("Arial", 15), pos=(35,130)) 
        self.enemy_hp_label  = sgc.Label(text="HP: " + str(self.enemy.enemy_model.current_health) + " / " + str(self.enemy.enemy_model.health_capacity), font=pg.font.SysFont("Arial", 15), pos=(300,130))
       
        self.attack_option = sgc.Button(label="Attack")
        self.item_option = sgc.Button(label="Item")
        self.retreat_option = sgc.Button(label="Retreat")

        self.attack_options_box = sgc.VBox(widgets =[self.attack_option, self.item_option, self.retreat_option], pos=(10, 180))

    def hide(self):
        self.title.remove()
        self.player_img.remove()
        self.enemy_img.remove()
        self.attack_options_box.remove()
        self.player_hp_label.remove()
        self.enemy_hp_label.remove()


    def show(self):
        self.update_stats()
        self.title.add()
        self.player_img.add()
        self.enemy_img.add()
        self.attack_options_box.add()
        self.player_hp_label.add()
        self.enemy_hp_label.add()

    def update_stats(self):
        self.player_hp_label.config(text="HP: " + str(self.player.player_model.current_health) + " / " + str(self.player.player_model.health_capacity), font=pg.font.SysFont("Arial", 15))
        self.enemy_hp_label.config(text="HP: " + str(self.enemy.enemy_model.current_health) + " / " + str(self.enemy.enemy_model.health_capacity), font=pg.font.SysFont("Arial", 15))



class StatsGUI: 
    def __init__(self, screen, font, player):
        self.player = player
        self.screen = screen
        self.font   = font
        
        big_image = pg.transform.rotozoom(player.image, 0, 3)
        self.char_img = sgc.Simple(surf=big_image, pos=(self.screen.rect.centerx-160,25))

        self.title = sgc.Label(text="Stats", font=self.font)
        self.title.rect.center = (self.screen.rect.centerx, 40)

        self.name_label = sgc.Label(text="Name: " + player.player_model.name, font=pg.font.SysFont("Arial", 20))
        self.name_label.rect.center = (self.screen.rect.centerx, 80)

        self.health_label = sgc.Label(text="Current Health: " + str(player.player_model.current_health) + " / " + str(player.player_model.health_capacity), font=pg.font.SysFont("Arial", 20))
        self.health_label.rect.center = (self.screen.rect.centerx, 120)

        self.strength_label = sgc.Label(text="Strength: " + str(player.player_model.strength), font=pg.font.SysFont("Arial", 20))
        self.strength_label.rect.center = (self.screen.rect.centerx, 160)

        self.money_label = sgc.Label(text="Money: " + str(player.player_model.money), font=pg.font.SysFont("Arial", 20))
        self.money_label.rect.center = (self.screen.rect.centerx, 200)

        self.stats_box = sgc.VBox(widgets =[self.name_label, self.health_label, self.strength_label, self.money_label], pos=(self.screen.rect.centerx-120, 80))

    def update_stats(self):
        self.health_label.config(text="Current Health: " + str(self.player.player_model.current_health) + " / " + str(self.player.player_model.health_capacity), font=pg.font.SysFont("Arial", 20))
        self.strength_label.config(text="Strength: " + str(self.player.player_model.strength),font=pg.font.SysFont("Arial", 20))
        self.money_label.config(text="Money: " + str(self.player.player_model.money), font=pg.font.SysFont("Arial", 20))
        self.stats_box = sgc.VBox(widgets =[self.name_label, self.health_label, self.strength_label, self.money_label], pos=(self.screen.rect.centerx-120, 80))



    def hide(self):
       self.title.remove()
       self.char_img.remove()
       self.stats_box.remove()
       self.health_label.remove()
       self.strength_label.remove()
       self.stats_box.remove()

    def show(self):
       self.title.add()
       self.char_img.add()
       self.stats_box.add()


