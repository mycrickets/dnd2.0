import src.utils.character.BaseChr as base_chr
import src.utils.character.MagicChr as magic_chr
import src.utils.utils as utilities


class BaseClass(base_chr.BaseChr, magic_chr.magic_chr):
    all_skills = []
    hp = 0
    hit_dice = ""
    prof_bonus = 0
    archetype = ""
    saving_throws = []
    skills = []
    features = []
    proficiencies = []
    resistances = []
    attack = []
    armor = []
    equip = []

    def __init__(self, level):
        base_chr.BaseChr.__init__(self, level)

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

    def set_equip(self, opts):
        """
        sets character equipment based on list of list of options given
        [[wpn1, wpn2], [armor1, armor2], etc]
        :param opts: list of list, shown above. possibly refactored in the future
        """
        # TODO

    def set_prof(self, opts):
        """
        sets character proficiencies (not skill proficiencies) based on list of options given
        :param opts: list of list of profs available to the character
        """
        flag = True
        while flag:
            avail = set(opts) - set(self.proficiencies)
            print("Which do you want to be proficient in? Options are listed below")
            for item in avail:
                print(item)
            choice = input("")
            assert choice in avail, "That wasn't an option"
            self.proficiencies.append(choice)
            flag = False
