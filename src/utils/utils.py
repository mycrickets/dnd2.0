import math
import random as r
import utils.dictionary as dictionary
import utils.spell_dict as spell_dict
from utils.background_dict import backgrounds


def valid_skills():
    return ["athletics", "acrobatics", "sleight of hand", "stealth", "arcana", "history", "investigation", "nature",
            "religion", "animal handling", "insight", "medicine", "perception", "survival", "deception", "intimidation",
            "performance", "persuasion"]


def chr_race_mod(input, race=False):
    try:
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
    except KeyError:
        return input


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
                alter_stat(chr, chr_race_mod(stat, race), 2, race)
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
    used for updating/leveling up. functionality for increasing any ability score by a given amount
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


def set_skills(chr, amt, opts):
    for i in range(0, int(amt)):
        flag = True
        ch = ""
        while flag:
            try:
                if isinstance(opts, list):
                    avail = set(opts) - set(chr.skills)
                    print("Which skill do you want to be proficient in? Options are listed below")
                    print("Choice " + str(i+1) + "/" + str(amt))
                    for item in sorted(avail):
                        print(item)
                    ch = input("")
                else:
                    ch = opts
                    avail = ch
                if is_valid_input(ch, valid_skills()) and is_valid_input(ch, avail):
                    chr.skills.append(ch)
                    flag = False
                else:
                    print(ch + " is already accounted for, or not on the allowed list. Try again.")
            except AssertionError:
                print(ch + " is already accounted for, or not on the allowed list. Try again.")


def get_modifier(chr, stat, clas=False):
    """
    gets the ability score modifier for a score passed in
    :param self: the object passed in - necessary because function is abstracted
    :param stat: the string of the stat wanted to get the mod of
    :return: the int of the modifier: +/- x
    """
    valid = False
    if clas:
        stat = chr_race_mod(stat, True)
        valid = True
    if is_valid_input(stat) or valid:
        base = getattr(chr, stat)
        return int(math.floor(base - 10) / 2)
    return None


def transfer_background_to_race(chr, race):
    bg = chr.background
    for addition in backgrounds.get(bg):
        response = backgrounds.get(bg).get(addition)
        response = response.strip()
        addition = addition.strip()
        if addition == "Skill Proficiencies":
            if is_substring(["choose", "Choose", "type of", "Type of", "from among"], response):
                response = get_skills_from_trigger_skill(response)
            else:
                response = response.strip().lower().split(",")
            for item in response:
                if item not in race.skills:
                    race.skills.append(item)
        elif addition == "Tool Proficiencies":
            if is_splittable(response) or is_substring(["choose", "Choose", "type of", "Type of", "from among", "choice"], response):
                tools = get_tools(response)
                race.proficiencies.extend(tools)
            else:
                race.proficiencies.append(response.strip().lower())
        elif addition == "Equipment":
            items = response.split(",")
            for piece in items:
                if is_substring(["choose", "Choose", "type of", "Type of", "from among", "choice"], piece):
                    race.equipment.append(get_equipment_from_trigger_eqp(piece))
                else:
                    race.equipment.append(piece.strip().lower())
        elif addition == "Feature":
            race.features.append(response.strip().lower())
        elif addition == "Language":
            race.languages.append(response.strip().lower())
        elif addition == "Languages":
            if "and" in response:
                lgs = response.split("and")
                for i in range(0, len(lgs)):
                    lgs[i] = lgs[i].lower().strip()
            else:
                lgs = get_lgs(response, race)
            for item in lgs:
                race.languages.append(item)
        else:
            print(addition)
    pass


def is_substring(substrings, string):
    for item in substrings:
        if item in string:
            return True
    return False


def is_splittable(response):
    try:
        if len(response.split(",")) == 1:
            if len(response.split("and")) > 1:
                return True
            if len(response.split("or")) > 1:
                return True
            return False
    except ValueError:
        return False
    return True


