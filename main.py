class DictionaryFileManager():
    def __init__(self, filename:str) -> None:
        self.filename = filename
    
    def write_dictionary_to_file(self, passed_in_dictionary:dict) -> None:
        with open('dictionary.txt', 'w') as f:
            for i in passed_in_dictionary:
                f.write(f"{i}, {passed_in_dictionary[i]}")

    def read_dictionary_from_file(self) -> dict:
        dictionary_from_file = {}
        try:
            with open('dictionary.txt', 'r') as f:
                for line in f:
                    name_number_list_from_file = line.split(',')
                    dictionary_from_file[name_number_list_from_file[0]] = name_number_list_from_file[1]
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

main()