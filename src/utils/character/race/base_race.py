import src.utils.character.base_chr as base_chr
import src.utils.utils as utilities

import random as r


class base_race:
    def __init__(self):
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

