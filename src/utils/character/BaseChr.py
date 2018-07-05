import src.utils.stats as stats
import src.utils.utils as utilities


class BaseChr:
    def __init__(self, check, level):
        scores = []
        if check:
            scores = utilities.init_scores(level)
        self.level = int(level)
        self.strength = scores[0]
        self.dexterity = scores[1]
        self.wisdom = scores[2]
        self.intelligence = scores[3]
        self.constitution = scores[4]
        self.charisma = scores[5]

