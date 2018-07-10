from src.utils.character.chr_clas.spec.barbarian import Barbarian
from src.utils.character.race.spec.dragonborn import Dragonborn

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
        #utilities.init_scores(self, self.level)
        self.race = None
        self.clas = None
        self.background = ""
        self.stats = []
        self.personality = ""

    def set_stats(self):
        pass

    def set_race(self):
        race = Dragonborn(self.level)
        self.race = race
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

