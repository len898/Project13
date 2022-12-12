class DictionaryFileManager():
    def __init__(self, filename:str) -> None:
        self.filename = filename
    
    def write_dictionary_to_file(self):
        pass



def main():
    building_numbers = {}
    entered_name = ""
    entered_name = input("Enter new name: ").capitalize()
    if entered_name != "":
        entered_building_num = input("Enter new building number: ")
        building_numbers[entered_name] = entered_building_num
    name_to_lookup = input("Enter name to look up: ").capitalize()
    if name_to_lookup.capitalize() in building_numbers:
        print(building_numbers[name_to_lookup])

main()