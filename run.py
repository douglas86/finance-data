from gspread.exceptions import SpreadsheetNotFound
from modules.template import Template

from modules.settings import gc


def main():
    t = Template("finance", "douglasmaxton@gmail.com")
    for spreadsheet in gc.openall():
        print("title", spreadsheet.title)
        print("id", spreadsheet.id)

    # gc.del_spreadsheet("1F3I-vZ5DtkV4_YQun_XAC5Gv58bLtTJoYlZyGsxa1sc")
    try:
        # gc.open("finance")
        print("Spreadsheet opened")
    except SpreadsheetNotFound:
        t.create_spreadsheet()


main()
