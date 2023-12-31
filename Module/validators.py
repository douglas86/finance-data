class Validators:
    """
    Class to check if data entering is correct
    """

    def __init__(self, number, option):
        self.number = number
        self.option = option

    def check_number_and_option(self):
        """
        Checks:
            checks if input is a number
            checks if input is one of the option provided
        :return:
        """
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
