from Module.validators import check_number_and_option


class Options:
    """
    This file is used to point you to the correct option class
    """

    def option_selected(self):
        """
        This will point you in the right direction for the option that was pressed
        :return:
        """

        while True:
            # print out options to select
            print("1. Salary")
            print("2. Daily Spending")
            print("3. Transfer Between Accounts")
            print("4. Loan, Credit Card or Debit order")
            print("5. Interest or Bank charges from accounts")

            number = check_number_and_option(5)

            print(f"number is {number}")


options = Options()
