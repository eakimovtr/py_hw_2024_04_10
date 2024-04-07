from typing import Any, Self

class UserList:
    # can initialize the collection with or without passing numbers
    def __init__(self, *numbers):
        self.num_list: list = []
        self.num_list.extend(numbers)
        
    # method to build new collection using user input
    @classmethod
    def from_user_input(cls) -> Self:
        print("Enter numbers. Type 'q' to end.")
        numbers: list = []
        while True:
            usr_input = input()
            if usr_input == 'q':
                break
            numbers.append(UserList.str_to_num(usr_input))
        return UserList(*numbers)
    
    def in_list(self, number) -> bool:
        return number in self.num_list 
    
    # allows user to add new number if there this number is not present in the collection
    def add(self, number) -> None:
        if not self.in_list(number):
            self.num_list.append(number)
        else:
            print(f"Number {number} is already present the list")
            
    # allows user to remove all user defined element entries from the collection
    def remove(self, value) -> None:
        self.num_list.remove(value)
    
    # displays collection in particular order
    def show(self, reverse=False) -> None:
        flag = -1 if reverse else 1
        print(self.num_list[::flag])
        
    # allows user to replace particular element (only first or all entries) with another
    def replace(self, key, value, first_entry=False) -> None:
        for i, num in enumerate(self.num_list):
            if num == key:
                self.num_list[i] = value
                if first_entry:
                    break
    
    def __str__(self) -> str:
        return self.num_list.__str__()
    
    # method for typecasting str input to numeric values (conditionally float or num)
    @staticmethod
    def str_to_num(input: str):
        try:
            if '.' in input:
                return float(input)
            if ',' in input:
                return float(input.replace(',', '.'))
            return int(input)
        except ValueError as e:
            print(f"Unable to cast '{input}' to numeric.")
    
    
# class for running the application
class RunList:
    def __init__(self):
        self.collection: UserList
    
    def main(self):
        self.collection = UserList.from_user_input()
        while True:
            print(self.collection)
            RunList.show_menu()
            usr_input = input("Type number of desired menu option. Type 'q' to quit")
            if usr_input == 'q':
                break
            self.run_user_command(usr_input)
            
    @staticmethod
    def show_menu() -> None:
        print("\n---MENU---\n")
        print("1. Add new number")
        print("2. Remove number")
        print("3. Show list")
        print("4. Check if number is in list")
        print("5. Replace number")
        print("\n----------\n")
        
    def run_user_command(self, usr_input: str):
        match usr_input:
            case '1':
                print("Enter new number")
                value = UserList.str_to_num(input())
                self.collection.add(value)
            case '2':
                print("Enter number to remove")
                value = UserList.str_to_num(input())
                self.collection.remove(value)
            case '3':
                usr_input = input("Show in reveresed direction? (y/n): ")
                if usr_input == 'y':
                    flag = True
                elif usr_input == 'n':
                    flag = False
                else:
                    print(f"Unknown flag {usr_input}. Use (y/n)")
                self.collection.show(reverse=flag)
            case '4':
                print("Enter number to check")
                value = UserList.str_to_num(input())
                print(self.collection.in_list(value))
            case '5':
                print("Enter number to replace")
                key = UserList.str_to_num(input())
                print("Enter new number")
                value = UserList.str_to_num(input())
                usr_input = input("Replace only the first entry? (y/n): ")
                if usr_input == 'y':
                    flag = True
                elif usr_input == 'n':
                    flag = False
                self.collection.replace(key, value, first_entry=flag)
            case _:
                print("Unknown command! Try again.")
                

RunList().main()