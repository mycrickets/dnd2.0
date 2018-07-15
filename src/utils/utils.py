import math
import random as r
import src.utils.dictionary as dictionary
import src.utils.spell_dict as spell_dict


def valid_skills():
    return ["athletics", "acrobatics", "sleight of hand", "stealth", "arcana", "history", "investigation", "nature",
            "religion", "animal handling", "insight", "medicine", "perception", "survival", "deception", "intimidation",
            "performance", "persuasion"]


def chr_race_mod(input, race=False):
    if race:
        opts = {"strength": "str_mod",
                "dexterity": "dex_mod",
                "wisdom": "wis_mod",
                "intelligence": "int_mod",
                "charisma": "cha_mod",
                "constitution": "con_mod"}
    else:
        opts = {"strength": "strength",
                "dexterity": "dexterity",
                "wisdom": "wisdom",
                "intelligence": "intelligence",
                "charisma": "charisma",
                "constitution": "constitution"}
    return opts[input]


def ability_score_increase(chr, race=False):
    """
    the functionality for levelling up: gets called to level up/increase an ability score. only functionality for finding out stat and value.
    :param chr: character object to manipulate
    :return: nothing
    """
    choice = input(
        "Level Up: do you want to level up 'one' ability score by two points, or 'two' scores by one each?\n")
    while True:
        six_to_string(chr, race)
        if choice == "one":
            stat = input("Which ability do you want to increase by two points? They're listed above\n")
            if is_valid_input(stat):
                alter_stat(chr, chr_race_mod(stat, race), 2, True)
                break
            else:
                print("I don't understand that. Please enter a correct skill")
        elif choice == "two":
            first = input("Which ability do you want to increase by one point?\n")
            alter_stat(chr, chr_race_mod(first, race), 1)
            second = input("Which other score do you want to increase by one point?\n")
            alter_stat(chr, chr_race_mod(second, race), 1)
            break
        else:
            print("I don't understand that. Please enter 'one' or 'two' next time!\n")
            choice = input("Level Up: do you want to level up 'one' ability score by two points, or 'two' scores by one each?\n")


def alter_stat(chr, stat, chg, valid=False):
    """
    used for updating/leveling up. functionality for increasing any abiltiy score by a given amount
    :param chr: character object with scores to be modified
    :param stat: the string stat to be changed
    :param chg: the integer amount the stat is to be changed by
    :return: True in the case of a success, string response in the case of failure
    """
    if valid or is_valid_input(stat):
        old = getattr(chr, stat)
        setattr(chr, stat, old + chg)
        new = getattr(chr, stat)
        if old != new:
            return True
        return "ERROR - did not update - contact admin"
    return False


def set_prof(chr, opts):
    """
    sets character proficiencies (not skill proficiencies) based on list of options given
    :param opts: list of list of profs available to the character
    """
    flag = True
    while flag:
        try:
            avail = set(opts) - set(chr.proficiencies)
            print("Which do you want to be proficient in? Options are listed below")
            for item in avail:
                print(item)
            choice = input("")
            assert choice in avail, "That wasn't an option"
            chr.proficiencies.append(choice)
            flag = False
        except AssertionError:
            pass


def set_skills(chr, opts):
    flag = True
    while flag:
        try:
            if isinstance(opts, list):
                avail = set(opts) - set(chr.skills)
                print("Which skill do you want to be proficient in? Options are listed below")
                for item in avail:
                    print(item)
                ch = input("")
            else:
                ch = opts
                avail = ch
            if is_valid_input(ch, valid_skills()) and is_valid_input(ch, avail):
                chr.skills.append(ch)
            flag = False
        except AssertionError:
            pass


def get_modifier(chr, stat):
    """
    gets the ability score modifier for a score passed in
    :param self: the object passed in - necessary because function is abstracted
    :param stat: the string of the stat wanted to get the mod of
    :return: the int of the modifier: +/- x
    """
    if is_valid_input(stat):
        base = getattr(chr, stat)
        print(base)
        return int(math.floor(base - 10) / 2)
    return -300


