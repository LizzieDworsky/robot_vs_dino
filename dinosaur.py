

class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = 250
    
    def dino_attack (self, robot):
        print (f"{self.name} attacks {robot.name} and does {str(self.attack_power)} damage.")
        robot.health -= self.attack_power
        print (f"{robot.name} now has {str(robot.health)} health left.")