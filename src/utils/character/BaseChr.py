import src.utils.stats as stats
import src.utils.utils as utilities


class BaseChr:
    def __init__(self, level, strength, dexterity, intelligence, wisdom, charisma, constitution):
        self.level = int(level)
        self.strength = int(strength)
        self.wisdom = int(wisdom)
        self.dexterity = int(dexterity)
        self.intelligence = int(intelligence)
        self.charisma = int(charisma)
        self.constitution = int(constitution)

