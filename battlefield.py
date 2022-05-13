from robot import Robot
from dinosaur import Dinosaur
from fleet import Fleet
from herd import Herd

class Battlefield:
    def __init__(self):
        self.robot = Robot("The Iron Giant")
        self.dinosaur = Dinosaur("Godzilla", 50)
        self.fleet = Fleet("Separatist droids")
        self.herd = Herd("Blue's pack")

    def run_game_one_vs_one(self):
        self.display_welcome_one_vs_one()
        self.battle_phase_one_vs_one()
        self.display_winner_one_vs_one()

    def run_game_one_vs_one_randomized(self):
        self.display_welcome_one_vs_one()
        self.random_battle_one_vs_one()
        self.display_winner_one_vs_one()
    
    def display_welcome_one_vs_one(self):
        print (f"The utimate battle begins. Who will win? {self.robot.name} or {self.dinosaur.name}? Let's find out!")
    
    def battle_phase_one_vs_one(self):
        while self.robot.health > 0 and self.dinosaur.health > 0:
            user_action = input (f"Who will attack next? If {self.robot.name} enter 1, if {self.dinosaur.name} enter 2: ")
            if user_action == "1" and self.robot.health > 0:
                self.robot.robo_attack(self.dinosaur)
            if user_action == "2" and self.dinosaur.health > 0:
                self.dinosaur.dino_attack(self.robot)

    def random_battle_one_vs_one(self):
        while self.robot.health > 0 and self.dinosaur.health > 0:
            user_action = input (f"Who will attack next? If {self.robot.name} enter 1, if {self.dinosaur.name} enter 2: ")
            if user_action == "1" and self.robot.health > 0:
                self.robot.robo_random_attack(self.dinosaur)
            if user_action == "2" and self.dinosaur.health > 0:
                self.dinosaur.dino_attack(self.robot)
    
    def display_winner_one_vs_one(self):
        if self.robot.health == 0:
            print (f"{self.dinosaur.name} defeats {self.robot.name}!")
        else:
            print (f"{self.robot.name} defeats {self.dinosaur.name}!")
    
    def run_game_fleet_vs_herd(self):
        self.display_welcome_fleet_vs_herd()
        self.battle_phase_fleet_vs_herd()
        self.display_winner_fleet_vs_herd()

    def display_welcome_fleet_vs_herd(self):
        print (f"The battle is about to begin! {self.fleet.name} vs {self.herd.name}")

    def battle_phase_fleet_vs_herd(self):
        self.fleet.unequip_all_weapons()
        self.fleet.equip_weapons()

    def display_winner_fleet_vs_herd(self):
        pass