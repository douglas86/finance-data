import pygsheets

from pydrive2.drive import GoogleDrive

from utils.keys import filename, folder_id
from utils.login_with_service_account import login_with_service_account

from Module.dates import current_year


# authorization for pygsheets
client = pygsheets.authorize(service_file=filename)


# access Google Drive and all its content
drive = GoogleDrive(login_with_service_account())

# Get a list of files inside folder
file_list = drive.ListFile(
    {"q": f"'{folder_id}' in parents and trashed=false"}
).GetList()

# opens the spreadsheet
spreadsheet = client.open(current_year)
