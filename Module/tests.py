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
