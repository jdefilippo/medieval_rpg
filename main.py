import pygame as pg
import random
from datetime import datetime
import pygame_gui
from gamemap import *
from gui import *
from globals import *


import sgc
from sgc.locals import *


inventory_item_selected = {}

class InventoryRadio(sgc.Radio):
    def __init__(self,group, label, item_name):
        sgc.Radio.__init__(self,group=group, label=label)
        self.item_name = item_name
        inventory_item_selected[self.item_name] = False


    def on_select(self):
        global inventory_item_selected
        inventory_item_selected = dict.fromkeys(inventory_item_selected, False)
        inventory_item_selected[self.item_name] = True
        print(inventory_item_selected)


class NewTraderGUI: 
    def __init__(self,screen,font):
        self.screen = screen 
        self.font   = font         
        self.playerTitle = sgc.Label(text="Player Inventory", font=self.font)
        self.playerTitle.rect.center = (self.screen.rect.centerx-120, 40)
        self.playerTitle.add()

        self.traderTitle = sgc.Label(text="Trader Inventory", font=self.font)
        self.traderTitle.rect.center = (self.screen.rect.centerx+120, 40)
        self.traderTitle.add()       

        self.quitButton = sgc.Button(label="Quit", pos=(self.screen.rect.centerx,300))
        self.quitButton.add(order=3)

        self.player_radio_box = None
        self.player_radios    = []

        self.trader_radio_box = None
        self.trader_radios    = []


        
    def update_player_inventory_gui(self, player_inventory):
        radios = []
        for item in player_inventory: 
            name     = item
            newDesc  = item + " x " + str(player_inventory[item][0])
            radios.append(InventoryRadio(group="group1", label=newDesc, item_name=name))

        
        if self.player_radio_box: 
            self.player_radio_box.remove()

        self.player_radios = radios
        self.player_radio_box = sgc.VBox(widgets=radios, pos=(40,40+40))       
        self.player_radio_box.add(order=2) 
        

    def update_trader_inventory_gui(self, trader_inventory):
        radios = []
        for item in trader_inventory: 
            name     = item
            newDesc  = item + " x " + str(trader_inventory[item][0])
            radios.append(InventoryRadio(group="group1", label=newDesc, item_name=name))

        
        if self.trader_radio_box: 
            self.trader_radio_box.remove()

        self.trader_radios = radios
        self.trader_radio_box = sgc.VBox(widgets=radios, pos=(40,40+40))       
        self.trader_radio_box.add(order=2)      




    def hide(self):
        self.traderTitle.remove()
        self.playerTitle.remove()
        if self.player_radio_box is not None: 
            self.player_radio_box.remove()


    def show(self):
        self.traderTitle.add()
        self.playerTitle.add()
        if self.player_radio_box is not None: 
            self.player_radio_box.add()




