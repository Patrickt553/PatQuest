from random import randint



class Enemy:
    def __init__(self, health, strength, mana, name):
        self.health = health
        self.strength = strength
        self.mana = mana
        self.name = name


class Kobold(Enemy):
    def __init__(self):
        super(Kobold, self).__init__(health=20,
                                     strength=3,
                                     mana=10,
                                     name='Kobold')


class Orc(Enemy):
    def __init__(self):
        super(Orc, self).__init__(health=25,
                                  strength=5,
                                  mana=3,
                                  name='Orc')

class Sorceror(Enemy):
    def __init__(self):
        super(Sorceror, self).__init__(health=15,
                                       strength=0,
                                       mana=18,
                                       name='Sorceror')



def getEnemy():
    enemyList = [Orc, Kobold, Sorceror]
    enemychoice = randint(0, (len(enemyList) - 1))
    enemyPick = enemyList[int(enemychoice)]
    if enemyPick == Orc:
        enemy = Orc()
    elif enemyPick == Kobold:
        enemy = Kobold()
    elif enemyPick == Sorceror:
        enemy = Sorceror()

    return enemy


