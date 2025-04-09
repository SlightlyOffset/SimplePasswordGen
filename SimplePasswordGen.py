'''
Simple Password Generator:
    Create a program that generates random passwords of a specified length, with options for including uppercase letters, lowercase letters, numbers, and symbols.
'''

import string as st
import secrets as sc

def main():
    def genpass(length=8, include="yyyy"):
        pass
    
    def menu():
        print("--- Password Generator ---")
        
        while True:
            begin = input("Begin? (Y/n): ")
            
            if begin.strip().lower() == "y" or begin.strip().lower() == "":
                length = input("Password length(Default = 8): ")
                
                include_list = []
                uppercase = input("\nInclude uppercase letters?(Y/n): ")
                include_list.append(uppercase)
                lowercase = input("Include lowercase letters?(Y/n): ")
                include_list.append(lowercase)
                number = input("Include number?(Y/n): ")
                include_list.append(number)
                punctuation = input("Include punctuation?(Y/n): ")
                include_list.append(punctuation)
                
                print("".join(include_list))
            
            elif begin.strip().lower() == "n":
                print("\nExiting...")
                return
            
            else:
                print("\nError: Accept only 'y' and 'n' input.\n")
                
                
    menu()
    
if __name__ == "__main__":
    main()