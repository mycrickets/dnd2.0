import src.utils.character.BaseChr as base_chr
import src.utils.character.MagicChr as magic_chr
import src.utils.utils as utilities

import random as r


class BaseRace(base_chr.BaseChr, magic_chr.magic_chr):
    def __init__(self, check, level):
        base_chr.BaseChr.__init__(self, check, level)
        self.level = int(level)
        self.age_low = 0
        self.age_high = 0
        self.weight_low = 0
        self.weight_high = 0
        self.height_low = 0
        self.height_high = 0
        self.size = ""
        self.speed = 0
        self.swim_spd = 0
        self.languages = []

    def get_age(self):
        return r.randrange(self.age_low, self.age_high)

    def get_weight(self):
        return r.randrange(self.weight_low, self.weight_high)

    def get_height(self):
        return r.randrange(self.height_low, self.height_high)
