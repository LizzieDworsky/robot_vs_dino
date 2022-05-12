import random
from weapon import Weapon


class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 250
        self.weapon = [Weapon("Laser Vision", 50), Weapon("Arm Cannon", 50), Weapon("Energy Claw", 25), Weapon("Energy Cannon", 100), Weapon("Tri Scorpion Cannons", 25), Weapon("Spark Spinner Gun", 25)]
    
    def robo_attack(self, dinosaur):
        active_weapon = random.choice (self.weapon)
        print (f"{self.name} attacks {dinosaur.name} and does {str(active_weapon.attack_power)} damage with his {active_weapon.name}.")
        dinosaur.health -= active_weapon.attack_power
        print (f"{dinosaur.name} now has {str(dinosaur.health)} health left.")