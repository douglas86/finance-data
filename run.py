from gspread.exceptions import SpreadsheetNotFound


from Module.template import template
from Module.options import select_option


def main():
    """
    This is the main function that runs the entire program
    :return:
    """

    # check to see if the spreadsheet with current_year is created
    try:
        template.open_spreadsheet()
        select_option()
    except SpreadsheetNotFound:
        # creates the spreadsheet using a template
        # renaming file with current_year
        template.create_spreadsheet()
        select_option()


main()
