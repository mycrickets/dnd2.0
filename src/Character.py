from utils.character.race.spec.dragonborn import Dragonborn
from utils.character.race.spec.dwarf import Dwarf
from utils.character.race.spec.elf import Elf
from utils.character.race.spec.gnome import Gnome
from utils.character.race.spec.half_elf import HalfElf
from utils.character.race.spec.half_orc import HalfOrc
from utils.character.race.spec.halfling import Halfling
from utils.character.race.spec.human import Human
from utils.character.race.spec.tiefling import Tiefling

from utils.character.chr_clas.spec.barbarian import Barbarian
from utils.character.chr_clas.spec.bard import Bard
from utils.character.chr_clas.spec.cleric import Cleric
from utils.character.chr_clas.spec.druid import Druid
from utils.character.chr_clas.spec.fighter import Fighter
from utils.character.chr_clas.spec.monk import Monk
from utils.character.chr_clas.spec.paladin import Paladin
from utils.character.chr_clas.spec.ranger import Ranger
from utils.character.chr_clas.spec.rogue import Rogue
from utils.character.chr_clas.spec.sorcerer import Sorcerer
from utils.character.chr_clas.spec.warlock import Warlock
from utils.character.chr_clas.spec.wizard import Wizard

from utils.background_dict import backgrounds

import utils.utils as utilities

import random as r


