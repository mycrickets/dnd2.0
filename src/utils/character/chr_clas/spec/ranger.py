from utils.character.chr_clas.BaseClass import BaseClass
from utils.character.MagicChr import MagicChr
import utils.utils as utilities


class Ranger(BaseClass, MagicChr):
    def __init__(self, char):
        BaseClass.__init__(self, char.level)
        MagicChr.__init__(self)
        cant_ct = 0
        self.level = int(char.level)
        self.set_magic(self.level, cant_ct, "ranger")
        self.str_mod = char.strength
        self.dex_mod = char.dexterity
        self.wis_mod = char.wisdom
        self.int_mod = char.intelligence
        self.cha_mod = char.charisma
        self.con_mod = char.constitution
        self.level_scores([3, 7, 11, 15, 18])
        all_skills = list({"animal handling", "athletics", "insight", "investigation", "nature", "perception", "stealth", "survival"} - set(char.race.skills))
        archetype_opts = ["Beast Master", "Gloom Stalker", "Horizon Walker", "Hunter", "Monster Slayer", "Primeval Guardian"]
        level_features = [[0, ["Favored Enemy", "Natural Explorer"]], [1, "Spellcasting"], [2, "Primeval Awareness"],
                          [4, "Extra Attack"], [7, "Land's Stride"], [9, "Hide in Plain Sight"],
                          [13, "Vanish"], [17, "Feral Senses"], [19, "Foe Slayer"]]
        wpn_opts = [["Two shortswords", "Two simple martial weapons (please input)"]]
        eqp_opts = [["Dungeoneer's Pack", "Explorer's Pack"]]
        amor = utilities.get_from_list(["Scale Mail", "Leather Armor"], 1, "armor")
        if amor == "Scale Mail":
            self.armor.append(["Scale Mail", "14"])
        else:
            self.armor.append(["Leather Armor", "11"])
        self.saving_throws = ["strength", "dexterity"]
        self.magic_throw = "wisdom"
        self.magic_dc = self.prof_bonus + self.wis_mod + 8
        utilities.set_skills(self, 3, all_skills)
        self.init_hit_dice(10)
        self.init_hp(10, "constitution", 10)
        self.styles = []
        utilities.append_proficiencies(self, ["light armor", "medium armor", "shields", "simple weapons", "martial weapons"])
        self.set_equip(wpn_opts, True)
        self.set_equip(eqp_opts, False)
        utilities.equip(self, "Longbow and Quiver of 20 arrows")
        self.level_features(level_features)
        if self.level > 1:
            self.set_style()
        if self.level > 2:
            arch_choice = self.init_archetype(archetype_opts)
            self.set_arch(arch_choice)

    def set_arch(self, arch_choice):
        arch = {}
        if arch_choice == "Beast Master":
            arch['feature'] = [[0, "Ranger's Companion"], [6, "Exceptional Training"], [10, "Bestial Fury"], [14, "Share Spells"]]
        elif arch_choice == "Gloom Stalker":
            arch['spells'] = [[[0, "one"], ["Disguise Self"]],
                              [[4, "two"], ["Rope Trick"]],
                              [[8, "three"], ["Fear"]],
                              [[12, "four"], ["Greater Invisibility"]],
                              [[16, "five"], ["Seeming"]]]
            arch['feature'] = [[0, ["Dread Ambusher", "Umbral Sight"]],
                               [10, "Stalker's Flurry"],
                               [14, "Shadowy Dodge"]]
            if self.level > 6:
                if "wisdom" in self.saving_throws:
                    self.saving_throws.append(utilities.get_from_list(["charisma", "intelligence"], 1, "saving throw"))
                else:
                    self.saving_throws.append("wisdom")
        elif arch_choice == "Horizon Walker":
            arch['spells'] = [[[0, "one"], ["Protection from Good and Evil"]],
                              [[4, "two"], ["Misty Step"]],
                              [[8, "three"], ["Haste"]],
                              [[12, "four"], ["Banishment"]],
                              [[16, "five"], ["Teleportation Circle"]]]
            arch['feature'] = [[0, ["Detect Portal", "Planar Warrior"]],
                               [6, "Ethereal Step"],
                               [10, "Distant Strike"],
                               [14, "Spectral Defense"]]
        elif arch_choice == "Hunter":
            zero = utilities.get_from_list(["Colossus Slayer", "Giant Killer", "Horde Breaker"], 1, "feature")
            six = None
            ten = None
            fourteen = None
            if self.level > 6:
                six = utilities.get_from_list(["Escape the Horde", "Multiattack Defense", "Steel Will"], 1, "feature")
            if self.level > 10:
                ten = utilities.get_from_list(["Volley", "Whirlwind Attack"], 1, "feature")
            if self.level > 14:
                fourteen = utilities.get_from_list(["Evasion", "Stand Against the Tide", "Uncanny Dodge"], 1, "feature")
            arch['feature'] = [[0, zero],
                               [6, six],
                               [10, ten],
                               [14, fourteen]]
        elif arch_choice == "Monster Slayer":
            arch['spells'] = [[[0, "one"], ["Protection from Good and Evil"]],
                              [[4, "two"], ["Zone of Truth"]],
                              [[8, "three"], ["Magic Circle"]],
                              [[12, "four"], ["Banishment"]],
                              [[16, "five"], ["Hold Monster"]]]
            arch['feature'] = [[0, ["Hunter's Sense", "Slayer's Prey"]],
                               [6, "Supernatural Defense"],
                               [10, "Magic-user's Nemesis"],
                               [14, "Slayer's Counter"]]
        else:
            arch_choice = "Primeval Guardian"
            arch['spells'] = [[[0, "one"], ["Entangle"]],
                              [[4, "two"], ["Enhance Ability"]],
                              [[8, "three"], ["Conjure Animals"]],
                              [[12, "four"], ["Giant Insect"]],
                              [[16, "five"], ["Insect Plague"]]]
            arch['feature'] = [[0, ["Guardian Soul", "Piercing Thorns"]],
                               [6, "Ancient Fortitude"],
                               [10, "Rooted Defense"],
                               [14, "Guardian Aura"]]
        self.level_arch(arch)

    def set_style(self):
        style_opts = list({"archery", "defense", "dueling", "two weapon fighting",
                           "mariner", "close quarters shooter", "tunnel fighter"} - set(self.styles))
        ch = utilities.get_from_list(style_opts, 1, "style")
        self.styles.append(ch.capitalize())
        self.features.append(ch.capitalize())
