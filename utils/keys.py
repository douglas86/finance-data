import heroku3


from simple_dotenv import GetEnv

"""
This file contains all of my environment variables
"""


filename = "creds2.json" or heroku3.from_key("CREDS")
folder_id = GetEnv("FOLDER_ID") or heroku3.from_key("FOLDER_ID")
file_id = GetEnv("FILE_ID") or heroku3.from_key("FILE_ID")
