from src.utils.character.chr_clas.BaseClass import BaseClass
from src.utils.character.MagicChr import MagicChr
import src.utils.utils as utilities


class Paladin(BaseClass, MagicChr):
    def __init__(self, char):
        BaseClass.__init__(self, char.level)
        MagicChr.__init__(self)
        cant_ct = 0
        self.level = int(char.level)
        self.set_magic(self.level, cant_ct, "paladin")
        self.str_mod = char.race.str_mod
        self.dex_mod = char.race.dex_mod
        self.wis_mod = char.race.wis_mod
        self.int_mod = char.race.int_mod
        self.cha_mod = char.race.cha_mod
        self.con_mod = char.race.con_mod
        all_skills = list({"athletics", "insight", "intimidation", "medicine", "persuasion", "religion"} - set(char.race.skills))
        archetype_opts = ["ancients", "conquest", "crown", "devotion", "redemption", "vengeance"]
        if char.alignment.includes("evil" or "Evil"):
            print("wew")
            archetype_opts.extend(["oathbreaker", "treachery"])
        level_features = [[0, ["Divine Sense", "Lay on Hands"]], []]

