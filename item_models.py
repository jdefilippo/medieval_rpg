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
    def print_stats(self):
        print("")


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

    def __init__(self, name="Jewel", wgt=1, val=100):
        self.name = name
        self.wgt = wgt
        self.val = val
    def print_stats(self):
        textResult = "Name: " + str(self.name) + " | Weight: " + str(self.wgt) + " | Value: " +  str(self.val)
        return textResult


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
    def print_stats(self):
        textResult = "Name: " + str(self.name) + " | Weight: " + str(self.wgt) + " | Value: " +  str(self.val) + " | Potency: " +  str(self.potency)
        return textResult


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
    def print_stats(self):
        textResult = "Name: " + str(self.name) + " | Weight: " + str(self.wgt) + " | Value: " +  str(self.val) + " | Potency: " +  str(self.potency)
        return textResult



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
    def print_stats(self):
        textResult = "Name: " + str(self.name) + " | Weight: " + str(self.wgt) + " | Value: " +  str(self.val) + " | Potency: " +  str(self.potency)
        return textResult



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
    def print_stats(self):
        textResult = "Name: " + str(self.name) + " | Weight: " + str(self.wgt) + " | Value: " +  str(self.val) + " | Potency: " +  str(self.potency)
        return textResult



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
    def print_stats(self):
        textResult = "Name: " + str(self.name) + " | Weight: " + str(self.wgt) + " | Value: " +  str(self.val) + " | Potency: " +  str(self.potency)
        return textResult
