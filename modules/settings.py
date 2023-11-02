import pygsheets
import heroku3


heroku_cred = heroku3.from_key("CREDS")
filename = "creds.json" or heroku_cred
client = pygsheets.authorize(service_file=filename)
