from weapon import Weapon


class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 250
        self.weapon = Weapon("Arm Cannon", 50)
    
    def robo_attack(self, dinosaur):
        print (f"{self.name} attacks {dinosaur.name} and does {str(self.weapon.attack_power)} damage with his {self.weapon.name}.")
        dinosaur.health -= self.weapon.attack_power
        print (f"{dinosaur.name} now has {str(dinosaur.health)} health left.")