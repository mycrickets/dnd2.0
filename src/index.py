import src.utils.utils as utilities
import src.Character as character
import random as r


def main():

    while True:
        command = input("what do you want to do? 'create' character, 'search feature' for any feature or proficiency, "
                        "'search spell' for any spell, 'help', or 'exit'? \n")
        command = command.strip()
        if command == "create":
            print("creation of character")
            chr = character.Character(5)
            chr.set_race()
            chr.set_class()
            utilities.score_to_string(chr)
            utilities.character_to_string(chr)
            utilities.special_to_string(chr)
            utilities.feature_to_string(chr)
            utilities.magic_to_string(chr)

            # chr.to_string()
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

