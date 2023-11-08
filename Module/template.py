from Module.settings import drive
from Module.dates import current_year


class Template:
    """
    Copies and creates the basic blueprint from template spreadsheet
    """

    def __init__(self, file_id, folder_id):
        """
        Initializes class
        :param file_id: in my case it is the id of template spreadsheet stored in Google Drive
        :param folder_id: this is the id of the folder were you want the file to be store in
        """
        self.file_id = file_id
        self.folder_id = folder_id

    def copy_file(self):
        """
        copies the file from file_id and renames it to the current year
        :return:
        """
        drive.auth.service.files().copy(
            fileId=self.file_id,
            body={
                "parents": [{"id": self.folder_id}],
                "title": current_year,
            },
        ).execute()


template = Template(
    "1-M5rHQY78wq_VWDUWLhz2hZvux3lY9y7lOT7PY4uGS0", "1jDCB53uToJ7nDm5_vxZr7019Zje9RmcX"
)
