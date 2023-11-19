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
        """
        Checks if number is:
            no more than two decimal places
            if value is a number
            must not be a negative number
        :return:
        """
        try:
            splitting = str(self.number).split(".")
            assert 0 < float(self.number) and len(splitting) <= 2
            assert len(splitting) <= 2 and len(splitting[-1]) <= 2
        except AssertionError:
            print("Value can't be negative")
            print("There must be no more than 2 decimal places")
            return False
        except ValueError:
            print("Your input is not a number")
            return False
        else:
            return True

    def check_salary(self):
        """
        Checks:
            check if no decimal return true
            check if one or two decimal return true
            check if more than three decimal returns false
            check if negative number returns false
            check if not a number return false
        :return:
        """
        try:
            splitting = self.number.split(".")
            assert float(self.number) > 0
            if len(splitting) == 2:
                assert len(splitting[-1]) <= 2
        except AssertionError:
            print("There can't be a negative number")
            print("Number can't have more than 2 decimal places")
            return False
        except ValueError:
            print("Your input is not a number")
            return False
        else:
            return True
