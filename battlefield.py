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
        self.herd.blue_attack(self.fleet.robots[0])
        self.herd.charlie_attack(self.fleet.robots[1])
        self.herd.delta_attack(self.fleet.robots[2])
        self.herd.echo_attack(self.fleet.robots[0])
        self.fleet.grevious_attack(self.herd.pack[0])
        self.fleet.grevious_attack(self.herd.pack[1])
        self.fleet.commando_attack(self.herd.pack[2])
        self.fleet.droideka_attack(self.herd.pack[3])


        while (self.fleet.robots[0].health >0 or self.fleet.robots[1].health >0 or self.fleet.robots[2].health >0) and (self.herd.pack[0].health >0 or self.herd.pack[1].health >0 or self.herd.pack[2].health >0 or self.herd.pack[3].health >0):
            print (f"Currently on the {self.fleet.name} side {self.fleet.robots[0].name} has {str(self.fleet.robots[0].health)} health, {self.fleet.robots[1].name} has {str(self.fleet.robots[1].health)} health, and {self.fleet.robots[2].name} has {str(self.fleet.robots[2].health)} health.")
            print (f"On the {self.herd.name} side {self.herd.pack[0].name} has {str(self.herd.pack[0].health)} health, {self.herd.pack[1].name} has {str(self.herd.pack[1].health)} health, {self.herd.pack[2].name} has {str(self.herd.pack[2].health)} health, and {self.herd.pack[3].name} has {str(self.herd.pack[3].health)} health.")
            user_action_one = input (f"Who will attack next? If {self.fleet.name} enter 1, if {self.herd.name} enter 2: ")
            if user_action_one == "1":
                user_action_two = input(f"Who would you like use for your attack, if {} enter 1, if {} enter 2, if {} enter 3: ")
                if user_action_two == "1":
                    user_action_three = input(f"Who would you like {} to attack, if {} enter 1, if {} enter 2, if {} enter 3, if {} enter 4: ")
                    if user_action_three == "1":
                        pass
                    elif user_action_three == "2":
                        pass
                    elif user_action_three == "3":
                        pass
                    elif user_action_three == "4": 
                        pass
                elif user_action_two == "2":
                    user_action_three = input(f"Who would you like {} to attack, if {} enter 1, if {} enter 2, if {} enter 3, if {} enter 4: ")
                    if user_action_three == "1":
                        pass
                    elif user_action_three == "2":
                        pass
                    elif user_action_three == "3":
                        pass
                    elif user_action_three == "4": 
                        pass
                elif user_action_one == "3":
                    user_action_three = input(f"Who would you like {} to attack, if {} enter 1, if {} enter 2, if {} enter 3, if {} enter 4: ")
                    if user_action_three == "1":
                        pass
                    elif user_action_three == "2":
                        pass
                    elif user_action_three == "3":
                        pass
                    elif user_action_three == "4": 
                        pass
            elif user_action_one == "2":
                user_action_two = input(f"Who would you like to use for your attack, if {} enter 1, if {} enter 2, if{} enter 3, if {} enter 4: ")
                if user_action_two == "1":
                    user_action_three = input(f"Who would you like {} to attack, if {} enter 1, if {} enter 2, if {} enter 3: ")
                    if user_action_three == "1":
                        pass
                    elif user_action_three == "2":
                        pass
                    elif user_action_three == "3":
                        pass
                elif user_action_two == "2":
                    user_action_three = input(f"Who would you like {} to attack, if {} enter 1, if {} enter 2, if {} enter 3: ")
                    if user_action_three == "1":
                        pass
                    elif user_action_three == "2":
                        pass
                    elif user_action_three == "3":
                        pass
                elif user_action_two == "3":
                    user_action_three = input(f"Who would you like {} to attack, if {} enter 1, if {} enter 2, if {} enter 3: ")
                    if user_action_three == "1":
                        pass
                    elif user_action_three == "2":
                        pass
                    elif user_action_three == "3":
                        pass
                elif user_action_two == "4":
                    user_action_three = input(f"Who would you like {} to attack, if {} enter 1, if {} enter 2, if {} enter 3: ")
                    if user_action_three == "1":
                        pass
                    elif user_action_three == "2":
                        pass
                    elif user_action_three == "3":
                        pass

    def display_winner_fleet_vs_herd(self):
        if self.fleet.robots[0].health == 0 and self.fleet.robots[1].health == 0 and self.fleet.robots[2].health == 0:
            print (f"{self.herd.name} defeats {self.fleet.name}!")
        else:
            print (f"{self.fleet.name} defeats {self.herd.name}!")