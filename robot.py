from weapon import Weapon
#(10 points): As a developer, I want a Robot to have a name, health, and active_weapon.
#(10 points): As a developer, I want a Robot to have the ability to attack a Dinosaur on a Battlefield. 
# This attack method should lower the Dinosaur’s health by the attack_power of the Robot’s active_weapon.


class Robot:
    def __init__(self):
        self.name = ""
        self.health = 0
        self.weapon = Weapon()
    
    def robo_attack(self, dinosaur):
        pass
        #void