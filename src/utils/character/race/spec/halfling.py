from src.utils.character.race.BaseRace import BaseRace
import src.utils.utils as utilities


class Halfling(BaseRace):
    def __init__(self, level):
        BaseRace.__init__(self, level)
        self.level = int(level)
        self.dex_mod = 2
        self.age_low = 18
        self.age_high = 225
        self.height_low = 34
        self.height_high = 40
        self.weight_low = 35
        self.weight_high = 45
        self.size = "small"
        self.speed = 25
        self.set_swim()
        self.set_awh(self)
        self.advantages = ["being frightened"]
        utilities.transfer_languages(self, ["common", "halfling"], True)
        features = ["Lucky", "Brave", "Nimble"]
        for item in features:
            self.features.append(item)
        self.set_subrace()

    def set_subrace(self):
        ch = input("Which Halfling subrace do you want to be: stout or lightfoot? ")
        ch = ch.strip()
        if ch == "stout":
            self.subrace = "Stout Halfling"
            self.con_mod = 1
            self.resistances.append("poison damage")
            self.advantages.append("poison damage")
        else:
            self.subrace = "Lightfoot Halfling"
            self.cha_mod = 1
            self.features.append("Naturally Stealthy")

