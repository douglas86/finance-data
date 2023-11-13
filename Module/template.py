from Module.settings import client

from Module.dates import current_year


class Template:
    """
    Creates the spreadsheet needed for the current year with all data copied from template spreadsheet
    """

    account_balances = []
    reserve_from_previous_year = []
    debit_orders = []
    transfers_between_accounts = []
    data_to_update_spreadsheet_with = [{"range": "A1", "values": [[int(current_year)]]}]

    def __init__(self, file_id, folder_id):
        """
        Initializes class with variables
        :param file_id:
        :param folder_id:
        """
        self.file_id = file_id
        self.folder_id = folder_id

    def __iter__(self, crud_operation, lists=None):
        """
        Special built-in function to iterate over a list, dictionary or tuple
        :return:
        """

        def split_unwanted_pound_symbol(l):
            return [eval(n.strip("£")) for x in l for n in x]

        # gets batch data from spreadsheet
        # appends it to the correct list
        if crud_operation == "get":
            getting = self.open_spreadsheet().worksheet("data").batch_get(lists)
            self.account_balances.append(split_unwanted_pound_symbol(getting[0]))
            self.reserve_from_previous_year.append(
                split_unwanted_pound_symbol(getting[1])
            )
            self.transfers_between_accounts.append(getting[2])
            self.debit_orders.append(getting[3])
        # updates batch data to spreadsheet
        else:
            self.open_spreadsheet().sheet1.batch_update(
                self.data_to_update_spreadsheet_with
            )

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
        self.__iter__("get", ["D9:O24", "J33:L48", "Q9:R24", "C33:H47"])

        return f"Data has been fetched from {current_year} spreadsheet"

    def update_rows_and_columns(self, dictionary):
        """
        Updates data in account balances
        :return:
        """

        # row number to start at
        range_to_start_at = dictionary["start"]
        # row number to stop at
        range_to_end_at = dictionary["end"]
        # variable to start at in a list
        place_in_list_to_start = 0
        # variable for where I want to stop in a list
        stop_in_list = dictionary["stop_in_list"]
        # name of the column to start at
        start_column = dictionary["start_column"]
        # name of the column to stop at
        end_column = dictionary["end_column"]
        lists = dictionary["lists"]

        while range_to_start_at < range_to_end_at:
            self.data_to_update_spreadsheet_with.append(
                {
                    "range": f"{start_column}{range_to_start_at}:{end_column}{range_to_end_at}",
                    "values": [
                        lists[
                            place_in_list_to_start : place_in_list_to_start
                            + stop_in_list
                        ]
                    ],
                }
            )

            range_to_start_at += 1
            place_in_list_to_start += stop_in_list

    def update_debit_orders(self):
        """
        Updates the debit orders with title, day and amount in the spreadsheet
        :return:
        """

        # order debit orders in numerical order based on day of the month
        self.debit_orders[0].sort(key=lambda x: int(x[1]))

        def update_spreadsheet_list(start_column, start_row, count, element_in_list):
            self.data_to_update_spreadsheet_with.append(
                {
                    "range": f"{start_column}{start_row+count}",
                    "values": [[self.debit_orders[0][count][element_in_list]]],
                }
            )

        # iterates over debit order to be updated to spreadsheet
        for i in range(len(self.debit_orders[0])):
            # updates the name of the debit order
            update_spreadsheet_list("C", 43, i, 0)
            # updates the day of the month
            update_spreadsheet_list("F", 43, i, 1)
            # updates the value of the debit order as a float number
            # strips pound and converts it to number
            self.data_to_update_spreadsheet_with.append(
                {
                    "range": f"BP{25+i}",
                    "values": [[eval(self.debit_orders[0][i][5].split("£")[1])]],
                }
            )

    def update_data(self):
        """
        Once data has been fetched
        Calls __iter__ method to iterate over and update data to spreadsheet
        :return:
        """

        update_account_balances = {
            "start": 5,
            "end": 21,
            "stop_in_list": 12,
            "start_column": "BE",
            "end_column": "DP",
            "lists": self.account_balances[0],
        }
        update_reserve_from_previous_year = {
            "start": 25,
            "end": 41,
            "stop_in_list": 3,
            "start_column": "BI",
            "end_column": "BK",
            "lists": self.reserve_from_previous_year[0],
        }

        self.update_rows_and_columns(update_account_balances)
        self.update_rows_and_columns(update_reserve_from_previous_year)
        self.update_debit_orders()

        # iterates around a list then updates it in spreadsheet
        self.__iter__("updating")

        return "Spreadsheet data has been updated"

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

        # get and update data from spreadsheet
        print(self.get_data())
        print(self.update_data())

        # print("debit orders", self.debit_orders)
        self.update_debit_orders()


# variable to call the class Template
template = Template(
    file_id="1-M5rHQY78wq_VWDUWLhz2hZvux3lY9y7lOT7PY4uGS0",
    folder_id="1jDCB53uToJ7nDm5_vxZr7019Zje9RmcX",
)
