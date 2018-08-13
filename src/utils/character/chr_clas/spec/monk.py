from src.utils.character.chr_clas.BaseClass import BaseClass
from src.utils.character.MagicChr import MagicChr
import src.utils.utils as utilities


class Monk(BaseClass, MagicChr):
    def __init__(self, char):
        BaseClass.__init__(self, char.level)
        self.level = int(char.level)
        self.str_mod = char.race.str_mod
        self.dex_mod = char.race.dex_mod
        self.wis_mod = char.race.wis_mod
        self.int_mod = char.race.int_mod
        self.cha_mod = char.race.cha_mod
        self.con_mod = char.race.con_mod
        all_skills = list({"acrobatics", "athletics", "history", "insight", "religion", "stealth"} - set(char.race.skills))
        archetype_opts = ["drunken master", "four elements", "kensei", "long death", "open hand", "shadow", "sun soul", "tranquility"] # base hotel and casino
        level_features = [[0, ["Unarmored Defense", "Martial Arts"]], [1, ["Ki", "Unarmored Movement"]], [2, "Deflect Missiles"],
                          [3, "Slow Fall"],  [4, "Extra Attack"],
                          [5, "Ki-Empowered Strikes"], [6, ["Evasion", "Stillness of Mind"]],
                          [12, "Tongue of the Sun and Moon"], [13, "Diamond Soul"],
                          [14, "Timeless Body"]]
        ki_features = [[1, ["Flurry of Blows", "Patient Defense", "Step of the Wild"]],
                       [4, "Stunning Strike"], [13, "Diamond Soul"], [17, "Empty Body"], [19, "Perfect Self"]]

        for item in ["disease", "poison"]:
            if self.level > 9:
                self.resistances.append(item)
        if self.level > 12:
            self.languages.append("All Languages (Monk Feature)")
        if self.level > 13:
            self.saving_throws = ["strength", "wisdom", "dexterity", "intelligence", "charisma", "constitution"]
        else:
            self.saving_throws = ["strength", "dexterity"]
        self.ki_features = []
        self.ki_dc = 0
        self.elem_feat = []
        wpn_opts = [["shortsword", "any simple weapon (please input)"]]
        eqp_opts = [["dungeoneer's pack", "explorer's pack"]]
        prof = utilities.get_from_list(["artisans tools", "musical instrument"], 1, "proficiency")
        if prof == "musical instrument":
            prof = input("Which instrument do you want to be proficient in?\n")
        utilities.append_proficiencies(self, ["simple weapons", "shortswords", prof])
        self.set_equip(wpn_opts, True)
        self.set_equip(eqp_opts, False)
        utilities.equip(self, "10 darts")
        utilities.set_skills(self, 2, all_skills)
        self.init_hit_dice(8)
        self.init_hp(10, "constitution", 8)
        self.level_features(level_features)
        for item in ki_features:
            lvl = item[0]
            ch = item[1]
            if self.level > int(lvl):
                if isinstance(ch, list):
                    for feat in ch:
                        self.ki_features.append(feat)
                else:
                    self.ki_features.append(ch)
        self.level_scores([3, 7, 11, 15, 18])
        if self.level > 1:
            self.ki_dc = 8 + self.prof_bonus + self.wis_mod
        arch_choice = self.init_archetype(archetype_opts)
        self.set_arch(arch_choice)

    def set_arch(self, arch_choice):
        print(arch_choice)
        arch = {}
        if arch_choice == "drunken master":
            self.skills.append("Performance")
            self.proficiencies.append("Brewer's Supplies")
            arch['feature'] = [[0, "Drunken Technique"], [5, ["Leap to Your Feet", "Redirect Attack"]], [16, "Intoxicated Frenzy"]]
            if self.level > 10:
                self.ki_features.append("Drunkard's Luck")
        elif arch_choice == "four elements":
            self.elem_feat.append("Elemental Attunement")
            self.set_elem()
            for level in [5, 10, 16]:
                if self.level > level:
                    self.set_elem()
        elif arch_choice == "kensei":
            arch['feature'] = [[0, "Path of the Kensei"], [5, "One with the Blade"], [10, "Sharpen the Blade"],
                               [16, "Unerring Accuracy"]]
        elif arch_choice == "long death":
            arch['feature'] = [[0, "Touch of Death"], [5, "Hour of Reaping"], [10, "Mastery of Death"],
                               [16, "Touch of the Long Death"]]
        elif arch_choice == "open hand":
            arch['feature'] = [[0, "Open Hand Technique"], [5, "Wholeness of Body"], [10, "Tranquility"], [16, "Quivering Palm"]]
        elif arch_choice == "shadow":
            MagicChr.__init__(self)
            cant_ct = 1
            self.set_magic(self.level, cant_ct, "monk")
            self.ki_features.append("Shadow Arts")
            arch['feature'] = [[5, "Shadow Step"], [10, "Cloak of Shadows"], [16, "Opportunist"]]
        elif arch_choice == "sun soul":
            arch['feature'] = [[0, "Radiant Sun Bolt"], [5, "Searing Arc Strike"], [10, "Searing Sunburst"], [16, "Sun Shield"]]
            arch['attack'] = [[0, "Radiant Sun Bolt"], [10, "Searing Sunburst"]]
            if self.level > 5:
                self.ki_features.append("Searing Arc Strike")
        else:
            arch_choice = "tranquility"
            arch['feature'] = [[0, ["Path of Tranquility", "Healing Hands"]], [5, "Emissary of Peace"], [10, "Douse the Flames of Anger"], [16, "Anger of a Gentle Soul"]]
            if self.level > 5:
                utilities.set_skills(self, 1, ["performance", "persuasion"])
        self.level_arch(arch)

    def set_elem(self):
        base_elem = ["Fangs of the Fire Snake", "Fist of Four Thunders", "Fist of Unbroken Air", "Rush of the Gale Spirits",
                     "Shape the Flowing River", "Sweeping Cinder Strike", "Water Whip"]
        if self.level > 5:
            base_elem.extend(["Clench of the North Wind", "Gong of the Summit"])
        if self.level > 10:
            base_elem.extend(["Flames of the Phoenix", "Mist Stance", "Ride the Wind"])
        if self.level > 16:
            base_elem.extend(["River of Hungry Flame", "Breath of Winter", "Eternal Mountain Defense"])
        ch = set(base_elem)-set(self.elem_feat)
        elem = list(ch)
        print("Which elemental discipline do you want to learn? They are printed below")
        for item in sorted(elem):
            print(item)
        self.elem_feat.append(input(""))

