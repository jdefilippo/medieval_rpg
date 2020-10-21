class ItemModel: 
    def __init__(self, name="",wgt=0,val=0):
        self.name = ""
        self.wgt = wgt
        self.val = val

### VALUABLES ### 

class Coin(ItemModel):
    def __init__(self, name="Coin",wgt=1,val=10):
        self.name = name
        self.wgt = wgt
        self.val = val
        self.id = 0

class Jewel(ItemModel):
    def __init__(self,name="Jewel",wgt=1,val=50,potency=1):
        self.name = name
        self.wgt = wgt 
        self.val = val 
        self.potency = potency
        self.id = 1


class Armor(ItemModel):
    def __init__(self,name="Armor",wgt=1,val=50,potency=1):
        self.name = name
        self.wgt = wgt 
        self.val = val 
        self.potency = potency
        self.id = 1

class MagicSpell(ItemModel):
    def __init__(self,name="Magic Spell",wgt=1,val=50,potency=1):
        self.name = name
        self.wgt = wgt 
        self.val = val 
        self.potency = potency
        self.id = 1

class Sword(ItemModel):
    def __init__(self,name="Sword",wgt=1,val=50,potency=1):
        self.name = name
        self.wgt = wgt 
        self.val = val 
        self.potency = potency
        self.id = 1

class HealthPotion(ItemModel):
    def __init__(self,name="Health Potion",wgt=1,val=50,potency=1):
        self.name = name
        self.wgt = wgt 
        self.val = val 
        self.potency = potency
        self.id = 1

class Mushrooms(ItemModel):
    def __init__(self,name="Murshrooms",wgt=1,val=50,potency=1):
        self.name = name
        self.wgt = wgt 
        self.val = val 
        self.potency = potency
        self.id = 1


class PlayerModel: 
    def __init__(self, name="Van Eycke", hp=20, maxHp=40, strength=5,inventory={}, cur_wgt=0, max_wgt=99, wealth=10, weapon=None, money=20): 
        self.name = name
        #self.hp = hp
        #self.maxHp = maxHp
        self.current_health = hp
        self.health_capacity = maxHp
        self.inventory = inventory
        self.cur_wgt    = cur_wgt
        self.max_wgt    = max_wgt
        self.wealth    = wealth
        self.weapon    = weapon
        self.money     = money
        self.strength  = strength

    def equip_weapon(self, weapon):
        if self.weapon == None: 
            self.weapon = weapon
        else:
            self.add_inventory(self.weapon) 
            self.weapon = weapon

    def unequip_weapon(self):
        if self.weapon == None:
            return 
        else:
            self.add_inventory(self.weapon) 
            self.weapon = None

    def get_hp(self):
        return self.hp 
    def set_hp(self,hp):
        self.hp = hp

    def set_strength(self,strength):
        self.strength = strength 
    def get_strength(self):
        return self.strength
    
    def heal(self, potency):
        if self.hp + potency > self.maxHp:
            self.hp = self.maxHp
        else:
            self.hp += potency
        self.printStats()


    def add_inventory(self,item):
        if item.name == "Coin":
            self.money += 10
            return
        if self.cur_wgt + item.wgt > self.max_wgt: 
            print("Item cannot be picked up. Inventory is full. ")
            return
        if item.name in self.inventory: 
            self.inventory[item.name] = [self.inventory[item.name][0]+1,item]
        else:
            self.inventory[item.name] = [1, item] 
        self.cur_wgt += item.wgt
    
    def remove_item(self,itemName):
        if self.inventory[itemName][0] == 1: 
            del self.inventory[itemName]
        else:
            self.inventory[itemName][0] -= 1