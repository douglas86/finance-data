from Module.settings import client

from Module.dates import current_year


class Template:
    """
    Creates the spreadsheet needed for the current year with all data copied from template spreadsheet
    """

    account_balances = []
    transfers_between_accounts = []
    debit_orders = []
    reserve_from_previous_year = []

    def __init__(self, file_id, folder_id):
        """
        Initializes class with variables
        :param file_id:
        :param folder_id:
        """
        self.file_id = file_id
        self.folder_id = folder_id

    def __iter__(self, crud_operation, lists):
        """
        Special built-in function to iterate over a list, dictionary or tuple
        :return:
        """
        # gets batch data from spreadsheet
        if crud_operation == "get":
            getting = self.open_spreadsheet().worksheet("data").batch_get(lists)
            self.account_balances.append(getting[0])
            self.account_balances.append(getting[1])
            self.account_balances.append(getting[2])
            self.account_balances.append(getting[3])
            print("getting", getting)
            return f"Data fetched from {current_year} spreadsheet"
        # updates batch data to spreadsheet
        else:
            self.open_spreadsheet().sheet1.batch_update(lists)
            return f"Data has been updated to {current_year} spreadsheet"

    def open_spreadsheet(self):
        """
        Opens up the spreadsheet
        :return:
        """
        return client.open(title=str(current_year), folder_id=self.folder_id)

    def get_data(self):
        """
        Calls __iter__ to iterate over data from spreadsheet
        :return:
        """
        # gathers 4 groups of data from data worksheet
        print(self.__iter__("get", ["D9:O24", "J33:L48", "Q9:R24", "C33:H47"]))

    def update_data(self):
        """
        Once data has been fetched
        Calls __iter__ method to iterate over and update data to spreadsheet
        :return:
        """

        # list to update spreadsheet with
        list_to_update_spreadsheet = [{"range": "A1", "values": [[int(current_year)]]}]

        # variables to call with updating list above
        acc_data_range = 5
        acc_data_values = 0

        # iteration to update the list above
        while acc_data_range < 21:
            list_to_update_spreadsheet.append(
                {
                    "range": f"BE{acc_data_range}:DP{acc_data_range}",
                    "values": [
                        self.list_data()[acc_data_values : acc_data_values + 12]
                    ],
                }
            )
            # acc_data_range updates by one as the rows are one after the other in spreadsheet
            acc_data_range += 1
            # acc_data_values updates by 12 as there are 12 months in a year
            # and columns are one after the other
            acc_data_values += 12

        print(self.__iter__("updating", list_to_update_spreadsheet))

    def list_data(self):
        """
        Combines multiple lists in a list to one complete list
        :return:
        """
        return [
            eval(x)
            for i in range(len(self.account_balances[0]))
            for x in self.account_balances[0][i]
        ]

    def create_spreadsheet(self):
        """
        Creates the spreadsheet
        Gets and Updates data once the spreadsheet is created
        :return:
        """

        # Copies template spreadsheet
        # and creates a spreadsheet based on current_year
        client.copy(
            file_id=self.file_id,
            title=current_year,
            copy_permissions=True,
            folder_id=self.folder_id,
        )

        print(f"{current_year} spreadsheet created")

        # get and update data was spreadsheet has been created
        self.get_data()
        # self.update_data()

        print("list", self.account_balances)


# variable to call the class Template
template = Template(
    file_id="1-M5rHQY78wq_VWDUWLhz2hZvux3lY9y7lOT7PY4uGS0",
    folder_id="1jDCB53uToJ7nDm5_vxZr7019Zje9RmcX",
)
