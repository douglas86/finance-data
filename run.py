from gspread.exceptions import SpreadsheetNotFound


from Module.template import template
from Module.options import options


def main():
    """
    This is the main function that runs the entire program
    :return:
    """

    print("This is a simple program to keep track of my day-to-day financials")
    print("This program is a simple terminal emulator in order to automate the process")
    print(
        "When a new year begins it creates a new Spreadsheet from a template spreadsheet"
    )
    print("It uses the current year of your computer as its title")

    # check to see if the spreadsheet with current_year is created
    try:
        template.open_spreadsheet()
        options.start()
    except SpreadsheetNotFound:
        # creates the spreadsheet using a template
        # renaming file with current_year
        template.create_spreadsheet()
        options.start()


if __name__ == "__main__":
    main()
