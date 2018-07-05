import src.utils.character.chr_clas.spec as classes
from src.utils.character.race.spec.dragonborn import Dragonborn
import src.utils.utils as utilities


class Character:
    def __init__(self, level):
        self.level = int(level)
        self.race = None
        self.clas = ""
        self.background = ""
        self.stats = ""
        self.personality = ""

    def set_stats(self):
        pass

    def set_race(self):
        race = Dragonborn(self.level)
        self.race = race

    def set_class(self):
        pass

    def set_background(self):
        pass

    def set_personality(self):
        pass

