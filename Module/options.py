from Module.settings import current_month


class Options:
    """
    This file is used to point you to the correct option class
    """

    def option_selected(self):
        """
        This will point you in the right direction for the option that was pressed
        :return:
        """

        # print out options to select
        print("1. Salary")
        print("2. Daily Spending")
        print("3. Transfer Between Accounts")
        print("4. Loan, Credit Card or Debit order")
        print("5. Interest or Bank charges from accounts")

        number = input("What option do you want to pick? ")

        print(f"The current month is {current_month}")
        print(f"Your number is {number}")


options = Options()
