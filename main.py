from random import randint
import sys
from Enemy import getEnemy

itemList = ['Potion', 'FireBomb']
inventory =[]


def roll():
    dice = int(randint(1, 6))
    return dice


class Player:
    def __init__(self, health, inventory, strength, mana, name, prof):
        self.health = health
        self.inventory = inventory
        self.strength = strength
        self.mana = mana
        self.name = name
        self.prof = prof

class Fighter(Player):
    def __init__(self):
        super(Fighter, self).__init__(health=25,
                                      inventory=inventory,
                                      strength=5,
                                      mana=5,
                                      name=input('What is your name: '),
                                      prof='Fighter')
        prof = 'Fighter'
        max_hp = 25
        max_mana = 5


class Mage(Player):
    def __init__(self):
        super(Mage, self).__init__(health=15,
                                   inventory=inventory,
                                   strength=0,
                                   mana=30,
                                   name=input('What is your name: '),
                                   prof='Mage')
        prof = 'Mage'
        max_hp = 15
        max_mana = 30

def proffesion():
    pchoice = int(input('Choose a class:\n'
                             '1. Fighter\n'
                             '2. Mage\n'
                             '>>> '))

    if pchoice == 1:
        prof = Fighter()
    elif pchoice == 2:
        prof = Mage()
    return prof

def drop_table():
    drop_int = randint(0, (len(itemList) - 1))
    drop_tick = str(itemList[int(drop_int)])
    print('You found a ' + str(drop_tick) + '!')
    inventory.append(drop_tick)

def health_potion():
    restore = randint(3, 8)
    player.health = player.health + restore

def fire_bomb():
    damage = randint(10, 20)
    return damage



def attackphase():
    enemy = getEnemy()
    print('You encounter a ' + enemy.name + '\n')
    while True:
        if player.health <= 0:
            print('You are dead! Try again? Y/N\n')
            tryagain = str(input('>>>'))
            if tryagain == 'Y':
                break
            else:
                sys.exit()
        if enemy.health <= 0:
            print('The ' + enemy.name + ' has been defeated!\n')
            drop_table()
            break
        else:
            pass

        print('Choose an action:\n'
              '1.Attack with weapon\n'
              '2.Spells/Skills\n'
              '3.Inventory\n'
              '4.Character Sheet\n'
              '5.Quit\n')

        attackPhaseChoice = int(input('>>> '))

        if attackPhaseChoice == 1:

            pre_damage = randint(1, 5)
            damage = pre_damage + player.strength
            enemy.health = enemy.health - damage
            print('You hit the ' + enemy.name + ' for ' + str(damage) + ' damage!\n')

            preEnemyDamage = randint(1, 5)
            enemyDamage = preEnemyDamage + enemy.strength
            player.health = player.health - enemyDamage
            print('The ' + enemy.name + ' hits you for ' + str(enemyDamage) + ' damage!\n')


        if attackPhaseChoice == 2:
            if player.prof == 'Fighter':
                print('Skills:\n'
                      '1.Focused Strike\n')
                skillChoice = int(input('>>> '))
                if skillChoice == 1:
                    pre_damage = 5
                    damage = pre_damage + player.strength
                    enemy.health = enemy.health - damage
                    print('You hit the ' + enemy.name + ' for ' + str(damage) + ' damage!\n')

                    preEnemyDamage = randint(1, 5)
                    enemyDamage = preEnemyDamage + enemy.strength
                    player.health = player.health - enemyDamage
                    print('The ' + enemy.name + ' hits you for ' + str(enemyDamage) + ' damage!\n')

            if player.prof == 'Mage':
                print('Spells:\n'
                      '1.Fireball\n')

                spellChoice = int(input('>>> '))
                if  spellChoice == 1:
                    player.mana = player.mana - 6
                    fire_ball_damage = 6 + randint(1, 6)
                    enemy.health = enemy.health - fire_ball_damage
                    print('Your Fireball burns the ' + enemy.name + ' for ' + str(fire_ball_damage) + ' damage!')
                    print('You have ' + str(player.mana) + ' mana left\n')

                    preEnemyDamage = randint(1, 5)
                    enemyDamage = preEnemyDamage + enemy.strength
                    player.health = player.health - enemyDamage
                    print('The ' + enemy.name + ' hits you for ' + str(enemyDamage) + ' damage!')



        if attackPhaseChoice == 3:
            print('Items in bag:')
            selectnumber = 1
            for x in inventory:
                print(str(selectnumber) + '. ' + x)
                selectnumber = selectnumber + 1

            print('')
            selection = int(input('>>> '))
            if selection == inventory.index('Potion'):
                pre_restored_hp = player.health
                health_potion()
                print('You drink the potion and restore ' + str(player.health - pre_restored_hp) + '!')
            elif selection == inventory.index('FireBomb'):
                fb_damage = fire_bomb()
                enemy.health = enemy.health - fb_damage
                print('You hurl the bomb at the ' + enemy.name + ' for ' + str(fb_damage) + ' damage!')
            inventory.pop(int(selection) - 1)
        if attackPhaseChoice == 4:
            print('You have ' + str(player.health) + ' health and ' + str(player.mana) + ' mana left.')
        if attackPhaseChoice == 5:
            sys.exit()


player = proffesion()


while True:

    print('What would you like to do?: \n'
          '1.Fight a monster\n'
          '2.Spells/Skills\n'
          '3.Inventory\n'
          '4.Character Sheet\n'
          '5.Quit')
    mainMenuChoice = int(input('>>>'))

    if mainMenuChoice == 1:
        attackphase()

    if mainMenuChoice == 2:
        if player.prof == 'Fighter':
            print('Skills (Choose for description:\n'
                  '1. Focused Strike\n')
            spellDescrip = int(input('>>> '))
            if spellDescrip == 1:
                print('The Fighter puts all of his focus into a singular blow.\n'
                      'Guaranteeing maximum damage on his next hit. Cost: 2 mana.\n'
                      '\n')

        if player.prof == 'Mage':
            print('Spells (Choose for description:\n'
                  '1.Fireball\n')
            spellDescrip = int(input('>>>'))
            if spellDescrip == 1:
                print('The Mage compels the heavens above to release a fiery\n'
                      'bolt of flame dealing 6 + (1 - 6) damage. Cost: 6 mana.\n')

    if mainMenuChoice == 3:
        print('Items in bag:')
        selectnumber = 1
        for x in inventory:
            print(str(selectnumber) + '. ' + x)
            selectnumber = selectnumber + 1

    if mainMenuChoice == 4:
        pass
    if mainMenuChoice == 5:
        sys.exit()
    else:
        pass
