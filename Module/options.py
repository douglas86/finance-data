from Module.validators import Validators
from Module.template import template
from Module.settings import current_month

from utils.helpers import select_option, help_with_anything_else


class Options:
    """
    All the options get selected from this class
    """

    # data from spreadsheet
    data = {}
    data_to_be_updated = []

    def __iter__(self, crud_operation, lists=None):
        """
        Special built-in function to iterate over a list, dictionary or tuple
        :param crud_operation: only pass in get if needing to get data from spreadsheet
        :return:
        """
        # opens up spreadsheet with current month
        opening = template.open_spreadsheet().worksheet(current_month)

        # fetches all data from spreadsheet
        # loads data to self.data variable
        if crud_operation == "get":
            getting = (
                opening.batch_get(lists)
            )
            self.data["deposit"] = getting[0]
            self.data["withdraw"] = getting[1]
            self.data["deposit_withdraw_totals"] = getting[2]
            self.data["debit_orders"] = getting[3]
            self.data["transfers"] = getting[4]
            self.data["growth_rate"] = getting[5]
            self.data["total_account_balances"] = getting[6]
        # updates spreadsheet when called
        else:
            opening.batch_update(self.data_to_be_updated)

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

        while True:
            # print out options to select
            print("1. Salary")
            print("2. Daily Spending")
            print("3. Transfer Between Accounts")
            print("4. Loan, Credit Card or Debit order")
            print("5. Interest or Bank charges from accounts")
            print("6. Quit")

            number = select_option()
            validators = Validators(number=number, option=6)
            correct_answer = validators.check_number_and_option()

            if correct_answer:
                match int(number):
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
                    case 6:
                        break

    def salary_option(self):
        """
        Options related to your salary
        :return:
        """

        salary = self.data['deposit'][0][-1]
        company = self.data['deposit'][0][1]

        while True:
            print(f'Your current salary is: {salary if salary != '£0' else "You have not entered a salary yet!"}')
            print(f'{company if company != 'Salary' else "You have not yet entered a company name"}')
            print(f'1. Update salary: {salary}')
            print(f'2. Update company: {company}')
            print(f'3. Quit')

            number = select_option()
            validators = Validators(number=number, option=3)
            correct_answer = validators.check_number_and_option()

            if correct_answer:
                match int(number):
                    case 1:
                        salary_number = input('Please enter your salary amount?\n')
                        valid = Validators(number=salary_number, option=3)
                        check_salary = valid.check_number()
                        if check_salary:
                            self.data_to_be_updated.append({
                                "range": "G10",
                                "values": [[float(salary_number)]]
                            })
                            help_with_anything_else()
                    case 2:
                        company_name = input('Please enter the name of your company?\n')
                        self.data_to_be_updated.append({
                            "range": "C10",
                            "values": [[str(company_name)]]
                        })
                        help_with_anything_else()
                    case 3:
                        self.__iter__("updating")
                        self.data_to_be_updated = []
                        print('Salary data has been updated!')
                        break

    def daily_spending_option(self):
        print("Daily Spending option was selected")

    def transfer_between_accounts_option(self):
        print("Transfer between accounts option was selected")

    def loan_credit_or_debit_order_option(self):
        print("Loan, Credit or Debit Order option was selected")

    def interest_bank_charges_option(self):
        print("Interest or bank charges option was selected")


options = Options()
