from utils.character.race.BaseRace import BaseRace
import utils.utils as utilities


class Human(BaseRace):
    def __init__(self, level):
        BaseRace.__init__(self, level)
        self.level = int(level)
        self.str_mod = 1
        self.con_mod = 1
        self.dex_mod = 1
        self.wis_mod = 1
        self.int_mod = 1
        self.cha_mod = 1
        self.age_low = 16
        self.age_high = 70
        self.weight_low = 80
        self.weight_high = 200
        self.height_low = 54
        self.height_high = 76
        self.size = "medium"
        self.speed = 30
        self.set_swim()
        self.set_awh(self)
        utilities.transfer_languages(self, ["common", input("Which language do you want to learn? ")], True)


