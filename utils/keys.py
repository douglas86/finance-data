import heroku3


from simple_dotenv import GetEnv

"""
This file contains all of my environment variables
"""


filename = "creds.json" or heroku3.from_key("CREDS")
folder_id = GetEnv("FOLDER_ID") or heroku3.from_key("FOLDER_ID")
