import pstats
from unicodedata import name
from dinosaur import Dinosaur

class Herd:
    def __init__(self, name):
        self.name = name
        self.herd = [Dinosaur("Blue", 75), Dinosaur("Charlie", 50), Dinosaur("Delta", 50), Dinosaur("Echo", 50)]

    def assign_dino_to_herd(self, dinosaur_name, dino_attack):
        self.herd.append(Dinosaur(dinosaur_name, dino_attack))

    def blue_attack(self, robot):
        print(f"{self.herd[0].name} attacks {robot.name} and does {str(self.herd[0].attack_power)} damage.")
        robot.health -= self.herd[0].attack_power
        print(f"{robot.name} now has {str(robot.health)} health left")

    def charlie_attack(self, robot):
        print(f"{self.herd[1].name} attacks {robot.name} and does {str(self.herd[1].attack_power)} damage.")
        robot.health -= self.herd[1].attack_power
        print(f"{robot.name} now has {str(robot.health)} health left")

    def delta_attack(self, robot):
        print(f"{self.herd[2].name} attacks {robot.name} and does {str(self.herd[2].attack_power)} damage.")
        robot.health -= self.herd[2].attack_power
        print(f"{robot.name} now has {str(robot.health)} health left")

    def echo_attack(self, robot):
        print(f"{self.herd[3].name} attacks {robot.name} and does {str(self.herd[3].attack_power)} damage.")
        robot.health -= self.herd[3].attack_power
        print(f"{robot.name} now has {str(robot.health)} health left")