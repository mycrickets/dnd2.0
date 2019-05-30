from utils.character.race.BaseRace import BaseRace
from utils.character.MagicChr import MagicChr
import utils.utils as utilities


class HalfElf(BaseRace, MagicChr):
    def __init__(self, level):
        BaseRace.__init__(self, level)
        MagicChr.__init__(self)
        self.level = int(level)
        self.cha_mod = 2
        self.age_low = 17
        self.age_high = 175
        self.weight_low = 100
        self.weight_high = 140
        self.height_low = 55
        self.height_high = 75
        self.speed = 30
        self.size = "medium"

        utilities.ability_score_increase(self, True, "two")
        self.set_awh(self)
        self.proficiencies.append("darkvision")
        self.advantages = ["Being Charmed", "Sleep by Magic"]
        utilities.transfer_languages(self, ["common", "elvish", input("What language do you want to learn?\n")], True)