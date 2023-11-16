from Module.validators import check_number_and_option


class Options:
    """
    All the options get selected from this class
    """

    def start(self):
        """
        Initially starts this class
        :return:
        """
        self.options()

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
                print("You entered the number 1")
            case 2:
                print("You entered the number 2")
            case 3:
                print("You entered the number 3")
            case 4:
                print("You entered the number 4")
            case 5:
                print("You entered the number 5")

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
