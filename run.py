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
        file_id="1IDBajh6jk92aCg3BSAvW923Z5mt1JR8PQRYQANi6D9M",
    )

    # check to see if the spreadsheet with current_year is created
    try:
        template.open_spreadsheet()
        print("spreadsheet open")
    except SpreadsheetNotFound:
        # creates the spreadsheet using a template
        # renaming file with current_year
        template.create_spreadsheet()


main()
