from gspread.exceptions import SpreadsheetNotFound


from Module.template import template

from Module.tests import delete_spreadsheet


def main():
    """
    This is the main function that runs the entire program
    :return:
    """

    # Deleted spreadsheet
    delete_spreadsheet(
        file_id="1ZK1dHDCXaloQzAnrY6ZlCskypVKRCqUTt48sFXnI21g",
    )

    # check to see if the spreadsheet with current_year is created
    try:
        template.open_spreadsheet()
        print("spreadsheet open")
    except SpreadsheetNotFound:
        template.create_spreadsheet()


main()
