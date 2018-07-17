from src.utils.character.BaseChr import BaseChr
from src.utils.character.MagicChr import MagicChr
import random as r


class BaseRace(BaseChr, MagicChr):
    def __init__(self, level):
        BaseChr.__init__(self, level)
        self.level = int(level)
        self.age = 0
        self.weight = 0
        self.height = 0
        self.speed = 30
        self.swim_spd = 0
        self.hp = 0
        self.fly_spd = 0
        self.languages = []
        self.proficiencies = []
        self.resistances = []
        self.features = []
        self.skills = []
        self.subrace = ""
        self.str_mod = 0
        self.wis_mod = 0
        self.dex_mod = 0
        self.int_mod = 0
        self.cha_mod = 0
        self.con_mod = 0
        self.set_swim()

    def set_subrace(self):
        pass

    def set_swim(self):
        if self.swim_spd == 0 or 15:
            self.swim_spd = self.speed / 2

    def set_awh(self, chr):
        self.get_weight(chr)
        self.get_age(chr)
        self.get_height(chr)

    def get_age(self, chr):
        self.age = int(r.randrange(chr.age_low, chr.age_high))

    def get_weight(self, chr):
        self.weight = int(r.randrange(chr.weight_low, chr.weight_high))

    def get_height(self, chr):
        self.height = int(r.randrange(chr.height_low, chr.height_high))
