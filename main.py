import pygame as pg
import random
from datetime import datetime
import pygame_gui
from game_map import *

from globals import *
from gui import * 



import sgc
from sgc.locals import *


global player_inventory_item_selected
global trader_inventory_item_selected 
global player_inventory_item_objects  
global trader_inventory_item_objects




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

        print(self.player.player_model.money)


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





def main():
        
    pg.init()
    done = False
    screen = pg.display.set_mode((SCREEN_LENGTH, SCREEN_WIDTH))
    screen_rect = screen.get_rect()
    pg.display.set_caption('Medieval RPG')
    clock = pg.time.Clock()
    playerSpeed = 4
    gMap = GameMap(
        screen,
        'mapDef.xlsx',
        'art/characters.png',
        'art/basictiles.png',
        'art/things.png')
    gMap.initialize()

    clock = pg.time.Clock()


    all_sprites_list = pg.sprite.Group()

    player = gMap.get_player_sprites()
    friend_sprites = gMap.get_friend_sprites()
    enemy_sprites  = gMap.get_enemy_sprites()
    blocked_sprites = gMap.get_blocked_sprites()
    item_sprites = gMap.get_item_sprites()
    door_sprites = gMap.get_door_sprites()
    animated_sprites = gMap.get_animated_sprites()
    used_sprites = []
    used_sprites_locs = set()


    


    all_sprites_list.add(player)
    all_sprites_list.add(friend_sprites)
    all_sprites_list.add(blocked_sprites)
    all_sprites_list.add(item_sprites)
    all_sprites_list.add(door_sprites)
    all_sprites_list.add(animated_sprites)
    all_sprites_list.add(enemy_sprites)

    all_sprites_list.add(used_sprites)

    ### UPDATE THIS
    gui_screen = sgc.surface.Screen((SCREEN_LENGTH, SCREEN_WIDTH))
    my_font = pg.font.SysFont("Arial", 30)
    my_font_2 = pg.font.SysFont("Arial", 20)

    inventory_gui = InventoryGUI(gui_screen, my_font)
    inventory_gui_on = False

    trader_gui    = TraderGUI(gui_screen, my_font_2, player)
    trader_gui_on = False

    first_trader = friend_sprites[0]
    first_trader.trader_model.add_inventory(Jewel())
    first_trader.trader_model.add_inventory(Jewel())
    first_trader.trader_model.add_inventory(Armor())

    trader_gui.update_trader_inventory_gui(first_trader.trader_model.inventory)

    first_enemy = enemy_sprites[0]


    player.player_model.add_inventory(Jewel())
    inventory_gui.update_inventory_gui(player.player_model.inventory)
    trader_gui.update_player_inventory_gui(player.player_model.inventory)

    stats_gui = StatsGUI(gui_screen, my_font, player)
    stats_gui_on = False

    battle_gui = BattleGUI(gui_screen, my_font, player, first_enemy)
    battle_gui_on = False


    gui_on = False

    # pick a font you have and set its size
    my_font = pg.font.SysFont("Comic Sans MS", 15)
    # apply it to text on a label
    label = my_font.render("Python and Pygame are Fun!", 1, pg.Color('#000000'))
    # put the label object on the screen at point x=100, y=100
    window_surface = pg.display.set_mode((SCREEN_LENGTH, SCREEN_WIDTH))

    background = pg.Surface((SCREEN_LENGTH, SCREEN_WIDTH))

    message_box_on = True
    start_time = datetime.now()

    while not done:

        time = clock.tick(60)


        player.lastMove = -1

        for event in pg.event.get():
            sgc.event(event)
            if event.type == GUI:

                if event.gui_type == "click" and event.widget is trader_gui.sell_button:
                    print("Sell button")
                    for item in player_inventory_item_selected:
                        if player_inventory_item_selected[item] == True:
                            print("This was selected to be sold: ", item)

                            # Inventory management
                            player.player_model.remove_item(item)
                            first_trader.trader_model.add_inventory(player_inventory_item_objects[item])

                            # Money calculation 
                            player.player_model.money += player_inventory_item_objects[item].val
                            print(player.player_model.money)

                            # Update the view 
                            trader_gui.update_player_inventory_gui(player.player_model.inventory)
                            trader_gui.update_trader_inventory_gui(first_trader.trader_model.inventory)
                            trader_gui.update_stats()


                if event.gui_type == "click" and event.widget is battle_gui.attack_option:
                    battle_gui.player.player_model.fight_enemy(battle_gui.enemy.enemy_model)
                    battle_gui.update_stats()

                if event.gui_type == "click" and event.widget is battle_gui.retreat_option:
                    battle_gui_on = False
                    battle_gui.hide()



                            
                if event.gui_type == "click" and event.widget is trader_gui.buy_button:
                    print("Buy button")
                    for item in trader_inventory_item_selected:
                        if trader_inventory_item_selected[item] == True:
                            print("This was selected to be bought: ", item)
                            print(player.player_model.money-trader_inventory_item_objects[item].val)
                            if player.player_model.money - trader_inventory_item_objects[item].val >= 0:

                                # Inventory management
                                first_trader.trader_model.remove_item(item)
                                player.player_model.add_inventory(trader_inventory_item_objects[item])

                                # Money calculation 
                                player.player_model.money -= trader_inventory_item_objects[item].val

                                # Update the view 
                                trader_gui.update_trader_inventory_gui(first_trader.trader_model.inventory)
                                trader_gui.update_player_inventory_gui(player.player_model.inventory)
                                trader_gui.update_stats()
                            else:
                                print("Cannot buy item")



                if event.gui_type == "click" and event.widget is inventory_gui.quit_button:
                    inventory_gui_on = False
                if event.gui_type == "click" and event.widget is inventory_gui.drop_button:
                    for item in player_inventory_item_selected:
                        if player_inventory_item_selected[item] == True:
                            print("This was selected to be dropped: ", item)
                            #print(player_inventory_item_objects[item])
                            player.player_model.remove_item(item)
                            inventory_gui.update_inventory_gui(player.player_model.inventory)
                    
                    # Take the dictionary and find the one which is selected. If none are selected, then do nothing.
            elif event.type == pg.QUIT:
                done = True
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_q and inventory_gui_on:
                    inventory_gui_on = False
                    inventory_gui.hide()
                if event.key == pg.K_q and trader_gui_on: 
                    trader_gui_on = False
                    trader_gui.hide()
                if event.key == pg.K_q and stats_gui_on: 
                    stats_gui_on = False
                    stats_gui.hide()
                if event.key == pg.K_q and battle_gui_on: 
                    battle_gui_on = False
                    battle_gui.hide()

                if event.key == pg.K_i and not inventory_gui_on:                      
                    inventory_gui_on = True
                    inventory_gui.show()                    
                    trader_gui.hide()
                    stats_gui.hide()
                    battle_gui.hide()
                if event.key == pg.K_t and not trader_gui_on: 
                    trader_gui_on = True
                    trader_gui.show()
                    inventory_gui.hide()
                    stats_gui.hide()
                    battle_gui.hide()
                if event.key == pg.K_p and not stats_gui_on: 
                    stats_gui_on = True
                    stats_gui.show()
                    inventory_gui.hide()
                    trader_gui.hide()
                    battle_gui.hide()

        keys = pg.key.get_pressed()
        #gui_on = inventory_gui_on or trader_gui_on or stats_gui_on or battle_gui_on
        if (keys[pg.K_LEFT] or keys[pg.K_a]) and not gui_on:
            player.move_left(playerSpeed)

        if (keys[pg.K_RIGHT] or keys[pg.K_d]) and not gui_on:
            player.move_right(playerSpeed)

        if (keys[pg.K_DOWN] or keys[pg.K_s]) and not gui_on:
            player.move_down(playerSpeed)

        if (keys[pg.K_UP] or keys[pg.K_w]) and not gui_on:
            player.move_up(playerSpeed)

        for sprite in blocked_sprites[:]:
            if player.rect.colliderect(sprite.rect):
                player.rect.x = player.prev_x
                player.rect.y = player.prev_y

        for sprite in friend_sprites[:]:
            if player.rect.colliderect(sprite.rect):
                player.rect.x = player.prev_x
                player.rect.y = player.prev_y
                sprite.display_label = True
                sprite.start_display_time = datetime.now()

        for sprite in enemy_sprites[:]:
            if player.rect.colliderect(sprite.rect):
                player.rect.x = player.prev_x
                player.rect.y = player.prev_y
                # sprite.display_label = True
                #sprite.start_display_time = datetime.now()
                battle_gui_on = True
                inventory_gui.hide()                    
                trader_gui.hide()
                stats_gui.hide()
                battle_gui.show()

        for sprite in item_sprites[:]:
            if player.rect.colliderect(sprite.rect) and sprite not in used_sprites:
                if sprite.item_model.name == "Coin":
                    debug_log("Found money!")
                    print("Found money")
                    player.player_model.money += 10
                    stats_gui.update_stats()
                    trader_gui.update_stats()
                    #inventory_gui.update_money()

                else:
                    print(player.player_model.inventory)
                    player.player_model.add_inventory(sprite.item_model)
                    print(player.player_model.inventory)
                    inventory_gui.update_inventory_gui(player.player_model.inventory)
                    print(player.player_model.inventory)
                    trader_gui.update_player_inventory_gui(player.player_model.inventory)
                    print(player.player_model.inventory)


                debug_log(sprite.item_model.name)
                used_sprites.append(sprite)
                used_sprites_locs.add((sprite.rect.x, sprite.rect.y))
                sprite.kill()
                debug_log(used_sprites_locs)

        for sprite in door_sprites[:]:
            if player.rect.colliderect(sprite.rect):
                sprite.image = sprite.openImg.convert_alpha()
            else:
                sprite.image = sprite.closeImg.convert_alpha()

        if gui_on:
            pass
            #inventory_gui.manager.update(time_delta)
            #window_surface.blit(background, (0, 0))
            #inventory_gui.manager.draw_ui(window_surface)
            #pg.display.update()
        else:
            gMap.render_display(used_sprites_locs)
            all_sprites_list.update()
            all_sprites_list.draw(screen)
            player.rest()

            for sprite in friend_sprites[:]:
                if sprite.display_label:
                    label = my_font.render(sprite.label, 1, pg.Color('#000000'))
                    screen.blit(label, (150, 0))
                    if (datetime.now() - sprite.start_display_time).seconds > 3:
                        sprite.display_label = False


            if inventory_gui_on or trader_gui_on or stats_gui_on or battle_gui_on: 
                gui_screen.fill((0,0,0))
                sgc.update(time)


            pg.display.flip()
            clock.tick(30)


if __name__=="__main__": 
    main() 