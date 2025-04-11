'''
Simple Password Generator:
    Create a program that generates random passwords of a specified length, with options for including uppercase letters, lowercase letters, numbers, and symbols.
'''

import string as st
import secrets as sc

def main():
    def genpass(length, include):
        print("genpass called")     # Debug
        
        character_types = [
        (st.ascii_uppercase, include[0]),
        (st.ascii_lowercase, include[1]),
        (st.digits, include[2]),
        (st.punctuation, include[3])
        ]
    
        random_pool = []
        for char_type, inclusion in character_types:
            if inclusion == "y":
                random_pool.append(char_type)
        
        print(f"Debug:\nalphabet pool: {random_pool}")  # Debug
        
        alphabet = "".join(random_pool)
        
        print(f"Debug:\nalphabet pool: {alphabet}")     # Debug
        
        password = "".join(sc.choice(alphabet) for times in range(length))
        print(f"Password: {password}")
        
        
    def menu():
        print("--- Password Generator ---")
        
        while True:
            begin = input("Begin? (Y/n): ")
            
            # Need error handling for this entire block
            if begin.strip().lower() == "y" or begin.strip().lower() == "":
                try:
                    length = int(input("Password length(Default = 8): "))
                except:
                    print("Error: Input is not a number. Will use 8 as befault value.")
                    length = 8
                
                include_list = []
                uppercase = input("\nInclude uppercase letters?(Y/n): ")
                if uppercase == "y" or uppercase == "n":
                    include_list.append(uppercase)
                else:
                    include_list.append("y")    # Use "y" as default
                lowercase = input("Include lowercase letters?(Y/n): ")
                if lowercase == "y" or lowercase == "n":
                    include_list.append(lowercase)
                else:
                    include_list.append("y")    # Use "y" as default
                number = input("Include number?(Y/n): ")
                if number == "y" or number == "n":
                    include_list.append(number)
                else:
                    include_list.append("y")    # Use "y" as default
                punctuation = input("Include punctuation?(Y/n): ")
                if punctuation == "y" or punctuation == "n":
                    include_list.append(punctuation)
                else:
                    include_list.append("y")    # Use "y" as default
                
                # Need better interface
                print("".join(include_list))
                print("All invalid input will be turnned to 'y' as default")
                
                print("calling genpass...")
                genpass(length, include_list)
            
            elif begin.strip().lower() == "n":
                print("\nExiting...")
                return
            
            else:
                print("\nError: Accept only 'y' and 'n' input.\n")
                
                
    menu()
    
if __name__ == "__main__":
    main()