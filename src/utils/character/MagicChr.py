import utils.utils as utilities


class MagicChr:
    def __init__(self):
        self.magic_throw = ""
        self.magic_dc = 0
        self.magic_attack = ""
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
        self.magic_ct = utilities.count_spells(self)

    def set_magic(self, level, cant_ct, clas):
        """
        set the necessary spell slots/spells known for any character, provided their level and class
        :param level: int, the character's level
        :param cant_ct: int, amount of cantrips known (varies by class)
        :param clas: string of the character's class
        :return: N/A
        """
        level = int(level)
        cant_ct = int(cant_ct)
        self.cantrips[0] = int(cant_ct)
        self.cantrips[1].append(input("\nInitialization: Which " + str(cant_ct) + " " + clas + " cantrips do you want to learn?\n"))
        if clas in ["ranger", "paladin"]:
            if level > 1:
                self.one[0] = 2
                self.one[1].append(input("\nLevel up: What level one spell do you want to learn?\n"))
            if level > 2:
                self.one[0] = 3
                self.one[1].append(input("\nLevel up: What other level one spell do you want to learn?\n"))
            if level > 4:
                self.one[0] = 4
                self.one[1].append(input("\nLevel up: What final level one spell do you want to learn?\n"))
                self.two[0] = 2
                self.two[1].append(input("\nLevel up: What first level two spell do you want to learn?\n"))
                self.two[1].append(input("\nLevel up: What second level two spell do you want to learn?\n"))
            if level > 6:
                self.two[0] = 3
                self.two[1].append(input("\nLevel up: What final level two spell do you want to learn?\n"))
            if level > 8:
                self.three[0] = 2
                self.three[1].append(input("\nLevel up: What first level three spell do you want to learn?\n"))
                self.three[1].append(input("\nLevel up: What second level three spell do you want to learn?\n"))
            if level > 10:
                self.three[0] = 3
                self.three[1].append(input("\nLevel up: What final level three spell do you want to learn?\n"))
            if level > 12:
                self.four[0] = 1
                self.four[1].append(input("\nLevel up: What level four spell do you want to learn?\n"))
            if level > 14:
                self.four[0] = 2
                self.four[1].append(input("\nLevel up: What level four spell do you want to learn?\n"))
            if level > 16:
                self.four[0] = 3
                self.four[1].append(input("\nLevel up: What final level four spell do you want to learn?\n"))
            if level > 17:
                self.five[0] = 1
                self.five[1].append(input("\nLevel up: What level five spell do you want to learn?\n"))
            if level > 18:
                self.five[0] = 2
                self.five[1].append(input("\nLevel up: What final level five spell do you want to learn?\n"))
        elif clas in ["wizard", "sorcerer", "warlock", "bard", "cleric", "druid", "necromancer"]:
            if level > 0:
                self.one[0] = 2
                self.one[1].append(input("\nLevel up: What first level one spell do you want to learn?\n"))
                self.one[1].append(input("\nLevel up: What second level one spell do you want to learn?\n"))
            if level > 3:
                self.cantrips[0] += 1
                self.cantrips[1].append(input("\nLevel up: what other cantrip do you want to add?"))
            if level > 9:
                self.cantrips[0] += 1
                self.cantrips[1].append(input("\nLevel up: what other cantrip do you want to add?"))
            if level > 1:
                self.one[0] = 3
                self.one[1].append(input("\nLevel up: What other level one spell do you want to learn?\n"))
            if level > 2:
                self.one[0] = 4
                self.one[1].append(input("\nLevel up: What final level one spell do you want to learn?\n"))
                self.two[0] = 2
                self.two[1].append(input("\nLevel up: What first level two spell do you want to learn?\n"))
                self.two[1].append(input("\nLevel up: What second level two spell do you want to learn?\n"))
            if level > 3:
                self.two[0] = 3
                self.two[1].append(input("\nLevel up: What final level two spell do you want to learn?\n"))
            if level > 4:
                self.three[0] = 2
                self.three[1].append(input("\nLevel up: What two level three spells do you want to learn?\n"))
            if level > 5:
                self.three[0] = 3
                self.three[1].append(input("\nLevel up: What final level three spells do you want to learn?\n"))
            if level > 6:
                self.four[0] = 1
                self.four[1].append(input("\nLevel up: What level four spell do you want to learn?\n"))
            if level > 7:
                self.four[0] = 2
                self.four[1].append(input("\nLevel up: What level four spell do you want to learn?\n"))
            if level > 8:
                self.four[0] = 3
                self.four[1].append(input("\nLevel up: What final level four spell do you want to learn?\n"))
                self.five[0] = 1
                self.five[1].append(input("\nLevel up: What level five spell do you want to learn?\n"))
            if level > 9:
                self.five[0] = 2
                self.five[1].append(input("\nLevel up: What level five spell do you want to learn?\n"))
            if level > 10:
                self.six[0] = 1
                self.six[1].append(input("\nLevel up: What level six spell do you want to learn?\n"))
            if level > 12:
                self.seven[0] = 2
                self.seven[1].append(input("\nLevel up: What level seven spell do you want to learn?\n"))
            if level > 14:
                self.eight[0] = 1
                self.eight[1].append(input("\nLevel up: What final level eight spell do you want to learn?\n"))
            if level > 16:
                self.nine[0] = 1
                self.nine[1].append(input("\nLevel up: What final level nine spell do you want to learn?\n"))
            if level > 17:
                self.five[0] = 3
                self.five[1].append(input("\nLevel up: What final level five spell do you want to learn?\n"))
            if level > 18:
                self.six[0] = 2
                self.six[1].append(input("\nLevel up: What final level six spell do you want to learn?\n"))
            if level > 19:
                self.seven[0] = 2
                self.seven[1].append(input("\nLevel up: What final level seven spell do you want to learn?\n"))
        elif clas in ["eldritch", "rogue"]:
            if level > 2:
                self.one[0] += 2
                self.one[1].append(input("\nLevel up: What first level one spell do you want to learn?\n"))
                self.one[1].append(input("\nLevel up: What second level one spell do you want to learn?\n"))
            if level > 3:
                self.cantrips[0] += 1
                self.cantrips[1].append(input("\nLevel up: What final cantrip do you want to add?"))
                self.one[0] += 1
                self.one[1].append(input("\nLevel up: What other level one spell do you want to learn?\n"))
            if level > 6:
                self.one[0] += 1
                self.one[1].append(input("\nLevel up: What final level one spell do you want to learn?\n"))
                self.two[0] += 2
                self.two[1].append(input("\nLevel up: What first level two spell do you want to learn?\n"))
                self.two[1].append(input("\nLevel up: What second level two spell do you want to learn?\n"))
            if level > 9:
                self.two[0] += 1
                self.two[1].append(input("\nLevel up: What final level two spell do you want to learn?\n"))
            if level > 12:
                self.three[0] += 2
                self.three[1].append(input("\nLevel up: What two level three spells do you want to learn?\n"))
            if level > 15:
                self.three[0] += 1
                self.three[1].append(input("\nLevel up: What final level three spell do you want to learn?\n"))
            if level > 18:
                self.four[0] += 1
                self.four[1].append(input("\nLevel up: What level four spell do you want to learn?\n"))

    def add_spell(self, spells, chr_level):
        """
        adds spells to chr input
        :param chr_level: level of character
        :param spells: list of lists: [[[(int) level, (str) level], [spells]], [level, [spells]]]
        :return: N/A
        """
        print(spells)
        print(chr_level)

        chr_level = int(chr_level)
        set_level = spells[0][0]
        spell_lvl = spells[0][1]
        spells = spells[1]
        for item in spells:
            if chr_level > set_level:
                if spell_lvl == "one":
                    plinth = self.one
                elif spell_lvl == "two":
                    plinth = self.two
                elif spell_lvl == "three":
                    plinth = self.three
                elif spell_lvl == "four":
                    plinth = self.four
                elif spell_lvl == "five":
                    plinth = self.five
                elif spell_lvl == "six":
                    plinth = self.six
                elif spell_lvl == "seven":
                    plinth = self.seven
                elif spell_lvl == "eight":
                    plinth = self.eight
                elif spell_lvl == "nine":
                    plinth = self.nine
                else:
                    plinth = self.cantrips
                plinth[0] += 1
                if item not in plinth[1]:
                    plinth[1].append(item)
                else:
                    plinth[0] -= 1
