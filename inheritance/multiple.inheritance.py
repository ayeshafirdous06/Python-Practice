#in multiple inheritance, child class inherits from multiple parent classes.
class icedragon():
    def __init__(self,ice):
        self.ice=ice
    def iceattack(self):
        return f'{self.ice} is attacking with ice..!'
class firedragon():
    def __init__(self,fire):
        self.fire=fire
    def fireattack(self):
        return f'{self.fire} is now attacking with fire..!'
class icefi(icedragon,firedragon):
    def __init__(self,ice,fire):
       icedragon.__init__(self,ice)
       firedragon.__init__(self,fire)
    def attack(self):
        return f'i can attack with both ice and fire..!'
p=icefi("frost","flame")
print(p.iceattack())
print(p.fireattack())
print(p.attack())