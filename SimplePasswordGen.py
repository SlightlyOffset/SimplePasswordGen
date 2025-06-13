'''
Simple Password Generator Program
=================================

This program generate password based on user's options such as whether or not to include uppercase, lowercase, number, or punctuation.

---------
Author: SlightlyOffset
Version: 1.1
Update: 13 June 2025
---------
'''

import string as st
import secrets as sc
try:
    import entropy
    entropy_unavailable = False
except ModuleNotFoundError:
    entropy_unavailable = True
    print("WARNING: Module 'entropy.py' not found in directory.")
    print("         Password strength estimation will not work.\n")

def genpass(length, include):
    '''
    Function to perform password generation with user selected option with error handling for empty sequence(in case no option is selected)

    Args:
        length (int): The desired length of the password.
        include (list): A list of 'y' or 'n' indicating whether to include
                        uppercase, lowercase, numbers, and punctuation, respectively.

    Returns:
        str: The generated password.
    '''
    random_pool = ""
    if include[0] == "y":
        random_pool += st.ascii_uppercase
    if include[1] == "y":
        random_pool += st.ascii_lowercase
    if include[2] == "y":
        random_pool += st.digits
    if include[3] == "y":
        random_pool += st.punctuation
    try:
        password = "".join(sc.choice(random_pool) for _ in range(length))
    except IndexError:
        print("\nERROR: Cannot choose from an empty sequence.")
        input("\nPress 'Enter' to return to menu.")
        return

    print("\n--- Password Generated ---")

    # Box formatted password display.
    print()
    print(f" --{'-' * (10 + length)}-- ")
    print(f"|  Password: {password}  |")
    print(f" --{'-' * (10 + length)}-- ")

    if entropy_unavailable:
        password_strength = "Unavailable"
    else:
        password_strength = entropy.main(include, password)

    print()
    print(f" --{'-' * (20 + len(password_strength))}-- ")
    print(f"|  Estimated strength: {password_strength}  |")
    print(f" --{'-' * (20 + len(password_strength))}-- ")

    print("\nNOTE: All passwords generated should not be saved locally without encryption such as .txt or .csv.")

    input("\nPress 'Enter' to return to menu...")
    print("\nReloading...")
    return

def main():
    def get_valid_yes_no(prompt):
        '''
        Function for prompting user with error handling(Input validation).

        Args:
            prompt (str): The message to display to the user.

        Returns:
            str: The validated lowercase response ('y' or 'n').
        '''
        while True:
            response = input(prompt).strip().lower()
            if response in ["y", "n", ""]:
                if response == "":
                    response = "y"
                return response
            else:
                print("\nERROR: Please enter only 'y' or 'n'")

    def get_valid_length(prompt):
        '''
        Function for prompting password length from user with some error handling.

        Args:
            prompt (str): The message to display to the user.

        Returns:
            int: The validated positive integer length.
        '''
        while True:
            try:
                length = int(input(prompt))
                if length > 0:
                    return length
                else:
                    print("\nERROR: Password length must be a positive integer.")
            except ValueError:
                print("\nERROR: Invalid input. Please enter a number.")

    def menu():
        '''
        Display the main menu for Password Generator.

        Allow user to choose what and what not to include in the random pool for password generation and display before proceeding with user input(y/n)
        '''
        print("--- Password Generator ---")

        while True:
            begin = input("\nBegin? (Y/n): ")

            if begin.strip().lower() == "y" or begin.strip().lower() == "":
                print("\nPassword length is recommended to be 8 characters long or more.")
                length = get_valid_length("Password length: ")

                uppercase = get_valid_yes_no("\nInclude uppercase letters?(Y/n): ")
                lowercase = get_valid_yes_no("Include lowercase letters?(Y/n): ")
                number = get_valid_yes_no("Include number?(Y/n): ")
                punctuation = get_valid_yes_no("Include punctuation?(Y/n): ")

                include_list = [uppercase, lowercase, number, punctuation]

                # Raise warn flag if all options is not selected.
                warn_flag = False
                no_counter = 0
                for inclusion in include_list:
                    if inclusion == "n":
                        no_counter += 1

                if no_counter == 4:     # All options is not selected --> Error
                    warn_flag = True

                # Box formatted options display.
                print("")
                print("","-" * 30)
                print(f"| Random pool will include: {'':<3}|")
                print(f"| Uppercase Characters: {'yes' if uppercase == 'y' else 'no':<7}|")
                print(f"| Lowercase Characters: {'yes' if lowercase == 'y' else 'no':<7}|")
                print(f"| Number Characters: {'yes' if number == 'y' else 'no':<10}|")
                print(f"| Punctuation Characters: {'yes' if punctuation == 'y' else 'no':<5}|")
                print("","-" * 30)

                # Box formatted password length display.
                print("")
                print(f" --{'-' * (17 + len(str(length)))}-- ")
                print(f"|  Password length: {length}  |")
                print(f" --{'-' * (17 + len(str(length)))}-- ")

                # Display warning message if no options is selected.
                print("WARNING: All options is deselected. Proceeding will result in an error.") if warn_flag else print("")

                while True:
                    confirm = input("\nContinue with selected options? (Y/n): ").lower().strip()
                    if confirm in ["y", ""]:
                        genpass(length, include_list)
                        break
                    elif confirm == "n":
                        print("\nReturning to menu...")
                        break
                    else:
                        print("\nERROR: Accept only 'y' and 'n' input.\n")

            elif begin.strip().lower() == "n":
                print("\nExiting...")
                return

            else:
                print("\nERROR: Accept only 'y' and 'n' input.\n")

    menu()

if __name__ == "__main__":
    main()
