import src.utils.utils as utils
from src.Character import Character


class TestHandler:
    char = Character
    skills = ["strength", "dexterity", "wisdom", "intelligence", "charisma", "constitution"]

    def test_valid_skills(self):
        skills = utils.valid_skills()
        assert "athletics" in skills
        assert "acrobatics" in skills
        assert "sleight of hand" in skills
        assert "stealth" in skills
        assert "arcana" in skills
        assert len(skills) == 18

    def test_chr_race_mod_race_true(self):
        for item in TestHandler.skills:
            assert item[:3] == utils.chr_race_mod(item, True)[:3]

    def test_chr_race_mod_race_false(self):
        for item in TestHandler.skills:
            assert item == utils.chr_race_mod(item, False)

    def test_chr_race_mod_bad_input(self):
        assert "bad_input" == utils.chr_race_mod("bad_input", False)

    def test_chr_race_mod_good_input(self):
        assert "strength" == utils.chr_race_mod("strength", False)

    def test_alter_stat(self):
        TestHandler.char.strength = 10
        TestHandler.char.dexterity = 10
        TestHandler.char.intelligence = 10
        TestHandler.char.wisdom = 10
        TestHandler.char.charisma = 10
        TestHandler.char.constitution = 10
        for item in TestHandler.skills:
            stat = item
            chg = 5
            assert utils.alter_stat(TestHandler.char, stat, chg)
            assert getattr(TestHandler.char, item) == 15

    def test_alter_stat_bad_stat(self):
        stat = "bad_stat"
        chg = 5
        assert not utils.alter_stat(TestHandler.char, stat, chg)

    def test_get_modifier(self):
        char = TestHandler.char
        stat = TestHandler.skills
        for item in stat:
            assert utils.get_modifier(char, item) == 2
