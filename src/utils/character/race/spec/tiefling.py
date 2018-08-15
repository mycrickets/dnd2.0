from utils.character.race.BaseRace import BaseRace
from utils.character.MagicChr import MagicChr
import utils.utils as utilities


class Tiefling(BaseRace):
    def __init__(self, level):
        BaseRace.__init__(self, level)
        MagicChr.__init__(self)
        self.level = int(level)
        self.int_mod = 1
        ch = input("Do you want to increase charisma or dexterity? ")
        utilities.alter_stat(self, "cha_mod" if ch == "charisma" else "dex_mod", 2, False)
        self.age_low = 16
        self.age_high = 80
        self.weight_low = 80
        self.weight_high = 200
        self.height_low = 54
        self.height_high = 76
        self.size = "medium"
        self.speed = 30
        self.set_awh(self)
        self.set_swim()
        self.features.append("darkvision")
        self.resistances.append("fire damage")
        utilities.transfer_languages(self, ["common", "infernal"], True)

        self.set_subrace()

    def set_subrace(self):
        ch = input("Which Tiefling subrace do you want to be: devil, hellfire, winged, or infernal? ")
        ch = ch.strip()
        cantrip = ""
        one = ""
        two = ""
        if ch == "devil":
            self.subrace = "Devil Tiefling"
            cantrip = "Vicious Mockery"
            one = "Charm Person"
            two = "Enthrall"
        elif ch == "hellfire":
            self.subrace = "Hellfire Tiefling"
            cantrip = "Thaumaturgy"
            one = "Burning Hands"
            two = "Darkness"
        elif ch == "winged":
            self.subrace = "Winged Tiefling"
            self.fly_spd = 30
            self.features.append("You can fly now. That's cool, I guess...")
        else:
            self.subrace = "Infernal Tiefling"
            cantrip = "Thaumaturgy"
            one = "Hellish Rebuke"
            two = "Darkness"
        if one != "":
            spells = [[[0, "cantrip"], [cantrip]], [[2, "one"], [one]], [[4, "two"], [two]]]
            for item in spells:
                self.add_spell(item, self.level)
        self.magic_throw = "charisma"
        self.magic_dc = self.cha_mod


