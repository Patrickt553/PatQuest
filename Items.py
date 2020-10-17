from main import player
from random import randint
class Weapon:
    def __init__(self, attk, defns, name, equipped):
        self.attk = attk
        self.defns = defns
        self.name = name
        self.equipped = equipped

class sword(Weapon):
    def __init__(self):
        super(sword, self).__init__(attk=5,
                                    defns=0,
                                    name='Sword',
                                    equipped=False)


def health_potion():
    restore = randint(3, 8)
    player.health = player.health + restore


def fire_bomb():
    damage = randint(10, 20)
    return damage