def get_tools(response):
    tools = []
    if is_substring(["choose", "Choose", "type of", "Type of", "from among", "or"], response):
        items = response.split(",")
        for question in items:
            if not is_substring(["choose", "Choose", "type of", "Type of", "from among", "or"], question):
                tools.append(question.lower().strip())
            else:
                if "or" in question:
                    ch = question.split("or")
                    for i in range(0, len(ch)):
                        ch[i] = ch[i].strip("Your choice of ")
                    for boy in ch:
                        print(boy)
                    tools.append(input("Which tool proficiency do you want? They're listed above\n"))
                else:
                    ct = question.lower().strip().split()[:1]
                    if ct[0] == "one":
                        ct = 1
                    elif ct[0] == "two":
                        ct = 2
                    else:
                        ct = 1
                    for i in range(0, ct):
                        yo = question.lower().strip().split()[1:]
                        sh = ""
                        for item in yo:
                            sh += item + " "
                        if "and" in sh:
                            each = sh.split(" and ")
                            for item in each:
                                print("What " + item.strip() + " do you want to be proficient in?")
                                tools.append(input(""))
                        else:
                            print(str(i + 1) + "/" + str(ct))
                            print("What " + sh.strip() + " do you want to be proficient in?")
                            tools.append(input(""))
    else:
        if "and" in response:
            each = response.split(" and ")
            for i in range(0, len(each)):
                each[i] = each[i].strip().lower()
            tools = each
        else:
            for item in response.split(","):
                tools.append(item.lower().strip())
    return tools


def get_lgs(response, race):
    results = []
    response = response.strip().lower()
    if "or" in response:
        check = response.split()[:1]
        if check not in race.languages:
            race.languages.append(check)
        else:
            for i in range(0, 1):
                print(str(i + 1) + "/" + str(1))
                results.append(input("Background Initialization: What language do you want to learn?\n"))
    else:
        ct = response.split()[:1]
        if ct == "one" or ct == "any":
            ct = 1
        else:
            ct = 2
        for i in range(0, ct):
            print(str(i+1) + "/" + str(ct))
            results.append(input("Background Initialization: What language do you want to learn?\n"))
    return results


def get_equipment_from_trigger_eqp(response):
    response = response.strip()
    amt = response.split(" ")
    ct = -1
    for item in amt:
        if item == "(":
            amt = amt.remove(amt.index(item))
    for item in amt:
        if item == ")":
            amt = amt.remove(amt.index(item))
    indices = [i for i, x in enumerate(amt) if x == "of"]
    for item in indices:
        if amt[item] == "of" and amt[item+1] == "your":
            ct = amt[item-1]
    ct = ct.replace("(", "]").replace(")", "]").split("]")
    ct = "".join(ct)
    if ct == "one":
        ct = 1
    else:
        ct = 2
    choices = response.split("or")
    fin = []
    for item in choices:
        spt = list(item)
        index = len(item)
        for charr in spt:
            if charr == "(":
                index = spt.index(charr)
        fin.append(item[:index])
    for i in range(0, len(fin)):
        fin[i] = fin[i].strip().lower()
    flag = True
    while flag:
        print("Which piece of equipment or type of equipment do you want?")
        for item in fin:
            print(item)
        ch = input("")
        return ch


def get_skills_from_trigger_skill(response):
    results = []
    split = response.split(",")
    flag = False
    i = 0
    while not flag:
        selection = split[i]
        i += 1
        if "from among" in selection:
            hit = split[split.index(selection):]
            rst = []
            choices = []
            for item in hit:
                rst.extend(item.split(" "))
            index = -1
            for item in rst:
                if item == "":
                    rst.remove(item)
            for item in rst:
                if item.lower() in valid_skills():
                    choices.append(item.lower())
                if item == "from":
                    index = rst.index(item)
            ct = rst[index-1]
            if ct == "one":
                ct = 1
            elif ct == "two":
                ct = 2
            else:
                print(ct, " huh")
            fin = get_from_list(choices, int(ct), "background skill")
            results.extend(fin)
            flag = True
        else:
            results.append(selection.lower())
            if i == 2:
                flag = True
    return results


def get_from_list(list, amt, desc=None):
    addition = " "
    if desc:
        addition += desc + " "
    results = []
    for i in range(0, int(amt)):
        flag = True
        ch = ""
        j = 1
        while flag:
            try:
                if amt >= j:
                    print("Which" + addition + "do you want to have?")
                    if amt > 1:
                        print(str(j) + "/" + str(amt))
                    for item in sorted(set(list)-set(results)):
                        print(item)
                    ch = input("")
                    if is_valid_input(ch, list) or is_valid_input(ch.capitalize(), list):
                        if amt >= j:
                            j += 1
                            results.append(ch.strip())
                        else:
                            return ch
                    else:
                        assert 1 == 2
                else:
                    if len(results) == 1:
                        return results[0]
                    return results
            except AssertionError:
                print(ch + " isn't in the list")

    if len(results) == 1:
        return results[0]
    return results


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
    chr.weapons.append(items)
    chr.equipment.append(items)


def append_proficiencies(chr, profs):
    for item in profs:
        chr.proficiencies.append(item)


