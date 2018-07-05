import src.utils.utils as utilities
import src.Character as character


def main():
    while True:
        command = input("what do you want to do? 'create' character, 'search feature' for any feature or proficiency, "
                        "'search spell' for any spell, 'help', or 'exit'? \n")
        command = command.strip()
        if command == "create":
            print("creation of character")
            chr = character.Character(int(input("What level are you?")))
            chr.set_race()

            print(str(chr.race.size))

            '''print("Let's talk about some of your stats.")
            choice = input("Do you want to do a dice 'roll' for your stats, or the standard 'array'?")
            stats = []
            if choice == "roll":
                stats = roll_stats(chr)
            else:
                stats = [15, 14, 13, 12, 10, 8]'''

            '''chr.set_race()
            chr.set_class()
            chr.count_spells()'''

            # print(chr.to_string())

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
