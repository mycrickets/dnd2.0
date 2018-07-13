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

    def init_hit_dice(self, die):
        """
        initializes hit dice for character
        :param die: string of which die to add. d8, d10, d12 are most common
        """
        self.hit_dice = str(self.level) + die

    def init_hp(self, base, mod):
        """
        initialize hp for character
        :param base: base hp as integer: 8 or 10 is most common
        :param mod: which score is used to calculate increase in hp
        """
        self.hp = int(base) + (utilities.get_modifier(self, mod) * self.level)

    def set_skills(self, amt, extra=None):
        """
        sets character skills based on amount of skills able to learn
        :param extra: in case of character learning skills outside of their base skills for class.
        :param amt: int total amount of skills able to learn
        """
        skill_set = self.all_skills
        if extra:
            skill_set = extra
        for i in range(0, int(amt)):
            flag = True
            while flag:
                choices = set(skill_set) - set(self.skills)
                print("Which skill do you want to learn? Your choices are listed below")
                for item in choices:
                    print(item)
                response = input("")
                assert response in choices, "That wasn't an option"
                self.skills.append(input(""))
                flag = False

    def set_archetype(self, opts):
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
            assert choice in opts, "That wasn't an option."
            self.archetype = choice
            flag = False
        return self.archetype

    def set_equip(self, opts, wpn_armor=False):
        """
        sets character equipment based on list of list of options given
        [[wpn1, wpn2], [armor1, armor2], etc]
        :param wpn_armor: if the list contains weapons: if so, they need to be in equip + wpns, otherwise only equipment
        :param opts: list of list, shown above. possibly refactored in the future
        """
        flag = True
        while flag:
            try:
                for lists in opts:
                    print("Which do you want to equip?")
                    for item in lists:
                        print(item)
                    choice = input("")
                    assert choice in lists
                    if wpn_armor:
                        utilities.equip(self, choice)
                    else:
                        self.equipment.append(choice)
                    flag = False
            except AssertionError:
                pass


