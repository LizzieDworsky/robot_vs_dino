import random
from weapon import Weapon


class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 250
        self.weapon = [Weapon("Laser Vision", 50), Weapon("Energy Cannon", 100), Weapon("Energy Claw", 25), Weapon("Arm Cannon", 50), Weapon("Tri Scorpion Cannons", 25), Weapon("Spark Spinner Gun", 25)]
    
    def robo_attack(self, dinosaur):
        user_choice = input (f"Please select what weapon {self.name} should use. For {self.weapon[0].name} with damage {self.weapon[0].attack_power} enter 1. For {self.weapon[1].name} with damage {self.weapon[1].attack_power} enter 2. For {self.weapon[2].name} with damage {self.weapon[2].attack_power} enter 3. ")
        if user_choice == "1":
            active_weapon = self.weapon[0]
        elif user_choice == "2":
            active_weapon = self.weapon[1]
        elif user_choice == "3":
            active_weapon = self.weapon[2]
        print (f"{self.name} attacks {dinosaur.name} and does {str(active_weapon.attack_power)} damage with his {active_weapon.name}.")
        dinosaur.health -= active_weapon.attack_power
        print (f"{dinosaur.name} now has {str(dinosaur.health)} health left.")

    def robo_random_attack(self, dinosaur):
        active_weapon = random.choice (self.weapon)
        print (f"{self.name} attacks {dinosaur.name} and does {str(active_weapon.attack_power)} damage with his {active_weapon.name}.")
        dinosaur.health -= active_weapon.attack_power
        print (f"{dinosaur.name} now has {str(dinosaur.health)} health left.")