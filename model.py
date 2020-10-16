
class PlayerModel: 
    def __init__(self, name="Van Eycke", hp=1, maxHp=1, strength=0,inventory={}, curWgt=0, maxWgt=0): 
        self.name = name
        self.hp = hp
        self.maxHp = maxHp
        self.strength = strength
        self.inventory = inventory
        self.curWgt    = curWgt
        self.maxWgt    = maxWgt