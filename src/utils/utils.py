import math
import src.utils.dictionary as dictionary


def ability_score_increase(chr):
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
    assert stat in ["charisma", "constitution", "dexterity", "intelligence", "strength", "wisdom"], "That's not an ability. Try again, please"
    old = getattr(chr, stat)
    setattr(chr, stat, old + chg)


def get_modifier(self, stat):
    assert stat in ["charisma", "constitution", "dexterity", "intelligence", "strength", "wisdom"], "That's not an ability, please try again."
    base = self.getattr(stat)
    return math.floor(base - 10) / 2


def search_dict(value):
    comp = dict((k.lower(), v.lower()) for k, v in dictionary.dictionary.items())

