import src.utils.character.BaseChr as BaseChr
import src.utils.character.race.BaseRace as BaseRace
import src.utils.utils as utilities


class Dragonborn(BaseRace.BaseRace):
    def __init__(self, level):
        BaseRace.BaseRace.__init__(self, True, level)
        self.resistances = []
        self.attacks = []
        self.color = ""
        self.weapons = []


