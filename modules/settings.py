import heroku3
import gspread
from google.oauth2.service_account import Credentials


class Settings:
    SCOPE = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive.file",
        "https://www.googleapis.com/auth/drive",
    ]

    # gets environment variable when live on heroku
    heroku_conn = heroku3.from_key("CREDS")

    # checks file for local or heroku
    # if local loads creds.json file
    # if live loads heroku_conn variable
    filename = "creds.json" or heroku_conn

    # credentials variable for google spreadsheet
    credentials = Credentials.from_service_account_file(filename=filename, scopes=SCOPE)

    # spreadsheet authorization
    gc = gspread.authorize(credentials)


# variable to call when ever you want to talk to spreadsheet
gc = Settings.gc
