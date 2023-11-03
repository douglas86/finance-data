from pygsheets.exceptions import SpreadsheetNotFound

from modules.template import Template

from tests.delete_spreadsheet import delete_spreadsheet


def main():
    client = Template("finance", "douglasmaxton@gmail.com")

    delete_spreadsheet()

    try:
        client.open_spreadsheet()
        print("Spreadsheet open")
    except SpreadsheetNotFound:
        client.create_spreadsheet()
        print("File not found")


main()
