#(10 points): As a developer, I want a Dinosaur to have a name, health, and attack power.
#(10 points): As a developer, I want a Dinosaur to have the ability to attack a Robot on a Battlefield. 
# This attack method should lower a Robot’s health by the value of the Dinosaur’s attack_power.


class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = 100
    
    def dino_attack (self, robot):
        print (f"{self.name} attacks {robot.name} and does {str(self.attack_power)} damage.")
        robot.health -= self.attack_power
        print (f"{robot.name} now has {str(robot.health)} health left.")