from utils.character.race.BaseRace import BaseRace
from utils.character.MagicChr import MagicChr
import utils.utils as utilities


class Gnome(BaseRace, MagicChr):
    def __init__(self, level):
        BaseRace.__init__(self, level)
        MagicChr.__init__(self)
        self.level = int(level)
        self.int_mod = 2
        self.age_low = 35
        self.age_high = 400
        self.height_low = 34
        self.height_high = 50
        self.weight_low = 38
        self.weight_high = 45
        self.size = "small"
        self.speed = 25
        self.proficiencies.append("darkvision")
        self.advantages = ["intelligence", "charisma", "wisdom"]
        utilities.transfer_languages(self, ["common", "gnomish"], True)
        self.subrace = ""

        self.set_awh(self)
        self.set_subrace()

    def set_subrace(self):
        self.subrace = input("Which Gnomish subrace do you want to be: forest, rock, or deep?")
        if self.subrace == "forest":
            self.subrace = "Forest Gnome"
            self.dex_mod = 1
            self.add_spell([[0, "cantrip"], ["Minor Illusion"]], self.level)
            self.features.append("Speak with Small Beasts")
        elif self.subrace == "deep":
            self.subrace = "Deep Gnome"
            self.dex_mod = 1
            self.age_low = 25
            self.age_high = 225
            self.height_low = 35
            self.height_high = 43
            self.weight_low = 75
            self.weight_high = 125
            self.set_awh(self)
            self.proficiencies.append("Dexterity")
            utilities.transfer_languages(self, "undercommon", True)
        else:
            self.subrace = "Rock Gnome"
            self.con_mod = 1
            features = ["Artificer's Lore", "Tinker"]
            for item in features:
                self.features.append(item)
            self.proficiencies.append("Artisan's Tools")



