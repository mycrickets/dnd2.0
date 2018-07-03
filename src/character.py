import src.utils.character.chr_clas.spec as classes
import src.utils.character.race.spec as races
import src.utils.utils as utilities


class Character:
    def __init__(self, level, stats, race, clas, background):
        self.level = int(level)
        self.race = race
        self.clas = clas
        self.strength = int(stats[0])
        self.dexterity = int(stats[1])
        self.wisdom = int(stats[2])
        self.intelligence = int(stats[3])
        self.constitution = int(stats[4])
        self.charisma = int(stats[5])
        self.background = background
        self.name = ""
        self.player_name = ""
        self.age = 0
        self.weight = 0
        self.height = 0
        self.sex = ""
        self.background = ""
        self.traits = ""
        self.ideals = ""
        self.flaws = ""
        self.bonds = ""
        self.alignment = ""



