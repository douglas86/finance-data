from modules.dates import get_current_year
from modules.settings import gc


class Template:
    """
    Creates all-template needs for the spreadsheet
    """

    def __init__(self, name, email_address):
        """
        Initialization of this class
        :param name:
        :param email_address:
        """
        self.name = name
        self.email_address = email_address

    def create_spreadsheet(self):
        """
        Creates a Spreadsheet and shares it with my email address
        :return:
        """
        # Create the spreadsheet and shares it with me
        sh = gc.create(self.name)
        sh.share(self.email_address, perm_type="user", role="writer")

        # Creates a worksheet based on current year
        worksheet = sh.add_worksheet(title=str(get_current_year()), rows=400, cols=400)
        sh.del_worksheet(sh.sheet1)

        worksheet.merge_cells("B2:I5")
        worksheet.update("B2", "January")

        return "Spreadsheet created"
