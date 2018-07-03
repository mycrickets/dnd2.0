import src.utils.utils as utilities


class magic_chr:
    magic_throw = None
    magic_dc = 0
    magic_attack = None
    magic_ct = 0
    spells = None

    def __init__(self):
        '''self.magic_throw = ""
        self.magic_dc = 0
        self.attack = ""
        self.cantrips = [0, []]
        self.one = [0, []]
        self.two = [0, []]
        self.three = [0, []]
        self.four = [0, []]
        self.five = [0, []]
        self.six = [0, []]
        self.seven = [0, []]
        self.eight = [0, []]
        self.nine = [0, []]
        self.spells = [self.cantrips, self.one, self.two, self.three, self.four,
                        self.five, self.six, self.seven, self.eight, self.nine]
        self.magic_ct = utilities.count_spells(self)'''

    def set_magic(self, level, cant_ct, clas):
        """
        set the necessary spell slots/spells known for any character, provided their level and class
        :param level: int, the character's level
        :param cant_ct: int, amount of cantrips known (varies by class)
        :param clas: string of the character's class
        :return: nothing
        """
        level = int(level)
        cant_ct = int(cant_ct)
        if clas in ["ranger", "paladin"]:
            if level > 1:
                self.one[0] = 2
                self.one[1].append(input("Level up: What other level one spell do you want to learn?"))
            if level > 2:
                self.one[0] = 3
                self.one[1].append(input("Level up: What final level one spell do you want to learn?"))
            if level > 4:
                self.one[0] = 4
                self.one[1].append(input("Level up: What final level one spell do you want to learn?"))
                self.two[0] = 2
                self.two[1].append(input("What two level two spells do you want to learn?"))
            if level > 6:
                self.two[0] = 3
                self.two[1].append(input("Level up: What final level two spell do you want to learn?"))
            if level > 7:
                self.four[0] = 2
                self.four[1].append(input("Level up: What level four spell do you want to learn?"))
            if level > 8:
                self.three[0] = 2
                self.three[1].append(input("Level up: What two level three spells do you want to learn?"))
                self.four[0] = 3
                self.four[1].append(input("Level up: What final level four spell do you want to learn?"))
            if level > 10:
                self.three[0] = 3
                self.three[1].append(input("Level up: What final level three spells do you want to learn?"))
            if level > 12:
                self.four[0] = 1
                self.four[1].append(input("Level up: What level four spell do you want to learn?"))
            if level > 14:
                self.four[0] = 2
                self.four[1].append(input("Level up: What level four spell do you want to learn?"))
                self.five[0] = 1
                self.five[1].append(input("What level five spell do you want to learn?"))
            if level > 16:
                self.four[0] = 3
                self.four[1].append(input("Level up: What final level four spell do you want to learn?"))
            if level > 17:
                self.five[0] = 3
                self.five[1].append(input("Level up: What final level five spell do you want to learn?"))
            if level > 18:
                self.five[0] = 2
                self.five[1].append(input("Level up: What level five spell do you want to learn?"))

        elif clas in ["wizard", "sorcerer", "warlock", "bard", "cleric", "druid"]:
            self.cantrips[0] = int(cant_ct)
            self.cantrips[1].append(input("Initialization: What " + str(cant_ct) + " " + clas + "cantrips do you want "
                                                                                                "to add?"))
            if level > 3:
                self.cantrips[0] += 1
                self.cantrips[1].append(input("Level up: what other cantrip do you want to add?"))
            if level > 9:
                self.cantrips[0] += 1
                self.cantrips[1].append(input("Level up: what other cantrip do you want to add?"))
            self.one[0] = 2
            self.one[1].append(input("What two level one spells do you want to learn?"))
            if level > 1:
                self.one[0] = 3
                self.one[1].append(input("Level up: What other level one spell do you want to learn?"))
            if level > 2:
                self.one[0] = 4
                self.one[1].append(input("Level up: What final level one spell do you want to learn?"))
                self.two[0] = 2
                self.two[1].append(input("What two level two spells do you want to learn?"))
            if level > 3:
                self.two[0] = 3
                self.two[1].append(input("Level up: What final level two spell do you want to learn?"))
            if level > 4:
                self.three[0] = 2
                self.three[1].append(input("Level up: What two level three spells do you want to learn?"))
            if level > 5:
                self.three[0] = 3
                self.three[1].append(input("Level up: What final level three spells do you want to learn?"))
            if level > 6:
                self.four[0] = 1
                self.four[1].append(input("Level up: What level four spell do you want to learn?"))
            if level > 7:
                self.four[0] = 2
                self.four[1].append(input("Level up: What level four spell do you want to learn?"))
            if level > 8:
                self.four[0] = 3
                self.four[1].append(input("Level up: What final level four spell do you want to learn?"))
                self.five[0] = 1
                self.five[1].append(input("What level five spell do you want to learn?"))
            if level > 9:
                self.five[0] = 2
                self.five[1].append(input("Level up: What level five spell do you want to learn?"))
            if level > 10:
                self.six[0] = 1
                self.six[1].append(input("Level up: What level six spell do you want to learn?"))
            if level > 12:
                self.seven[0] = 2
                self.seven[1].append(input("Level up: What level seven spell do you want to learn?"))
            if level > 14:
                self.eight[0] = 1
                self.eight[1].append(input("Level up: What final level eight spell do you want to learn?"))
            if level > 16:
                self.nine[0] = 1
                self.nine[1].append(input("Level up: What final level nine spell do you want to learn?"))
            if level > 17:
                self.five[0] = 3
                self.five[1].append(input("Level up: What final level five spell do you want to learn?"))
            if level > 18:
                self.six[0] = 2
                self.six[1].append(input("Level up: What final level six spell do you want to learn?"))
            if level > 19:
                self.seven[0] = 2
                self.seven[1].append(input("Level up: What final level seven spell do you want to learn?"))

        # TODO: add_spell, magic_to_string
