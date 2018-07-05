from src.utils.character.chr_clas.BaseClass import BaseClass


class Barbarian(BaseClass):
    def __init__(self, char):
        BaseClass.__init__(self, False, char.level)
        race = char.race
        print(char.strength)
