import utils.utils as utilities
from Character import Character


def main():
    while True:
        command = input("what do you want to do? 'create' character, 'search feature' for any feature or proficiency, "
                        "'search spell' for any spell, 'help', or 'exit'? \n")
        command = command.strip()
        if command == "create":
            print("Creation of Character")
            level = 10
            flag = False
            while not flag:
                level = input("What level is your character?\n")
                try:
                    level = int(level)
                    if level > 20:
                        print("Your level can't be above 20. Try again.")
                    if level < 1:
                        print("Your level can't be lower than 1. Try again.")
                    flag = True
                except (TypeError, ValueError):
                    print("Please enter a number")
            chr = Character(int(level))
            chr.set_personality()
            chr.set_alignment()
            chr.set_background()
            chr.set_race()
            chr.set_class()
            chr.trigger_end()
            # above to get all features, equip, etc from race and class to character. otherwise not accessible.
            utilities.combat_to_string(chr)
            utilities.score_to_string(chr)
            utilities.character_to_string(chr)
            utilities.special_to_string(chr)
            utilities.feature_to_string(chr)
            utilities.magic_to_string(chr)
        elif command == "help":
            print("Type in: "
                  "\ncreate: \tcreate a new character"
                  "\nsearch feature: \tsearch for any feature, skill, or proficiency."
                  "\nsearch spell: \t search for any spell."
                  "\nhelp: \t\tdisplay this menu"
                  "\nexit: \t\texit the program")

        elif command == "search feature":
            flag = True
            while flag:
                print("This will allow you to search for any feature (for now). \n"
                      "Please type in the word or phrase you are searching for.\n"
                      "Type 'exit' to exit searching")
                word = input("What feature are you looking for?\n")
                srch = word.strip().lower()
                if srch == "exit":
                    flag = False
                print(utilities.search_dict(srch))
                print("\n")

        elif command == "search spell":
            flag = True
            while flag:
                print("This will allow you to search any spell.\n"
                      "Please enter the spell you're looking for.\n"
                      "Type 'exit' to exit the search function")
                word = input("What spell are you looking for?\n")
                srch = word.strip().lower()
                if srch == "exit":
                    flag = False
                print(utilities.search_spell_dict(srch))
                print("\n")

        elif command == "exit":
            print("thank you!")
            break

        else:
            print(command + " is not recognized as a command. please try again!")


if __name__ == '__main__':
    main()

