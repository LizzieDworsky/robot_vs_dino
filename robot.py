from weapon import Weapon
#(10 points): As a developer, I want a Robot to have a name, health, and active_weapon.
#(10 points): As a developer, I want a Robot to have the ability to attack a Dinosaur on a Battlefield. 
# This attack method should lower the Dinosaur’s health by the attack_power of the Robot’s active_weapon.


class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.weapon = Weapon("sword", 10)
    
    def robo_attack(self, dinosaur):
        print (f"{self.name} attacks {dinosaur.name} and does {str(self.weapon.attack_power)} damage.")
        dinosaur.health -= self.weapon.attack_power
        print (f"{dinosaur.name} now has {str(dinosaur.health)} left.")