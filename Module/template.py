from Module.settings import client, current_year
from utils.keys import FOLDER_ID, FILE_ID


class Template:
    """
    Creates the spreadsheet needed for the current year with all data copied from template spreadsheet
    """

    # Places data that was gathered from spreadsheet in a correct list
    account_balances = []
    reserve_from_previous_year = []
    debit_orders = []
    transfers_between_accounts = []
    # Append to list for what you want updated to spreadsheet
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
            """
            Filter out the unwanted pound symbol
            :param l:
            :return: The amount as a number
            """
            return [eval(n.strip("£")) for x in l for n in x]

        # gets batch data from spreadsheet
        # appends it to the correct list above
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
        return client.open(title=str(current_year), folder_id=str(self.folder_id))

    def get_data(self):
        """
        Calls __iter__ to iterate over data from spreadsheet
        :return:
        """
        # gathers 4 groups of data from data worksheet
        self.__iter__("get", ["D9:O24", "J33:L48", "Q9:R24", "C33:H47"])

        print(f"Data has been fetched from {current_year} spreadsheet")

    def update_rows_and_columns(self, dictionary):
        """
        Updates data in account balances
        :return:
        """

        # row number to start at
        range_to_start_at = dictionary["start_row"]
        # row number to stop at
        range_to_end_at = dictionary["end_row"]
        # variable to start at in a list
        place_in_list_to_start = 0
        # variable for where I want to stop in a list
        stop_in_list = dictionary["stop_in_list"]
        # name of the column to start at
        start_column = dictionary["start_column"]
        # name of the column to stop at
        end_column = dictionary["end_column"]
        lists = dictionary["lists"]

        # while loop to create the data needed for updating spreadsheet
        # this while loop updates the account balances and previous year data from the year before
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

            # increments the while loop so that it knows what to update
            range_to_start_at += 1
            place_in_list_to_start += stop_in_list

    def update_debit_orders(self):
        """
        Updates the debit orders with title, day and amount in the spreadsheet
        :return:
        """

        # debit orders are order based on numerical order by day of the month
        self.debit_orders[0].sort(key=lambda x: int(x[1]))

        def update_spreadsheet_list(start_column, start_row, count, element_in_list):
            """
            This function is used to dynamically update the data used concerning my debit orders
            :param start_column: Column letter for where you want to start appending to
            :param start_row: Row number for when the data needs to start from
            :param count: Running variable to add to the row number
            :param element_in_list: This is where the data sits in each debit order list
            :return: Does not return anything but updates the list for spreadsheet
            """
            self.data_to_update_spreadsheet_with.append(
                {
                    "range": f"{start_column}{start_row+count}",
                    "values": [[self.debit_orders[0][count][element_in_list]]],
                }
            )

        # iterates over debit order to be updated to spreadsheet
        # updates with title, day and amount
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

        print("Debit order has been updated with title, day of month and amount")

    def update_rows(self, dictionary):
        """
        This will update a row selection
        :param dictionary:
        :return:
        """

        row = dictionary["row"]
        column = dictionary["column"]
        lists = dictionary["lists"]

        for number in range(len(lists)):
            self.data_to_update_spreadsheet_with.append(
                {"range": f"{column}{row+number}", "values": [[lists[number]]]}
            )

    def update_transfers_between_accounts(self):
        """
        Update account transfers
        :return:
        """
        # Gathers all lists needed for transfers between accounts
        amount_to_deposit_into_savings_pots = self.transfers_between_accounts[0][4:10]
        loans = self.transfers_between_accounts[0][10:13]
        pensions = self.transfers_between_accounts[0][13:15]

        def strip_percentage(string):
            """
            Removes the percentage sign from number
            :param string:
            :return:
            """
            return int(string.strip("%"))

        def strip_pound(lists):
            """
            Strip away the £ symbol and convert it to a list
            :param lists:
            :return: List with float numbers
            """
            l = [amount.strip("£") for lis in lists for amount in lis if amount]
            num = [float(number.replace(",", "")) for number in l]

            return num

        update_savings_pot = {
            "row": 47,
            "column": "L",
            "lists": strip_pound(amount_to_deposit_into_savings_pots),
        }

        update_transfer = {
            "row": 43,
            "column": "K",
            "lists": [
                strip_percentage(self.transfers_between_accounts[0][0][0]) / 100,
                strip_percentage(self.transfers_between_accounts[0][1][0]) / 100,
            ],
        }

        update_loans = {
            "row": 53,
            "column": "L",
            "lists": strip_pound(loans),
        }

        update_pension = {
            "row": 56,
            "column": "L",
            "lists": strip_pound(pensions),
        }

        self.update_rows(update_savings_pot)
        self.update_rows(update_transfer)
        self.update_rows(update_loans)
        self.update_rows(update_pension)

        print("transfers between accounts have been updated")

    def update_data(self):
        """
        Once data has been fetched
        Calls __iter__ method to iterate over and update data to spreadsheet
        :return:
        """

        update_account_balances = {
            "start_row": 5,
            "end_row": 21,
            "stop_in_list": 12,
            "start_column": "BE",
            "end_column": "DP",
            "lists": self.account_balances[0],
        }
        update_reserve_from_previous_year = {
            "start_row": 25,
            "end_row": 41,
            "stop_in_list": 3,
            "start_column": "BI",
            "end_column": "BK",
            "lists": self.reserve_from_previous_year[0],
        }

        # update account balances from the previous year
        self.update_rows_and_columns(update_account_balances)
        # update October, November and December data from the previous year
        self.update_rows_and_columns(update_reserve_from_previous_year)
        # updating debit orders data with title, day of month and amount
        self.update_debit_orders()
        # updating funds transfers
        self.update_transfers_between_accounts()

        # iterates around a list then updates it in spreadsheet
        self.__iter__("updating")

        print(f"All data has been successfully updated to {current_year} Spreadsheet")

    def delete_sheet(self):
        """
        Once all data has been fetched and updated delete 'data' worksheet
        :return:
        """
        worksheet = self.open_spreadsheet().get_worksheet(12)
        self.open_spreadsheet().del_worksheet(worksheet)

        print("Data worksheet deleted")

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
        self.get_data()
        self.update_data()

        # deletes the data worksheet after all data has been retrieved
        self.delete_sheet()


# variable to call the class Template
template = Template(
    file_id=FILE_ID,
    folder_id=FOLDER_ID,
)
