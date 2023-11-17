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


def exit_loop():
    while True:
        print("Please enter a number from one two 5")

        number = input("Please select an option from above?\n")

        validators = Validators(number=number, option=5)

        c = validators.check_number_and_option()

        if c:
            break
