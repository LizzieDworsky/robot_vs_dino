from robot import Robot
from weapon import Weapon

class Fleet:
    def __init__(self, name):
        self.name = name
        self.robots = [Robot("General Grievous"), Robot("Commando Droid"), Robot("Droideka")]

    def unequip_all_weapons(self):
        self.robots[0].weapons = []
        self.robots[1].weapons = []
        self.robots[2].weapons = []
    
    def equip_weapons(self):
        self.robots[0].weapons = [Weapon("Lightsaber", 75)]
        self.robots[1].weapons = [Weapon("Vibrosword", 50)]
        self.robots[2].weapons = [Weapon("Repeating Blasters", 50)]

    def assign_robot_to_fleet(self, robot_name):
        self.robots.append(Robot(robot_name))

    def grevious_attack(self, dinosaur):
        print (f"{self.robots[0].name} attacks {dinosaur.name} with his {self.robots[0].weapons[0].name} and does {str(self.robots[0].weapons[0].attack_power)} damage.")
        dinosaur.health -= self.robots[0].weapons[0].attack_power
        print (f"{dinosaur.name} now has {str(dinosaur.health)} health left.")

    def commando_attack(self, dinosaur):
        print (f"{self.robots[1].name} attacks {dinosaur.name} with his {self.robots[1].weapons[0].name} and does {str(self.robots[1].weapons[0].attack_power)} damage.")
        dinosaur.health -= self.robots[1].weapons[0].attack_power
        print (f"{dinosaur.name} now has {str(dinosaur.health)} health left.")

    def droideka_attack(self, dinosaur):
        print (f"{self.robots[2].name} attacks {dinosaur.name} with his {self.robots[2].weapons[0].name} and does {str(self.robots[2].weapons[0].attack_power)} damage.")
        dinosaur.health -= self.robots[2].weapons[0].attack_power
        print (f"{dinosaur.name} now has {str(dinosaur.health)} health left.")