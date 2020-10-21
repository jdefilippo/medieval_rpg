import pygame as pg
import random

import pygame_gui

from view import *
from model import *



SCREEN_WIDTH  = 400
SCREEN_LENGTH = 400

pg.init()
done = False
screen = pg.display.set_mode((SCREEN_LENGTH,SCREEN_WIDTH))
screen_rect = screen.get_rect()
pg.display.set_caption('Medieval RPG')
clock=pg.time.Clock()
playerSpeed = 4

gMap = GameMap(screen, 'mapDef.xlsx', 'art/characters.png', 'art/basictiles.png', 'art/things.png')

gMap.initialize()

all_sprites_list = pg.sprite.Group()

## TODO: Figure out a better day to handle this
###charSet = gMap.getCharSet()


player          = gMap.get_player_sprites()

merchant        = gMap.get_friend_sprites()

blocked_sprites  = gMap.get_blocked_sprites()
item_sprites     = gMap.get_item_sprites()
door_sprites     = gMap.get_door_sprites()
animated_sprites = gMap.get_animated_sprites() 
used_sprites     = [] 
used_sprites_locs = set()


merchant[0].set_clock(clock)


all_sprites_list.add(player)
all_sprites_list.add(merchant)
all_sprites_list.add(blocked_sprites)
all_sprites_list.add(item_sprites)
all_sprites_list.add(door_sprites)
all_sprites_list.add(animated_sprites)

all_sprites_list.add(used_sprites)

def collision_with_player(player, sprite):
    if player.rect.colliderect(sprite.rect):
        player.playerModel.add_inventory(sprite.item_model)   
        return True
    return False

### GUI TEST
gui_on = False
#manager = pygame_gui.UIManager((400,400), pygame_gui.PackageResource(package='data.themes', resource='theme_2.json'))
#manager = pygame_gui.UIManager(window_resolution=(400,400), theme_path=pygame_gui.PackageResource(package='./', resource='label.json'))
manager = pygame_gui.UIManager((400,400), pygame_gui.PackageResource(package='data.themes', resource='theme_2.json'))
#manager = pygame_gui.UIManager((400,400),pygame_gui.PackageResource(package='data.themes',
#                                                    resource='theme_2.json'))
'''
        self.ui_manager = UIManager(self.options.resolution,
                                    PackageResource(package='data.themes',
                                                    resource='theme_2.json'))
        self.ui_manager.preload_fonts([{'name': 'fira_code', 'point_size': 10, 'style': 'bold'},
                                       {'name': 'fira_code', 'point_size': 10, 'style': 'regular'},
                                       {'name': 'fira_code', 'point_size': 10, 'style': 'italic'},
                                       {'name': 'fira_code', 'point_size': 14, 'style': 'italic'},
                                       {'name': 'fira_code', 'point_size': 14, 'style': 'bold'}
                                       ])

                                       '''

#hello_button = pygame_gui.elements.UITextBox('Say hey', 
#                                             pg.Rect((50, 50), (100, 50)),
#                                             manager=manager)

'''
hello_button2 = pygame_gui.elements.UIButton(relative_rect=pg.Rect((50, 200), (100, 50)),
                                             text='Say Hello2',
                                             manager=manager)'''

'''
hello_button = pygame_gui.elements.UITextBox('<font size=4>        <b>Coin</b> : ' + str(player.playerModel.money) + ' </font>', 
                                             pg.Rect((50, 50), (250, 50)),
                                             manager=manager)
                                             '''




stats_title = pygame_gui.elements.UILabel(pg.Rect((75, 0), (250, 50)), "STATS",
                                   manager=manager,
                                   object_id='#inventory')

coin_stat = pygame_gui.elements.UILabel(pg.Rect((-77, 75), (250, 25)), 'Coin: ' + str(player.player_model.money),
                                   manager=manager,
                                   object_id='#coin')

coin_stat2 = pygame_gui.elements.UILabel(pg.Rect((-71, 50), (250, 25)), 'HP: ' + str(player.player_model.current_health) + '/' +  str(player.player_model.health_capacity),
                                   manager=manager,
                                   object_id='#coin')   

coin_stat3 = pygame_gui.elements.UILabel(pg.Rect((-62, 100), (250, 25)), 'Strength: ' + str(player.player_model.strength),
                                   manager=manager,
                                   object_id='#coin')  

stats_title = pygame_gui.elements.UILabel(pg.Rect((75, 125), (250, 50)), "INVENTORY",
                                   manager=manager,
                                   object_id='#inventory')

thing_2= pygame_gui.elements.UILabel(pg.Rect((75, 175), (250, 50)), "No items in inventory", manager=manager, object_id="#coin")

###thing_2= pygame_gui.elements.UIDropDownMenu(relative_rect=pg.Rect((75, 200), (250, 50)), manager=manager, options_list=[], starting_option="")




#health_bar =pygame_gui.elements.UIScreenSpaceHealthBar(pg.Rect((75, 200), (250, 25)),
#                                                 manager=manager, sprite_to_monitor=player.playerModel)#


'''health_bar =pygame_gui.UIScreenSpaceHealthBar(pg.Rect((int(self.rect.width / 9),
                                                              int(self.rect.height * 0.7)),
                                                             (200, 20)),
                                                 manager=manager)'''


