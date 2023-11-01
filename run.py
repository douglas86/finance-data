from gspread.exceptions import SpreadsheetNotFound
from modules.template import Template

from modules.settings import gc
from tests.delete_spreadsheet import delete_spreadsheet


def main():
    t = Template("finance", "douglasmaxton@gmail.com")

    delete_spreadsheet()

    try:
        gc.open("finance")
        print("Spreadsheet opened")
    except SpreadsheetNotFound:
        print(t.create_spreadsheet())


main()
