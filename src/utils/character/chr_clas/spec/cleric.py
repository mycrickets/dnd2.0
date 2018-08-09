from src.utils.character.chr_clas.BaseClass import BaseClass
from src.utils.character.MagicChr import MagicChr
import src.utils.utils as utilities


class Cleric(BaseClass, MagicChr):
    def __init__(self, char):
        BaseClass.__init__(self, char.level)
        MagicChr.__init__(self)
        cant_ct = 3
        self.level = int(char.level)
        self.set_magic(self.level, cant_ct, "cleric")
        self.str_mod = char.race.str_mod
        self.dex_mod = char.race.dex_mod
        self.wis_mod = char.race.wis_mod
        self.int_mod = char.race.int_mod
        self.cha_mod = char.race.cha_mod
        self.con_mod = char.race.con_mod
        self.divine_ct = 2 if self.level > 5 else 3 if self.level > 17 else 1
        all_skills = list({"history", "insight", "medicine", "persuasion", "religion"} - set(char.race.skills))
        archetype_opts = ["arcana", "ambition", "city", "death", "forge", "grave", "knowledge", "life", "light", "nature", "order", "protection", "solidarity", "strength", "tempest", "trickery", "war", "zeal"]
        level_features = [[0, ["Ritual Casting", "Spellcasting Focus"]], [1, ["Turn Undead"]], [4, ["Destroy Undead"]], [9, ["Divine Intervention"]]]
        wpn_opts = [["Mace", "Warhammer"], ["Light crossbow with 20 bolts", "Any other simple weapon (please input)"]]
        equip_opts = [["Priest's Pack", "Explorer's Pack"], ["Scale Mail", "Leather Armor", "Chain Mail"]]
        self.saving_throws = ["wisdom", "charisma"]
        self.magic_throw = "wisdom"
        self.magic_dc = 8 + self.prof_bonus + self.wis_mod
        utilities.append_proficiencies(self, ["light armor", "medium armor", "shields", "all simple weapons"])
        self.set_equip(wpn_opts, True)
        self.set_equip(equip_opts, False)
        utilities.set_skills(self, 2, all_skills)
        self.init_hit_dice(8)
        self.init_hp(8, "constitution", "8")
        self.equipment.append("Shield")
        self.equipment.append(input("What holy symbol do you want to use?"))
        self.level_features(level_features)
        self.level_scores([3, 7, 11, 15, 18])
        arch_choice = self.init_archetype(archetype_opts)
        self.set_arch(arch_choice, char)

    def set_arch(self, arch_choice, char):
        arch = {}
        if arch_choice == "arcana":
            arch['feature'] = [[5, "Spell Breaker"], [7, "Potent Spellcasting"], [17, "Arcane Abjuration"]]
            arch['skill'] = [[0, "arcana"]]
            arch['spell'] = [[[0, "cantrip"], [input("Arcana Divine Initialization: What two wizard cantrips do you want to learn?")]], [[0, "one"], ["Detect Magic", "Magic Missile"]],
                             [[3, "two"], ["Magic Weapon", "Nystul's Magic Aura"]], [[5, "three"], ["Dispel Magic", "Magic Circle"]], [[7, "four"], ["Arcana Eye", "Leomund's Secret Chest"]], [[9, "five"], ["Planar Binding", "Teleportation Circle"]]]
        elif arch_choice == "ambition":
            arch['feature'] = [[0, ["Warding Flame", "Invoke Duplicity"]], [5, "Cloak of Shadows"], [7, "Potent Spellcasting"], [16, "Improved Duplicity"]]
            arch['spell'] = [[[0, "one"], ["Bane", "Disguise Self"]], [[3, "two"], ["Mirror Image", "Ray of Enfeeblement"]], [[5, "three"], ["Bestow Curse", "Vampiric Touch"]], [[7, "four"], ["Death Ward", "Dimension Door"]], [[9, "five"], ["Dominate Person", "Modify Memory"]]]
        elif arch_choice == "city":
            arch['spell'] = [[[0, "one"], ["Comprehend Language", "Remote Access", "On/Off"]], [[3, "two"], ["Find Vehicle", "Heat Metal"]], [[5, "three"], ["Lightning Bolt", "Protection from Ballistics"]], [[7, "four"], ["Locate Creature", "Synchronicity"]], [[9, "five"], ["Commune with City", "Shutdown"]]]
            arch['proficiency'] = [[0, ["sidearms", "vehicles (land)"]]]
            arch['feature'] = [[0, "Heart of the City"], [1, "Spirits of the City"], [5, "Block Watch"], [7, "Divine Strike"], [16, "Express Transit"]]
        elif arch_choice == "death":
            arch['spell'] = [[[0, "cantrip"], [input("Death Divine Initialization: What necromancy cantrip do you want to learn?")]], [[0, "one"], ["False Life", "Ray of Sickness"]], [[3, "two"], ["Blindness/Deafness", "Ray of Enfeeblement"]], [[5, "three"], ["Animate Dead", "Vampiric Touch"]], [[7, "four"], ["Blight", "Death Ward"]], [[9, "five"], ["Antilife Shell", "Cloudkill"]]]
            arch['proficiency'] = [[0, "martial weapons"]]
            arch['feature'] = [[0, "Reaper"], [1, "Touch of Death"], [5, "Inescapable Destruction"], [7, "Divine Strike"], [16, "Improved Reaper"]]
        elif arch_choice == "forge":
            arch['spell'] = [[[0, "one"], ["Identify", "Searing Smite"]],
                             [[3, "two"], ["Heat Metal", "Magic Weapon"]],
                             [[5, "three"], ["Elemental Weapon", "Protection from Energy"]],
                             [[7, "four"], ["Fabricate", "Wall of Fire"]],
                             [[9, "five"], ["Animate Objects", "Creation"]]]
            arch['proficiency'] = [[0, ["heavy armor", "smith's tools"]]]
            arch['resistance'] = [[5, "fire damage"], [16, "Immunity to fire damage"]]
            arch['feature'] = [[0, "Blessing of the Forge"], [1, "Artisan's Blessing"], [5, "Soul of the Forge"], [7, "Divine Strike"], [16, "Saint of Forge and Fire"]]
        elif arch_choice == "grave":
            arch['spell'] = [[[0, "one"], ["Bane", "False Life"]],
                             [[3, "two"], ["Gentle Repose", "Ray of Enfeeblement"]],
                             [[5, "three"], ["Revivify", "Vampiric Touch"]],
                             [[7, "four"], ["Blight", "Death Ward"]],
                             [[9, "five"], ["Antilife Shell", "Raise Dead"]]]
            arch['feature'] = [[0, ["Circle of Mortality", "Eyes of the Grave"]], [1, "Path to the Grave"], [5, "Sentinel at Death's Door"], [7, "Potent Spellcasting"], [16, "Keeper of Souls"]]
        elif arch_choice == "knowledge":
            arch['spell'] = [[[0, "one"], ["Command", "Identify"]],
                             [[3, "two"], ["Augury", "Suggestion"]],
                             [[5, "three"], ["Nondetection", "Speak with Dead"]],
                             [[7, "four"], ["Arcane Eye", "Confusion"]],
                             [[9, "five"], ["Legend Lore", "Scrying"]]]
            arch['language'] = [[0, [input("Knowledge Domain Initialization: What language do you want to learn?"), input("Knowledge Domain Initialization: What language do you want to learn?")]]]
            utilities.set_skills(self, 2, ["Arcana", "History", "Nature", "Religion"])
            arch['feature'] = [[0, "Blessing of Knowledge"], [1, "Knowledge of the Ages"], [5, "Read Thoughts"], [7, "Potent Spellcasting"], [16, "Visions of the Past"]]
        elif arch_choice == "life":
            arch['spell'] = [[[0, "one"], ["Bless", "Cure Wounds"]],
                             [[3, "two"], ["Lesser Restoration", "Spiritual Weapon"]],
                             [[5, "three"], ["Beacon of Hope", "Revivify"]],
                             [[7, "four"], ["Death Ward", "Guardian of Faith"]],
                             [[9, "five"], ["Mass Cure Wounds", "Raise Dead"]]]
            arch['proficiency'] = [[0, "heavy armor"]]
            arch['feature'] = [[0, "Disciple of Life"], [1, "Preserve Life"], [5, "Blessed Healer"], [7, "Divine Strike"], [16, "Supreme Healing"]]
        elif arch_choice == "light":
            arch['spell'] = [[[0, "cantrip"], ["Light"]], [[0, "one"], ["Burning Hands", "Faerie Fire"]],
                             [[3, "two"], ["Flaming Sphere", "Scorching Ray"]],
                             [[5, "three"], ["Daylight", "Fireball"]],
                             [[7, "four"], ["Guardian of Faith", "Wall of Fire"]],
                             [[9, "five"], ["Flame Strike", "Scrying"]]]
            arch['feature'] = [[0, "Warding Flame"], ["Radiance of the Dawn"], [5, "Improved Flame"], [7, "Potent Spellcasting"], [16, "Corona of Light"]]
        elif arch_choice == "nature":
            arch['spell'] = [[[0, "cantrip"], [input("Nature Domain Initialization: What Druid cantrip do you want to learn?")]], [[0, "one"], ["Animal Friendship", "Speak with Animals"]],
                             [[3, "two"], ["Barkskin", "Spike Growth"]],
                             [[5, "three"], ["Plant Growth", "Wind Wall"]],
                             [[7, "four"], ["Dominate Beast", "Grasping Vine"]],
                             [[9, "five"], ["Insect Plague", "Tree Stride"]]]
            utilities.set_skills(self, 1, ["Animal Handling", "Nature", "Survival"])
            arch['proficiency'] = [[0, "Heavy armor"]]
            arch['feature'] = [[1, "Charm Animals and Plants"], [5, "Dampen Elements"], [7, "Divine Strike"], [16, "Master of Nature"]]
        elif arch_choice == "zeal":
            arch['spell'] = [[[0, "one"], ["Searing Smite", "Thunderous Smite"]],
                             [[3, "two"], ["Magic Weapon", "Shatter"]],
                             [[5, "three"], ["Haste", "Fireball"]],
                             [[7, "four"], ["Fire Shield (warm shield only)", "Freedom of Movement"]],
                             [[9, "five"], ["Destructive Wave", "Flame Strike"]]]
            arch['proficiency'] = [[0, ["heavy armor", "martial weapons"]]]
            arch['feature'] = [[0, "Priest of Zeal"], [1, "Consuming Fervor"], [5, "Resounding Strike"],
                               [7, "Divine Strike"], [16, "Blaze of Glory"]]
        elif arch_choice == "order":
            arch['spell'] = [[[0, "one"], ["Command", "Heroism"]],
                             [[3, "two"], ["Enhance Ability", "Hold Person"]],
                             [[5, "three"], ["Mass Healing Word", "Slow"]],
                             [[7, "four"], ["Compulsion", "Locate Creature"]],
                             [[9, "five"], ["Commune", "Dominate Person"]]]
            arch['proficiency'] = [[0, "Heavy armor"]]
            arch['feature'] = [[0, "Voice of Authority"], [1, "Order's Demand"], [5, "Order's Dominion"],
                               [7, "Divine Strike"], [16, "Order's Wrath"]]
        elif arch_choice == "protection":
            arch['spell'] = [[[0, "one"], ["Compelled Duel", "Protection from Good and Evil"]],
                             [[3, "two"], ["Aid", "Protection from Poison"]],
                             [[5, "three"], ["Protection from Energy", "Slow"]],
                             [[7, "four"], ["Guardian of Faith", "Otiluke's Resilient Sphere"]],
                             [[9, "five"], ["Antilife Shell", "Wall of Force"]]]
            arch['proficiency'] = [[0, "Heavy armor"]]
            arch['feature'] = [[0, "Shield of the Faithful"], [1, "Radiant Defense"], [5, "Blessed Healer"], [7, "Divine Strike"], [16, "Indomitable Defense"]]
        elif arch_choice == "solidarity":
            arch['spell'] = [[[0, "one"], ["Bless", "Guiding Bolt"]],
                             [[3, "two"], ["Aid", "Warding Bond"]],
                             [[5, "three"], ["Beacon of Hope", "Crusader's Mantle"]],
                             [[7, "four"], ["Guardian of Faith", "Aura of Life"]],
                             [[9, "five"], ["Circle of Power", "Mass Cure Wounds"]]]
            arch['proficiency'] = [[0, "Heavy armor"]]
            arch['feature'] = [[0, "Solidarity's Action"], [1, "Preserve Life"], [5, "Oketra's Blessing"],
                               [7, "Divine Strike"], [16, "Supreme Healing"]]
        elif arch_choice == "strength":
            arch['spell'] = [[[0, "cantrip"], [input("Strength Domain Initialization: What Druid cantrip do you want to learn?")]], [[0, "one"], ["Divine Favor", "Shield of Faith"]],
                             [[3, "two"], ["Enhance Ability", "Protection from Poison"]],
                             [[5, "three"], ["Haste", "Protection from Energy"]],
                             [[7, "four"], ["Dominate Beast", "Stoneskin"]],
                             [[9, "five"], ["Destructive Wave", "Insect Plague"]]]
            utilities.set_skills(self, 1, ["Animal Handling", "Athletics", "Nature", "Survival"])
            arch['proficiency'] = [[0, "Heavy armor"]]
            arch['feature'] = [[1, "Feat of Strength"], [5, "Rhona's Blessing"],
                               [7, "Divine Strike"]]
            arch['resistance'] = [[16, ["Nonmagical bludgeoning damage", "Nonmagical piercing damage", "Nonmagical slashing damage"]]]
        elif arch_choice == "tempest":
            arch['spell'] = [[[0, "one"], ["Fog Cloud", "Thunderwave"]],
                             [[3, "two"], ["Gust of Wind", "Shatter"]],
                             [[5, "three"], ["Call Lightning", "Sleet Storm"]],
                             [[7, "four"], ["Control Water", "Ice Storm"]],
                             [[9, "five"], ["Destructive Wave", "Insect Plague"]]]
            arch['proficiency'] = [[0, ["heavy armor", "martial weapons"]]]
            arch['feature'] = [[0, "Wrath of the Storm"], [1, "Destructive Wrath"], [5, "Thunderbolt Strike"],
                               [7, "Divine Strike"], [16, "Stormborn"]]
        elif arch_choice == "trickery":
            arch['spell'] = [[[0, "one"], ["Charm Person", "Disguise Self"]],
                             [[3, "two"], ["Mirror Image", "Pass Without Trace"]],
                             [[5, "three"], ["Blink", "Dispel Magic"]],
                             [[7, "four"], ["Dimension Door", "Polymorph"]],
                             [[9, "five"], ["Dominate Person", "Modify Memory"]]]
            arch['feature'] = [[0, "Blessing of the Trickster"], [1, "Invoke Duplicity"], [5, "Cloak of Shadows"],
                               [7, "Divine Strike"], [16, "Improved Duplicity"]]
        elif arch_choice == "war":
            arch['spell'] = [[[0, "one"], ["Divine Favor", "Shield of Faith"]],
                             [[3, "two"], ["Magic Weapon", "Spiritual Weapon"]],
                             [[5, "three"], ["Crusader's Mantle", "Spirit Guardians"]],
                             [[7, "four"], ["Freedom of Movement", "Stoneskin"]],
                             [[9, "five"], ["Flame Strike", "Hold Monster"]]]
            arch['proficiency'] = [[0, ["heavy armor", "martial weapons"]]]
            arch['feature'] = [[0, "War Priest"], [1, "Guided Strike"], [5, "War God's Blessing"],
                               [7, "Divine Strike"]]
            arch['resistance'] = [
                [16, ["Nonmagical bludgeoning damage", "Nonmagical piercing damage", "Nonmagical slashing damage"]]]
        else:
            arch_choice = "life"
            arch['spell'] = [[[0, "one"], ["Bless", "Cure Wounds"]],
                             [[3, "two"], ["Lesser Restoration", "Spiritual Weapon"]],
                             [[5, "three"], ["Beacon of Hope", "Revivify"]],
                             [[7, "four"], ["Death Ward", "Guardian of Faith"]],
                             [[9, "five"], ["Mass Cure Wounds", "Raise Dead"]]]
            arch['proficiency'] = [[0, "heavy armor"]]
            arch['feature'] = [[0, "Disciple of Life"], [1, "Preserve Life"], [5, "Blessed Healer"],
                               [7, "Divine Strike"], [16, "Supreme Healing"]]
        self.level_arch(arch)

