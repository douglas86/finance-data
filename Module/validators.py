class Validators:
    """
    Class to check if data entering is correct
    """

    def __init__(self, number, option):
        self.number = number
        self.option = option

    def check_number_and_option(self):
        try:
            # check if number between 2 values
            assert 0 < int(self.number) <= self.option
            return True
        except AssertionError:
            print(f"Value must be between 1 and {self.option}")
            return False
        except ValueError:
            print("You must enter a number?")
            return False

    def check_number(self):
        try:
            # splits number by full stop
            splitting = str(self.number).split(".")
            assert 0 < float(self.number) and 1 < len(splitting[-1]) >= 2 >= len(
                splitting
            )
            return True
        except AssertionError:
            print("There must be no more than 2 decimal places")
        except ValueError:
            print("Your input is not a number")

    def check_pound_amount(self):
        try:
            number = float(input("Please enter an amount in £\n"))
            if type(number) == float and len(str(number).split(".")[-1]) <= 2:
                return number
            else:
                raise AssertionError
        except AssertionError:
            print("There must be no more than 2 decimal places")
        except ValueError:
            print("Your input is not a number")
