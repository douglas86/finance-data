import heroku3


import os
from dotenv import load_dotenv

"""
This file is used to work with environment variables
"""

load_dotenv()

filename = "creds2.json" or heroku3.from_key("CREDS")
FOLDER_ID = os.environ["FOLDER_ID"] or heroku3.from_key("FOLDER_ID")
FILE_ID = os.environ["FILE_ID"] or heroku3.from_key("FILE_ID")
