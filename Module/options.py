from prettytable import PrettyTable


from Module.validators import Validators
from Module.template import template
from Module.settings import current_month

from utils.helpers import select_option, help_with_anything_else


class Options:
    """
    All the options get selected from this class
    """

    # data from spreadsheet
    data = {}
    data_to_be_updated = []

    def __iter__(self, crud_operation, lists=None):
        """
        Special built-in function to iterate over a list, dictionary or tuple
        :param crud_operation: only pass in get if needing to get data from spreadsheet
        :return:
        """
        # opens up spreadsheet with current month
        opening = template.open_spreadsheet().worksheet(current_month)

        # fetches all data from spreadsheet
        # loads data to self.data variable
        if crud_operation == "get":
            getting = opening.batch_get(lists)
            self.data["withdraw"] = getting[0]
        # updates spreadsheet when called
        else:
            opening.batch_update(self.data_to_be_updated)

    def start(self):
        """
        Initially starts this class
        :return:
        """
        self.get_data()
        self.options()

    def get_data(self):
        """
        Gathers all initial data needed for the current month
        :return:
        """

        # gets withdraw information
        self.__iter__(
            "get",
            [
                "C17:L31",
            ],
        )

    def options(self):
        """
        Used to show what options are available
        :return:
        """

        while True:
            # print out options to select
            print("Option 3 with quit this terminal")
            print("1. Salary")
            print("2. Daily Spending")
            print("3. Quit")

            number = select_option()
            validators = Validators(number=number, option=3)
            correct_answer = validators.check_number_and_option()

            if correct_answer:
                match int(number):
                    case 1:
                        self.salary_option()
                    case 2:
                        self.daily_spending_option()
                    case 3:
                        break

    def salary_option(self):
        """
        Options related to your salary
        :return:
        """

        while True:
            print("Option 3 will quit this menu and update spreadsheet")
            print(f"1. Update salary")
            print(f"2. Update company")
            print(f"3. Quit")

            number = select_option()
            validators = Validators(number=number, option=3)
            correct_answer = validators.check_number_and_option()

            if correct_answer:
                match int(number):
                    case 1:
                        salary = input("Please enter your salary amount?\n")
                        validator = Validators(number=salary, option=2)
                        check_salary = validator.check_salary()
                        if check_salary:
                            self.data_to_be_updated.append(
                                {"range": "G10", "values": [[float(salary)]]}
                            )
                    case 2:
                        company_name = input("Please enter the name of your company?\n")
                        self.data_to_be_updated.append(
                            {"range": "C10", "values": [[str(company_name)]]}
                        )
                    case 3:
                        self.__iter__("updating")
                        self.data_to_be_updated = []
                        print("Salary data has been updated!")
                        break

            help_with_anything_else()

    def daily_spending_option(self):
        """
        Updates monthly expenses
        :return:
        """

        # creates the table
        table = PrettyTable()
        # keeps track of all monthly expenses
        monthly_expenses = {}
        # extracts data already stored in spreadsheet
        withdraw = self.data["withdraw"]

        # if there is data in the spreadsheet already
        # append it to monthly_expenses dictionary
        if len(withdraw) > 0:
            for i in range(len(withdraw)):
                monthly_expenses[withdraw[i][0]] = float(withdraw[i][-1].strip("£"))

        def table_prettified():
            """
            Draws out the table
            :return:
            """
            table.field_names = ["column1", "column2", "column3"]
            table.add_row(
                [
                    "1. Clothing and Footwear",
                    "2. Technology",
                    "3. Groceries",
                    # "4. Eating Out",
                ]
            )
            table.add_row(
                [
                    "5. Luxury Items",
                    "6. Personal Care",
                    "7. Transport",
                    # "8. General"
                ]
            )
            table.add_row(
                [
                    "9. Bills",
                    "10. Charity",
                    "11. Entertainment",
                    # "12. Gifts"
                ]
            )
            table.add_row(
                [
                    "13. Herbs, spices and sources",
                    "14. Holidays",
                    "15. Household chemicals",
                    # "16. Laundry",
                ]
            )
            # table.add_row(
            #     (
            #         [
            #             "17. Education",
            #             "18. Home Improvements",
            #             "19. Family Assistance",
            #             "20. Quit",
            #         ]
            #     )
            # )

        def item_name(item):
            """
            Once item selection is selected, then ask for price and update the monthly expenses dictionary
            :param item:
            :return:
            """
            while True:
                price = input("How much is this purchase?\n")
                valid = Validators(number=price, option=20)
                answer = valid.check_salary()

                if answer:
                    try:
                        monthly_expenses[item] += float(price)
                    except KeyError:
                        monthly_expenses[item] = float(price)
                    break

        def columns(lists, start_column):
            """
            Updates columns with data
            :param lists:
            :param start_column:
            :return:
            """
            for num in range(len(lists)):
                self.data_to_be_updated.append(
                    {"range": f"{start_column}{17+num}", "values": [[lists[num]]]}
                )

        def update_spreadsheet_with_expenses():
            """
            Updates spreadsheet when a Quit option is selected
            :return:
            """
            column1_title = []
            column1_price = []
            column2_title = []
            column2_price = []

            for key, value in monthly_expenses.items():
                if len(column1_title) < 15:
                    column1_title.append(key)
                    column1_price.append(value)
                else:
                    column2_title.append(key)
                    column2_price.append(value)

            columns(column1_title, "C")
            columns(column1_price, "G")
            columns(column2_title, "H")
            columns(column2_price, "L")

            self.__iter__("updating")
            self.data_to_be_updated = []
            print("All expense data has been updated")

        table_prettified()

        while True:
            # prints table to the terminal
            print(table)

            print("Option 20 will quit this menu and update spreadsheet")
            option = select_option()
            validator = Validators(number=option, option=20)
            check_answer = validator.check_number_and_option()

            if check_answer:
                match int(option):
                    case 1:
                        item_name("Clothing and Footwear")
                    case 2:
                        item_name("Technology")
                    case 3:
                        item_name("Groceries")
                    case 4:
                        item_name("Eating Out")
                    case 5:
                        item_name("Luxury Items")
                    case 6:
                        item_name("Personal Care")
                    case 7:
                        item_name("Transport")
                    case 8:
                        item_name("General")
                    case 9:
                        item_name("Bills")
                    case 10:
                        item_name("Charity")
                    case 11:
                        item_name("Entertainment")
                    case 12:
                        item_name("Gifts")
                    case 13:
                        item_name("Herbs, spices and sources")
                    case 14:
                        item_name("Holidays")
                    case 15:
                        item_name("Household chemicals")
                    case 16:
                        item_name("Laundry")
                    case 17:
                        item_name("Education")
                    case 18:
                        item_name("Home Improvements")
                    case 19:
                        item_name("Family Assistance")
                    case 20:
                        update_spreadsheet_with_expenses()
                        break


options = Options()
