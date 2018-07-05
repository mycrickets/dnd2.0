import math
import src.utils.dictionary as dictionary
import src.utils.spell_dict as spell_dict


def ability_score_increase(chr):
    """
    the functionality for levelling up: gets called to level up/increase an ability score. only functionality for finding out stat and value.
    :param chr: character object to manipulate
    :return: nothing
    """
    choice = input("Level Up: do you want to level up 'one' ability score by two points, or 'two' scores by one each?\n")
    while True:
        for item in chr.stats:
            print(item)
        if choice == "one":
            stat = input("Which ability do you want to increase by two points? They're listed above\n")
            alter_stat(chr, stat, 2)
            break
        elif choice == "two":
            first = input("Which ability do you want to increase by one point?\n")
            alter_stat(chr, first, 1)
            second = input("Which other score do you want to increase by one point?\n")
            alter_stat(chr, second, 1)
            break
        else:
            print("I don't understand that. Please enter 'one' or 'two' next time!\n")


def alter_stat(chr, stat, chg):
    """
    used for updating/leveling up. functionality for increasing any abiltiy score by a given amount
    :param chr: character object with scores to be modified
    :param stat: the string stat to be changed
    :param chg: the integer amount the stat is to be changed by
    :return: True in the case of a success, string response in the case of failure
    """
    assert stat in ["charisma", "constitution", "dexterity", "intelligence", "strength", "wisdom"], "That's not an ability. Try again, please"
    old = chr.__getattribute__(stat)
    setattr(chr, stat, old + chg)
    new = chr.__getattribute__(chr, stat)
    if old != new:
        return True
    return "ERROR - did not update - contact admin"


def get_modifier(chr, stat):
    """
    gets the ability score modifier for a score passed in
    :param self: the object passed in - necessary because function is abstracted
    :param stat: the string of the stat wanted to get the mod of
    :return: the int of the modifier: +/- x
    """
    assert stat in ["charisma", "constitution", "dexterity", "intelligence", "strength", "wisdom"], "That's not an ability, please try again."
    base = chr.__getattribute__(stat)
    print(base)
    return int(math.floor(base - 10) / 2)


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


def count_spells(chr):
    """
    returns the total amount of spells a character knows.
    :param chr: the character object to learn about
    :return: the total amount of spells they know
    """
    count = 0
    for level in chr.spells:
        count += level[0]
    return count


def init_scores(chr, level):
    chr.strength = 10
    chr.dexterity = 10
    chr.intelligence = 10
    chr.wisdom = 10
    chr.charisma = 10
    chr.constitution = 10

