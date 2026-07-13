# single inheritance is a inheritance where only one child and parent classes exists.
# child class inherits from only one base class.
# it is the simple and most common type of inheritance.
class Ninja():
    def __init__(self,name,rank):
        self.name=name
        self.rank=rank
    def introduce(self):
        return f'hey im {self.name} and im at rank {self.rank}'
class Shadowninja(Ninja):
    def __init__(self,name,rank,weapon,hp):
        super().__init__(name,rank)
        self.weapon=weapon
        self.hp=hp
    def attack(self):
        return f'{self.name} attacked with {self.weapon}'
    def hide(self):
        if self.hp >= 80:
            return (f"{self.name} hid into shadows")
        else:
            return ("hp is too low to hide")
p=Shadowninja("ayesha","jonin","katana",80)
print(p.introduce())
print(p.attack())
print(p.hide())