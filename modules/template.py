# from modules.dates import get_current_year
# from modules.settings import gc
#
# from utils.formatting.title_formatting import title_formatting
#
#
# class Template:
#     """
#     Creates all-template needs for the spreadsheet
#     """
#
#     def __init__(self, name, email_address):
#         """
#         Initialization of this class
#         :param name:
#         :param email_address:
#         """
#         self.name = name
#         self.email_address = email_address
#
#     def create_spreadsheet(self):
#         """
#         Creates a Spreadsheet and shares it with my email address
#         :return:
#         """
#         # Create the spreadsheet and shares it with me
#         sh = gc.create(self.name)
#         sh.share(self.email_address, perm_type="user", role="writer")
#
#         # Creates a worksheet based on current year
#         worksheet = sh.add_worksheet(
#             title=str(get_current_year()), rows=1000, cols=1000
#         )
#         # Deletes sheet that was created with spreadsheet
#         sh.del_worksheet(sh.sheet1)
#
#         # This variable is the number cell that January starts at
#         first_month_starts_at = 2
#
#         # The List of all the months in the year
#         # This will be the titles for each section in the sheet
#         months = [
#             "January",
#             "February",
#             "March",
#             "April",
#             "May",
#             "June",
#             "July",
#             "August",
#             "September",
#             "October",
#             "November",
#             "December",
#             "Total",
#         ]
#
#         # Iterates through the months to give it a Look and style
#         for month in months:
#             title_formatting(worksheet, first_month_starts_at, month)
#             first_month_starts_at += 40
#
#         return "Spreadsheet created"
from modules.settings import user


class Template:
    """
    This will create the templates needed for the spreadsheets
    """

    def __init__(self, name, email_address):
        """
        Initializes Template class
        :param name:
        :param email_address:
        """
        self.name = name
        self.email_address = email_address

    def open_spreadsheet(self):
        """
        Opens the spreadsheet
        :return:
        """
        return user.open(self.name)

    def create_spreadsheet(self):
        """
        Creates a new Spreadsheet
        :return:
        """
        user.create(title=self.name)
        spreadsheet = user.open(self.name)
        spreadsheet.share(self.email_address, role="writer")
        print("Spreadsheet created")