# noinspection PyAttributeOutsideInit
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
        self.background = None
        self.personality = ""
        self.trait = ""
        self.ideals = ""
        self.flaws = ""
        self.bonds = ""

        '''race/class specific'''
        # Barbarian
        self.rage_ct = None
        self.rage_dmg = None
        # Cleric
        self.divine_ct = None
        # Fighter
        self.maneuvers = None
        self.sup_dice_ct = None
        self.sup_dice = None
        # Monk
        self.ki_features = None
        self.ki_dc = None
        self.elem_feat = None
        # Rogue
        self.sneak_dmg = None
        # Sorcerer
        self.metamagic_features = None
        self.color = None
        self.fly_speed = None
        # Warlock
        self.invocations = None
        self.pact = None
        self.pact_desc = None
        # Wizard
        self.spell_master = None
        self.sig_spells = None
        # Fighter, Paladin, Ranger
        self.styles = None
        # Rogue, Bard
        self.expert_skills = None

    def set_background(self):
        while True:
            bg_names = backgrounds.keys()
            print("Listing all Backgrounds:")
            for item in bg_names:
                print(item)
            print("input 'choose' or 'search' to choose a background or find out more about that background")
            choice = input("")
            ch = choice.strip()
            if ch == "choose":
                flag = False
                while not flag:
                    bg = input("Which background do you want to have? input 'exit' to go back and search. This is case-sensitive\n")
                    if bg.strip().lower() == "exit":
                        flag = True
                    elif utilities.is_valid_input(bg, bg_names):
                        self.background = bg
                        return
                    else:
                        print(bg + " isn't a recognized background.")
            elif utilities.is_valid_input(ch, bg_names):
                self.background = choice.strip()
                return
            elif ch == "search":
                flag = False
                while not flag:
                    bg = input("Which background do you want to learn more about?\n")
                    if utilities.is_valid_input(bg, bg_names):
                        print("\n")
                        for item in backgrounds.get(bg):
                            print(item + ": " + backgrounds.get(bg).get(item))
                        import time
                        print("\n")
                        time.sleep(1)
                        flag = True
                    else:
                        print("That's not valid input. Try again.")
            elif ch == "random":
                self.background = bg_names[r.randrange(0, len(bg_names))]
            else:
                print(ch + " is not recognized as a command. Try again.")

    def set_race(self):
        race = utilities.get_from_list(["Dragonborn", "Dwarf", "Elf", "Gnome", "Half Elf", "Half Orc", "Halfling", "Tiefling", "Human"], 1, "race")
        # race = "Half Orc" - for testing
        race = race.strip().lower()
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
        elif race in ["half orc", "half_orc", "halforc"]:
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
        utilities.transfer_background_to_race(self, race)
        self.race = race
        self.hp += self.race.hp
        self.strength += self.race.str_mod
        self.dexterity += self.race.dex_mod
        self.wisdom += self.race.wis_mod
        self.intelligence += self.race.int_mod
        self.charisma += self.race.cha_mod
        self.constitution += self.race.con_mod
        for i in range(0, len(self.race.skills)):
            self.race.skills[i] = self.race.skills[1].strip()

    def set_class(self):
        char_class = utilities.get_from_list(["Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard"], 1, "class")
        char_class = char_class.strip().lower()
        if char_class == "barbarian":
            char_class = Barbarian(self)
            self.class_name = "Barbarian"
        elif char_class == "bard":
            char_class = Bard(self)
            self.class_name = "Bard"
        elif char_class == "cleric":
            char_class = Cleric(self)
            self.class_name = "Cleric"
            self.divine_ct = char_class.divine_ct
        elif char_class == "druid":
            char_class = Druid(self)
            self.class_name = "Druid"
        elif char_class == "fighter":
            char_class = Fighter(self)
            self.class_name = "Fighter"
            self.maneuvers = char_class.maneuvers
            self.styles = char_class.styles
            self.sup_dice_ct = char_class.sup_dice_ct
            self.sup_dice = char_class.sup_dice
        elif char_class == "monk":
            char_class = Monk(self)
            self.class_name = "Monk"
            self.ki_features = char_class.ki_features
            self.ki_dc = char_class.ki_dc
            self.elem_feat = char_class.elem_feat
        elif char_class == "paladin":
            char_class = Paladin(self)
            self.class_name = "Paladin"
            self.styles = char_class.styles
        elif char_class == "ranger":
            char_class = Ranger(self)
            self.class_name = "Ranger"
            self.styles = char_class.styles
        elif char_class == "rogue":
            char_class = Rogue(self)
            self.class_name = "Rogue"
            self.sneak_dmg = char_class.sneak_dmg
            self.expert_skills = char_class.expert_skills
        elif char_class == "sorcerer":
            char_class = Sorcerer(self)
            self.class_name = "Sorcerer"
            self.metamagic_features = char_class.metamagic_features
            self.color = char_class.color
            self.fly_speed = char_class.fly_speed
        elif char_class == "warlock":
            char_class = Warlock(self)
            self.class_name = "Warlock"
            self.invocations = char_class.invocations
            self.pact = char_class.pact
            self.pact_desc = char_class.pact_desc
        else:
            char_class = Wizard(self)
            self.spell_master = char_class.spell_master
            self.sig_spells = char_class.sig_spells
        self.clas = char_class
        self.hp += self.clas.hp
        self.strength = self.clas.str_mod
        self.dexterity = self.clas.dex_mod
        self.wisdom = self.clas.wis_mod
        self.intelligence = self.clas.int_mod
        self.charisma = self.clas.cha_mod
        self.constitution = self.clas.con_mod

    def set_alignment(self):
        cols = ["lawful", "neutral", "chaotic", "true"]
        rows = ["good", "neutral", "evil"]
        flag = False
        while not flag:
            ch = input("What alignment are you?\n")
            try:
                split = ch.split(" ")
                for i in range(0, 1):
                    if utilities.is_valid_input(split[i].lower(), cols) or utilities.is_valid_input(split[1].lower(), rows):
                        self.alignment = ch
                        if self.alignment.lower() == "neutral neutral":
                            self.alignment = "True Neutral"
                        flag = True
                    else:
                        print(ch + " is not recognized as a valid input. Please try again.")
            except IndexError:
                print(ch + " is not recognized as a valid input. Please try again.")

    def set_personality(self):
        self.name = input("What's your character's name?\n")
        self.player_name = input("What's your name (the player)?\n")
        self.gender = input("What's " + self.name + "'s gender?\n")
        self.personality = input("Tell me a bit about " + self.name + "'s personality\n")
        self.trait = input("What is " + self.name + "'s main trait?\n")
        self.ideals = input("What are " + self.name + "'s ideals?\n")
        self.flaws = input("What are " + self.name + "'s flaws?\n")
        self.bonds = input("What are " + self.name + "'s bonds?\n")

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
        except AttributeError:
            pass
        try:
            for item in self.clas.weapons:
                self.fin_weapons.append(item)
        except AttributeError:
            pass
        self.fin_armor = None
        try:
            self.fin_armor = self.race.armor
        except AttributeError:
            pass
        try:
            self.fin_armor = self.clas.armor
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
            for item in self.race.equipment:
                self.fin_equip.append(item)
        except AttributeError:
            pass
        try:
            for item in self.clas.equipment:
                self.fin_equip.append(item)
        except AttributeError:
            pass
        self.fin_magic = []
        self.fin_dc = 0
        self.fin_throw = ""
        try:
            for i in range(0, len(self.race.spells)):
                lvl = [[0], []]
                lvl[0][0] += int(self.race.spells[i][0])
                for item in self.race.spells[i][1]:
                    lvl[1].append(item)
                lvl[0][0] += int(self.clas.spells[i][0])
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
