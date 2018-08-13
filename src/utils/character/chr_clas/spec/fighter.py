from src.utils.character.chr_clas.BaseClass import BaseClass
from src.utils.character.MagicChr import MagicChr
import src.utils.utils as utilities


class Fighter(BaseClass, MagicChr):
    def __init__(self, char):
        BaseClass.__init__(self, char.level)
        self.level = int(char.level)
        self.str_mod = char.race.str_mod
        self.dex_mod = char.race.dex_mod
        self.wis_mod = char.race.wis_mod
        self.int_mod = char.race.int_mod
        self.cha_mod = char.race.cha_mod
        self.con_mod = char.race.con_mod
        self.level_scores([3, 5, 7, 11, 13, 15, 18])
        all_skills = list({"acrobatics", "animal handling", "athletics", "history", "insight", "intimidation"} - set(char.race.skills))
        archetype_opts = ["arcane", "battle", "brute", "cavalier", "champion", "eldritch", "monster", "purple", "samurai", "scout", "sharpshooter"]
        level_features = [[0, "Second Wind"], [1, "Action Surge"], [4, "Extra Attack"], [8, "Indomitable"]]
        wpn_opts = [["A martial weapon and a shield", "Two martial weapons"], ["A light crossbow and 20 bolts", "Two handaxes"]]
        eqp_opts = [["Dungeoneer's Pack", "Explorer's Pack"]]
        self.saving_throws = ["strength", "constitution"]
        utilities.append_proficiencies(self, ["All armors", "All shields", "All weapons"])
        self.set_equip(wpn_opts, True)
        self.set_equip(eqp_opts, False)
        spnch = utilities.get_from_list(["leather armor and longbow", "chain mail"], 1, "selection")
        if spnch == "leather armor and longbow":
            utilities.equip(self, "Longbow with 20 arrows")
            self.armor.append(["Leather Armor", "11"])
        else:
            self.armor.append(["Chain Mail", "16"])
        utilities.set_skills(self, 2, all_skills)
        self.init_hit_dice("10")
        self.init_hp(10, "constitution", "10")
        self.maneuvers = []
        self.styles = []
        self.sup_dice_ct = None
        self.sup_dice = None
        self.level_features(level_features)
        self.set_style()
        if self.level > 2:
            arch_choice = self.init_archetype(archetype_opts)
            self.set_arch(arch_choice, char)

    def set_style(self):
        style_opts = list({"archery", "defense", "dueling", "great weapon fighting", "protection", "two weapon fighting",
                           "mariner", "close quarters shooter", "tunnel fighter"} - set(self.styles))
        ch = utilities.get_from_list(style_opts, 1, "style")
        self.styles.append(ch.capitalize())
        self.features.append(ch.capitalize())

    def set_maneuver(self, amt):
        base_opt = ["Commander's Strike", "Disarming Attack", "Distracting Strike", "Evasive Footwork", "Feinting Attack", "Goading Attack", "Lunging Attack", "Maneuvering Attack"
                    "Menacing Attack", "Parry", "Riposte", "Sweeping Attack", "Trip Attack"]
        fin_opt = set(base_opt) - set(self.maneuvers)
        for i in range(0, amt):
            print("Which Battle Master Maneuver do you want to take? They're printed below")
            for item in sorted(fin_opt):
                print(item)
            choice = input("")
            flag = True
            while flag:
                if choice in fin_opt:
                    self.maneuvers.append(choice)
                    flag = False
                else:
                    print("That's not in the list. Try again")

    def arcane_shot(self, amt):
        base_opt = ["Banishing Arrow", "Beguiling Arrow", "Bursting Arrow", "Enfeebling Arrow", "Grasping Arrow", "Piercing Arrow", "Seeking Arrow", "Shadow Arrow"]
        fin_opt = set(base_opt) - set(self.arcane_choices)
        for i in range(0, amt):
            print("Which Arcane Shot Feature do you want to take? They're printed below")
            for item in fin_opt:
                print(item)
            choice = input("")
            flag = True
            while flag:
                if choice in fin_opt:
                    self.arcane_choices.append(choice)
                    flag = False
                else:
                    print("That's not in the list. Try again")

    def set_arch(self, arch_choice, char):
        arch = {}
        if arch_choice == "arcane":
            MagicChr.__init__(self)
            self.magic_throw = "intelligence"
            self.magic_dc = 8 + self.prof_bonus + self.int_mod
            cantrip = utilities.get_from_list(["druidcraft", "prestidigitation"], 1, "cantrip")
            self.add_spell([[0, "cantrip"], [cantrip]], 0)
            utilities.set_skills(self, 1, ["arcana", "nature"])
            self.arcane_choices = []
            self.arcane_shot_desc = []
            for trig in [0, 0, 6, 9, 14, 17]:
                if self.level > trig:
                    self.arcane_shot(1)
            arch['feature'] = [[6, ["Magic Arrow", "Curving Shot"]], [14, "Ever-Ready Shot"]]

        elif arch_choice == "battle":
            self.sup_dice_ct = 6 if self.level > 14 else 5 if self.level > 6 else 4
            self.sup_dice = str(self.sup_dice_ct) + "d12" if self.level > 17 else "d10" if self.level > 9 else "d8"
            arch['feature'] = [[0, ["Superiority Dice", "Maneuvers"]], [6, "Know Your Enemy"], [14, "Relentless"]]
            for level in [0, 0, 0, 6, 6, 9, 9, 14, 14]:
                if self.level > level:
                    self.set_maneuver(1)

        elif arch_choice == "brute":
            arch['feature'] = [[0, "Brute Force"], [6, "Brutish Durability"], [14, "Devastating Critical"], [17, "Survivor"]]
            if self.level > 9:
                self.set_style()

        elif arch_choice == "cavalier":
            ch = utilities.get_from_list(["language", "skill"], 1, "option")
            if ch == "language":
                self.languages.append(input("What language do you want to learn?"))
            else:
                utilities.set_skills(self, 1, ["animal handling", "history", "insight", "performance", "persuasion"])
            arch['feature'] = [[0, ["Born to the Saddle", "Unwavering Maneuver"]], [6, "Warding Maneuver"], [9, "Hold the Line"], [14, "Ferocious Charger"], [17, "Vigilant Defender"]]

        elif arch_choice == "champion":
            arch['feature'] = [[0, "Improved Critical"], [6, "Remarkable Athlete"], [14, "Superior Critical"], [17, "Survivor"]]
            if self.level > 9:
                self.set_style()

        elif arch_choice == "eldritch":
            MagicChr.set_magic(self, self.level, 2, "eldritch")
            self.magic_dc = 8 + self.prof_bonus + self.int_mod
            self.magic_throw = "intelligence"
            arch['feature'] = [[0, "Weapon Bond"], [6, "War Magic"], [9, "Eldritch Strike"], [14, "Arcane Charge"], [17, "Improved War Magic"]]

        elif arch_choice == "monster":
            ch = utilities.get_from_list(["proficient in a new skill", "proficient in a new tool"], 1)
            if ch == "proficient in a new tool":
                self.proficiencies.append(input("What toolset do you want to be proficient in?"))
            else:
                utilities.set_skills(self, 2, ["arcana", "history", "insight", "investigation", "nature", "perception"])
            self.sup_dice_ct = 6 if self.level > 14 else 5 if self.level > 6 else 4
            self.sup_dice = str(self.sup_dice_ct) + "d12" if self.level > 17 else "d10" if self.level > 9 else "d8"
            arch['feature'] = [[0, ["Superiority Dice", "Hunter's Mysticism"]], [6, "Monster Slayer"], [14, "Relentless"]]
        elif arch_choice == "purple":
            arch['feature'] = [[0, "Rallying Cry"], [6, "Royal Envoy"], [9, "Inspiring Surge"], [14, "Bulwark"]]
            if self.level > 6:
                if "persuasion" not in self.skills or char.skills:
                    self.skills.append("persuasion")
                else:
                    utilities.set_skills(self, 1, ["animal handling", "insight", "intimidation", "performance"])

        elif arch_choice == "samurai":
            arch['feature'] = [[0, "Fighting Spirit"], [6, "Elegant Courtier"], [9, "Tireless Spirit"], [14, "Rapid Strike"], [17, "Strength Before Death"]]
            arch['skill'] = [[6, utilities.get_from_list(["history", "insight", "performance", "persuasion"], 1, "skill")]]

        elif arch_choice == "scout":
            utilities.set_skills(self, 3, ["acrobatics", "athletics", "investigation", "medicine", "nature", "perception", "stealth", "survival"])
            arch['feature'] = [[0, ["Natural Explorer (Fighter)", "Superiority Dice"]], [14, "Relentless"]]
            self.sup_dice_ct = 6 if self.level > 14 else 5 if self.level > 6 else 4
            self.sup_dice = str(self.sup_dice_ct) + "d12" if self.level > 17 else "d10" if self.level > 9 else "d8"

        else:
            arch_choice = "sharpshooter"
            arch['feature'] = [[0, "Steady Aim"], [6, "Careful Eyes"], [9, "Close-Quarters Shooting"], [14, "Rapid Strike"], [17, "Snap Shot"]]
            arch['skill'] = [[6, utilities.get_from_list(["perception", "investigation", "survival"], 1, "skill")]]
        self.level_arch(arch)
