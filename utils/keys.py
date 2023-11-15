import heroku3


from simple_dotenv import GetEnv

"""
This file is used to work with environment variables
"""


filename = "creds2.json" or heroku3.from_key("CREDS")
FOLDER_ID = GetEnv("FOLDER_ID") or heroku3.from_key("FOLDER_ID")
FILE_ID = GetEnv("FILE_ID") or heroku3.from_key("FILE_ID")
