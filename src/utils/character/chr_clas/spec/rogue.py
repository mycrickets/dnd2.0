from utils.character.chr_clas.BaseClass import BaseClass
from utils.character.MagicChr import MagicChr

import utils.utils as utilities
import math


class Rogue(BaseClass, MagicChr):
    def __init__(self, char):
        BaseClass.__init__(self, char.level)
        self.level = int(char.level)
        self.str_mod = char.strength
        self.dex_mod = char.dexterity
        self.wis_mod = char.wisdom
        self.int_mod = char.intelligence
        self.cha_mod = char.charisma
        self.con_mod = char.constitution
        self.level_scores([3, 7, 11, 15, 18])
        all_skills = list({"acrobatics", "athletics", "deception", "insight", "intimidation", "investigation",
                           "perception", "performance", "persuasion", "sleight of hand", "stealth"} - set(char.race.skills))
        archetype_opts = ["Arcane Trickster", "Assassin", "Inquisitive", "Mastermind", "Scout", "Swashbuckler", "Thief"]
        level_features = [[0, ["Thieves' Cant", "Sneak Attack"]], [1, "Cunning Action"], [4, "Uncanny Dodge"],
                          [6, "Evasion"], [10, "Reliable Talent"], [13, "Blindsense"], [17, "Elusive"], [19, "Stroke of Luck"]]
        wpn_opts = [["Shortsword", "Shortbow and quiver of 20 arrows"], ["Shortsword", "Rapier"]]
        eqp_opts = [["Burglar's Pack", "Dungeoneer's Pack", "Explorer's Pack"]]
        self.saving_throws = ["dexterity", "intelligence"]
        if self.level > 15:
            self.saving_throws.append("wisdom")
        utilities.append_proficiencies(self, ["light armor", "simple weapons", "hand crossbow", "longswords", "rapiers", "shortswords", "thieves' tools"])
        self.set_equip(wpn_opts, True)
        self.set_equip(eqp_opts, False)
        utilities.equip(self, "Two daggers")
        self.equipment.append("Thieves' tools")
        self.armor = ["Leather armor", "11"]
        utilities.set_skills(self, 4, all_skills)
        self.init_hit_dice(8)
        self.init_hp(8, "constitution", 8)
        self.sneak_dmg = 0
        self.expert_skills = []
        self.level_features(level_features)
        if self.level > 0:
            self.set_expertise(char, 2)
        if self.level > 2:
            arch_choice = self.init_archetype(archetype_opts)
            self.set_arch(arch_choice)
        if self.level > 5:
            self.set_expertise(char, 2)
        self.set_sneak_attack_dmg()

    def set_sneak_attack_dmg(self):
        self.sneak_dmg = str(math.ceil(self.level / 2)) + " d6"

    def set_expertise(self, char, amt):
        for i in range(0, int(amt)):
            flag = False
            while not flag:
                skills = set(char.race.skills).union(set(self.skills)) - set(self.expert_skills)
                pot_skills = list(skills)
                print("Expertise: Which skill do you want to double your proficiency bonus for?\n"
                      "Your known and valid skills are listed below")
                print("Choice: " + str(i+1) + "/" + str(amt))
                for item in sorted(pot_skills):
                    print(item)
                ch = input("")
                if utilities.is_valid_input(ch, pot_skills):
                    self.expert_skills.append(ch)
                    flag = True

    def set_arch(self, arch_choice):
        arch = {}
        if arch_choice == "arcane trickster":
            MagicChr.__init__(self)
            self.set_magic(self.level, 2, "rogue")
            self.magic_throw = "intelligence"
            self.magic_dc = 8 + self.prof_bonus + self.int_mod
            arch['spells'] = [[[0, "cantrip"], "Mage Hand"]]
            arch['feature'] = [[0, "Mage Hand Legerdemain"], [8, "Magical Ambush"], [12, "Versatile Trickster"], [16, "Spell Thief"]]
        elif arch_choice == "assassin":
            arch['proficiency'] = [[0, ["Disguise Kit", "Poisoner's Kit"]]]
            arch['feature'] = [[0, "Assassinate"], [8, "Infiltration Expertise"], [12, "Imposter"], [16, "Death Strike"]]
        elif arch_choice == "inquisitive":
            arch['feature'] = [[0, ["Ear for Deceit", "Eye for Detail", "Insightful Fighting"]], [8, "Steady Eye"], [12, "Unerring Eye"], [16, "Eye for Weakness"]]
        elif arch_choice == "mastermind":
            arch['proficiency'] = [[0, ["Disguise Kit", "Forgery Kit", input("What gaming set do you want proficiency in ?")]]]
            arch['language'] = [[0, [input("Which new language do you want to learn?"), input("Which second new language do you want to learn?")]]]
            arch['feature'] = [[0, ["Master of Intrigue", "Master of Tactics"]],
                               [8, "Insightful Manipulator"],
                               [12, "Misdirection"],
                               [16, "Soul of Deceit"]]
        elif arch_choice == "scout":
            arch['feature'] = [[0, ["Skirmisher", "Survivalist"]],
                               [12, "Ambush Master"],
                               [16, "Sudden Strike"]]
            arch['skill'] = [[0, ["nature", "survival"]]]
            arch['proficiency'] = [[12, "Initiative rolls"]]
        elif arch_choice == "swashbuckler":
            arch['feature'] = [[0, ["Fancy Footwork", "Rakish Audacity"]],
                               [8, "Panache"],
                               [12, "Elegant Maneuver"],
                               [16, "Master Duelist"]]
        else:
            arch_choice = "thief"
            arch['feature'] = [[0, ["Fast Hands", "Second-story Work"]],
                               [8, "Supreme Sneak"],
                               [12, "Use Magic Device"],
                               [16, "Thief's Reflexes"]]
        self.level_arch(arch)