def search_dict(value):
    """
    function that searches through the dictionary. does not do functionality for the search loop
    :param value: the word or phrase to be searched
    :return: the string of the definition, or the string of an error, in that case
    """
    comp = dict((k.lower(), v.lower()) for k, v in dictionary.dictionary.items())
    try:
        result = comp[value]
        response = "\n" + value + ": "
        line = ""
        for word in result.split():
            line += word + " "
            if len(line) > 120:
                response += "\n" + line
                line = ""
        return response
    except KeyError:
        return value + " was not found"


def search_spell_dict(spell):
    """
    function that searches through the spell dictionary, parses the spell response, does not do functionality for search loop.
    :param spell: spell name to be searched for
    :return: the string response.
    """
    comp = dict((k.lower(), v) for k, v in spell_dict.spells.items())
    try:
        response = "\n" + spell + ": "
        result = comp[spell.lower()]
        for item in result:
            for k in item:
                response += "\n" + k + ": " + item[k]
        return response
    except KeyError:
        return spell + " was not found"


def equip(chr, items):
    """
    equips an item or an array of items to the character's weapons and equipment.
    :param chr: character object to have things equipped to
    :param items: the array of item or items to equip to equipment & weapons
    :return: nothing
    """
    for obj in items:
        chr.weapons.append(obj)
        chr.equipment.append(obj)


def append_proficiencies(chr, profs):
    for item in profs:
        chr.proficiencies.append(item)


def count_spells(chr):
    """
    returns the total amount of spells a character knows.
    :param chr: the character object to learn about
    :return: the total amount of spells they know
    """
    if chr.spells:
        count = 0
        for level in chr.spells:
            count += level[0]
        return count
    return 0


def init_scores(chr):
    flag = True
    scores = []
    choices = ["strength", "dexterity", "wisdom", "intelligence", "charisma", "constitution"]
    chr_choices = []
    assigned = 0
    choice = input("Do you want to 'roll' your scores, or use the 'basic' preset scores?")
    if choice.lower() == "roll":
        while flag:
            while assigned < 6:
                d1 = r.randint(1, 6)
                d2 = r.randint(1, 6)
                d3 = r.randint(1, 6)
                d4 = r.randint(1, 6)
                end = (d1 + d2 + d3 + d4) - min(d1, d2, d3, d4)
                scores.append(int(end))
                assigned += 1
            if sum(scores) >= 70:
                flag = False
            else:
                scores = []
                assigned = 0
                print("BUG")
                print("\n\n\n\n")
    else:
        scores = [15, 14, 13, 12, 10, 8]
    while 0 <= len(chr_choices) < 6:
        chr_score = ""
        pennant = False
        plinth = False
        while not pennant:
            # each loop of assignment. either do score_num or score -> num
            print("below are the scores you have left to assign")
            for item in choices:
                print(item)
            print("below are the remaining scores:")
            for item in scores:
                print(item)
            chr_score = input("Which score do you want to assign? please input from list above\n")
            plinth = is_one_string(chr_score)
            pennant = is_valid_input(chr_score, choices, scores)
        flag = False
        if plinth:
            while not flag:
                flag = set_two_score(chr, chr_score)
                # print("You can't assign that to " + chr_score.strip().split()[0])
            choices.remove(chr_score.strip().split()[0])
            scores.remove(int(chr_score.strip().split()[1]))
            chr_choices.append(chr_score.strip().split()[0])
        else:
            while not flag:
                flag = set_one_score(chr, chr_score, scores)
                # if flag:
                #   print("You can't assign that to " + chr_score)
            choices.remove(chr_score)
            chr_choices.append(chr_score)
            scores.remove(getattr(chr, chr_score))
        print("hit me")
        if len(choices) < 2:
            setattr(chr, choices[0], scores[0])
            print(choices[0] + " was assigned: " + str(scores[0]))
            print("\n")
            break


