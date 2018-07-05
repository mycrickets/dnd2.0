import src.utils.character.chr_clas.spec as classes
import src.utils.character.race.spec as races
import src.utils.character.BaseChr as base_chr
import src.utils.utils as utilities


class Character(base_chr.BaseChr):
    def __init__(self, level):
        self.strength = 0
        self.dexterity = 0
        self.wisdom = 0
        self.intelligence = 0
        self.charisma = 0
        self.constitution = 0
        super(Character, self).__init__(self, level, self.strength, self.dexterity, self.intelligence,
                                        self.wisdom, self.charisma, self.constitution)
        self.level = int(level)
        self.race = ""
        self.clas = ""
        self.background = ""
        self.stats = ""
        self.personality = ""

    def set_stats(self):
        pass

    def set_race(self):
        pass

    def set_class(self):
        pass

    def set_background(self):
        pass

    def set_personality(self):
        pass