'''
htm_text_block_2 = pygame_gui.elements.UITextBox('<font face=fira_code size=2 color=#000000><b>Hey, What the heck!</b>'
                             '<br><br>'
                             'This is some <a href="test">text</a> in a different box,'
                             ' hooray for variety - '
                             'if you want then you should put a ring upon it. '
                             '<body bgcolor=#990000>What if we do a really long word?</body> '
                             '<b><i>derp FALALALALALALALXALALALXALALALALAAPaaaaarp gosh'
                             '</b></i></font>',
                             pg.Rect((-30, 50), (250, 100)),
                             manager=manager,
                             object_id="#text_box_2")                    

'''


'''
coin_stat2 = pygame_gui.elements.UILabel(pg.Rect((-30, 100), (250, 50)), '   HP: ' + str(player.playerModel.money),
                                   manager=manager,
                                   object_id='#coin')
'''

#hello_button2 = pygame_gui.elements.UIButton(relative_rect=pg.Rect((50, 200), (100, 50)),
#                                             text='Say Hello2',
#                                             manager=manager)
#thing = pygame_gui.elements.UIVerticalScrollBar(relative_rect=pg.Rect((50, 200), (100, 50)), manager=manager, visible_percentage=0.5)
#thing_2= pygame_gui.elements.UIDropDownMenu(relative_rect=pg.Rect((50, 200), (100, 50)), manager=manager, options_list=["eggs", "ham", "spam"], starting_option="eggs")


'''htm_text_block_2 = pygame_gui.elements.UITextBox('<font face=fira_code size=2 color=#000000><b>Hey, What the heck!</b>'
                             '<br><br>'
                             'This is some <a href="test">text</a> in a different box,'
                             ' hooray for variety - '
                             'if you want then you should put a ring upon it. '
                             '<body bgcolor=#990000>What if we do a really long word?</body> '
                             '<b><i>derp FALALALALALALALXALALALXALALALALAAPaaaaarp gosh'
                             '</b></i></font>',
                             pg.Rect((50, 200), (100, 50)),
                             manager=manager,
                             object_id="#text_box_2")                        
'''
window_surface = pg.display.set_mode((400, 400))

background = pg.Surface((400, 400))
#background.fill(pg.Color('#545454'))
#background.fill(pg.Color('#000000'))
background.fill(manager.ui_theme.get_colour('dark_bg'))


### USE FOR CREATING BLACK BORDER
#window_surface = pg.display.set_mode((400, 400)) 


while not done:

    if gui_on: 
        time_delta = clock.tick(60)/1000.0



    player.lastMove = -1 

    for event in pg.event.get(): 
        if event.type == pg.QUIT:
            done = True
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_q and gui_on:
                gui_on = False
            if event.key == pg.K_i:
                gui_on = True
                time_delta = clock.tick(60)/1000.0

        elif event.type == pg.USEREVENT:
            if event.user_type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
                print("Selected option:", event.text)
        if gui_on:
            manager.process_events(event)
        
    
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


    for sprite in item_sprites[:]: 
        if player.rect.colliderect(sprite.rect) and sprite not in used_sprites:
            if sprite.item_model.name == "Coin":
                print("Found money!")
                player.player_model.money += 10 
                coin_stat.set_text('Coin: ' + str(player.player_model.money))
                #hello_button = pygame_gui.elements.UITextBox('Coin = ' + str(player.playerModel.money), 
                #                             pg.Rect((50, 50), (250, 50)),
                #                             manager=manager)

            else: 
                print("Found ", sprite.item_model.name)
                player.player_model.add_inventory(sprite.item_model) 
                newInventory = player.player_model.inventory
                newOptions = [i + " x " + str(newInventory[i][0]) for i in newInventory] 
                print(newOptions)
                try: 
                    thing_2.kill()
                except NameError:
                    pass                
                try: 
                    thing3.kill()
                    thing3= pygame_gui.elements.UIDropDownMenu(relative_rect=pg.Rect((10, 200), (250, 50)), manager=manager, options_list=newOptions, starting_option=newOptions[0])
                except NameError:
                    thing3= pygame_gui.elements.UIDropDownMenu(relative_rect=pg.Rect((10, 200), (250, 50)), manager=manager, options_list=newOptions, starting_option=newOptions[0])

            print(sprite.item_model.name)  
            used_sprites.append(sprite)
            used_sprites_locs.add((sprite.rect.x, sprite.rect.y))
            sprite.kill()  
            print(used_sprites_locs)
   
            
    for sprite in door_sprites[:]:
        if player.rect.colliderect(sprite.rect):
            sprite.image = sprite.openImg.convert_alpha() 
        else:
            sprite.image = sprite.closeImg.convert_alpha() 


    if gui_on: 
        manager.update(time_delta)
        window_surface.blit(background, (0, 0))
        manager.draw_ui(window_surface)
        pg.display.update()
    else:
        gMap.render_display(used_sprites_locs)
        all_sprites_list.update()
        all_sprites_list.draw(screen)
        player.rest()
        pg.display.flip()
        clock.tick(30)