def is_valid_input(arg, choices=None, scores=None):
    if not choices:
        choices = ["strength", "dexterity", "wisdom", "intelligence", "charisma", "constitution", "hp"]
    try:
        if is_one_string(arg):
            choice = arg.strip().split()[0]
            score = int(arg.strip().split()[1])
            assert choice in choices
            assert score in scores
            return True
        else:
            assert arg in choices
            return True
    except AssertionError:
        return False


def is_one_string(arg):
    """
    sees if the input is the score & num in one string or not
    :param arg:
    :return: bool - true if it is, false else
    """
    try:
        int(arg.strip().split()[1])
        return True
    except (ValueError, IndexError):
        return False


def set_two_score(chr, sng):
    try:
        ability = sng.strip().split()[0]
        score = sng.strip().split()[1]
        old = getattr(chr, ability)
        setattr(chr, ability, score)
        new = getattr(chr, ability)
        return True if new != old else False
    except AssertionError:
        return False


def set_one_score(chr, sng, scores):
    try:
        old = getattr(chr, sng)
        for item in scores:
            print(item)
        play_choice = input("Which score do you want to assign to " + sng)
        assert int(play_choice) in scores, print(play_choice + " isn't in the list you're allowed to use.")
        setattr(chr, sng, int(play_choice))
        new = getattr(chr, sng)
        return True if new != old else False
    except AssertionError:
        return False


def transfer_languages(chr, languages=None, race=False, clas=False, transfer=False):
    one = False
    if isinstance(languages, str):
        add_language(chr, languages)
        one = True
    if not one:
        if race:
            for item in languages:
                add_language(chr, item)
        elif clas:
            for item in languages:
                add_language(chr, item)
        elif transfer:
            try:
                for item in chr.race.languages:
                        add_language(chr, item)
            except AttributeError:
                pass
            try:
                for item in chr.clas.languages:
                        add_language(chr, item)
            except AttributeError:
                pass


def add_language(chr, item):
    if item not in chr.languages:
        chr.languages.append(item)


def combat_to_string(chr):
    # armor, weapons, equipment
    pass


def magic_to_string(chr):
    # cantrips, spells, spell dc, spell saving throw
    try:
        cantrips = "cantrips known: "
        for item in chr.fin_magic[0][1]:
            cantrips += "\n" + item
        i = 0
        print(cantrips)
        spells = ""
        for spell in chr.fin_magic[1:]:
            for item in spell:
                if isinstance(item, list):
                    place = "Spells level " + str(i+1) + ": \t"
                    spells += place
                    for thing in item:
                        spells = spells + str(thing) + " "
                    spells += "\n"
                    i += 1
        if spells == "":
            spells = "No known spells"
        print(spells)
        spell_dc = "Spell DC: " + chr.magic_dc
        spell_throw = "Spell Throw: " + chr.magic_throw
        output = [spell_dc, spell_throw]
        for item in output:
            print(item)
    except AttributeError:
        print("hit error")


def score_to_string(chr):
    # level, str->cha, hit dice, max hp, speed, swim speed, fly speed
    level = "level: \t" + str(chr.level)
    strength = "strength: \t" + str(chr.strength)
    dexterity = "dexterity: \t" + str(chr.dexterity)
    wisdom = "wisdom: \t" + str(chr.wisdom)
    intelligence = "intelligence: \t" + str(chr.intelligence)
    charisma = "charisma: \t" + str(chr.charisma)
    constitution = "constitution: \t" + str(chr.constitution)
    hit_dice = "hit dice: \t" + str(chr.clas.hit_dice)
    max_hp = "max hp: \t" + str(chr.hp)
    speed = "speed: \t" + str(chr.race.speed)
    swim_spd = "swimming speed: \t" + str(chr.race.swim_spd)
    fly_speed = "flying speed: \t" + str(chr.race.fly_spd)
    output = [level, strength, dexterity, wisdom, intelligence, charisma, constitution, hit_dice, max_hp, speed, swim_spd, fly_speed]
    for item in output:
        print(item)


