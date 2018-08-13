from src.utils.character.chr_clas.BaseClass import BaseClass
from src.utils.character.MagicChr import MagicChr
import src.utils.utils as utilities


class Wizard(BaseClass, MagicChr):
    def __init__(self, char):
        BaseClass.__init__(self, char.level)
        MagicChr.__init__(self)
        cant_ct = 3
        self.level = int(char.level)
        self.set_magic(self.level, cant_ct, "wizard")
        self.str_mod = char.strength
        self.dex_mod = char.dexterity
        self.wis_mod = char.wisdom
        self.int_mod = char.intelligence
        self.cha_mod = char.charisma
        self.con_mod = char.constitution
        self.level_scores([3, 7, 11, 15, 18])
        all_skills = list({"arcana", "history", "insight", "investigation", "medicine", "religion"} - set(char.race.skills))
        archetype_opts = ["Artificer", "Bladeslinging", "Lore Mastery", "School of Abjuration", "School of Conjuration",
                          "School of Divination", "School of Enchantment", "School of Evocation", "School of Illusion",
                          "School of Invention", "School of Necromancy", "School of Transmutation", "Technomancy",
                          "Theurgy", "War Magic"]
        level_features = [[0, ["Ritual Casting", "Spellcasting Focus", "Arcane Recovery"]],
                          [17, "Spell Mastery"], [19, "Signature Spells"]]
        wpn_opts = [["Quarterstaff", "Dagger"]]
        eqp_opts = [["Explorer's Pack", "Scholar's Pack"], ["Component Pouch", "Arcane Focus"]]
        self.saving_throws = ["intelligence", "wisdom"]
        self.magic_throw = "intelligence"
        self.magic_dc = 8 + self.prof_bonus + self.int_mod
        utilities.append_proficiencies(self, ["daggers", "darts", "slings", "quarterstaffs", "light crossbows"])
        self.set_equip(wpn_opts, True)
        self.set_equip(eqp_opts, False)
        self.equipment.append("Spellbook")
        self.spell_master = []
        self.sig_spells = []
        utilities.set_skills(self, 2, all_skills)
        self.init_hit_dice(6)
        self.init_hp(6, "constitution", 6)
        self.level_features(level_features)
        if self.level > 1:
            arch_choice = self.init_archetype(archetype_opts)
            self.set_arch(arch_choice)
        if self.level > 17:
            one = utilities.get_from_list(self.one[1], 1, "mastered spell")
            self.spell_master.append(one)
            two = utilities.get_from_list(self.two[1], 1, "mastered spell")
            self.spell_master.append(two)
        if self.level > 19:
            three = utilities.get_from_list(self.three[1], 2, "signature spell")
            self.sig_spells.extend(three)
    
    def set_arch(self, arch_choice):
        arch = {}
        if arch_choice == "Artificer":
            arch['feature'] = [[0, ["Infuse Potions", "Infuse Scrolls"]],
                               [5, "Infuse Weapons and Armor"],
                               [9, "Superior Artificer"],
                               [13, "Master Artificer"]]
        elif arch_choice == "Bladeslinging":
            arch['feature'] = [[0, "Bladesong"],
                               [5, "Extra Attack"],
                               [9, "Song of Defense"],
                               [13, "Song of Victory"]]
            arch['proficiency'] = [[0, ["light armor", input("Which one handed melee weapon do you want to be proficient in?")]]]
            arch['skill'] = [[0, "performance"]]
        elif arch_choice == "Lore Mastery":
            arch['feature'] = [[0, ["Lore Master", "Spell Secrets"]],
                               [5, "Alchemical Casting"],
                               [9, "Prodigious Memory"],
                               [13, "Master of Magic"]]
        elif arch_choice == "School of Abjuration":
            arch['feature'] = [[0, ["Abjuration Savant", "Arcane Ward"]],
                               [5, "Projected Ward"],
                               [9, "Improved Abjuration"],
                               [13, "Spell Resistance"]]
            arch['resistance'] = [[0, "Spell Damage"]]
        elif arch_choice == "School of Conjuration":
            arch['feature'] = [[0, ["Conjuration Savant", "Minor Conjuration"]],
                               [5, "Benign Transposition"],
                               [9, "Focused Conjuration"],
                               [13, "Durable Summons"]]
        elif arch_choice == "School of Divination":
            arch['feature'] = [[0, ["Divination Savant", "Portent"]],
                               [5, "Expert Divination"],
                               [9, "The Third Eye"],
                               [13, "Greater Portent"]]
        elif arch_choice == "School of Enchantment":
            arch['feature'] = [[0, ["Enchantment Savant", "Hypnotic Gaze"]],
                               [5, "Instinctive Charm"],
                               [9, "Split Enchantment"],
                               [13, "Alter Memories"]]
        elif arch_choice == "School of Evocation":
            arch['feature'] = [[0, ["Evocation Savant", "Sculpt Spells"]],
                               [5, "Potent Cantrip"],
                               [9, "Empowered Evocation"],
                               [13, "Overchannel"]]
        elif arch_choice == "School of Illusion":
            arch['feature'] = [[0, ["Illusion Savant", "Improved Minor Illusion"]],
                               [5, "Malleable Illusions"],
                               [9, "Illusory Self"],
                               [13, "Illusory Reality"]]
            arch['spells'] = [[[0, "cantrip"], ["Minor Illusion"]]]
        elif arch_choice == "School of Invention":
            arch['feature'] = [[0, ["Arcanomechanical Armor", "Reckless Casting"]],
                               [5, "Alchemical Casting"],
                               [9, "Prodigious Inspiration"],
                               [13, "Controlled Chaos"]]
            arch['proficiency'] = [[0, ["light armor", input("What two tools do you want to be proficient in? Please input.\n")]]]
            self.equipment.append("Suit of Arcanomechanical Armor")
            self.armor = ["Arcanomechanical Armor", str(12 + self.dex_mod)]
        elif arch_choice == "School of Necromancy":
            arch['feature'] = [[0, ["Necromancy Savant", "Grim Harvest"]],
                               [5, "Undead Thralls"],
                               [9, "Inured to Undeath"],
                               [13, "Command Undead"]]
            arch['spells'] = [[[5, "three"], ["Animate Dead"]]]
            arch['resistance'] = [[9, "Necrotic Damage"]]
        elif arch_choice == "School of Transmutation":
            arch['feature'] = [[0, ["Transmutation Savant", "Minor Alchemy"]],
                               [5, "Transmuter's Stone"],
                               [9, "Shapechanger"],
                               [13, "Master Transmuter"]]
            arch['spells'] = [[[9, "four"], ["Polymorph"]]]
        elif arch_choice == "Technomancy":
            arch['feature'] = [[0, "Technological Savant"],
                               [5, "Program Spell"],
                               [9, "Online Casting"],
                               [13, "Chained Device"]]
            arch['proficiency'] = [[0, ["sidearms", "hacking tools"]]]
        elif arch_choice == "Theurgy":
            arch['feature'] = [[0, ["Divine Inspiration", "Arcane Initiate", "Channel Arcana"]],
                               [5, "Arcane Acolyte"],
                               [9, "Arcane Priest"],
                               [13, "Arcane High Priest"]]
        else:
            arch_choice = "War Magic"
            arch['feature'] = [[0, ["Arcane Deflection", "Tactical Wit"]],
                               [5, "Power Surge"],
                               [9, "Durable Magic"],
                               [13, "Deflecting Shroud"]]
        self.level_arch(arch)



