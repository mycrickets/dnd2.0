import src.utils.character.BaseChr as base_chr
import src.utils.character.MagicChr as magic_chr
import src.utils.utils as utilities

import random as r


class BaseRace(base_chr.BaseChr, magic_chr.magic_chr):
    def __init__(self, level):
        base_chr.BaseChr.__init__(self, level)
        self.level = int(level)
        self.age = 0
        self.weight = 0
        self.height = 0
        self.speed = 0
        self.swim_spd = 0
        self.fly_spd = 0
        self.languages = []
        self.subrace = ""
        self.str_mod = 0
        self.wis_mod = 0
        self.dex_mod = 0
        self.int_mod = 0
        self.cha_mod = 0
        self.con_mod = 0

    def get_age(self, chr):
        self.age = int(r.randrange(chr.age_low, chr.age_high))

    def get_weight(self, chr):
        self.weight = int(r.randrange(chr.weight_low, chr.weight_high))

    def get_height(self, chr):
        self.height = int(r.randrange(chr.height_low, chr.height_high))

    def set_mod(self, str=0, dex=0, itl=0, wis=0, cha=0, con=0):
        self.str_mod = int(str)
        self.dex_mod = int(dex)
        self.wis_mod = int(wis)
        self.int_mod = int(itl)
        self.cha_mod = int(cha)
        self.con_mod = int(con)

