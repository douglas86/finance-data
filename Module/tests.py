from Module.settings import GSPREAD_CLIENT

from Module.validators import Validators


def delete_spreadsheet(file_id):
    """
    Deletes spreadsheet by file_id
    :param file_id: This can be found in the address bar for the current spreadsheet
    :return:
    """
    GSPREAD_CLIENT.del_spreadsheet(file_id=file_id)
    print("File deleted")


def testing():
    salary = input("Please enter your salary amount?\n")
    validator = Validators(number=salary, option=2)
    check_salary = validator.check_salary()

    print("check salary", check_salary)
