'''
Simple Password Generator Program
=================================

This is a terminal-based password generator that allows users to customize their
passwords by selecting whether to include uppercase letters, lowercase letters,
digits, and punctuation symbols. The program generates secure passwords using
Python's `secrets` module for cryptographically strong randomness.

Features:
---------
- Customizable character pool (uppercase, lowercase, digits, punctuation)
- User input validation with helpful prompts and error handling
- Visually formatted password output for readability
- Hybrid entropy-based password strength estimation (if 'entropy.py' is available)
- Graceful fallback when strength module is missing
- Emphasis on user security awareness and good password practices

Dependencies:
-------------
- Standard libraries: `string`, `secrets`
- Optional module: `entropy.py` (for password strength evaluation)

Security Notes:
---------------
- Passwords are NOT stored or logged.
- Users are warned not to save generated passwords in plain text files.
- Estimated strength does NOT reflect real-world resistance to all attack vectors.

---------
Author: SlightlyOffset
Version: 1.1.1-beta
Updated: 16 June 2025
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
    if include[0]: random_pool += st.ascii_uppercase
    if include[1]: random_pool += st.ascii_lowercase
    if include[2]: random_pool += st.digits
    if include[3]: random_pool += st.punctuation
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

    print("\nNOTE: The strength estimation did not reflect the real world strength against attacking attempts.")
    print("       User still need to practice cautions while using the password.")
    print("NOTE: All passwords generated should not be saved locally without encryption such as .txt or .csv.")

    input("\nPress 'Enter' to return to menu...")
    print("\nReturning to menu...")
    return

def main():
    def get_valid_yes_no(prompt):
        '''
        Function for prompting user with error handling(Input validation).

        Args:
            prompt (str): The message to display to the user.

        Returns:
            bool: True for yes (y/Enter), False for no (n)
 
        '''
        while True:
            response = input(prompt).strip().lower()
            if response in ["y", ""]:
                return True
            elif response in ["n"]:
                return False
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
            begin = get_valid_yes_no("\nBegin? (Y/n): ")

            if begin:
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
                    if not inclusion:
                        no_counter += 1

                if no_counter == 4:     # All options is not selected --> Error
                    warn_flag = True

                # Box formatted options display.
                print()
                print("","-" * 30)
                print(f"| Random pool will include: {'':<3}|")
                print(f"| Uppercase Characters: {'yes' if uppercase else 'no':<7}|")
                print(f"| Lowercase Characters: {'yes' if lowercase else 'no':<7}|")
                print(f"| Number Characters: {'yes' if number else 'no':<10}|")
                print(f"| Punctuation Characters: {'yes' if punctuation else 'no':<5}|")
                print("","-" * 30)

                # Box formatted password length display.
                print()
                print(f" --{'-' * (17 + len(str(length)))}-- ")
                print(f"|  Password length: {length}  |")
                print(f" --{'-' * (17 + len(str(length)))}-- ")

                # Display warning message if no options is selected.
                print("WARNING: All options is deselected. Proceeding will result in an error.") if warn_flag else print("")

                while True:
                    confirm = get_valid_yes_no("\nContinue with selected options? (Y/n): ")
                    if confirm:
                        genpass(length, include_list)
                        break
                    else:
                        print("\nReturning to menu...")
                        break

            else:
                print("\nExiting...")
                return

    menu()

if __name__ == "__main__":
    main()
