import gspread
from google.oauth2.service_account import Credentials
from datetime import date, datetime


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]

# credentials
CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("template")
client = gspread.Client(auth=SCOPED_CREDS)

# working with dates
today = date.today()
current_year = today.year
now = datetime.now()
current_month = now.strftime("%B")
