import random
from traceback import print_exc

class Creature:
    
    def __init__(self, name, health, power, lucky, spread_power, initiative):
        self.name = name
        self.health = health
        self.power = power
        self.lucky = lucky
        self.spread_power = spread_power
        self.initiative = initiative

    def status(self):
        
        print('Name is: {0}'.format(self.name) )
        print('Healthe is: {0}'.format(self.health) )
        print('Power is: {0}'.format(self.power) )
        print('************************************')

class Battle():

    def __init__(self, hero, monster = []):
        self.hero = hero
        self.monster = monster

    @staticmethod
    def damage(unit):

        UNIT_POWER = unit.power
        UNIT_LUCKY = unit.lucky
        UNIT_SPREAD_POWER = unit.spread_power
        UNIT_TOTAL_DAMAGE = 0

        UNIT_TOTAL_DAMAGE = random.randint(UNIT_POWER - UNIT_SPREAD_POWER, UNIT_POWER + UNIT_SPREAD_POWER)

        # условие для критического удара(х2)
        r = 0
        if random.random() <= (UNIT_LUCKY):
            UNIT_TOTAL_DAMAGE *= 2
            """ print('CRIT')
            r +=1
            print('ver :{0} '.format(r)) """
        else:
            UNIT_TOTAL_DAMAGE *= 1
        
        return UNIT_TOTAL_DAMAGE
        
    def battle_status():
        pass

    @staticmethod
    def queue(hero, monster):

        HERO_INITIATIVE = hero.initiative
        MONSTER_INITIATIVE = monster.initiative

        

        pass

    def battle(self):
        
        HERO_HEALTH = self.hero.health
        MONSTER_HEALTH = []

        for m in self.monster:
            MONSTER_HEALTH.append(m.health)
        
        #while HERO_HEALTH > 0:
        if len(MONSTER_HEALTH) > 0:# если есть живые монстры, то продолжаем бой
            for i in range(len(MONSTER_HEALTH)):
                if MONSTER_HEALTH[i] <= 0:# если хп монстра равно или меньше 0, то он выбывает из боя
                    MONSTER_HEALTH.pop(i)
                else:
                    MONSTER_HEALTH[i] -= self.damage(hero)# наносим удар монстру(
                    HERO_HEALTH -= self.damage(monsters[i])
                    print('Monster hp: {0}'.format(MONSTER_HEALTH[i]))
                    print('Hero hp: {0}'.format(HERO_HEALTH))
            else:
                print('Battle is done!')

                    


            
            

        """ battle_round = 0

        #while self.unit1.health > 0 and self.unit2.health >0:
            battle_round += 1           
                      
            #self.unit1.health -= damage_2
            #self.unit2.health -= damage_1
            if self.unit1.health <= 0:
                print('Battle is done! Rounds: {0}'.format(battle_round))
                print('Winner is: {0}'.format(self.unit2.name))
                self.unit1.health = 0
                break
            if self.unit2.health <= 0:
                print('Battle is done! Rounds: {0}'.format(battle_round))
                print('Battle is done!')
                print('Winner is: {0}'.format(self.unit1.name))
                self.unit2.health = 0
                break
             """

         #pass







hero = Creature('Hero', 1000, 7, 0.2, 2, 1)
monsters = []

for m in range(30):
    rand_power = random.randint(5, 8)
    monsters.append(Creature('Monster', 200, rand_power, 0.1, 4, 2))
    #print(monsters[m])


battle1 = Battle(hero, monsters)
battle1.battle()
#battle1.damage(hero, monsters)




