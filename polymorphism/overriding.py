#overriding means defining same method name to do different tasks
class Wizard():
    def ok(self):
        return f'me normal jaadu kartau'
class Darkwizard(Wizard):
    def ok(self,spell):
        return super().ok() + f'\ndarkwizard {spell}'
d=Darkwizard()
print(d.ok(" hu me,me kaala jaadu kartau"))