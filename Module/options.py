from Module.validators import Validators
from Module.template import template
from Module.settings import current_month


class Options:
    """
    All the options get selected from this class
    """

    data = {}
    data_to_be_updated = []

    def __iter__(self, crud_operation, lists=None):
        """
        Special built-in function to iterate over a list, dictionary or tuple
        :param crud_operation: only pass in get if needing to get data from spreadsheet
        :return:
        """
        if crud_operation == "get":
            getting = (
                template.open_spreadsheet().worksheet(current_month).batch_get(lists)
            )
            self.data["deposit"] = getting[0]
            self.data["withdraw"] = getting[1]
            self.data["deposit_withdraw_totals"] = getting[2]
            self.data["debit_orders"] = getting[3]
            self.data["transfers"] = getting[4]
            self.data["growth_rate"] = getting[5]
            self.data["total_account_balances"] = getting[6]
        else:
            print("You have entered the incorrect crud_operations")

    def start(self):
        """
        Initially starts this class
        :return:
        """
        self.get_data()
        self.options()

    def get_data(self):
        """
        Gathers all initial data needed for the current month
        :return:
        """

        # 1st list: gets deposit information
        # 2nd list: gets withdraw information
        # 3rd list: gets totals of deposit, withdraw and balance
        # 4th list: gets debit orders and its data
        # 5th list: gets transfer between accounts data
        # 6th list: gets interest and bank charges
        # 7th list: gets growth rate and reserve/payback on all accounts
        # 8th list: gets total account balances on all accounts
        self.__iter__(
            "get",
            [
                "C10:L15",
                "C17:L31",
                "C33:L36",
                "C43:G57",
                "H43:L57",
                "S12:T27",
                "AC12:AG27",
                "AH12:AH27",
            ],
        )

    def options(self):
        """
        Used to show what options are available
        :return:
        """

        flag = True

        while flag:
            # print out options to select
            print(
                "Please enter an option from one of the following only type the number:"
            )
            print("1. Salary")
            print("2. Daily Spending")
            print("3. Transfer Between Accounts")
            print("4. Loan, Credit Card or Debit order")
            print("5. Interest or Bank charges from accounts")

            # validation for if number and between 1 and 5
            number = Validators(option=5).check_number_and_option()

            self.switch_case(number)

    def switch_case(self, number):
        """
        Determines were to send data, once a number is pressed
        :return:
        """

        match number:
            case 1:
                self.salary_option()
            case 2:
                self.daily_spending_option()
            case 3:
                self.transfer_between_accounts_option()
            case 4:
                self.loan_credit_or_debit_order_option()
            case 5:
                self.interest_bank_charges_option()

    def salary_option(self):
        """
        Options related to your salary
        :return:
        """
        while True:
            print("Please, enter the option that you are wanting?")
            print("1. Do you want to update your salary")
            print("2. What is  the name of your company")

            number = float(input("Please enter your data here?"))

    def daily_spending_option(self):
        print("Daily Spending option was selected")

    def transfer_between_accounts_option(self):
        print("Transfer between accounts option was selected")

    def loan_credit_or_debit_order_option(self):
        print("Loan, Credit or Debit Order option was selected")

    def interest_bank_charges_option(self):
        print("Interest or bank charges option was selected")


options = Options()
