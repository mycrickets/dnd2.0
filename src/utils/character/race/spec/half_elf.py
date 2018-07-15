from src.utils.character.race.BaseRace import BaseRace
from src.utils.character.MagicChr import MagicChr
import src.utils.utils as utilities


class HalfElf(BaseRace, MagicChr):
    def __init__(self, level):
        BaseRace.__init__(self, level)
        MagicChr.__init__(self)
        self.level = int(level)
        self.cha_mod = 2
        self.age_low = 17
        self.age_high = 175
        self.weight_low = 100
        self.weight_high = 140
        self.height_low = 55
        self.height_high = 75
        self.speed = 30
        self.size = "medium"

        utilities.ability_score_increase(self, True)
        self.set_awh(self)
        self.proficiencies.append("darkvision")
        self.advantages = ["Being Charmed", "Sleep by Magic"]
        utilities.transfer_languages(self, ["common", "elvish", input("What language do you want to learn?")], True)
        self.set_subrace()

    def set_subrace(self):
        opts = ["weapon", "cantrip", "fleet", "mask", "drow", "swim", "versatile"]
        print("What extra feature do you want to have? Options are listed below.")
        for item in opts:
            print(item)
        ch = input("")
        if utilities.is_valid_input(ch, opts):
            if ch == "weapon":
                utilities.append_proficiencies(self, ["longsword", "shortsword", "shortbow", "longbow"])
            elif ch == "cantrip":
                self.add_spell([[[0, "cantrip"], [input("What wizard cantrip do you want to learn?")]]], self.level)
                self.magic_throw = "intelligence"
            elif ch == "fleet":
                self.speed = 35
                self.set_swim()
            elif ch == "mask":
                self.features.append("Mask of the Wild")
            elif ch == "drow":
                self.add_spell([[[0, "cantrip"], ["Dancing Lights"]], [[2, "one"], ["Faerie Fire"]], [[4, "two"], ["Darkness"]]],self.level)
                self.magic_throw = "charisma"
            elif ch == "swim":
                self.swim_spd = 30
            elif ch == "versatile":
                for i in range(0, 2):
                    utilities.set_skills(self, input("What skill do you want to be proficient in? "))
        else:
            for i in range(0, 2):
                utilities.set_skills(self, input("What skill do you want to be proficient in? "))


