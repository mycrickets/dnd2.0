import src.utils.character.BaseChr as BaseChr
import src.utils.character.race.BaseRace as BaseRace
import src.utils.utils as utilities


class Dragonborn(BaseRace.BaseRace):
    def __init__(self):
        super(Dragonborn, self).__init__()
        self.resistances = []
        self.attacks = []
        self.color = ""
        self.weapons = []


