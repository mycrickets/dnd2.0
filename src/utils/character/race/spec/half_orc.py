from utils.character.race.BaseRace import BaseRace
import utils.utils_file as utilities


class HalfOrc(BaseRace):
    def __init__(self, level):
        BaseRace.__init__(self, level)
        self.str_mod = 2
        self.con_mod = 1
        self.age_low = 13
        self.age_high = 70
        self.weight_low = 100
        self.weight_high = 300
        self.height_low = 58
        self.height_high = 86
        self.speed = 30
        self.size = "medium"
        self.set_awh(self)
        self.subrace = "No Subrace"

        utilities.append_proficiencies(self, ["darkvision"])
        self.skills.append("intimidation")
        features = ["Relentless Endurance", "Savage Attacks"]
        for item in features:
            self.features.append(item)
        utilities.transfer_languages(["common", "orcish"])

