from utils.character.chr_clas.BaseClass import BaseClass
from utils.character.MagicChr import MagicChr
import utils.utils_file as utilities


class Bard(BaseClass, MagicChr):
    def __init__(self, char):
        BaseClass.__init__(self, char.level)
        MagicChr.__init__(self)
        cant_ct = 2
        self.level = int(char.level)
        self.set_magic(self.level, cant_ct, "bard")
        self.str_mod = char.strength
        self.dex_mod = char.dexterity
        self.wis_mod = char.wisdom
        self.int_mod = char.intelligence
        self.cha_mod = char.charisma
        self.con_mod = char.constitution
        self.level_scores([3, 7, 11, 15, 18])
        self.expert_skills = []
        all_skills = list(set(utilities.valid_skills()) - set(char.race.skills))
        archetype_opts = ["glamour", "lore", "satire", "sword", "valor", "whisper"]
        level_features = [[1, ["Jack of all Trades", "Song of Rest"]], [2, ["Expertise"]], [4, ["Font of Inspiration"]],
                          [5, ["Countercharm"]], [9, "Magical Secrets"],
                          [13, "Magical Secrets x2"], [17, "Magical Secrets x3"], [19, ["Superior Inspiration"]]]
        equip_opts = [["rapier", "longsword", "any other simple weapon (please input)"]]
        non_wpn_equip = [["Diplomats pack", "Entertainers pack"], ["a lute", "any other musical instrument (please input)"]]
        self.saving_throws = ["dexterity", "charisma"]
        self.magic_throw = "charisma"
        self.magic_dc = 8 + self.prof_bonus + self.cha_mod
        utilities.append_features(self, ["Ritual Casting", "Spellcasting Focus", "Bardic Inspiration"])
        utilities.append_proficiencies(self, ["light armor", "simple weapons", "hand crossbows", "longswords", "rapiers", "shortswords"])
        self.add_instrument(3)
        self.set_equip(equip_opts, True)
        self.set_equip(non_wpn_equip, False)
        self.armor.append(["leather", "11"])
        utilities.equip(self, "dagger")
        utilities.set_skills(self, 3, all_skills)
        self.init_hit_dice(8)
        self.init_hp(8, "constitution", 8)
        self.level_features(level_features)
        if self.level > 2:
            arch_choice = self.init_archetype(archetype_opts)
            self.set_arch(arch_choice, char)
            self.set_expertise(char, 2)
        if self.level > 9:
            self.set_expertise(char, 2)

    def add_instrument(self, amt):
        for i in range(0, int(amt)):
            self.equipment.append(input("Which instrument do you want to have?\n"))

    def set_expertise(self, char, amt):
        for i in range(0, int(amt)):
            flag = False
            while not flag:
                skills = set(char.race.skills).union(set(self.skills)) - set(self.expert_skills)
                pot_skills = list(skills)
                print("Which skill do you want to double your proficiency bonus for?\n"
                      "Your known and valid skills are listed below")
                print("Choice: " + str(i+1) + "/" + str(amt))
                for item in pot_skills:
                    print(item)
                ch = input("")
                if utilities.is_valid_input(ch, pot_skills):
                    self.expert_skills.append(ch)
                    flag = True

    def set_arch(self, arch_choice, char):
        arch = {}
        if arch_choice == "glamour":
            arch['feature'] = [[0, "Mantle of Inspiration"], [0, "Enthralling Performance"], [5, "Mantle of Majesty"],
                               [13, "Unbreakable Majesty"]]
        elif arch_choice == "lore":
            all_skills = list(set(utilities.valid_skills()) - set(char.race.skills) - set(self.skills))
            utilities.set_skills(self, 3, all_skills)
            arch['feature'] = [[2, "Cutting Words"], [5, "Additional Magic Secrets"], [13, "Peerless Skill"]]
        elif arch_choice == "satire":
            arch['proficiency'] = [[0, "Thieves' tools"]]
            arch['skill'] = [[0, "sleight of hand"]]
            all_skills = list(set(utilities.valid_skills()) - set(char.race.skills) - set(self.skills))
            utilities.set_skills(self, 1, all_skills)
            arch['feature'] = [[0, "Tumbling Fool"], [5, "Fool's Insight"], [13, "Fool's Luck"]]
            arch['spells'] = [[[5, "two"], ["Detect Thoughts"]]]
        elif arch_choice == "sword":
            arch['proficiency'] = [[0, ["medium armor", "scimitar"]]]
            opts = ["dueling", "two weapon"]
            print("College of Swords: Which fighting style do you want to join? They're listed below")
            print("dueling")
            print("two weapon")
            style = input("")
            arch['feature'] = [[0, "Blade Flourish"], [5, "Extra Attack"], [13, "Master's Flourish"]]
            flag = True
            while flag:
                if utilities.is_valid_input(style, opts):
                    if style == "dueling":
                        print("dueling\n\n")
                        arch['feature'].append([0, ["Dueling (Bard)"]])
                    else:
                        print("other archetype\n\n")
                        arch['feature'].append([0, ["Two-Weapon Fighting (Bard)"]])
                    flag = False
        elif arch_choice == "valor":
            arch['proficiency'] = [[0, ["medium armor"]], [0, ["shields"]], [0, ["martial weapons"]]]
            arch['feature'] = [[0, "Combat Inspiration"], [5, "Extra Attack"], [13, "Battle Magic"]]
        else:
            arch_choice = "whisper"
            arch['feature'] = [[0, ["Psychic Blades", "Words of Terror"]], [5, ["Mantle of Whispers"]], [13, ["Shadow Lore"]]]
        self.level_arch(arch)

