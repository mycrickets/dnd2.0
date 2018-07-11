from src.utils.character.chr_clas.BaseClass import BaseClass
import src.utils.utils as utilities


class Barbarian(BaseClass):
    def __init__(self, char):
        BaseClass.__init__(self, char.level)
        utilities.transfer_languages(self, ["test1", "test2", "draconic"], False, True)
