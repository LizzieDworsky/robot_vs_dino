from robot import Robot

class Fleet:
    def __init__(self):
        self.robots = []

    def unequip_all_weapons(self):
        self.robots.weapons = []
    
    def equip_weapon(self, name, attack_power):
        
        pass

    def assign_robot_to_fleet(self, robot_name):
        self.robots.append(Robot(robot_name))
        pass
