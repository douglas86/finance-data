class Validators:
    """
    Class to check if data entering is correct
    """

    def __init__(self, option):
        self.option = option

    def check_number_and_option(self):
        try:
            number = int(input("Please select an option from above?\n"))
            assert 0 < number <= self.option and type(number) == int
            return number
        except AssertionError:
            print(f"Value must be between 1 and {self.option}")
        except ValueError:
            print("You must enter a number?")

    def check_pound_amount(self):
        try:
            number = float(input("Please enter an amount in £\n"))
            print("number", type(number))
            if type(number) == float and len(str(number).split(".")[-1]) <= 2:
                return number
            else:
                raise AssertionError
        except AssertionError:
            print("There must be no more than 2 decimal places")
        except ValueError:
            print("Your input is not a number")

    def check_float_number(self):
        try:
            number = float(input("Please enter the amount in £\n"))
            assert type(number) == float or type(number) == int
            if len(str(number).split(".")[-1]) != 2:
                raise ValueError
            return number
        except AssertionError:
            print(f"Value must be between 1 and {self.option}")
        except ValueError:
            print("You must enter a number?")
