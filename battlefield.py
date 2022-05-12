from robot import Robot
from dinosaur import Dinosaur

class Battlefield:
    def __init__(self):
        self.robot = Robot("The Iron Giant")
        self.dinosaur = Dinosaur("Godzilla", 50)

    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()
    
    def display_welcome(self):
        print (f"The utimate battle begins. Who will win? {self.robot.name} or {self.dinosaur.name}? Let's find out!")
    
    def battle_phase(self):
        while self.robot.health > 0 and self.dinosaur.health > 0:
            if self.robot.health > 0:
                self.robot.robo_attack(self.dinosaur)
            if self.dinosaur.health > 0:
                self.dinosaur.dino_attack(self.robot)
    
    def display_winner(self):
        if self.robot.health == 0:
            print (f"{self.dinosaur.name} defeats {self.robot.name}!")
        else:
            print (f"{self.robot.name} defeats {self.dinosaur.name}!")