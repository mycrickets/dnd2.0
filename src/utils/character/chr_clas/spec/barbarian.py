from utils.character.chr_clas.BaseClass import BaseClass
import utils.utils as utilities


class Barbarian(BaseClass):
    def __init__(self, char):
        BaseClass.__init__(self, char.level)
        self.level = int(char.level)
        self.rage_ct = 2
        self.rage_dmg = 2
        self.str_mod = char.strength
        self.dex_mod = char.dexterity
        self.wis_mod = char.wisdom
        self.int_mod = char.intelligence
        self.cha_mod = char.charisma
        self.con_mod = char.constitution
        self.level_scores([3, 7, 11, 15, 18])
        all_skills = list({"animal handling", "athletics", "intimidation", "nature", "perception", "survival"} - set(char.race.skills))
        archetype_opts = ["cannibal", "ancestor", "berserker", "storm", "totem", "zealot"]
        if char.race_name == "dwarf":
            archetype_opts.append("battlerager")
        level_features = [[1, ["Reckless Attack", "Danger Sense"]], [4, ["Extra Attack", "Fast Movement"]], [6, ["Feral Instinct"]], [8, ["Brutal Critical"]],
                          [10, ["Relentless Rage"]], [14, ["Persistant Rage"]], [17, ["Indomitable Might"]], [20, ["Primal Champion"]]]
        utilities.append_features(self, ["Rage", "Unarmored Defense"])
        utilities.append_proficiencies(self, ["light armor", "medium armor", "shields", "simple weapons", "martial weapons"])
        equip_opts = [["greataxe", "any other martial melee weapon (please input)"], ["two handaxes", "any other simple melee weapon (please input)"]]
        self.saving_throws = ["strength", "constitution"]
        if self.level > 1:
            self.advantages.append("Dexterity against effects you can see")
        if self.level > 2:
            arch_choice = self.init_archetype(archetype_opts)
            self.rage_ct = 3
            self.set_arch(arch_choice)
        if self.level > 5:
            self.rage_ct = 4
        if self.level > 6:
            self.advantages.append("Initiative rolls")
        if self.level > 8:
            self.rage_dmg = 3
        if self.level > 11:
            self.rage_ct = 5
        if self.level > 15:
            self.rage_dmg = 4
        if self.level > 16:
            self.rage_ct = 6
        if self.level > 19:
            self.str_mod += 4
            self.con_mod += 4
            self.rage_ct = 7
        utilities.set_skills(self, 2, all_skills)
        self.init_hit_dice(12)
        self.init_hp(12, "charisma", 12)
        self.level_features(level_features)
        self.set_equip(equip_opts, True)
        utilities.equip(self, "Javelin x4")
        self.equipment.append("Explorer's Pack")

    def set_arch(self, arch_choice):
        arch = {}
        if arch_choice == "cannibal":
            arch['feature'] = [[0, "All Consuming Rage"], [5, "Biting Rebuke"], [9, "Heart of Enemies"], [13, "Spirit of the Slain"]]
        elif arch_choice == "ancestor":
            arch['feature'] = [[0, "Ancestral Protectors"], [5, "Spirit Shield"], [9, "Consult the Spirit"], [13, "Vengeful Ancestors"]]
        elif arch_choice == "battlerager":
            arch['feature'] = [[0, "Battlerager Armor"], [5, "Reckless Abandon"], [9, "Battlerager Charge"], [13, "Spiked Retribution"]]
        elif arch_choice == "beserker":
            arch['feature'] = [[0, "Frenzy"], [5, "Mindless Rage"], [9, "Intimidating Presence"], [13, "Retaliation"]]
        elif arch_choice == "storm":
            element = input("Storm archetype: Which element do you want to be? desert, sea, or tundra?")
            if element == "desert":
                arch['resistance'] = [[5, "Fire"]]
            elif element == "sea":
                arch['resistance'] = [[5, "Lightning"]]
            else:
                element = "tundra"
                arch['resistance'] = [[5, "Cold"]]
            arch['feature'] = [[0, "Storm Aura: " + element], [5, "Storm Soul: " + element], [9, "Shielding Storm"], [13, "Raging Storm: "+ element]]
        elif arch_choice == "totem":
            animal = input("Totem archetype: What totem spirit do you want to embody? bear, eagle, wolf, elk, or tiger?\n")
            if animal == "bear":
                arch['advantage'] = [[2, "strength"]]
            elif animal == "tiger":
                if self.level > 2:
                    arch['skills'] = [2, ["Athletics", "Acrobatics", "Stealth", "Survival"]]
            arch['feature'] = [[0, "Totem Spirit: " + animal], [2, "Aspect of the Beast: " + animal], [9, "Spirit Walker"], [13, "Totemic Attunement: " + animal]]
        else:
            arch_choice = "zealot"
            arch['feature'] = [[2, "Divine Fury"], [2, "Warrior of the Gods"], [5, "Fanatical Focus"], [9, "Zealous Presence"], [13, "Rage Beyond Death"]]
        self.level_arch(arch, list(arch.keys()))
