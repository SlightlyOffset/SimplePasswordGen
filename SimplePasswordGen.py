'''
Simple Password Generator:
    Create a program that generates random passwords of a specified length, with options for including uppercase letters, lowercase letters, numbers, and symbols.
'''

import string as st
import secrets as sc

def main():
    def genpass(length, include):
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
            print("\nError: Cannot choose from an empty sequence.")
            input("\nPress 'Enter' to return to menu.")
            return
        
        print("\n--- Password Generated ---")
        
        print("")
        print(f" --{'-' * (10 + length)}-- ")
        print(f"|  Password: {password}  |")
        print(f" --{'-' * (10 + length)}-- ")
        
        input("\nPress 'Enter' to return to menu...")
        print("\n\n")
        return
            
    def get_valid_yes_no(prompt):
        while True:
            response = input(prompt).strip().lower()
            if response in ["y", "n"]:
                return response
            else:
                print("\nError: Please enter only 'y' or 'n'")
        
    def get_valid_length(prompt):
        while True:
            try:
                length = int(input(prompt))
                if length > 0:
                    return length
                else:
                    print("\nError: Password length must be a positive integer.")
            except ValueError:
                print("\nError: Invalid input. Please enter a number.")
    
    def menu():
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
                
                warn_flag = False
                no_counter = 0
                for inclusion in include_list:
                    if inclusion == "n":
                        no_counter += 1
                    
                if no_counter == 4:     # All options is not selected --> Error
                    warn_flag = True
                    
                print("")
                print("","-" * 30)
                print(f"| Random pool will include: {'':<3}|")
                print(f"| Uppercase Characters: {'yes' if uppercase == 'y' else 'no':<7}|")
                print(f"| Lowercase Characters: {'yes' if lowercase == 'y' else 'no':<7}|")
                print(f"| Number Characters: {'yes' if number == 'y' else 'no':<10}|")
                print(f"| Punctuation Characters: {'yes' if punctuation == 'y' else 'no':<5}|")
                print("","-" * 30)
                
                print("")
                print(f" --{'-' * (17 + len(str(length)))}-- ")
                print(f"|  Password length: {length}  |")
                print(f" --{'-' * (17 + len(str(length)))}-- ")
                
                print("WARNING: All options is deselected. Proceeding will result in an error.") if warn_flag else print("")
                
                while True:
                    confirm = input("\nContinue with selected options? (Y/n): ").lower().strip()
                    if confirm in ["y", ""]:
                        password = genpass(length, include_list)
                        break
                    elif confirm == "n":
                        print("\nReloading...")
                        break
                    else:
                        print("\nError: Accept only 'y' and 'n' input.\n")
                    
            elif begin.strip().lower() == "n":
                print("\nExiting...")
                return
            
            else:
                print("\nError: Accept only 'y' and 'n' input.\n")
                
    menu()
    
if __name__ == "__main__":
    main()
