from Module.validators import Validators
from Module.settings import GSPREAD_CLIENT


def delete_spreadsheet(file_id):
    """
    Deletes spreadsheet by file_id
    :param file_id: This can be found in the address bar for the current spreadsheet
    :return:
    """
    GSPREAD_CLIENT.del_spreadsheet(file_id=file_id)
    print("File deleted")


def switch(number):
    print("switch case selected")
    match number:
        case 1:
            print("Number 1 selected")
        case 2:
            return option_two()
        case 3:
            print("Number 3 selected")
        case 4:
            print("Number 4 selected")
        case 5:
            print("Number 5 selected")


def option_two():
    while True:
        print("Please enter a number from one two 2")

        number = input("Please select an option from above")

        validators = Validators(number=number, option=2)

        c = validators.check_number_and_option()

        if c:
            break


def exit_loop():
    while True:
        print("Please enter a number from one two 5")

        number = input("Please select an option from above?\n")

        validators = Validators(number=number, option=5)

        c = validators.check_number_and_option()
        print(f"c: {c}")

        if c:
            switch(int(number))