def append_features(chr, features):
    for item in features:
        chr.features.append(item)


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
    choice = input("Do you want to 'roll' your scores, or use the 'basic' preset scores?\n")
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
                print("\n\n\n\n")
                print("BUG at utils line 262")
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
            choices.remove(chr_score.strip().split()[0])
            scores.remove(int(chr_score.strip().split()[1]))
            chr_choices.append(chr_score.strip().split()[0])
        else:
            while not flag:
                flag = set_one_score(chr, chr_score, scores)
            choices.remove(chr_score)
            chr_choices.append(chr_score)
            scores.remove(getattr(chr, chr_score))
        if len(choices) < 2:
            setattr(chr, choices[0], int(scores[0]))
            print(choices[0] + " was assigned: " + str(scores[0]))
            print("\n")
            break


def is_valid_input(arg, choices=None, scores=None, case_sensitive=False):
    if not choices:
        choices = ["strength", "dexterity", "wisdom", "intelligence", "charisma", "constitution", "hp"]
    try:
        if is_one_string(arg):
            choice = arg.strip().split()[0]
            score = int(arg.strip().split()[1])
            if not case_sensitive:
                assert choice in choices
            else:
                assert choice in choices or choice.capitalize() in choices or choice.lower() in choices
            assert score in scores
            return True
        else:
            if not case_sensitive:
                assert arg in choices
            else:
                assert arg in choices or arg.capitalize() in choices or arg.lower() in choices
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
        setattr(chr, ability, int(score))
        new = getattr(chr, ability)
        return True if new != old else False
    except AssertionError:
        return False


def set_one_score(chr, sng, scores):
    try:
        old = getattr(chr, sng)
        for item in scores:
            print(item)
        play_choice = input("Which score do you want to assign to " + sng + "?\n")
        assert int(play_choice) in scores, print(str(play_choice) + " isn't in the list you're allowed to use.")
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
    if chr.fin_armor:
        if isinstance(chr.fin_armor, list):
            chr.fin_equip.append(chr.fin_armor)
            chr.fin_armor = chr.fin_armor[0]
        armor = "armor: " + chr.fin_armor[0]
        dc = "armor DC: " + str(chr.fin_armor[1])
    else:
        armor = "armor: No Armor"
        dc = str(10 + get_modifier(chr, "dexterity"))
    weapons = "weapons: "
    for item in chr.fin_weapons:
        weapons += "\n\t" + item.capitalize()
    attack = "attacks: "
    for item in chr.fin_attacks:
        attack += "\n\t" + item.capitalize()
    equipment = "equipment: "
    for item in chr.fin_equip:
        if isinstance(item, str):
            equipment += "\n\t" + item.strip().capitalize()
        elif isinstance(item, list):
            for it in item:
                equipment += "\n\t" + it.strip().capitalize()
    output = [armor, dc, weapons, attack, equipment]
    for item in output:
        print(item + "\n")


def magic_to_string(chr):
    # cantrips, spells, spell dc, spell saving throw
    try:
        cantrips = "cantrips known: "
        for item in chr.fin_magic[0][1]:
            cantrips += "\n\t" + str(item)
        i = 0
        print(cantrips)
        spells = ""
        for spell in chr.fin_magic[1:]:
            place = "Spells level " + str(i + 1) + ": \t\n"
            spells += place
            for item in spell[1]:
                spells += "\t" + item + "\n"
            i += 1
        if spells == "":
            spells = "No known spells"
        print(spells)
        spell_dc = "Spell DC: " + str(chr.fin_dc)
        spell_throw = "Spell Throw: " + chr.fin_throw
        output = [spell_dc, spell_throw]
        for item in output:
            print(item)
    except (AttributeError, IndexError):
        pass


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
    try:
        fly_speed = "flying speed: \t" + str(chr.race.fly_spd) + str(chr.clas.fly_speed)
    except AttributeError:
        try:
            fly_speed = "flying speed: \t" + str(chr.race.fly_spd)
        except AttributeError:
            try:
                fly_speed = "flying speed: \t" + str(chr.clas.fly_spd)
            except AttributeError:
                fly_speed = "flying speed: 0"

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
    skil_dict = {
        'strength': ["athletics"],
        'dexterity': ["acrobatics", "sleight of hand", "stealth"],
        'intelligence': ["arcana", "history", "investigation", "nature", "religion"],
        'wisdom': ["animal handling", "insight", "medicine", "perception", "survival"],
        'charisma': ["deception", "intimidation", "performance", "persuasion"],
        'constitution': []
    }
    skills = "skills: "
    for item in valid_skills():
        mod = 0
        if item in chr.fin_skills:
            print("item in fin skills")
            mod += int(chr.clas.prof_bonus)
            if chr.expert_skills:
                mod += int(chr.clas.prof_bonus)
        for yo in skil_dict:
            for v in skil_dict.get(yo):
                if item in v:
                    mod += int(get_modifier(chr, yo))
        skills += "\n\t" + item.strip().capitalize() + " + " + str(mod)
    features = "features: "
    for item in chr.fin_features:
        features += "\n\t" + str(item)
    saving_throws = "saving throws: "
    for item in chr.clas.saving_throws:
        saving_throws += "\n\t" + item
    languages = "languages known: "
    transfer_languages(chr, None, False, False, True)
    for item in chr.languages:
        languages += "\n\t" + item
    proficiencies = "proficient in: "
    for item in chr.fin_profs:
        proficiencies += "\n\t" + item
    feats = "feats known: "
    for item in chr.fin_feats:
        feats += "\n\t" + item
    resis = "resistant to: "
    for item in chr.fin_resis:
        resis += "\n\t" + item
    dis = "has permanent disadvantage to: "
    for item in chr.fin_dis:
        dis += "\n\t" + item
    adv = "has permanent advantage to: "
    for item in chr.fin_adv:
        adv += "\n\t" + item
    output = [skills, features, saving_throws, languages, proficiencies, feats, resis, dis, adv]
    for item in output:
        print(item + "\n")


