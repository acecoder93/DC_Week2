import random

class Character:

    def __init__ (self, power, health, name):
        self.power = power
        self.health = health
        self.name = name

    def attack(self, opponent):
        opponent.health -= self.power
        print ('{} did {} damage to the {}.'.format(self.name, self.power, opponent.name))
        print ('The {} did {} damage to {}.'.format(opponent.name, opponent.power, self.name))
        x = random.randint(1,10)
        if x <= 2:
            opponent.health -= (self.power * 2)
            print ('Critical hit!')


        if opponent.health <= 0:
            print ('{} is dead!'.format(opponent.name))

    def alive(self, opponent):
        while self.health > 0:
            self.health -= opponent.power
            opponent.health -= self.power
            if opponent.health <=0:
                print ('{} is dead.'.format(opponent.name))
            elif self.health <= 0:
                print ("{} is dead.".format())
            print("{} do {} damage to the {}.".format(self.name, self.power, opponent.name))
            print("The {} does {} damage to {}.".format(opponent.name, opponent.power, self.name))

        # if self.health <= 0:
        #     print("You are dead.")
        # elif opponent.health <= 0:
        #     print ("Opponent is dead.")

    def health_status(self, opponent):
        print ('{} have {} health.'.format(self.name, self.health))
        print ('{} has {} health.'.format(opponent.name, opponent.health))

class Hero(Character):
    def __init__(self, power, health, name):
        super().__init__(power, health, name)
        
    # def attack(self, opponent):
    #     opponent.health -= self.power
    #     print ('You did {} damage to the goblin.'.format(self.power))
    #     if opponent.health <= 0:
    #         print ('Goblin is dead!')

            
class Goblin(Character):
    def __init__(self, power, health, name):
        super().__init__(power, health, name)



playerselect = {
    'goblin' : Goblin(1, 9, 'Goblin'),
    'anujHero' : Hero(2, 10, 'Hero'),
#     'medicErick' : Medic (4, 5, 'Medic')
# # goblin = Goblin(1, 9, 'Goblin')
# # anuj = Hero(2, 10, 'Hero')
# medicErick = Medic(4, 5, 'Medic')
# zombie = Zombie(3, 10000000000000000, 'Zombie')
}

print(playerselect.value['goblin'])