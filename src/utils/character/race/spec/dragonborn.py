import src.utils.character.BaseChr as BaseChr
import src.utils.character.race.BaseRace as BaseRace
import src.utils.utils as utilities


class Dragonborn(BaseRace.BaseRace):
    def __init__(self, level):
        BaseRace.BaseRace.__init__(self, level)
        self.resistances = []
        self.age_low = 0
        self.age_high = 100
        self.weight_low = 100
        self.weight_high = 200
        self.height_low = 200
        self.height_high = 300
        self.attacks = []
        self.color = ""
        self.weapons = []
        self.size = "medium"
        self.options = {
            "black": ["acid", "dex", "line 5' by 30'"],
            "blue": ["lightning", "dex", "line 5' by 30'"],
            "brass": ["fire", "dex", "line 5' by 30'"],
            "bronze": ["lightning", "dex", "line 5' by 30'"],
            "copper": ["acid", "dex", "line 5' by 30'"],
            "gold": ["fire", "dex", "cone 15'"],
            "green": ["poison", "con", "cone 15'"],
            "red": ["fire", "dex", "cone 15'"],
            "silver": ["cold", "con", "cone 15'"],
            "white": ["cold", "con", "cone 15'"],
        }

        self.get_age(self)
        self.get_height(self)
        self.get_weight(self)
        utilities.add_language(self, ["draconic", "common"], True)
        self.set_color()
        self.set_weapon()
        self.set_resistance()
        self.set_mod(2, 0, 0, 0, 1, 0)

    def set_color(self):
        flag = False
        color = ""
        while not flag:
            opts = ["black", "blue", "brass", "bronze", "copper", "gold", "green", "red", "silver", "white"]
            print("Which color dragonborn do you want to be?")
            for item in opts:
                print(item)
            color = input("")
            color = color.strip()
            assert color in opts
            flag = True
        self.color = color

    def set_weapon(self):
        dmg = "2d6"
        if self.level > 10:
            dmg = "4d6"
        if self.level > 15:
            dmg = "5d6"
        self.weapons.append([self.options[self.color], dmg])

    def set_resistance(self):
        self.resistances.append(self.options[self.color][0])