def special_to_string(chr):
    # class/race specific: color for dragonborn
    output = []
    race = chr.race_name
    classs = chr.class_name
    if race == "dragonborn":
        color = "color: \t" + chr.race.color
        output.append(color)
    if classs == "Barbarian":
        rage_ct = "Rage Count: \t" + str(chr.clas.rage_ct)
        rage_dmg = "Rage Damage: \t" + str(chr.clas.rage_dmg)
        output.extend([rage_ct, rage_dmg])
    if classs == "Cleric":
        divine = "Divine Spell Count: " + str(chr.clas.divine_ct)
        output.extend([divine])
    if classs == "Fighter":
        maneuvers = "Maneuvers: "
        for item in chr.clas.maneuvers:
            maneuvers += "\n\t" + item
        ct = "Superior Dice Count: " + str(chr.clas.sup_dice_ct)
        dice = "Superior Dice Damage: " + str(chr.clas.sup_dice)
        output.extend([maneuvers, ct, dice])
    if classs == "Monk":
        features = "Ki Features: "
        for item in chr.clas.ki_features:
            features += "\n\t" + item
        dc = "Ki DC: \t\t" + str(chr.clas.ki_dc)
        elfeats = "Elemental Features: "
        for item in chr.clas.elem_feat:
            elfeats += "\n\t" + item
        output.extend([features, dc, elfeats])
    if classs == "Rogue":
        output.extend(["Sneak Damage: " + chr.clas.sneak_dmg])
    if classs == "Sorcerer":
        metfeat = "Metamagic Features: "
        for item in chr.clas.metamagic_features:
            metfeat += "\n\t" + item
        color = "Color: " + chr.clas.color
        output.extend([metfeat, color])
    if classs == "Warlock":
        inv = "Invocations: "
        for item in chr.clas.invocations:
            inv += "\n\t" + item
        pact = "Warlock Pact: " + chr.clas.pact
        pact_desc = "Warlock Pact Description: " + chr.clas.pact_desc
        pact_desc = pact_desc.split(" ")
        sent = ""
        fin_desc = ""
        for item in pact_desc:
            sent += item
            if len(sent) > 40:
                fin_desc += sent + "\n"
        fin_desc += sent
        output.extend([inv, pact, fin_desc])
    if classs == "Wizard":
        spells = "Mastered Spells: "
        for item in chr.clas.spell_master:
            spells += "\n\t" + item
        sig = "Signature Spells: "
        for item in chr.clas.sig_spells:
            sig += "\n\t" + item
        output.extend([spells, sig])
    if classs == "Fighter" or classs == "Paladin" or classs == "Ranger":
        styles = "Styles: "
        for item in chr.clas.styles:
            styles += "\n\t" + item
        output.extend([styles])
    if classs == "Rogue" or classs == "Bard":
        exp = "Expertise Skills: "
        for item in chr.clas.expert_skills:
            exp += "\n\t" + item
        output.extend([exp])
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
    alignment = "alignment: \t" + chr.alignment.capitalize()

    output = [name, play_name, gender, sex, age, weight, height, race, subrace, clas, archetype, background, personality, trait, ideal, flaw, bond, alignment]
    for item in output:
        print(item)
