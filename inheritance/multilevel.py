#multi-levelinheritance is a inheritancein which a childclass is parent for another child class.
class hero:
    def __init__(self,name,level,health):
        self.name=name
        self.level=level
        self.health=health
    def gethero(self):
        return f"name:{self.name},level:{self.level},health:{self.health}"
class warrior(hero):
    def __init__(self,name,level,health,weapon):
        super().__init__(name,level,health)
        self.weapon=weapon
    def getweapon(self):
        return f"weapon:{self.weapon}"
    def attack(self):
        return f"{self.name} attacked with {self.weapon} !"
class legendarywarrior(warrior):
    def __init__(self,name,level,health,weapon,dragonxp):
        super().__init__(name,level,health,weapon)
        self.dragon=dragonxp
    def fight(self):
        self.dragon-=20
        return f"{self.name} fought with dragon and now the dragon xp is {self.dragon}..!"
    def dragatck(self):
        self.health-=10
        return f"now the dragon attacked {self.name} and {self.name}'s health is {self.health}"
    def atck(self):
        self.dragon-=40
        return f'{self.name} attacks the dragon again now the dragon xp is {self.dragon}'
d=legendarywarrior("ayesha",5,100,"sword",100)
print(d.gethero())
print(d.getweapon())
print(d.attack())
print(d.fight())
print(d.dragatck())
t=input("wanna attack again? (yes/no):")
if t=="yes":
    print(d.atck())
else:
    print("attack kro maaaaa, yes type kro")
print(f"{d.name} attacks the dragon again  and now dragon xp is {d.dragon}and now {d.name} is the winner!")