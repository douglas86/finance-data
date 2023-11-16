from Module.validators import check_number_and_option


class Options:
    """
    All the options get selected from this class
    """

    def select_option(self):
        """
        Used to select the initial options
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

            # switch case depending on what option you selected
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


options = Options()
