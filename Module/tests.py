from Module.settings import GSPREAD_CLIENT


def delete_spreadsheet(file_id):
    """
    Deletes spreadsheet by file_id
    :param file_id:
    :return:
    """
    GSPREAD_CLIENT.del_spreadsheet(file_id=file_id)
    print("File deleted")
