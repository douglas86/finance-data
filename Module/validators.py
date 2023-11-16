class Validators:
    """
    Class to check if data entering is correct
    """

    def __init__(self, option):
        self.option = option

    def check_number_and_option(self):
        try:
            number = int(input("What is you number?\n"))
            assert 0 < number <= self.option and type(number) == int
            return number
        except AssertionError:
            print(f"Value must be between 1 and {self.option}")
        except ValueError:
            print("You must enter a number?")

    def check_float_number(self):
        try:
            number = float(input("Please enter the amount in £"))
            assert 0 < number <= self.option and type(number) == float
            if len(str(number).split(".")[-1]) != 2:
                raise ValueError
        except AssertionError:
            print(f"Value must be between 1 and {self.option}")
        except ValueError:
            print("You must enter a number?")
