from character_models import *
import random
import math

import pygame as pg
from globals import *

import numpy as np

class PlayerModel:
    """
    Creates a model representation for PlayerModel with default arguments.
    :param name: The name of the player
    :param hp: The hit point
    :param maxHp: The value of the item
    :param strength: The potency of the item
    :param inventory: The player's inventory-
    :param cur_wgt: The current weight of all items in player's inventory
    :param max_wgt: The maximum weight that a player can carry
    :param money: The current money in the player's possession, determined by initial amount
                   and any additional acquired coin
    :param weapon: The player's weapon, if any
    :param money: The potency of the item
    """

    def __init__(
            self,
            name="Van Eycke",
            hp=40,
            maxHp=40,
            strength=5,
            inventory={},
            cur_wgt=0,
            max_wgt=99,
            weapon=None,
            money=200):
        self.name = name
        self.current_health = hp
        self.health_capacity = maxHp
        self.inventory = inventory
        self.cur_wgt = cur_wgt
        self.max_wgt = max_wgt
        self.money = money
        self.strength = strength

    def process_item(self, item_model):
        if item_model.name == "Coin":
            self.money += 10
        else:
            self.add_inventory(item_model)


    def fight_enemy(self, enemy):
        first_swing = random.randint(0,2)
        if first_swing == 0:  # opponent strikes first
            damage_to_player = math.ceil(np.random.rand() * self.strength)
            self.current_health  -= damage_to_player
            if(self.current_health > 0):
                damage_to_enemy  = math.ceil(np.random.rand() * enemy.strength)
                enemy.current_health -= damage_to_enemy
            else:
                return 1 
        else: # player strikes first 
            damage_to_enemy  = math.ceil(np.random.rand() * enemy.strength)
            enemy.current_health -= damage_to_enemy
            if (enemy.current_health > 0):
                damage_to_player = math.ceil(np.random.rand() * self.strength)
                self.current_health  -= damage_to_player
            else:
                return 0

    """
    Equip a weapon from the player's inventory.
    :param weapon: The weapon to equip
    """

    def equip_weapon(self, weapon):
        if self.weapon is None:
            self.weapon = weapon
        else:
            self.add_inventory(self.weapon)
            self.weapon = weapon

    """
    Unequip the current weapon.
    """

    def unequip_weapon(self):
        if self.weapon is None:
            return
        else:
            self.add_inventory(self.weapon)
            self.weapon = None

    """
    Get the current hitpoints for player

    :return: The current hitpoints
    """

    def get_hp(self):
        return self.hp

    """
    Set the current hitpoints for player
    """

    def set_hp(self, hp):
        self.hp = hp

    """
    Get the current hitpoints for player

    :return: The player's current hitpoints
    """

    def set_strength(self, strength):
        self.strength = strength

    """
    Get the strength for player

    :return: The player's current strength
    """

    def get_strength(self):
        return self.strength

    """
    Health the player with potion
    """

    def heal(self, potency):
        if self.hp + potency > self.maxHp:
            self.hp = self.maxHp
        else:
            self.hp += potency
        self.printStats()

    """
    Add an item to the player's inventory

    :param item: the item object to be added
    """

    def add_inventory(self, item):
        if item.name == "Coin":
            self.money += 10
            return
        if self.cur_wgt + item.wgt > self.max_wgt:
            print("Item cannot be picked up. Inventory is full. ")
            return
        if item.name in self.inventory:
            self.inventory[item.name] = [
                self.inventory[item.name][0] + 1, item]
        else:
            self.inventory[item.name] = [1, item]
        self.cur_wgt += item.wgt

    """
    Add an item to the player's inventory

    :param item: the name of the item to be removed
    """

    def remove_item(self, itemName):
        if self.inventory[itemName][0] == 1:
            del self.inventory[itemName]
        else:
            self.inventory[itemName][0] -= 1

   

class EnemyModel:
    """
    Creates a model representation for PlayerModel with default arguments.
    :param name: The name of the player
    :param hp: The hit point
    :param maxHp: The value of the item
    :param strength: The potency of the item
    """

    def __init__(
            self,
            name="Enemy",
            hp=20,
            maxHp=40,
            strength=5):
        self.name = name
        self.current_health = hp
        self.health_capacity = maxHp
        self.strength = strength
    
