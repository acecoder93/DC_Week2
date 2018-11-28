import random

class Character:
    def __init__ (self, power, health, name, coins, coinbag): # add money/inventory
        self.power = power
        self.health = health
        self.name = name
        self.coins = coins
        self.coinbag = coinbag

    def attack(self, opponent):
        opponent.health -= self.power
        # print ('{} did {} damage to the {}.'.format(self.name, self.power, opponent.name))
        # print ('The {} did {} damage to {}.'.format(opponent.name, opponent.power, self.name))
        x = random.randint(1,10)
        if x <= 2:
            opponent.health -= (self.power * 2)
            print ('Critical hit!')
        if opponent.health <= 0:
            print ('{} is dead!'.format(opponent.name))
            print ('{} has dropped {} coins.'.format(opponent.name, opponent.coins))
            self.coinbag = opponent.coins

    def alive(self, opponent):
        print ('{} have {} health.'.format(self.name, self.health))
        print ('{} has {} health.'.format(opponent.name, opponent.health))
        while self.health > 0:
            self.health -= opponent.power
            # opponent.health -= self.power # Not needed as there is no action being committed
            if opponent.health <=0:
                if opponent.name == 'Zombie':
                    ZomboDaZombie.neverdie(enemy)
                elif opponent.health <= 0:
                    print ('{} is dead.'.format(opponent.name))
                    print ('{} has dropped {} coins.'.format(opponent.name, opponent.coins))
                    self.coinbag = opponent.coins

                elif self.health <= 0:
                    print ("{} is dead.".format(self.name))
                    print ('{} has dropped {} coins.'.format(self.name, self.coins))
                    self.coinbag = opponent.coins

            print("{} do {} damage to the {}.".format(self.name, self.power, opponent.name))
            print("The {} does {} damage to {}.".format(opponent.name, opponent.power, self.name))

    # def health_status(self, opponent): # Removed this section and inserted into alive section to consolidate code
    #     print ('{} have {} health.'.format(self.name, self.health))
    #     print ('{} has {} health.'.format(opponent.name, opponent.health))

class Hero(Character):
    def __init__(self, power, health, name, coins, coinbag):
        super().__init__(power, health, name, coins, coinbag)
            
class Goblin(Character):
    def __init__(self, power, health, name, coins, coinbag):
        super().__init__(power, health, name, coins, coinbag)

class Medic(Character):
    def __init__(self, power, health, name, coins, coinbag):


anuj = Hero(2, 10, 'Hero', 5, 5)


class Tonic:
    cost = 5
    name = 'tonic'
    def apply(self, character):
        self.health +=2
        print ('{}\'s health increased to {}.'.format(self.name, self.health))
class Sword:
    cost = 10
    name = 'sword'
    def apply(self, character):
        self.power += 2
        print ('{}\'s power increased to {}.'.format(self.name, self.power))



store_list = [Tonic, Sword]
items = [Tonic, Sword]
def do_shopping(self,hero):
    while True:
        print("=====================")
        print("Welcome to the store!")
        print("=====================")

        print ('You have {} coins.'.format(hero.coinbag))
        for x in range(len(store_list)):
            item = store_list[x]
            print ("{}. buy {} ({})".format(i+1, item.name, item.cost))
        print ('10. None - Exit Store')
        option_select = int(input('Enter a number: '))

        if option_select == 10:
            break
        else:
            item_to_purchase = store_list[option_select-1]
            item = item_to_purchase()
            hero.buy(item)


