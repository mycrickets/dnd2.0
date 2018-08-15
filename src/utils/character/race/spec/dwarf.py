from utils.character.race.BaseRace import BaseRace
import utils.utils as utilities


class Dwarf(BaseRace):
    def __init__(self, level):
        BaseRace.__init__(self, level)
        self.level = int(level)
        self.con_mod = 2
        self.age_low = 40
        self.age_high = 300
        self.weight_low = 140
        self.weight_high = 160
        self.height_low = 45
        self.height_high = 65
        self.speed = 25
        self.set_swim()
        self.size = "medium"
        self.set_awh(self)
        self.resistances.append("poison damage")

        proficiencies = ["darkvision", "battleaxe", "handaxe", "throwing hammer", "warhammer"]
        for item in proficiencies:
            self.proficiencies.append(item)
        utilities.set_prof(self, ["smith tools", "brew tools", "mason tools"])
        self.features.append("stonecunning")
        self.set_subrace()

    def set_subrace(self):
        self.subrace = input("Which Dwarven subrace do you want to be? 'hill' or 'mountain'?")
        if self.subrace == "hill":
            self.subrace = "Hill Dwarf"
            self.wis_mod = 1
            for i in range(0, self.level):
                utilities.alter_stat(self, 'hp', self.level)
        if self.subrace == "mountain":
            self.subrace = "Mountain Dwarf"
            self.str_mod = 2
            self.proficiencies.append("light armor")
            self.proficiencies.append("medium armor")
