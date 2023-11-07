import pygsheets


from pydrive2.drive import GoogleDrive
from utils.keys import filename, folder_id
from utils.login_with_service_account import login_with_service_account


client = pygsheets.authorize(service_file=filename)


drive = GoogleDrive(login_with_service_account())

# Get a list of files inside folder
file_list = drive.ListFile(
    {"q": f"'{folder_id}' in parents and trashed=false"}
).GetList()
