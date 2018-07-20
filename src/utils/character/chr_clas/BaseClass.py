from src.utils.character.BaseChr import BaseChr
from src.utils.character.MagicChr import MagicChr
import src.utils.utils as utilities


class BaseClass(BaseChr, MagicChr):
    def __init__(self, level):
        BaseChr.__init__(self, level)
        self.all_skills = []
        self.hit_dice = ""
        self.prof_bonus = 0
        self.archetype = ""
        self.saving_throws = []
        self.skills = []
        self.feats = []
        self.features = []
        self.proficiencies = []
        self.advantages = []
        self.disadvantages = []
        self.languages = []
        self.resistances = []
        self.attack = []
        self.armor = []
        self.equipment = []
        self.weapons = []
        self.str_mod = 0
        self.wis_mod = 0
        self.dex_mod = 0
        self.int_mod = 0
        self.cha_mod = 0
        self.con_mod = 0

    def init_prof_bonus(self):
        self.prof_bonus = 2
        if self.level > 4:
            self.prof_bonus = 3
        if self.level > 8:
            self.prof_bonus = 4
        if self.level > 12:
            self.prof_bonus = 5
        if self.level > 16:
            self.prof_bonus = 6

    def init_hit_dice(self, die):
        """
        initializes hit dice for character
        :param die: string of which die to add. d8, d10, d12 are most common
        """
        self.hit_dice = str(self.level) + "d" + str(die)

    def init_hp(self, base, mod, die):
        """
        initialize hp for character
        :param base: base hp as integer: 8 or 10 is most common
        :param mod: which score is used to calculate increase in hp
        """
        self.hp = int(base) + ((utilities.get_modifier(self, mod, True) + int(die)) * self.level)

    def init_archetype(self, opts):
        """
        sets archetype string for character from options given
        :param opts: list of strings, options of archetypes to choose from
        :return: string of option chosen for the class to invoke the function that relates to that archetype
        """
        flag = True
        while flag:
            print("Which archetype do you want to join? Your choices are listed below")
            for item in opts:
                print(item)
            choice = input("")
            if utilities.is_valid_input(choice, opts):
                self.archetype = choice
                flag = False
            else:
                pass
        return self.archetype

    def level_arch(self, arch, choices):
        """

        :param arch: the total dictionary passed in
        :param choices: the keys of the dictionaries to loop through
        :return:
        """
        for opt in choices:
            for item in arch[opt]:
                if isinstance(item[0], int):
                    lvl = item[0]
                else:
                    lvl = item[0][0]
                if self.level > lvl:
                    flag = True
                    while flag:
                        flag = not self.middleman(opt, item[1])

    def middleman(self, opt, item):
        if isinstance(item, list):
            for ind in item:
                return self.append_item(opt, ind)
        elif isinstance(item, str):
            return self.append_item(opt, item)
        else:
            return None

    def append_item(self, opt, item):
        """

        :param opt: the dict
        :param item:
        :return:
        """

        if opt == "proficiency":
            self.proficiencies.append(item)
        elif opt == "feature":
            self.features.append(item)
        elif opt == "skill":
            if utilities.is_valid_input(item, utilities.valid_skills()):
                self.skills.append(item)
            else:
                return False
        elif opt == "resistance":
            self.resistances.append(item)
        elif opt == "advantage":
            self.advantages.append(item)
        elif opt == "disadvantage":
            self.disadvantages.append(item)
        elif opt == "stat":
            utilities.alter_stat(self, item[0], item[1])
        elif opt == "attack":
            self.attack.append(item)
        elif opt == "language":
            self.languages.append(item)
        elif opt == "spells":
            self.add_spell(self.level, item)
        return True

    def set_equip(self, opts, wpn_armor):
        """
        sets character equipment based on list of list of options given
        [[wpn1, wpn2], [armor1, armor2], etc]
        :param wpn_armor: if the list contains weapons: if so, they need to be in equip + wpns, otherwise only equipment
        :param opts: list of list, shown above. possibly refactored in the future
        """
        for lists in opts:
            print("Which do you want to equip?")
            for item in lists:
                print(item)
            choice = input("")
            if wpn_armor:
                utilities.equip(self, choice)
            else:
                self.equipment.append(choice)

    def level_features(self, opts):
        """
        adds features to character/class input based on option list provided
        FOR FEATURES ONLY. ALL OTHER HAVE TO BE IN IND. CHARACTER CLASSES CLASS
        :param opts: list of options & levels, similar to adding spells function
        format: [[(int level), ["feature1", "feature2"]], [(int level2), ["feature3", "feature4"]]]
        :return: N/A
        """
        for level in opts:
            if self.level > int(level[0]):
                for item in level[1]:
                    self.features.append(item)

    def level_scores(self, levels):
        for item in levels:
            if self.level > int(item):
                utilities.ability_score_increase(self, True)


