
class PlayerModel: 
    def __init__(self, name="Van Eycke", hp=1, maxHp=1, strength=0,inventory={}, curWgt=0, maxWgt=0, wealth=10, weapon=None): 
        self.name = name
        self.hp = hp
        self.maxHp = maxHp
        self.strength = strength
        self.inventory = inventory
        self.curWgt    = curWgt
        self.maxWgt    = maxWgt
        self.wealth    = wealth
        self.weapon    = weapon

    def equipWeapon(self, weapon):
        if self.weapon == None: 
            self.weapon = weapon
        else:
            self.addInventory(self.weapon) 
            self.weapon = weapon

    def unequipWeapon(self):
        if self.weapon == None:
            return 
        else:
            self.addInventory(self.weapon) 
            self.weapon = None

    def getHp(self):
        return self.hp 
    def setHp(self,hp):
        self.hp = hp

    def setStrength(self,strength):
        self.strength = strength 
    def getStrength(self):
        return self.strength
    
    def heal(self, potency):
        if self.hp + potency > self.maxHp:
            self.hp = self.maxHp
        else:
            self.hp += potency
        self.printStats()


    def addInventory(self,item):
        if item.name == "Coin":
            self.money += 10
            return
        if self.curWgt + item.wgt > self.maxWgt: 
            print("Item cannot be picked up. Inventory is full. ")
            return
        if item.name in self.inventory: 
            self.inventory[item.name] = [self.inventory[item.name][0]+1,item]
        else:
            self.inventory[item.name] = [1, item] 
        self.curWgt += item.wgt
    
    def removeItem(self,itemName):
        if self.inventory[itemName][0] == 1: 
            del self.inventory[itemName]
        else:
            self.inventory[itemName][0] -= 1