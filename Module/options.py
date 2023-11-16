from Module.validators import check_number_and_option


class Options:
    """
    All the options get selected from this class
    """

    get_data_for_current_month = []

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

            # validation for if number and between 1 and 5
            number = check_number_and_option(5)

            self.switch_case(number)

    def switch_case(self, number):
        """
        Determines were to send data to based on option selected
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
        print("Salary option was selected")

    def daily_spending_option(self):
        print("Daily Spending option was selected")

    def transfer_between_accounts_option(self):
        print("Transfer between accounts option was selected")

    def loan_credit_or_debit_order_option(self):
        print("Loan, Credit or Debit Order option was selected")

    def interest_bank_charges_option(self):
        print("Interest or bank charges option was selected")


options = Options()
