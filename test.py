import random

class Testunit():

    def __init__(self, name, hp, id):
        self.name = name
        self.hp = hp
        self.id = id
    
    def info(self):
        print(self.name)
        print(self.age)

units = {}
unit_id = 0
for n in range(10):
    unit_id = n
    units[unit_id] = Testunit('Rat', random.randint(200, 300), unit_id)
    #print(units[n])
    r = units[n]

    print(r.hp)
    



