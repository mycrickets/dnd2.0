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
        self.str_mod = char.strength
        self.dex_mod = char.dexterity
        self.wis_mod = char.wisdom
        self.int_mod = char.intelligence
        self.cha_mod = char.charisma
        self.con_mod = char.constitution
        self.level_scores([3, 7, 11, 15, 18])
        all_skills = list({"athletics", "insight", "intimidation", "medicine", "persuasion", "religion"} - set(char.race.skills))
        archetype_opts = ["ancients", "conquest", "crown", "devotion", "redemption", "vengeance"]
        if "Evil" in char.alignment:
            archetype_opts.extend(["oathbreaker", "treachery"])
        level_features = [[0, ["Divine Sense", "Lay on Hands"]], [1, ["Fighting Style", "Divine Smite", "Spellcasting", "Spellcasting Focus"]],
                          [2, "Divine Health"], [4, "Extra Attack"], [5, "Aura of Protection"],
                          [9, "Aura of Courage"], [10, "Improved Divine Smite"], [13, "Cleansing Touch"]]
        wpn_opts = [["5 javelins", "any other simple melee weapon (please input)"], ["one martial weapon and a shield", "two martial weapons"]]
        eqp_opts = [["Priest's Pack", "Explorer's Pack"]]
        self.saving_throws = ["wisdom", "charisma"]
        self.magic_throw = "charisma"
        self.magic_dc = 8 + self.prof_bonus + self.cha_mod
        self.styles = []
        utilities.append_proficiencies(self, ["all armor", "shields", "simple weapons", "martial weapons"])
        self.set_equip(wpn_opts, True)
        self.set_equip(eqp_opts, False)
        self.equipment.append(input("What holy symbol do you want to use?\n"))
        self.armor.append(["chain mail", "16"])
        utilities.set_skills(self, 2, all_skills)
        self.init_hit_dice(10)
        self.init_hp(10, "constitution", 10)
        self.level_features(level_features)
        if self.level > 1:
            self.set_style()
            self.attack.append("Divine Smite")
        if self.level > 2:
            self.resistances.append("Immune to Disease")
            arch_choice = self.init_archetype(archetype_opts)
            self.set_arch(arch_choice)
        if self.level > 10:
            self.attack.append("Improved Divine Smite")

    def set_style(self):
        style_opts = list({"defense", "dueling", "great weapon fighting", "protection", "two weapon fighting",
                           "mariner", "close quarters shooter", "tunnel fighter"} - set(self.styles))
        ch = utilities.get_from_list(style_opts, 1, "style")
        self.styles.append(ch.capitalize())
        self.features.append(ch.capitalize())

    def set_arch(self, arch_choice):
        arch = {}
        if arch_choice == "ancients":
            arch['spells'] = [[[2, "one"], ["Ensnaring Strike", "Speak with Animals"]],
                             [[4, "two"], ["Moonbeam", "Misty Step"]],
                             [[8, "three"], ["Plant Growth", "Protection from Energy"]],
                             [[12, "four"], ["Ice Storm", "Stoneskin"]],
                             [[16, "five"], ["Commune with Nature", "Tree Stride"]]]
            arch['feature'] = [[0, ["Tenets of the Ancients", "Nature's Wrath", "Turn the Faithless"]],
                               [6, "Aura of Warding"],
                               [14, "Undying Sentinel"],
                               [19, "Elder Champion"]]
        elif arch_choice == "conquest":
            arch['spells'] = [[[2, "one"], ["Armor of Agathys", "Command"]],
                             [[4, "two"], ["Hold Person", "Spiritual Weapon"]],
                             [[8, "three"], ["Bestow Curse", "Fear"]],
                             [[12, "four"], ["Dominate Beast", "Stoneskin"]],
                             [[16, "five"], ["Cloudkill", "Dominate Person"]]]
            arch['feature'] = [[0, ["Tenets of Conquest", "Conquering Presence", "Guided Strike"]],
                               [6, "Aura of Conquest"],
                               [14, "Scornful Rebuke"],
                               [19, "Invincible Conqueror"]]
        elif arch_choice == "crown":
            arch['spells'] = [[[2, "one"], ["Command", "Compelled Duel"]],
                             [[4, "two"], ["Zone of Truth", "Warding Bond"]],
                             [[8, "three"], ["Spirit Guardians", "Aura of Vitality"]],
                             [[12, "four"], ["Banishment", "Guardian of Faith"]],
                             [[16, "five"], ["Circle of Power", "Geas"]]]
            arch['feature'] = [[0, ["Tenets of the Crown", "Champion Challenge", "Turn the Tide"]],
                               [6, "Divine Allegiance"],
                               [19, "Exalted Champion"]]
            arch['resistance'] = [[14, ["Paralysis", "Being Stunned"]]]
        elif arch_choice == "devotion":
            arch['spells'] = [[[2, "one"], ["Protection from Good and Evil", "Sanctuary"]],
                             [[4, "two"], ["Lesser Restoration", "Zone of Truth"]],
                             [[8, "three"], ["Beacon of Hope", "Dispel Magic"]],
                             [[12, "four"], ["Freedom of Movement", "Guardian of Faith"]],
                             [[16, "five"], ["Commune", "Flame Strike"]]]
            arch['feature'] = [[0, ["Tenets of Devotion", "Sacred Weapon", "Turn the Unholy"]],
                               [6, "Aura of Devotion"],
                               [14, "Purity of Spirit"],
                               [19, "Holy Nimbus"]]
        elif arch_choice == "redemption":
            arch['spells'] = [[[2, "one"], ["Sanctuary", "Sleep"]],
                             [[4, "two"], ["Calm Emotion", "Hold Person"]],
                             [[8, "three"], ["Counterspell", "Hypnotic Pattern"]],
                             [[12, "four"], ["Otiluke's Resilient Sphere", "Stoneskin"]],
                             [[16, "five"], ["Hold Monster", "Wall of Force"]]]
            arch['feature'] = [[0, ["Tenets of Redemption", "Emissary of Peace", "Rebuke the Violent"]],
                               [6, "Aura of the Guardian"],
                               [14, "Protection of Spirit"],
                               [19, "Emissary of Redemption"]]
            arch['resistance'] = [[19, "All Damage (Emissary of Redemption)"]]
        elif arch_choice == "oathbreaker":
            arch['spells'] = [[[2, "one"], ["Hellish Rebuke", "Inflict Wounds"]],
                             [[4, "two"], ["Crown of Madness", "Darkness"]],
                             [[8, "three"], ["Animate Dead", "Bestow Curse"]],
                             [[12, "four"], ["Blight", "Confusion"]],
                             [[16, "five"], ["Contagion", "Dominate Person"]]]
            arch['feature'] = [[0, ["Control Undead", "Dreadful Aspect"]],
                               [6, "Aura of Hate"],
                               [14, "Supernatural Resistance"],
                               [19, "Dread Lord"]]
            arch['resistance'] = [[14, ["Bludgeoning Damage", "Piercing Damage", "Slashing Damage"]]]
        elif arch_choice == "treachery":
            arch['spells'] = [[[2, "one"], ["Charm Person", "Expeditious Retreat"]],
                             [[4, "two"], ["Invisibility", "Mirror Image"]],
                             [[8, "three"], ["Gaseous Form", "Haste"]],
                             [[12, "four"], ["Confusion", "Greater Invisibility"]],
                             [[16, "five"], ["Dominate Person", "Passwall"]]]
            arch['feature'] = [[0, ["Conjure Duplicate", "Poison Strike"]],
                               [6, ["Cull the Herd", "Treacherous Strike"]],
                               [14, "Blackguard's Escape"],
                               [19, "Icon of Deceit"]]
        else:
            arch_choice = "vengeance"
            arch['spells'] = [[[2, "one"], ["Bane", "Hunter's Mark"]],
                             [[4, "two"], ["Hold Person", "Misty Step"]],
                             [[8, "three"], ["Haste", "Protection from Energy"]],
                             [[12, "four"], ["Banishment", "Dimension Door"]],
                             [[16, "five"], ["Hold Monster", "Scrying"]]]
            arch['feature'] = [[0, ["Tenets of Vengeance", "Anjure Enemy", "Vow of Enmity"]],
                               [6, "Relentless Avenger"],
                               [14, "Soul of Vengeance"],
                               [19, "Avenging Angel"]]
        self.level_arch(arch)

