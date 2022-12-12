"""
CS 131B Project 13
Programmer: Lennart Richter
Date: 12/11/2022
Description: A program that reads a file and returns a dictionary to user for tracking names and apartment nums
I promise that I understand the code I am submitting well enough to write similar code on a test.
"""

import pickle

#Class to manage the file the constructor takes a filename as parameter to become an instance attribute
class DictionaryFileManager():
    def __init__(self, filename:str) -> None:
        self.filename = filename
    
    #Function that takes a dictionary as parameter and writes that to a file using name from __init__
    def write_dictionary_to_file(self, passed_in_dictionary:dict) -> None:
        with open('dictionary.txt', 'wb') as f:
            pickle.dump(passed_in_dictionary,f)

    #Function that reads the file from the name passed in __init__ and reads the data into a dictionary and returns that
    def read_dictionary_from_file(self) -> dict:
        dictionary_from_file = {}
        try:
            with open('dictionary.txt', 'rb') as f:
                dictionary_from_file = pickle.load(f)
        except FileNotFoundError:
            return {}
        return dictionary_from_file

def main():
    manager = DictionaryFileManager('dictionary.txt')
    building_numbers = manager.read_dictionary_from_file()
    entered_name = ""
    entered_name = input("Enter new name: ").capitalize()
    if entered_name != "":
        entered_building_num = input("Enter new building number: ")
        building_numbers[entered_name] = entered_building_num
    name_to_lookup = input("Enter name to look up: ").capitalize()
    if name_to_lookup.capitalize() in building_numbers:
        print(building_numbers[name_to_lookup])
    manager.write_dictionary_to_file(building_numbers)

main()

"""
Sample Run
(.venv) PS C:\Users\lenna\Documents\CS131B\Project13> & c:/Users/lenna/Documents/CS131B/Project13/.venv/Scripts/python.exe c:/Users/lenna/Documents/CS131B/Project13/main.py
Enter new building number: 1
Enter name to look up: Lenni
1
(.venv) PS C:\Users\lenna\Documents\CS131B\Project13> & c:/Users/lenna/Documents/CS131B/Project13/.venv/Scripts/python.exe c:/Users/lenna/Documents/CS131B/Project13/main.py
Enter new name: Mark
Enter new building number: 2
Enter name to look up: Lenni
1
(.venv) PS C:\Users\lenna\Documents\CS131B\Project13> & c:/Users/lenna/Documents/CS131B/Project13/.venv/Scripts/python.exe c:/Users/lenna/Documents/CS131B/Project13/main.py
Enter new name: Kevin
Enter new building number: 4
Enter name to look up: Lenni
1
(.venv) PS C:\Users\lenna\Documents\CS131B\Project13> 
"""