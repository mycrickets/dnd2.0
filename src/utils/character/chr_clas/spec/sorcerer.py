from src.utils.character.chr_clas.BaseClass import BaseClass
from src.utils.character.MagicChr import MagicChr
import src.utils.utils as utilities


class Sorcerer(BaseClass, MagicChr):
    def __init__(self, char):
        BaseClass.__init__(self, char.level)
        MagicChr.__init__(self)
        cant_ct = 4
        self.level = int(char.level)
        self.set_magic(self.level, cant_ct, "sorcerer")
        self.str_mod = char.strength
        self.dex_mod = char.dexterity
        self.wis_mod = char.wisdom
        self.int_mod = char.intelligence
        self.cha_mod = char.charisma
        self.con_mod = char.constitution
        self.level_scores([3, 7, 11, 15, 18])
        all_skills = list({"arcana", "deception", "insight", "persuasion", "religion"} - set(char.race.skills))
        archetype_opts = ["Divine Soul", "Draconic Bloodline", "Giant Soul", "Phoenix Sorcery", "Sea Sorcery", "Shadow Magic", "Stone Sorcery", "Storm Sorcery", "Wild Magic", "Pyromancer"]
        level_features = [[0, "Spellcasting Focus"], [1, ["Sorcery Points", "Flexible Casting"]], [2, "Metamagic"], [19, "Sorcerous Restoration"]]
        wpn_opts = [["A Light crossbow with 20 bolts", "Any simple weapon (please input)"]]
        eqp_opts = [["Dungeoneer's pack", "Explorer's Pack"], ["Component Pouch", "Arcane Focus"]]
        self.saving_throws = ["constitution", "charisma"]
        self.magic_throw = "charisma"
        self.magic_dc = 8 + self.prof_bonus + self.cha_mod
        utilities.append_proficiencies(self, ["daggers", "darts", "slings", "quarterstaffs", "light crossbows"])
        self.set_equip(wpn_opts, True)
        self.set_equip(eqp_opts, False)
        utilities.set_skills(self, 2, all_skills)
        self.init_hit_dice(6)
        self.init_hp(6, "constitution", 6)
        utilities.equip(self, "two daggers")
        self.level_features(level_features)
        self.metamagic_features = []
        self.color = ""
        self.fly_speed = 0
        for level in [2, 2, 9, 16]:
            if self.level > level:
                self.set_metamagic()
        if self.level > 2:
            self.sorcery_pts = self.level
            arch_choice = self.init_archetype(archetype_opts)
            self.set_arch(arch_choice, char)

    def set_metamagic(self):
        flag = False
        opts = {"Careful Spell", "Distant Spell", "Empowered Spell", "Extended Spell",
                "Heightened Spell", "Quickened Spell", "Subtle Spell", "Twinned Spell"} - set(self.metamagic_features)
        print("Metamagic: Which feature do you want? Your options are printed below")
        for item in opts:
            print(item)
        while not flag:
            ch = input("")
            if utilities.is_valid_input(ch, opts):
                self.metamagic_features.append(ch)
                flag = True
            else:
                print(ch + " is an invalid input. Try again.")

    def set_arch(self, arch_choice, char):
        arch = {}
        if arch_choice == "divine soul":
            arch['feature'] = [[0, ["Divine Magic", "Favored by the Gods"]],
                               [5, "Empowered Healing"],
                               [13, "Otherworldly Wings"],
                               [17, "Unearthly Recovery"]]
            alignment = char.alignment
            arch['spells'] = [[[0, "one"], []]]
            spell = arch['spells'][0][1]
            if "Good" in alignment:
                spell.append("Cure Wounds")
            elif "Evil" in alignment:
                spell.append("Inflict Wounds")
            if "Lawful" in alignment:
                spell.append("Bless")
            elif "Chaotic" in alignment:
                spell.append("Bane")
            if "Neutral" in alignment:
                spell.append("Protection from Good and Evil")
        elif arch_choice == "draconic bloodline":
            self.color = utilities.get_from_list(["black", "blue", "brass", "bronze", "copper", "gold", "green", "red", "silver", "white"], 1, "ancestral color")
            arch['language'] = [[0, "Draconic"]]
            arch['feature'] = [[0, ["Dragon Ancestor", "Draconic Resilience"]], [5, "Elemental Affinity"],
                               [13, "Dragon Wings"],
                               [17, "Draconic Presence"]]
            self.hp += self.level
        elif arch_choice == "giant soul":
            self.hp += self.level
            ch = utilities.get_from_list(["cloud", "fire", "frost", "hill", "stone", "storm"], 1, "giant type")
            if ch == "cloud":
                arch['spells'] = [[[0, "one"], ["Fog Cloud", "Minor Illusion"]], [[2, "two"], ["Invisibility"]]]
            elif ch == "fire":
                arch['spells'] = [[[0, "one"], ["Burning Hands", "Fire bolt"]], [[2, "two"], ["Flaming Sphere"]]]
            elif ch == "frost":
                arch['spells'] = [[[0, "one"], ["Armor of Agathys", "Ray of Frost"]], [[2, "two"], ["Hold Person"]]]
            elif ch == "hill":
                arch['spells'] = [[[0, "one"], ["Heroism", "Shillelagh"]], [[2, "two"], ["Enlarge/Reduce"]]]
            elif ch == "stone":
                arch['spells'] = [[[0, "one"], ["Entangle", "Resistance"]], [[2, "two"], ["Spike Growth"]]]
            else:
                ch = "storm"
                arch['spells'] = [[[0, "one"], ["Shocking Grasp", "Thunderwave"]], [[2, "two"], ["Gust of Wind"]]]
            arch['feature'] = [[5, "Soul of Lost Ostoria (" + ch + ")"], [13, "Rage of Fallen Ostoria"], [17, "Blessing of the All Father"]]
            arch['stat'] = [[17, ["constitution", 2]]]
        elif arch_choice == "phoenix sorcery":
            arch['feature'] = [[0, ["Ignite", "Mantle of Flames"]],
                               [5, "Phoenix Spark"],
                               [13, "Nourishing Fire"],
                               [17, "Form of the Phoenix"]]
        elif arch_choice == "sea sorcery":
            arch['feature'] = [[0, ["Soul of the Sea", "Curse of the Sea"]],
                               [5, "Watery Defense"],
                               [13, "Shifting Form"],
                               [17, "Water Soul"]]
            arch['resistance'] = [[5, "Fire damage"], [17, ["Bludgeoning Damage", "Piercing Damage", "Slashing Damage"]]]
        elif arch_choice == "shadow magic":
            arch['feature'] = [[0, ["Darkvision", "Eyes of the Dark", "Strength of the Grave"]],
                               [5, "Hound of Ill Omen"],
                               [13, "Shadow Walk"],
                               [17, "Umbral Form"]]
            arch['spells'] = [[[2, "two"], ["Darkness"]]]
        elif arch_choice == "stone sorcery":
            arch['feature'] = [[0, "Stone's Durability"],
                               [5, "Stone Aegis"],
                               [13, "Stone's Edge"],
                               [17, "Earth Master's Aegis"]]
            arch['proficiency'] = [[0, ["shields", "simple weapons", "martial weapons"]]]
            self.hp += self.level
        elif arch_choice == "storm sorcery":
            arch['feature'] = [[0, ["Primordial", "Tempestuous Magic"]],
                               [5, ["Heart of the Storm", "Storm Guide"]],
                               [13, "Storm's Fury"],
                               [17, "Wind Soul"]]
            arch['resistance'] = [[5, ["Thunder Damage", "Lightning Damage"]], [17, ["Thunder Damage Immunity", "Lightning Damage Immunity"]]]
            if self.level > 17:
                self.fly_speed = 60
        elif arch_choice == "wild magic":
            arch['feature'] = [[0, ["Wild Magic Surge", "Tides of Chaos"]],
                               [5, "Bend Luck"],
                               [13, "Controlled Chaos"],
                               [17, "Spell Bombardment"]]
        else:
            arch_choice = "Pyromancer"
            arch['feature'] = [[0, "Heart of Fire"],
                               [5, "Fire in the Veins"],
                               [13, "Pyromancer's Fury"],
                               [17, "Fiery Soul"]]
            arch['resistance'] = [[5, "Fire Damage"], [17, "Fire Damage Immunity"]]
        self.level_arch(arch)
