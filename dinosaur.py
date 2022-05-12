#(10 points): As a developer, I want a Dinosaur to have a name, health, and attack power.
#(10 points): As a developer, I want a Dinosaur to have the ability to attack a Robot on a Battlefield. 
# This attack method should lower a Robot’s health by the value of the Dinosaur’s attack_power.


class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = 100
    
    def dino_attack (self, robot):
        pass
        #void