def six_to_string(chr, race=False):
    if race:
        strength = "strength mod: \t" + str(chr.str_mod)
        dexterity = "dexterity mod: \t" + str(chr.dex_mod)
        wisdom = "wisdom mod: \t" + str(chr.wis_mod)
        intelligence = "intelligence mod: \t" + str(chr.int_mod)
        charisma = "charisma mod: \t" + str(chr.cha_mod)
        constitution = "constitution mod: \t" + str(chr.con_mod)
    else:
        strength = "strength: \t" + str(chr.strength)
        dexterity = "dexterity: \t" + str(chr.dexterity)
        wisdom = "wisdom: \t" + str(chr.wisdom)
        intelligence = "intelligence: \t" + str(chr.intelligence)
        charisma = "charisma: \t" + str(chr.charisma)
        constitution = "constitution: \t" + str(chr.constitution)
    output = [strength, dexterity, wisdom, intelligence, charisma, constitution]
    for item in output:
        print(item)


def feature_to_string(chr):
    # skills, features, saving throws, languages, proficiencies, feats, resistances, disadvantages, advantages
    skills = "skills: "
    for item in chr.fin_skills:
        skills += "\n" + item
    features = "features: "
    for item in chr.fin_features:
        features += "\n" + item
    saving_throws = "saving throws: "
    for item in chr.clas.saving_throws:
        saving_throws += "\n" + item
    languages = "languages known: "
    transfer_languages(chr, None, False, False, True)
    for item in chr.languages:
        languages += "\n" + item
    proficiencies = "proficient in: "
    for item in chr.fin_profs:
        proficiencies += "\n" + item
    feats = "feats known: "
    for item in chr.fin_feats:
        feats += "\n" + item
    resis = "resistant to: "
    for item in chr.clas.resistances:
        resis += "\n" + item
    dis = "has permanent disadvantage to: "
    for item in chr.clas.disadvantages:
        dis += "\n" + item
    adv = "has permanent advantage to: "
    for item in chr.clas.advantages:
        adv += "\n" + item
    output = [skills, features, saving_throws, languages, proficiencies, feats, resis, dis, adv]
    for item in output:
        print(item + "\n")


# NEED TRANSFER/ADD ITEM FOR RACE -> CHR <- CLASS


def special_to_string(chr):
    # class/race specific: color for dragonborn
    output = []
    if chr.race_name == "dragonborn":
        output.append("color: \t" + chr.race.color)
    for item in output:
        print(item)


def character_to_string(chr):
    # name, play_name, age, sex, gender, height, weight, race, subrace, class, archetype, background, personality trait,
    # ideal, flaw, bond, alignment
    name = "name: \t" + chr.name
    play_name = "player name: \t" + chr.player_name
    gender = "gender: \t" + chr.gender
    sex = "sex: \t" + chr.sex
    age = "age: \t" + str(chr.race.age)
    weight = "weight: \t" + str(chr.race.weight) + " lbs"
    height = "height: \t" + str(chr.race.height) + " inches"
    race = "race: \t" + str(chr.race_name)
    subrace = "subrace: \t" + chr.race.subrace
    clas = "class: \t" + chr.class_name
    archetype = "archetype: \t" + chr.clas.archetype
    background = "background: \t" + chr.background
    personality = "personality: \t" + chr.personality
    trait = "trait: \t" + chr.trait
    ideal = "ideal: \t" + chr.ideals
    flaw = "flaw: \t" + chr.flaws
    bond = "bond: \t" + chr.bonds
    alignment = "alignment: \t" + chr.alignment

    output = [name, play_name, gender, sex, age, weight, height, race, subrace, clas, archetype, background, personality, trait, ideal, flaw, bond, alignment]
    for item in output:
        print(item)
