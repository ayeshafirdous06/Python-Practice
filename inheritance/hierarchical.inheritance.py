# hierarchical inheritance is a inheritance in which two different child classes inherit from one parent class
#both have a common parent , they dont inherit from each other
class character():
    def __init__(self,name,level):
        self.name=name
        self.level=level
    def ok(self):
        return f'name:{self.name}\nlevel:{self.level}'
class wizard(character):
    def __init__(self,name,level,spell):
        super().__init__(name,level)
        self.spell=spell
    def spe(self):
        return f'{self.name} spells a powerfull spell {self.spell}'
class knight(character):
    def __init__(self,name,level,weapon):
        super().__init__(name,level)
        self.weapon=weapon
    def wep(self):
        return f'{self.name} attacked with {self.weapon}'
d=wizard("merlin",50,"ayy ayy chal nikal")
print("------------wizard------------")
print(d.ok())
print(d.spe())
q=knight("arthur",50,"katana")
print("------------knight------------")
print(q.ok())
print(q.wep())