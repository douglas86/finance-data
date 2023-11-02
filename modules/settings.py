import pygsheets
import heroku3


def settings():
    """
    Call client to authorize you to use Google API with spreadsheets
    :return:
    """
    heroku_cred = heroku3.from_key("CREDS")
    filename = "creds.json" or heroku_cred
    client = pygsheets.authorize(service_file=filename)

    return client
