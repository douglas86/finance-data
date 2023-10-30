# import gspread
# from google.oauth2.service_account import Credentials
import json

# import os

# SCOPE = [
#     "https://www.googleapis.com/auth/spreadsheets",
#     "https://www.googleapis.com/auth/drive.file",
#     "https://www.googleapis.com/auth/drive",
# ]


# creds = json.load(open("creds.json"))
# CREDS = Credentials.from_service_account_file(client_secret, scopes=scopes)
# SCOPED_CREDS = CREDS.with_scopes(SCOPE)
# GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
# gc = GSPREAD_CLIENT.open("love_sandwiches")

dictionary = json.load(open("creds.json"))


def main():
    print("The json file is")
    print(dictionary)


main()
