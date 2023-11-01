from gspread.exceptions import SpreadsheetNotFound
from modules.template import create_spreadsheet

from modules.settings import gc


def main():
    try:
        gc.open("finance")
        print("Spreadsheet opened")
    except SpreadsheetNotFound:
        create_spreadsheet()


main()
