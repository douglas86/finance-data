import heroku3

import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]


# heroku variable to get environment variable when on heroku
heroku_conn = heroku3.from_key("CREDS")
# will load creds.json when on local machine when live will load heroku environment variable
CREDS = Credentials.from_service_account_file("creds.json" or heroku_conn, scopes=SCOPE)
# used to communicate with the spreadsheet
GSPREAD_CLIENT = gspread.authorize(CREDS)


def main():
    print("The json file is")
    gc = GSPREAD_CLIENT.open("love_sandwiches")
    print(gc)
    print("file opened")


main()
