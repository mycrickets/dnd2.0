from src.utils.character.race.spec.dragonborn import Dragonborn
from src.utils.character.race.spec.dwarf import Dwarf
from src.utils.character.race.spec.elf import Elf
from src.utils.character.race.spec.gnome import Gnome
from src.utils.character.race.spec.half_elf import HalfElf
from src.utils.character.race.spec.half_orc import HalfOrc
from src.utils.character.race.spec.halfling import Halfling
from src.utils.character.race.spec.human import Human
from src.utils.character.race.spec.tiefling import Tiefling

from src.utils.character.chr_clas.spec.barbarian import Barbarian
from src.utils.character.chr_clas.spec.bard import Bard

import src.utils.utils as utilities


class Character:
    def __init__(self, level):
        self.level = int(level)
        self.strength = 0
        self.dexterity = 0
        self.constitution = 0
        self.charisma = 0
        self.intelligence = 0
        self.wisdom = 0
        self.hp = 0
        utilities.init_scores(self)
        self.languages = []
        self.race = None
        self.race_name = ""
        self.clas = None
        self.class_name = ""
        self.alignment = ""
        self.name = ""
        self.player_name = ""
        self.gender = ""
        self.sex = ""
        self.background = ""
        self.personality = ""
        self.trait = ""
        self.ideals = ""
        self.flaws = ""
        self.bonds = ""

    def set_race(self):
        race = input("what race are you?\n")
        race = race.strip()
        if race == "dragonborn":
            race = Dragonborn(self.level)
            self.race_name = "Dragonborn"
        elif race == "dwarf":
            race = Dwarf(self.level)
            self.race_name = "Dwarf"
        elif race == "elf":
            race = Elf(self.level)
            self.race_name = "Elf"
        elif race == "gnome":
            race = Gnome(self.level)
            self.race_name = "Gnome"
        elif race in ["half elf", "half_elf"]:
            race = HalfElf(self.level)
            self.race_name = "Half Elf"
        elif race in ["half orc", "half_orc"]:
            race = HalfOrc(self.level)
            self.race_name = "Half Orc"
        elif race == "halfling":
            race = Halfling(self.level)
            self.race_name = "Halfling"
        elif race == "tiefling":
            race = Tiefling(self.level)
            self.race_name = "Tiefling"
        else:
            race = Human(self.level)
            self.race_name = "Human"
        self.race = race
        self.hp += self.race.hp
        self.strength += self.race.str_mod
        self.dexterity += self.race.dex_mod
        self.wisdom += self.race.wis_mod
        self.intelligence += self.race.int_mod
        self.charisma += self.race.cha_mod
        self.constitution += self.race.con_mod

    def set_class(self):
        char_class = input("What class are you?\n")
        char_class = char_class.strip()
        if char_class == "barbarian":
            char_class = Barbarian(self)
            self.class_name = "Barbarian"
        elif char_class == "bard":
            char_class = Bard(self)
            self.class_name = "Bard"

        self.clas = char_class
        self.hp += self.clas.hp
        self.strength = self.clas.str_mod
        self.dexterity = self.clas.dex_mod
        self.wisdom = self.clas.wis_mod
        self.intelligence = self.clas.int_mod
        self.charisma = self.clas.cha_mod
        self.constitution = self.clas.con_mod

    def set_background(self):
        pass

    def set_personality(self):
        pass

    def trigger_end(self):
        self.fin_features = []
        try:
            for item in self.clas.features:
                self.fin_features.append(item)
            for item in self.race.features:
                self.fin_features.append(item)
        except AttributeError:
            pass
        self.fin_skills = []
        try:
            for item in self.clas.skills:
                self.fin_skills.append(item)
            for item in self.race.skills:
                self.fin_skills.append(item)
        except AttributeError:
            pass
        self.fin_profs = []
        try:
            for item in self.clas.proficiencies:
                self.fin_profs.append(item)
            for item in self.race.proficiencies:
                self.fin_profs.append(item)
        except AttributeError:
            pass
        self.fin_feats = []
        try:
            for item in self.clas.feats:
                self.fin_feats.append(item)
        except AttributeError:
            pass
        self.fin_weapons = []
        try:
            for item in self.race.weapons:
                self.fin_weapons.append(item)
            for item in self.clas.weapons:
                self.fin_weapons.append(item)
        except AttributeError:
            pass
        self.fin_attacks = []
        try:
            for item in self.race.attacks:
                self.fin_attacks.append(item)
            for item in self.clas.attacks:
                self.fin_attacks.append(item)
        except AttributeError:
            pass
        self.fin_equip = []
        try:
            for item in self.race.equip:
                self.fin_equip.append(item)
            for item in self.clas.equip:
                self.fin_equip.append(item)
        except AttributeError:
            pass
        self.fin_magic = []
        self.fin_dc = 0
        self.fin_throw = ""
        try:
            for i in range(0, len(self.race.spells)):
                lvl = [[0], []]
                lvl[0][0]+=int(self.race.spells[i][0])
                for item in self.race.spells[i][1]:
                    lvl[1].append(item)
                lvl[0][0]+=int(self.clas.spells[i][0])
                for item in self.clas.spells[i][1]:
                    lvl[1].append(item)
                self.fin_magic.append(lvl)
            self.fin_dc = self.race.magic_dc + self.clas.prof_bonus
            self.fin_throw = self.race.magic_throw
        except AttributeError:
            try:
                for i in range(0, len(self.clas.spells)):
                    self.fin_magic.append(self.clas.spells[i])
                self.fin_dc = self.clas.magic_dc
                self.fin_throw = self.clas.magic_throw
            except AttributeError:
                pass
        self.fin_resis = []
        try:
            for item in self.race.resistances:
                self.fin_resis.append(item)
            for item in self.clas.resistances:
                self.fin_resis.append(item)
        except AttributeError:
            pass
        self.fin_dis = []
        try:
            for item in self.race.disadvantages:
                self.fin_dis.append(item)
            for item in self.clas.disadvantages:
                self.fin_dis.append(item)
        except AttributeError:
            pass
        self.fin_adv = []
        try:
            for item in self.race.advantages:
                self.fin_adv.append(item)
            for item in self.clas.advantages:
                self.fin_adv.append(item)
        except AttributeError:
            pass
        utilities.transfer_languages(self, None, False, False, True)
