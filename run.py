import gspread
from google.oauth2.service_account import Credentials
import json
import os

scopes = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]

creds = os.getenv("creds") or json.load(open("creds.json"))
CREDS = Credentials.from_service_account_file(creds, scopes=scopes)

gc = gspread.authorize(CREDS)


def main():
    print("main program")
    try:
        gc.open("love_sandwiches")
        print("file opened")
    except gspread.SpreadsheetNotFound:
        print("file not found")


main()
