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
        'art/things.png', 
        'art/dead.png')
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
                    for item in player_inventory_item_selected:
                        if player_inventory_item_selected[item] == True:

                            # Inventory management
                            player.player_model.remove_item(item)
                            first_trader.trader_model.add_inventory(player_inventory_item_objects[item])

                            # Money calculation 
                            player.player_model.money += player_inventory_item_objects[item].val

                            # Update the view 
                            trader_gui.update_player_inventory_gui(player.player_model.inventory)
                            trader_gui.update_trader_inventory_gui(first_trader.trader_model.inventory)
                            trader_gui.update_stats()

                if event.gui_type == "click" and event.widget is battle_gui.attack_option:
                    outcome = battle_gui.player.player_model.fight_enemy(battle_gui.enemy.enemy_model)
                    if outcome == 0: # enemy is killed 
                        battle_gui_on = False
                        battle_gui.update_stats()
                        battle_gui.hide()
                        battle_gui.enemy.express_defeat()
                    elif outcome == 1: # player is killed
                        quit()
                    else:      
                        battle_gui.update_stats()

                if event.gui_type == "click" and event.widget is battle_gui.retreat_option:
                    battle_gui_on = False
                    battle_gui.hide()
                    battle_gui.enemy.pause_patrol = False
                            
                if event.gui_type == "click" and event.widget is trader_gui.buy_button:
                    for item in trader_inventory_item_selected:
                        if trader_inventory_item_selected[item] == True:
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
                #if event.key == pg.K_q and battle_gui_on: 
                #    battle_gui_on = False
                #    battle_gui.hide()

                if event.key == pg.K_i and not inventory_gui_on:                      
                    inventory_gui_on = True
                    inventory_gui.show()                    
                    trader_gui.hide()
                    stats_gui.hide()
                    battle_gui.hide()
                #if event.key == pg.K_t and not trader_gui_on: 
                #    trader_gui_on = True
                #    trader_gui.show()
                #    inventory_gui.hide()
                #    stats_gui.hide()
                #    battle_gui.hide()
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
                trader_gui_on = True
                trader_gui.show()
                inventory_gui.hide()
                stats_gui.hide()
                battle_gui.hide()
                
                # Trader logic --- 
                #player.rect.x = player.prev_x
                #player.rect.y = player.prev_y
                #sprite.display_label = True
                #sprite.start_display_time = datetime.now()

        for sprite in enemy_sprites[:]:
            if player.rect.colliderect(sprite.rect) and sprite.alive:
                player.rect.x = player.prev_x
                player.rect.y = player.prev_y
                # sprite.display_label = True
                #sprite.start_display_time = datetime.now()
                battle_gui_on = True
                inventory_gui.hide()                    
                trader_gui.hide()
                stats_gui.hide()
                battle_gui.show()
                sprite.pause_patrol = True

        for sprite in item_sprites[:]:
            if player.rect.colliderect(sprite.rect) and sprite not in used_sprites:
                if sprite.item_model.name == "Coin":
                    debug_log("Found money!")
                    player.player_model.money += 10
                    stats_gui.update_stats()
                    trader_gui.update_stats()
                else:
                    player.player_model.add_inventory(sprite.item_model)
                    inventory_gui.update_inventory_gui(player.player_model.inventory)
                    inventory_gui.hide()

                    trader_gui.update_player_inventory_gui(player.player_model.inventory)
                    trader_gui.hide()


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