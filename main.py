import pygame as pg
import random

from datetime import datetime
import pygame_gui
from gamemap import *
from gui import *
from globals import *

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
# background.fill(pg.Color('#545454'))
# background.fill(pg.Color('#000000'))
background.fill(inventory_gui.manager.ui_theme.get_colour('dark_bg'))

message_box_on = True
start_time = datetime.now()

while not done:

    if gui_on:
        time_delta = clock.tick(60) / 1000.0

    player.lastMove = -1

    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_q and gui_on:
                gui_on = False
            if event.key == pg.K_i:
                gui_on = True
                time_delta = clock.tick(60) / 1000.0

        elif event.type == pg.USEREVENT:
            if event.user_type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
                debug_log("Selected option:", event.text)
        if gui_on:
            inventory_gui.manager.process_events(event)

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
                inventory_gui.update_inventory()

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

        # if(message_box_on):
        #    screen.blit(label, (0, 0))
        #current_time = datetime.now()
        # if(current_time - start_time).seconds > 3:
        #    message_box_on = False

        for sprite in friend_sprites[:]:
            if sprite.display_label:
                label = myfont.render(sprite.label, 1, pg.Color('#000000'))
                screen.blit(label, (150, 0))
                if (datetime.now() - sprite.start_display_time).seconds > 3:
                    sprite.display_label = False

        pg.display.flip()
        clock.tick(30)

        # if message_box_on == True:
        #    time_delta = clock.tick(60)/1000.0 ## may not do waht is expected, check for double counting
        #    message_box_gui.manager.update(time_delta)
        #    window_surface.blit(background, (0, 0))
        #    message_box_gui.manager.draw_ui(window_surface)
