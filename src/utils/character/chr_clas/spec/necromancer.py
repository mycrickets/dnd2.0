from utils.character.chr_clas.BaseClass import BaseClass
from utils.character.MagicChr import MagicChr
import utils.utils as utilities

class Necromancer(BaseClass, MagicChr):
    def __init__(self, char):
        BaseClass.__init__(self, char.level)
        MagicChr.__init__(self)
        cant_ct = 3
        self.level = int(char.level)
        self.set_magic(self.level, cant_ct, "necromancer")
        self.str_mod = char.strength
        self.dex_mod = char.dexterity
        self.wis_mod = char.wisdom
        self.int_mod = char.intelligence
        self.cha_mod = char.charisma
        self.con_mod = char.constitution
        self.level_scores([3, 7, 11, 15, 18])
        all_skills = list({"arcana", "deception", "history", "intimidation", "medicine", "perception", "religion"} - set(char.race.skills))
        archetype_opts = ["keeper", "reaper", "undertaker"]

        level_features = [[0, ["Spellcasting", "Life Tap"]], [1, "Necromancer Occult"], [2, ["Soul Harvest"]], [4, ["Spontaneous Unburial"]], [6, ["Animate Major Undead"]], [13, ["Ritualistic Unburial"]], [17, ["Macabre"]], [19, ["Seance", "Grim Harvest"]]]

        wpn_opts = [["Crescent Scythe", "Two Daggers"]]
        equip_opts = [["Leather Armor", "Padded Armor"], ["Dungeoneer's Pack", "Explorer's Pack"]]
        self.saving_throws = ["constitution", "charisma"]
        self.magic_throw = "charisma"
        self.magic_dc = 8 + self.prof_bonus + self.cha_mod
        utilities.append_proficiencies(self, ["light armor", "simple weapons"])
        self.set_equip(wpn_opts, True)
        self.set_equip(equip_opts, False)
        utilities.set_skills(self, 2, all_skills)
        self.init_hit_dice(6)
        self.init_hp(6, "constitution", 6)
        self.equipment.append("Spellcasting Focus")
        self.level_features(level_features)
        if self.level > 1:
            arch_choice = self.init_archetype(archetype_opts)
            self.set_arch(arch_choice)
    
    def set_arch(self, arch_choice):
        arch = {}
        if arch_choice == "keeper":
            arch['feature'] = [[1, "Life on Demand"], [5, "Expanded Intellect"], [9, "Aura of Wellbeing"], [13, "Refusal"]]
            arch['spells'] = [[[5, "cantrip"], ["Spare the Dying"]], [[5, "one"], ["Cure Wounds"]],
                             [[5, "two"], ["Lesser Restoration"]], [[5, "three"], ["Beacon of Hope", "Revivify"]], [[5, "four"], ["Death Ward"]], [[5, "five"], ["Greater Restoration"]], [[5, "seven"], ["Resurrection"]], [[5, "nine"], ["Mass Heal"]]]
        elif arch_choice == "reaper":
            arch['spells'] = [[[1, "one"], ["Inflict Wounds"]], [[1, "three"], ["Revivify", "Speak with Dead"]], [[1, "five"], ["Commune", "Raise Dead"]], [[1, "seven"], ["Resurrection"]], [[1, "nine"], ["True Resurrection"]], [[5, "one"], [input("Death's Knowledge: Which three spells from any class spell list do you want to learn?\n")]]]
            arch['feature'] = [[1, "Death's Knowledge"], [5, "Improved Soul Harvest"], [9, "Necrosis Spellcasting"], [13, "Grim"]]
        else:
            arch_choice = "undertaker"
            arch['resistance'] = [[1, "Necrotic Damage"]]
            arch['feature'] = [[1, "Unholy Resistance"], [5, "Improved Animate Dead"], [9, "Undead Resolve"],
                               [13, "Lord of the Undead"]]
        self.level_arch(arch)