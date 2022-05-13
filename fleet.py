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
