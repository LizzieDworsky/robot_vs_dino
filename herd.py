from dinosaur import Dinosaur

class Herd:
    def __init__(self, name):
        self.name = name
        self.herd = [Dinosaur("Blue", 75), Dinosaur("Charlie", 50), Dinosaur("Delta", 50), Dinosaur("Echo", 50)]

    def assign_dino_to_herd(self, dinosaur_name, dino_attack):
        self.herd.append(Dinosaur(dinosaur_name, dino_attack))