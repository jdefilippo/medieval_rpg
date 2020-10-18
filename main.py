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
pg.display.set_caption('Heart of Gold')
clock=pg.time.Clock()
playerSpeed = 4

gMap = GameMap(screen, 'mapDef.xlsx', 'art/characters.png', 'art/basictiles.png', 'art/things.png')

gMap.initialize()

all_sprites_list = pg.sprite.Group()

## TODO: Figure out a better day to handle this
###charSet = gMap.getCharSet()


player          = gMap.get_player_sprites()
merchant        = gMap.get_friend_sprites()
blockedSprites  = gMap.get_blocked_sprites()
itemSprites     = gMap.get_item_sprites()
doorSprites     = gMap.get_door_sprites()
animatedSprites = gMap.get_animated_sprites() 

all_sprites_list.add(player)
all_sprites_list.add(merchant)
all_sprites_list.add(blockedSprites)
all_sprites_list.add(itemSprites)
all_sprites_list.add(doorSprites)
all_sprites_list.add(animatedSprites)


### GUI TEST
gui_on = False
manager = pygame_gui.UIManager((400,400))
hello_button = pygame_gui.elements.UIButton(relative_rect=pg.Rect((50, 50), (100, 50)),
                                             text='Say Hello',
                                             manager=manager)
hello_button2 = pygame_gui.elements.UIButton(relative_rect=pg.Rect((50, 200), (100, 50)),
                                             text='Say Hello2',
                                             manager=manager)

#hello_button2 = pygame_gui.elements.UIButton(relative_rect=pg.Rect((50, 200), (100, 50)),
#                                             text='Say Hello2',
#                                             manager=manager)
#thing = pygame_gui.elements.UIVerticalScrollBar(relative_rect=pg.Rect((50, 200), (100, 50)), manager=manager, visible_percentage=0.5)
#thing2= pygame_gui.elements.UIDropDownMenu(relative_rect=pg.Rect((50, 200), (100, 50)), manager=manager, options_list=["eggs", "ham", "spam"], starting_option="eggs")


htm_text_block_2 = pygame_gui.elements.UITextBox('<font face=fira_code size=2 color=#000000><b>Hey, What the heck!</b>'
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

window_surface = pg.display.set_mode((400, 400))

background = pg.Surface((400, 400))
background.fill(pg.Color('#000000'))

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
                player.rect.y -= 16
        elif event.type == pg.USEREVENT:
            if event.user_type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
                print("Selected option:", event.text)
        if gui_on:
            manager.process_events(event)
        

    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT] and not gui_on:
            player.move_left(playerSpeed)

    if keys[pg.K_RIGHT] and not gui_on:
            player.move_right(playerSpeed)

    if keys[pg.K_DOWN] and not gui_on:
            player.move_down(playerSpeed)

    if keys[pg.K_UP] and not gui_on:
            player.move_up(playerSpeed)

    for sprite in blockedSprites[:]: 
        if player.rect.colliderect(sprite.rect):
            player.rect.x = player.prevX
            player.rect.y = player.prevY 

    for sprite in itemSprites[:]: 
        if player.rect.colliderect(sprite.rect):
            gui_on = True
            time_delta = clock.tick(60)/1000.0

    for sprite in doorSprites[:]:
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
        gMap.render_display()

        all_sprites_list.update()
        all_sprites_list.draw(screen)

        player.rest()

        pg.display.flip()

        clock.tick(30)