class NewInventoryGUI: 
    def __init__(self, screen, font):
        self.screen = screen
        self.font   = font
        self.radio_box = None
        self.radios    = []

        self.title = sgc.Label(text="Inventory", font=self.font)
        self.title.rect.center = (self.screen.rect.centerx, 40)
        self.title.add()

        self.dropButton = sgc.Button(label="Drop\nItem", pos=(self.screen.rect.centerx-160,300))
        self.dropButton.add(order=3)

        self.quitButton = sgc.Button(label="Quit", pos=(self.screen.rect.centerx,300))
        self.quitButton.add(order=3)
    
    def hide(self):
        self.title.remove()
        self.dropButton.remove()
        self.quitButton.remove()
        if self.radio_box is not None: 
            self.radio_box.remove()


    def show(self):
        self.title.add()
        self.dropButton.add()
        self.quitButton.add()
        if self.radio_box is not None: 
            self.radio_box.add()



    def updateInventoryGUI(self, playerInventory):
        radios = []
        for item in playerInventory: 
            name     = item
            newDesc  = item + " x " + str(playerInventory[item][0])
            radios.append(InventoryRadio(group="group1", label=newDesc, item_name=name))

        
        if self.radio_box: 
            self.radio_box.remove()

        self.radios = radios
        self.radio_box = sgc.VBox(widgets=radios, pos=(40,40+40))       
        self.radio_box.add(order=2)



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

    ### UPDATE THIS
    guiScreen = sgc.surface.Screen((SCREEN_LENGTH, SCREEN_WIDTH))
    myfont = pg.font.SysFont("Arial", 30)
    myfont2 = pg.font.SysFont("Arial", 15)

    newInventoryGUI = NewInventoryGUI(guiScreen, myfont)
    inventory_gui_on = False

    newTraderGUI    = NewTraderGUI(guiScreen, myfont2)
    trader_gui_on = False

    clock = pg.time.Clock()


    all_sprites_list = pg.sprite.Group()

    player = gMap.get_player_sprites()
    friend_sprites = gMap.get_friend_sprites()
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

    all_sprites_list.add(used_sprites)


    gui_on = False


    inventory_gui = InventoryGUI(player)
    trader_gui = TraderGUI(player, friend_sprites[0])


    ###
    ###

    # pick a font you have and set its size
    myfont = pg.font.SysFont("Comic Sans MS", 15)
    # apply it to text on a label
    label = myfont.render("Python and Pygame are Fun!", 1, pg.Color('#000000'))
    # put the label object on the screen at point x=100, y=100
    window_surface = pg.display.set_mode((SCREEN_LENGTH, SCREEN_WIDTH))

    background = pg.Surface((SCREEN_LENGTH, SCREEN_WIDTH))
    background.fill(inventory_gui.manager.ui_theme.get_colour('dark_bg'))

    message_box_on = True
    start_time = datetime.now()

    while not done:

        time = clock.tick(60)

        if gui_on:
            time_delta = clock.tick(60) / 1000.0

        player.lastMove = -1

        for event in pg.event.get():
            sgc.event(event)
            if event.type == GUI:
                if event.gui_type == "click" and event.widget is newInventoryGUI.quitButton:
                    inventory_gui_on = False
                if event.gui_type == "click" and event.widget is newInventoryGUI.dropButton:
                    for item in inventory_item_selected:
                        if inventory_item_selected[item] == True:
                            print("This was selected to be dropped: ", item)
                            player.player_model.remove_item(item)
                            newInventoryGUI.updateInventoryGUI(player.player_model.inventory)
                    
                    # Take the dictionary and find the one which is selected. If none are selected, then do nothing.
            elif event.type == pg.QUIT:
                done = True
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_q and inventory_gui_on:
                    inventory_gui_on = False
                if event.key == pg.K_q and trader_gui_on: 
                    trader_gui_on = False
                if event.key == pg.K_i:                      
                    inventory_gui_on = True
                    newTraderGUI.hide()
                    newInventoryGUI.show()

                if event.key == pg.K_t: 
                    trader_gui_on = True
                    newInventoryGUI.hide()
                    newTraderGUI.show()


            #elif event.type == pg.USEREVENT:
            #    if event.user_type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
            #        debug_log("Selected option:", event.text)

        keys = pg.key.get_pressed()
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

        for sprite in item_sprites[:]:
            if player.rect.colliderect(sprite.rect) and sprite not in used_sprites:
                if sprite.item_model.name == "Coin":
                    debug_log("Found money!")
                    player.player_model.money += 10
                    inventory_gui.update_money()

                else:
                    player.player_model.add_inventory(sprite.item_model)
                    newInventoryGUI.updateInventoryGUI(player.player_model.inventory)

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
            inventory_gui.manager.update(time_delta)
            window_surface.blit(background, (0, 0))
            inventory_gui.manager.draw_ui(window_surface)
            pg.display.update()
        else:
            gMap.render_display(used_sprites_locs)
            all_sprites_list.update()
            all_sprites_list.draw(screen)
            player.rest()

            for sprite in friend_sprites[:]:
                if sprite.display_label:
                    label = myfont.render(sprite.label, 1, pg.Color('#000000'))
                    screen.blit(label, (150, 0))
                    if (datetime.now() - sprite.start_display_time).seconds > 3:
                        sprite.display_label = False


            if inventory_gui_on or trader_gui_on: 
                guiScreen.fill((0,0,0))
                sgc.update(time)


            pg.display.flip()
            clock.tick(30)


if __name__=="__main__": 
    main() 