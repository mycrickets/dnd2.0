from src.utils.character.chr_clas.BaseClass import BaseClass
from src.utils.character.MagicChr import MagicChr
import src.utils.utils as utilities
import math


class Warlock(BaseClass, MagicChr):
    def __init__(self, char):
        BaseClass.__init__(self, char.level)
        MagicChr.__init__(self)
        cant_ct = 2
        self.level = int(char.level)
        self.set_magic(self.level, cant_ct, "warlock")
        self.str_mod = char.race.str_mod
        self.dex_mod = char.race.dex_mod
        self.wis_mod = char.race.wis_mod
        self.int_mod = char.race.int_mod
        self.cha_mod = char.race.cha_mod
        self.con_mod = char.race.con_mod
        self.level_scores([3, 7, 11, 15, 18])
        all_skills = list({"arcana", "deception", "history", "intimidation", "nature", "religion"} - set(char.race.skills))
        archetype_opts = ["Archfey", "Celestial", "Fiend", "Ghost in the Machine", "Great Old One", "Hexblade", "Raven Queen", "Seeker", "Undying"]
        level_features = [[10, "Mystic Arcanum"], [19, "Eldritch Master"]]
        wpn_opts = [["Light crossbow with 20 bolts", "Any simple weapon (please input)"]]
        eqp_opts = [["Dungeoneer's pack", "Scholar's pack"], ["Component pouch", "Arcane focus"]]
        self.saving_throws = ["wisdom", "charisma"]
        self.magic_throw = "charisma"
        self.magic_dc = 8 + self.prof_bonus + self.cha_mod
        utilities.append_proficiencies(self, ["light armor", "simple weapons"])
        self.set_equip(wpn_opts, True)
        self.set_equip(eqp_opts, False)
        utilities.set_skills(self, 2, all_skills)
        self.init_hit_dice(8)
        self.init_hp(8, "constitution", 8)
        for item in ["two daggers", input("Initialization: What simple weapon do you want to have?")]:
            utilities.equip(self, item)
        self.armor = ["leather armor", "11"]
        self.invocations = []
        self.pact = ""
        self.pact_desc = []
        self.level_features(level_features)
        arch_choice = self.init_archetype(archetype_opts)
        self.set_arch(arch_choice)
        if self.level > 1:
            self.set_pact()
        if self.level == 1:
            self.invocation_ct = 2
        elif 2 < self.level < 11:
            self.invocation_ct = int(math.ceil(self.level / 2))
        elif self.level > 10:
            self.invocation_ct = 5
        elif self.level > 11:
            self.invocation_ct = 6
        elif self.level > 14:
            self.invocation_ct = 7
        elif self.level > 17:
            self.invocation_ct = 8
        for x in range(0, int(self.invocation_ct)):
            self.choose_inv()

    def choose_inv(self):
        base_inv = ["Armor of Shadows", "Beast Speech", "Beguiling Influence", "Devil's Sight", "Eyes of the Rune Keeper",
                    "Fiendish Vigor", "Gaze of Two Minds", "Mask of Many Faces", "Misty Visions", "Thief of Five Fates"]
        prereq_inv = []
        if self.level > 4:
            prereq_inv.append("Cloak of Flies")
            prereq_inv.append("Gift of the Depths")
            prereq_inv.append("Mire the Mind")
            prereq_inv.append("One with Shadows")
            prereq_inv.append("Sign of Ill Omen")
            prereq_inv.append("Tomb of Levistus")
        if self.level > 6:
            prereq_inv.append("Bewitching Whispers")
            prereq_inv.append("Dreadful Word")
            prereq_inv.append("Ghostly Gaze")
            prereq_inv.append("Sculptor of Flesh")
            prereq_inv.append("Trickster's Escape")
        if self.level > 8:
            prereq_inv.append("Ascendant Step")
            prereq_inv.append("Minions of Chaos")
            prereq_inv.append("Otherworldly Leap")
            prereq_inv.append("Whispers of the Grave")
        if self.level > 14:
            prereq_inv.append("Master of Myriad Forms")
            prereq_inv.append("Shroud of Shadow")
            prereq_inv.append("Visions od Distant Realms")
            prereq_inv.append("Witch Sight")
        if "eldritch blast" in self.cantrips[1]:
            prereq_inv.append("Agonizing Blast")
            prereq_inv.append("Eldritch Spear")
            prereq_inv.append("Grasp of Hadar")
            prereq_inv.append("Lance of Lethargy")
            prereq_inv.append("Repelling Blast")
            if self.level > 4 and self.archetype == "Fiend":
                prereq_inv.append("Kiss of Mephistopheles")
            if self.archetype == "Raven Queen":
                prereq_inv.append("Raven Queen's Blessing")
        if self.pact == "Pact of the Blade":
            prereq_inv.append("Arcane Gunslinger")
            prereq_inv.append("Improved Pact Bringer")
            if self.level > 4:
                prereq_inv.append("Eldritch Smite")
                prereq_inv.append("Thirsting Blade")
            if self.level > 8:
                prereq_inv.append("Superior Pact Weapon")
            if self.level > 11:
                prereq_inv.append("Lifedrinker")
            if self.level > 14:
                prereq_inv.append("Ultimate Pact Weapon")
            if self.archetype == "Great Old One":
                prereq_inv.append("Claw of Acamar")
            if self.archetype == "Hexblade":
                prereq_inv.append("Curse Bringer")
            if self.archetype == "Fiend":
                prereq_inv.append("Mace of Dispater")
            if self.archetype == "Archfey":
                prereq_inv.append("Moon Bow")
        if self.pact == "Pact of the Tome":
            prereq_inv.append("Aspect of the Moon")
            prereq_inv.append("Book of Ancient Secrets")
            if self.archetype == "Raven Queen":
                prereq_inv.append("Chronicle of the Raven Queen")
        if self.pact == "Pact of the Chain":
            prereq_inv.append("Gift of the Ever-Living Ones")
            prereq_inv.append("Voice of the Chain Master")
            if self.level > 14:
                prereq_inv.append("Chains of Carceri")
        if self.archetype == "Hexblade":
            prereq_inv.append("Burning Hex")
            prereq_inv.append("Chilling Hex")
        if self.archetype == "Great Old One":
            prereq_inv.append("Caiphon's Beacon")
            if self.level > 6:
                prereq_inv.append("Gaze of Khirad")
            if self.level > 17:
                prereq_inv.append("Shroud of Ulban")
        if self.archetype == "Fiend":
            prereq_inv.append("Cloak of Baalzebul")
        if self.archetype == "Archfey":
            prereq_inv.append("Green Lord's Gift")
            prereq_inv.append("Sea Twins' Gift")
        if self.archetype == "Seeker":
            prereq_inv.append("Path of the Seeker")
            prereq_inv.append("Seeker's Speech")
        if self.level > 6 and (any("hex" in feat for feat in self.features) or any("hex" in spell for spell in self.spells)):
            prereq_inv.append("Relentless Hex")

        base = set(base_inv)
        pre = set(prereq_inv)
        invs = set(self.invocations)
        inv_set = (base.union(pre)) - invs
        inv = list(inv_set)
        choice = utilities.get_from_list(inv, 1, "invocation")
        self.invocations.append(choice)

    def set_pact(self):
        self.pact = utilities.get_from_list(["Pact of the Chain", "Pact of the Tome", "Pact of the Blade"], 1, "pact")
        if self.pact == "Pact of the Chain":
            self.pact_desc.append("You learn the Find Familiar spell and can cast it as a ritual. The spell doesn't count against your number of spells known. When you cast the spell, you can choose one of the normal forms for your familiar or one of the following special forms: imp, pseudodragon, quasit or sprite. Additionally, when you take the Attack action, you can forgo one of your own attacks to allow your familiar to make one attack of its own with its reaction.")
            self.add_spell([[[0, "one"], "Find Familiar"]], self.level)
        elif self.pact == "Pact of the Tome":
            self.pact_desc.append("Your patron gives you a grimoire called a Book of Shadows. When you gain this feature, choose three cantrips from any class's spell list (the three needn't be from the same list). While the book is on your person, you can cast those cantrips at will. They don't count against your number of cantrips known. If they don't appear on the warlock spell list, they are nonetheless warlock spells for you. If you lose your Book of Shadows, you can perform a 1-hour ceremony to receive a replacement from your patron. This ceremony can be performed during a short or long rest, and it destroys the previous book. The book turns to ash when you die.")
            self.cantrips[0] += 3
            self.cantrips[1].extend([input("Pact of the Tome: What cantrip do you want to learn?"), input("Pact of the Tome: What cantrip do you want to learn?"), input("Pact of the Tome: What cantrip do you want to learn?")])
        elif self.pact == "Pact of the Blade":
            self.pact_desc.append("You can use your action to create a pact weapon in your empty hand. You can choose the form that this melee weapon takes each time you create it. You are proficient with it while you wield it. This weapon counts as magical for the purpose of overcoming resistance and immunity to non-magical attacks and damage. Your pact weapon disappears if it is more than 5 feet away from you for 1 minute or more. It also disappears if you use this feature again, if you dismiss the weapon (no action required), or if you die.\nYou can transform one magic weapon into your pact weapon by performing a special ritual while you hold the weapon. You perform the ritual over the course of 1 hour, which can be done during a short rest. You can then dismiss the weapon, shunting it into an extra-dimensional space, and it appears whenever you create your pact weapon thereafter. You can't affect an artifact or a sentient weapon in this way. The weapon ceases being your pact weapon if you die, if you perform the 1-hour ritual on a different weapon, or if you use a 1-hour ritual to break your bond to it. The weapon appears at your feet if it is in the extra-dimensional space when the bond breaks.")
        else:
            print("Something went wrong @ pact, warlock")

    def set_arch(self, arch_choice):
        arch = {}
        if arch_choice == "Archfey":
            arch['feature'] = [[0, ["Expanded Spell List (Archfey)", "Fey Presence"]],
                               [5, "Misty Escape"],
                               [9, "Beguiling Defenses"],
                               [13, "Dark Delirium"]]
            arch['resistance'] = [[9, "Charm Immunity"]]
        elif arch_choice == "Celestial":
            arch['feature'] = [[0, ["Expanded Spell List (Celestial)", "Healing Light"]],
                               [5, "Radiant Soul"],
                               [9, "Celestial Resilience"],
                               [13, "Searing Vengeance"]]
            arch['spells'] = [[[0, "cantrip"], ["Sacred Flame", "Light"]]]
            arch['resistance'] = [[5, "Radiant Damage"]]
        elif arch_choice == "Fiend":
            arch['feature'] = [[0, ["Expanded Spell List (Fiend)", "Dark One's Blessing"]],
                               [5, "Dark One's Own Luck"],
                               [9, "Fiendish Resilience"],
                               [13, "Hurl Through Hell"]]
        elif arch_choice == "Ghost in the Machine":
            arch['feature'] = [[0, ["Expanded Spell List (Ghost)", "Information Surge"]],
                               [5, "Wire Walk"],
                               [9, "Personal Encryption"],
                               [13, "Technovirus"]]
            arch['spells'] = [[[0, "cantrip"], ["On/Off"]]]
            arch['proficiency'] = [[0, "Hacking Tools"]]
        elif arch_choice == "Great Old One":
            arch['feature'] = [[0, ["Expanded Spell List (Great Old One)", "Awakened Mind"]],
                               [5, "Entropic Ward"],
                               [9, "Thought Shield"],
                               [13, "Create Thrall"]]
            arch['resistance'] = [[9, "Psychic Damage"]]
        elif arch_choice == "Hexblade":
            arch['feature'] = [[0, ["Expanded Spell List (Hexblade)", "Hex Warrior", "Hexblade's Curse"]],
                               [5, "Accursed Specter"],
                               [9, "Armor of Hexes"],
                               [13, "Master of Hexes"]]
            arch['proficiency'] = [[0, ["medium armor", "shields", "martial weapons"]]]
        elif arch_choice == "Raven Queen":
            arch['feature'] = [[0, ["Expanded Spell List (Raven)", "Sentinel Raven"]],
                               [5, "Soul of the Raven"],
                               [9, "Raven's Shield"],
                               [13, "Queen's Right Hand"]]
            arch['resistance'] = [[9, ["Necrotic Damage", "Fright Immunity"]]]
            arch['proficiency'] = [[9, "Death Saving Throws"]]
        elif arch_choice == "Seeker":
            arch['feature'] = [[0, ["Expanded Spell List (Seeker)", "Shielding Aurora"]],
                               [2, "Pact of the Star Chain"],
                               [5, "Astral Refuge"],
                               [9, "Far Wanderer"],
                               [13, "Astral Sequestration"]]
            arch['resistance'] = [[9, ["Fire Damage", "Cold Damage"]]]
        else:
            arch_choice = "Undying"
            arch['feature'] = [[0, ["Expanded Spell List (Undying)", "Among the Dead"]],
                               [5, "Defy Death"],
                               [9, "Undying Nature"],
                               [13, "Indestructible Life"]]
            arch['spells'] = [[[0, "cantrip"], ["Spare the Dying"]]]
        self.level_arch(arch)


