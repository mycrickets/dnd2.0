from utils.character.race.BaseRace import BaseRace
from utils.character.MagicChr import MagicChr
import utils.utils_file as utilities


class Elf(BaseRace, MagicChr):
    def __init__(self, level):
        BaseRace.__init__(self, level)
        MagicChr.__init__(self)
        self.level = int(level)
        self.dex_mod = 2
        self.age_low = 80
        self.age_high = 700
        self.weight_low = 100
        self.weight_high = 180
        self.height_low = 54
        self.height_high = 75
        self.speed = 30
        self.size = "medium"
        self.magic_throw = "charisma"
        self.disadvantages = []
        self.features.append("darkvision")
        self.skills.append("perception")
        for item in ["being charmed", "magical damage"]:
            self.proficiencies.append(item)
        self.features.append("trance")
        self.set_awh(self)
        utilities.transfer_languages(self, ["common", "elvish"], True)
        self.set_subrace()

    def set_subrace(self):
        self.subrace = input("Which Elvish subrace do you want to be: High, Dark, or Wood?")
        self.subrace = self.subrace.lower()
        if self.subrace == "high":
            self.subrace = "High Elf"
            self.int_mod = 1
            utilities.append_proficiencies(self, ["longsword", "shortsword", "shortbow", "longbow"])
            utilities.transfer_languages(self, input("High Elf Initialization: What language do you want to learn?"), True)
            self.cantrips[0] += 1
            self.cantrips[1].append(input("High Elf Initialization: What wizard cantrip do you want to learn?"))
        elif self.subrace == "dark":
            self.subrace = "Dark Elf"
            self.cha_mod = 1
            try:
                self.proficiencies.remove("darkvision")
            except ValueError:
                pass
            utilities.append_proficiencies(self, ["superior darkvision", "rapier", "shortsword", "hand crossbow"])
            self.disadvantages.append("wisdom saving throws")
            self.add_spell([[[0, "cantrip"], ["Dancing Lights"]], [[2, "one"], ["Faerie Fire"]], [[4, "two"], ["Darkness"]]], self.level)
            self.magic_throw = "charisma"
            self.magic_dc = self.cha_mod
        else:
            self.subrace = "Wood Elf"
            self.wis_mod = 1
            utilities.append_proficiencies(self, ["longsword", "shortsword", "shortbow", "longbow"])
            self.speed = 35
            self.set_swim()
            self.features.append("Mask of the Wild")




