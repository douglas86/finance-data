def delete_spreadsheet(gspread_client, file_id):
    """
    Deletes spreadsheet by file_id
    :param gspread_client:
    :param file_id:
    :return:
    """
    gspread_client.del_spreadsheet(file_id=file_id)
    print("File deleted")
