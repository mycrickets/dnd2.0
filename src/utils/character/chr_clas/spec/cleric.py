from src.utils.character.chr_clas.BaseClass import BaseClass
from src.utils.character.MagicChr import MagicChr
import src.utils.utils as utilities


class Cleric(BaseClass, MagicChr):
    def __init__(self, char):
        BaseClass.__init__(self, char.level)
        MagicChr.__init__(self)
        cant_ct = 3
        self.level = int(char.level)
        self.set_magic(self.level, cant_ct, "cleric")
        self.str_mod = char.race.str_mod
        self.dex_mod = char.race.dex_mod
        self.wis_mod = char.race.wis_mod
        self.int_mod = char.race.int_mod
        self.cha_mod = char.race.cha_mod
        self.con_mod = char.race.con_mod
        self.divine_ct = 2 if self.level > 5 else 3 if self.level > 17 else 1
        all_skills = list({"history", "insight", "medicine", "persuasion", "religion"} - set(char.race.skills))
        archetype_opts = ["arcana", "ambition", "city", "death", "forge", "grave", "knowledge", "life", "light", "nature", "order", "protection", "solidarity", "strength", "tempest", "trickery", "war", "zeal"]
        level_features = [[0, ["Ritual Casting", "Spellcasting Focus"]], [1, ["Turn Undead"]], [4, ["Destroy Undead"]], [9, ["Divine Intervention"]]]
        wpn_opts = [["Mace", "Warhammer"], ["Light crossbow with 20 bolts", "Any other simple weapon (please input)"]]
        equip_opts = [["Priest's Pack", "Explorer's Pack"], ["Scale Mail", "Leather Armor", "Chain Mail"]]
        self.saving_throws = ["wisdom", "charisma"]
        self.magic_throw = "wisdom"
        self.magic_dc = 8 + self.prof_bonus + self.wis_mod
        utilities.append_proficiencies(self, ["light armor", "medium armor", "shields", "all simple weapons"])
        self.set_equip(wpn_opts, True)
        self.set_equip(equip_opts, False)
        utilities.set_skills(self, 2, all_skills)
        self.init_hit_dice(8)
        self.init_hp(8, "constitution", "8")
        self.equipment.append("Shield")
        self.equipment.append(input("What holy symbol do you want to use?"))
        self.level_features(level_features)
        self.level_scores([3, 7, 11, 15, 18])
        arch_choice = self.init_archetype(archetype_opts)
        self.set_arch(arch_choice, char)
        #gnEricName <- look up

    def set_arch(self, arch_choice, char):
        arch = {}

        if arch_choice == "arcana":
            arch['feature'] = [[5, "Spell Breaker"], [7, "Potent Spellcasting"], [17, "Arcane Abjuration"]]
            arch['skill'] = [[0, "arcana"]]
            arch['spell'] = [[[0, "cantrip"], [input("Arcana Divine Initialization: What two wizard cantrips do you want to learn?")]], [[0, "one"], ["Detect Magic", "Magic Missile"]],
                             [[3, "two"], ["Magic Weapon", "Nystul's Magic Aura"]], [[5, "three"], ["Dispel Magic", "Magic Circle"]], [[9, "five"], ["Planar Binding", "Teleportation Circle"]]]
        elif arch_choice == "ambition":
            arch['feature'] = [[0, ["Warding Flame", "Invoke Duplicity"]], [5, "Cloak of Shadows"], [7, "Potent Spellcasting"], [16, "Improved Duplicity"]]
            arch['spell'] =
        elif arch_choice == "city":
            pass
        elif arch_choice == "death":
            pass
        elif arch_choice == "forge":
            pass
        elif arch_choice == "grave":
            pass
        elif arch_choice == "knowledge":
            pass
        elif arch_choice == "life":
            pass
        elif arch_choice == "light":
            pass
        elif arch_choice == "nature":
            pass
        elif arch_choice == "zeal":
            pass
        elif arch_choice == "order":
            pass
        elif arch_choice == "protection":
            pass
        elif arch_choice == "solidarity":
            pass
        elif arch_choice == "strength":
            pass
        elif arch_choice == "tempest":
            pass
        elif arch_choice == "trickery":
            pass
        elif arch_choice == "war":
            pass
        else:
            arch_choice = "life"
        self.level_arch(arch)

