from src.utils.character.chr_clas.BaseClass import BaseClass
from src.utils.character.MagicChr import MagicChr
import src.utils.utils as utilities


class Druid(BaseClass, MagicChr):
    def __init__(self, char):
        BaseClass.__init__(self, char.level)
        MagicChr.__init__(self)
        cant_ct = 2
        self.level = int(char.level)
        self.set_magic(self.level, cant_ct, "druid")
        self.str_mod = char.strength
        self.dex_mod = char.dexterity
        self.wis_mod = char.wisdom
        self.int_mod = char.intelligence
        self.cha_mod = char.charisma
        self.con_mod = char.constitution
        self.level_scores([3, 7, 11, 15, 18])
        all_skills = list({"arcana", "animal handling", "insight", "medicine", "nature", "perception", "religion", "survival"} - set(char.race.skills))
        archetype_opts = ["dreams", "land", "moon", "shepherd", "spores", "twilight"]
        level_features = [[1, "Wild Shape"], [17, ["Timeless Body", "Beast Spells"]], [19, "Archdruid"]]
        wpn_opts = [["Wooden Shield", "Any other simple weapon (please input)"], ["A Scimitar", "Any other simple melee weapon (please input)"]]
        self.saving_throws = ["intelligence", "wisdom"]
        self.magic_throw = "wisdom"
        self.magic_dc = 8 + self.prof_bonus + self.wis_mod
        utilities.append_proficiencies(self, ["light armor", "medium armor", "shields", "clubs", "daggers", "darts", "javelins", "maces",
                            "quarterstaffs", "scimitars", "sickles", "slings", "spears", "herbalism kit"])
        self.set_equip(wpn_opts, True)
        self.armor.append(["Leather Armor", "11"])
        self.languages.append("Druidic")
        utilities.set_skills(self, 2, all_skills)
        self.init_hit_dice(8)
        self.init_hp(8, "constitution", 8)
        for item in ["explorer's pack", "druidic focus"]:
            self.equipment.append(item)
        self.level_features(level_features)
        if self.level > 1:
            arch_choice = self.init_archetype(archetype_opts)
            self.set_arch(arch_choice)

    # noinspection PyTypeChecker
    def set_arch(self, arch_choice):
        arch = {}
        if arch_choice == "dreams":
            arch['feature'] = [[0, "Balm of the Summer Court"],
                               [5, "Hearth of Midnight and Shadow"],
                               [9, "Hidden Paths"],
                               [13, "Walker in Dreams"]]
        elif arch_choice == "land":
            arch['spells'] = [[[0, "cantrip"], [input("Circle of the Land: Which Druid cantrip do you want to learn?")]]]
            arch['feature'] = [[0, "Natural Recovery"], [5, "Land's Stride"], [9, "Nature's Ward"], [13, "Nature's Sanctuary"]]
            arch['resistance'] = [[9, ["Poison", "Disease"]]]
            lands = utilities.get_from_list(["arctic", "coast", "desert", "forest", "grassland", "mountain", "swamp", "underdark"], 1)
            if lands == "arctic":
                arch['spells'].extend([[[2, "two"], ["Hold Person", "Spike Growth"]],
                                       [[4, "three"], ["Sleet Storm", "Slow"]],
                                       [[6, "four"], ["Freedom of Movement", "Ice Storm"]],
                                       [[8, "five"], ["Commune with Nature", "Cone of Cold"]]])
            elif lands == "coast":
                arch['spells'].extend([[[2, "two"], ["Mirror Image", "Misty Step"]],
                                       [[4, "three"], ["Water Breathing", "Water Walk"]],
                                       [[6, "four"], ["Control Water", "Freedom of Movement"]],
                                       [[8, "five"], ["Conjure Elemental", "Scrying"]]])
            elif lands == "desert":
                arch['spells'].extend([[[2, "two"], ["Blur", "Silence"]],
                                       [[4, "three"], ["Create Food and Water", "Protection from Energy"]],
                                       [[6, "four"], ["Blight", "Hallucinatory Terrain"]],
                                       [[8, "five"], ["Insect Plague", "Wall of Stone"]]])
            elif lands == "forest":
                arch['spells'].extend([[[2, "two"], ["Barkskin", "Spider Climb"]],
                                       [[4, "three"], ["Call Lightning", "Plant Growth"]],
                                       [[6, "four"], ["Divination", "Freedom of Movement"]],
                                       [[8, "five"], ["Commune with Nature", "Tree Stride"]]])
            elif lands == "grassland":
                arch['spells'].extend([[[2, "two"], ["Invisibility", "Pass Without Trace"]],
                                       [[4, "three"], ["Daylight", "Haste"]],
                                       [[6, "four"], ["Divination", "Freedom of Movement"]],
                                       [[8, "five"], ["Dream", "Insect Plague"]]])
            elif lands == "mountain":
                arch['spells'].extend([[[2, "two"], ["Spider Climb", "Spike Growth"]],
                                       [[4, "three"], ["Lightning Bolt", "Meld into Stone"]],
                                       [[6, "four"], ["Stone Shape", "Stoneskin"]],
                                       [[8, "five"], ["Passwall", "Wall of Stone"]]])
            elif lands == "swamp":
                arch['spells'].extend([[[2, "two"], ["Darkness", "Melf's Acid Arrow"]],
                                       [[4, "three"], ["Water Walk", "Stinking Cloud"]],
                                       [[6, "four"], ["Locate Creature", "Freedom of Movement"]],
                                       [[8, "five"], ["Scrying", "Insect Plague"]]])
            else:
                lands = "underdark"
                arch['spells'].extend([[[2, "two"], ["Spider Climb", "Web"]],
                                       [[4, "three"], ["Gaseous Form", "Stinking Cloud"]],
                                       [[6, "four"], ["Greater Invisibility", "Stone Shape"]],
                                       [[8, "five"], ["Cloudkill", "Insect Plague"]]])
        elif arch_choice == "moon":
            arch['feature'] = [[0, ["Combat Wild Shape", "Circle Forms"]],
                               [5, "Primal Strike"],
                               [9, "Elemental Wild Shape"],
                               [13, "Thousand Forms"]]
        elif arch_choice == "shepherd":
            arch['language'] = [[0, "Sylvan"]]
            arch['feature'] = [[0, ["Speech of the Woods", "Spirit Totem (" + utilities.get_from_list(["bear", "hawk", "unicorn"], 1) + ")"]],
                               [5, "Mighty Summoner"],
                               [9, "Guardian Spirit"],
                               [13, "Faithful Summons"]]
        elif arch_choice == "spores":
            arch['spells'] = [[[0, "cantrip"], ["Chill Touch"]], [[2, "two"], ["Gentle Repose", "Ray of Enfeeblement"]], [[4, "three"], ["Animate Dead", "Gaseous Form"]], [[6, "four"], ["Blight", "Confusion"]], [[8, "five"], ["Cloudkill", "Contagion"]]]
            arch['feature'] = [[0, ["Halo of Spores", "Symbiotic Entity"]],
                               [5, "Fungal Infestation"],
                               [9, "Spreading Spores"],
                               [13, "Fungal Body"]]
            arch['resistance'] = [[13, ["Blindness", "Deafness", "Frightened", "Poison", "Critical hits"]]]
        else:
            arch_choice = "twilight"
            arch['feature'] = [[0, "Harvest's Scythe"],
                               [5, "Speech Beyond the Grave"],
                               [9, "Watcher at the Threshold"],
                               [13, "Paths of the Dead"]]
        self.level_arch(arch)



