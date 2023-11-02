from pygsheets.exceptions import SpreadsheetNotFound
from modules.template import Template

from tests.delete_spreadsheet import delete_spreadsheet


def main():
    spreadsheet_title = "finance"
    email_address = "douglasmaxton@gmail.com"
    t = Template(spreadsheet_title, email_address)

    delete_spreadsheet()

    try:
        t.open_spreadsheet()
        print("Spreadsheet open")
    except SpreadsheetNotFound:
        t.create_spreadsheet()
        print("File not found")


main()
