from robot import Robot
from weapon import Weapon

class Fleet:
    def __init__(self):
        self.robots = [Robot("General Grievous"), Robot("Commando Droid"), Robot("Droideka")]

    def unequip_all_weapons(self):
        self.robots.weapons = []
    
    def equip_weapon(self, name, attack_power, index_location):
        self.robots[index_location].weapons = [Weapon(name, attack_power)]

    def assign_robot_to_fleet(self, robot_name):
        self.robots.append(Robot(robot_name))
