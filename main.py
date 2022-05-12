from robot import Robot
from weapon import Weapon
from dinosaur import Dinosaur
from battlefield import Battlefield

#(5 points): As a developer, I want to make at least 7 commits with good, descriptive messages.
#(5 points): As a developer, I want to make a class for each of the following: 
# Robot, Dinosaur, Weapon, Battlefield.

#(10 points): As a developer, I want the battle to conclude once either the robot 
# or the dinosaur has its health points reduced to zero.


my_robo = Robot("C-3PO")
my_dino = Dinosaur("T-rex", 20)
inactive_weapon = Weapon("sword", 50)
my_robo.robo_attack(my_dino)
my_dino.dino_attack(my_robo)
