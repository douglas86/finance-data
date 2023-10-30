import gspread
from google.oauth2.service_account import Credentials

scopes = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]

credentials = Credentials.from_service_account_file("creds.json", scopes=scopes)

gc = gspread.authorize(credentials)


def main():
    print("main program")
    try:
        gc.open("love_sandwiches")
        print("file opened")
    except gspread.SpreadsheetNotFound:
        print("file not found")


main()
