import src.utils.stats as stats
import src.utils.utils as utilities


class BaseChr:

    def __init__(self, race, clas, bg, level, scores):
        self.level = int(level)
        self.scores = scores
        self.clas = clas
        self.race = race
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


