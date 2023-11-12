from gspread.exceptions import SpreadsheetNotFound

from testing.delete_spreadsheet import delete_spreadsheet

from Module.template import template


def main():
    """
    This is the main function that runs the entire program
    :return:
    """

    # Deleted spreadsheet
    delete_spreadsheet(
        file_id="1vnD3B491jZsdobQG5WtWYd_vgykAqWcf3vi6_9Vqogo",
    )

    # check to see if the spreadsheet with current_year is created
    try:
        template.open_spreadsheet()
        print("spreadsheet open")
    except SpreadsheetNotFound:
        template.create_spreadsheet()


main()