class SkeletonModel(EnemyModel):
    """
    Creates a model representation for PlayerModel with default arguments.
    :param name: The name of the player
    :param hp: The hit point
    :param maxHp: The value of the item
    :param strength: The potency of the item
    """

    def __init__(
            self,
            name="Skeleton",
            hp=15,
            maxHp=40,
            strength=4):
        super().__init__(name, hp, maxHp, strength)
       
    
class BatModel:
    """
    Creates a model representation for PlayerModel with default arguments.
    :param name: The name of the player
    :param hp: The hit point
    :param maxHp: The value of the item
    :param strength: The potency of the item
    """

    def __init__(
            self,
            name="Enemy",
            hp=20,
            maxHp=10,
            strength=3):
        self.name = name
        self.current_health = hp
        self.health_capacity = maxHp
        self.strength = strength


class GhostModel:
    """
    Creates a model representation for PlayerModel with default arguments.
    :param name: The name of the player
    :param hp: The hit point
    :param maxHp: The value of the item
    :param strength: The potency of the item
    """

    def __init__(
            self,
            name="Enemy",
            hp=20,
            maxHp=15,
            strength=5):
        self.name = name
        self.current_health = hp
        self.health_capacity = maxHp
        self.strength = strength
    


class TraderModel:
    """
    Creates a model representation for PlayerModel with default arguments.
    :param name: The name of the player
    :param hp: The hit point
    :param maxHp: The value of the item
    :param strength: The potency of the item
    :param inventory: The player's inventory
    :param cur_wgt: The current weight of all items in player's inventory
    :param max_wgt: The maximum weight that a player can carry
    :param money: The current money in the player's possession, determined by initial amount
                   and any additional acquired coin
    :param weapon: The player's weapon, if any
    :param money: The potency of the item
    """

    def __init__(
            self,
            name="Van Eycke",
            hp=20,
            maxHp=40,
            strength=5,
            inventory={},
            cur_wgt=0,
            max_wgt=99,
            weapon=None,
            money=20):
        self.name = name
        self.current_health = hp
        self.health_capacity = maxHp
        self.inventory = inventory
        self.cur_wgt = cur_wgt
        self.max_wgt = max_wgt
        self.money = money
        self.strength = strength

    """
    Equip a weapon from the player's inventory.
    :param weapon: The weapon to equip
    """

    def equip_weapon(self, weapon):
        if self.weapon is None:
            self.weapon = weapon
        else:
            self.add_inventory(self.weapon)
            self.weapon = weapon

    """
    Unequip the current weapon.
    """

    def unequip_weapon(self):
        if self.weapon is None:
            return
        else:
            self.add_inventory(self.weapon)
            self.weapon = None

    """
    Get the current hitpoints for player

    :return: The current hitpoints
    """

    def get_hp(self):
        return self.hp

    """
    Set the current hitpoints for player
    """

    def set_hp(self, hp):
        self.hp = hp

    """
    Get the current hitpoints for player

    :return: The player's current hitpoints
    """

    def set_strength(self, strength):
        self.strength = strength

    """
    Get the strength for player

    :return: The player's current strength
    """

    def get_strength(self):
        return self.strength

    """
    Health the player with potion
    """

    def heal(self, potency):
        if self.hp + potency > self.maxHp:
            self.hp = self.maxHp
        else:
            self.hp += potency
        self.printStats()

    """
    Add an item to the player's inventory

    :param item: the item object to be added
    """

    def add_inventory(self, item):
        if item.name == "Coin":
            self.money += 10
            return
        if self.cur_wgt + item.wgt > self.max_wgt:
            print("Item cannot be picked up. Inventory is full. ")
            return
        if item.name in self.inventory:
            self.inventory[item.name] = [
                self.inventory[item.name][0] + 1, item]
        else:
            self.inventory[item.name] = [1, item]
        self.cur_wgt += item.wgt

    """
    Add an item to the player's inventory

    :param item: the name of the item to be removed
    """

    def remove_item(self, itemName):
        if self.inventory[itemName][0] == 1:
            del self.inventory[itemName]
        else:
            self.inventory[itemName][0] -= 1
