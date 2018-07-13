from src.utils.character.chr_clas.spec.barbarian import Barbarian
from src.utils.character.race.spec.dragonborn import Dragonborn
from src.utils.character.race.spec.dwarf import Dwarf
from src.utils.character.race.spec.elf import Elf

import src.utils.utils as utilities


class Character:
    def __init__(self, level):
        self.level = int(level)
        self.strength = 0
        self.dexterity = 0
        self.constitution = 0
        self.charisma = 0
        self.intelligence = 0
        self.wisdom = 0
        self.hp = 0
        #utilities.init_scores(self, self.level)
        self.languages = []
        self.race = None
        self.race_name = ""
        self.clas = None
        self.class_name = ""
        self.alignment = ""
        self.name = ""
        self.player_name = ""
        self.gender = ""
        self.sex = ""
        self.background = ""
        self.personality = ""
        self.trait = ""
        self.ideals = ""
        self.flaws = ""
        self.bonds = ""

    def set_race(self):
        race = input("what race are you?")
        race = race.strip()
        if race == "dragonborn":
            race = Dragonborn(self.level)
            self.race_name = "dragonborn"
        elif race == "dwarf":
            race = Dwarf(self.level)
            self.race_name = "dwarf"
        elif race == "elf":
            race = Elf(self.level)
            self.race_name = "elf"
        self.race = race
        self.hp += self.race.hp
        self.strength += self.race.str_mod
        self.dexterity += self.race.dex_mod
        self.wisdom += self.race.wis_mod
        self.intelligence += self.race.int_mod
        self.charisma += self.race.cha_mod
        self.constitution += self.race.con_mod

    def set_class(self):
        dnd_class = Barbarian(self)
        self.clas = dnd_class

    def set_background(self):
        pass

    def set_personality(self):
        pass

