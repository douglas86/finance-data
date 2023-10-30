import gspread
from google.oauth2.service_account import Credentials
import json

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]

creds = json.load(open("creds.json"))
CREDS = Credentials.from_service_account_file(creds)
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
gc = GSPREAD_CLIENT.open("love_sandwiches")


def main():
    print("main program")
    try:
        gc.open("love_sandwiches")
        print("file opened")
    except gspread.SpreadsheetNotFound:
        print("file not found")


main()
