def check_number_and_option(option):
    try:
        number = int(input("What is you number?\n"))
        assert 0 < number <= option and type(number) == int
        return number
    except AssertionError:
        print("Value must be between 1 and 5")
    except ValueError:
        print("You must enter a number?")