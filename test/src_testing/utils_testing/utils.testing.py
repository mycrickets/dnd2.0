import src.utils.utils as utils


class TestHandler:
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
            assert item[:3] == utils.chr_race_mod(item, True)

    def test_chr_race_mod_race_false(self):
        for item in TestHandler.skills:
            assert item == utils.chr_race_mod(item, False)

    def test_chr_race_mod_bad_input(self):
        assert "bad_input" == utils.chr_race_mod("bad_input", False)

    def test_chr_race_mod_good_input(self):
        assert "strength" == utils.chr_race_mod("strength", False)
