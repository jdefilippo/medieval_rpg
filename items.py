class ItemModel:
    """
    Creates a model representation for a generic item with default arguments.
    :param name: The name of the object
    :param wgt: The weight of the object in inventory
    :param val: The value of the item
    """

    def __init__(self, name="", wgt=0, val=0):
        self.name = ""
        self.wgt = wgt
        self.val = val


class Coin(ItemModel):
    """
    Creates a model representation for Coin with default arguments.
    :param name: The name of the object
    :param wgt: The weight of the object in inventory
    :param val: The value of the item
    """

    def __init__(self, name="Coin", wgt=1, val=10):
        self.name = name
        self.wgt = wgt
        self.val = val


class Jewel(ItemModel):
    """
    Creates a model representation for Jewel with default arguments.
    :param name: The name of the object
    :param wgt: The weight of the object in inventory
    :param val: The value of the item
    :param potency: The potency of the item
    """

    def __init__(self, name="Jewel", wgt=1, val=50):
        self.name = name
        self.wgt = wgt
        self.val = val


class Armor(ItemModel):
    """
    Creates a model representation for Armor with default arguments.
    :param name: The name of the object
    :param wgt: The weight of the object in inventory
    :param val: The value of the item
    :param potency: The potency of the item
    """

    def __init__(self, name="Armor", wgt=1, val=50, potency=1):
        self.name = name
        self.wgt = wgt
        self.val = val
        self.potency = potency


class MagicSpell(ItemModel):
    """
    Creates a model representation for MagicSpell with default arguments.
    :param name: The name of the object
    :param wgt: The weight of the object in inventory
    :param val: The value of the item
    :param potency: The potency of the item
    """

    def __init__(self, name="Magic Spell", wgt=1, val=50, potency=1):
        self.name = name
        self.wgt = wgt
        self.val = val
        self.potency = potency


class Sword(ItemModel):
    """
    Creates a model representation for Sword with default arguments.
    :param name: The name of the object
    :param wgt: The weight of the object in inventory
    :param val: The value of the item
    :param potency: The potency of the item
    """

    def __init__(self, name="Sword", wgt=1, val=50, potency=1):
        self.name = name
        self.wgt = wgt
        self.val = val
        self.potency = potency


class HealthPotion(ItemModel):
    """
    Creates a model representation for HealthPotion with default arguments.
    :param name: The name of the object
    :param wgt: The weight of the object in inventory
    :param val: The value of the item
    :param potency: The potency of the item
    """

    def __init__(self, name="Health Potion", wgt=1, val=50, potency=1):
        self.name = name
        self.wgt = wgt
        self.val = val
        self.potency = potency


class Mushrooms(ItemModel):
    """
    Creates a model representation for Mushrooms with default arguments.
    :param name: The name of the object
    :param wgt: The weight of the object in inventory
    :param val: The value of the item
    :param potency: The potency of the item
    """

    def __init__(self, name="Mushrooms", wgt=1, val=50, potency=1):
        self.name = name
        self.wgt = wgt
        self.val = val
        self.potency = potency


class PlayerModel:
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
