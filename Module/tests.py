from prettytable import PrettyTable

from Module.settings import GSPREAD_CLIENT
from Module.validators import Validators
from utils.helpers import select_option


def delete_spreadsheet(file_id):
    """
    Deletes spreadsheet by file_id
    :param file_id: This can be found in the address bar for the current spreadsheet
    :return:
    """
    GSPREAD_CLIENT.del_spreadsheet(file_id=file_id)
    print("File deleted")


def c():
    column = {}
    print("c", column)
    while True:

        def item_name(item):
            price = input("How much is this purchase?\n")
            validators = Validators(number=price, option=2)
            amount = validators.check_number()
            if amount:
                try:
                    column[item] += float(price)
                except KeyError:
                    column[item] = float(price)

                print("columnB", column)

                print("column", column)

        def switch_case(options):
            match int(options):
                case 1:
                    item_name("Rent")
                case 2:
                    item_name("Debit orders")

        option = select_option()
        validators = Validators(number=option, option=2)
        check_answer = validators.check_number_and_option()

        if check_answer:
            switch_case(option)


# column1 = {}
# column2 = {}
#
#
# def daily_spending():
#     table = PrettyTable()
#
#     # Creates a neat table to be displayed
#     table.field_names = ["Column1", "Column2", "Column3", "Column4"]
#     table.add_row(
#         [
#             "1. Clothing and footwear",
#             "2. Debit orders",
#             "3. Groceries",
#             "4. Eating Out",
#         ]
#     )
#     table.add_row(["5. Luxury Items", "6. Personal Care", "7. Transport", "8. General"])
#     table.add_row(
#         [
#             "9. Monzo Flex (credit card)",
#             "10. Bills",
#             "11. Charity",
#             "12. Entertainment",
#         ]
#     )
#     table.add_row(
#         [
#             "13. Gifts",
#             "14. Herbs, spices and sources",
#             "15. Holidays",
#             "16. Household chemicals",
#         ]
#     )
#     table.add_row(
#         [
#             "17. Laundry",
#             "18. Education",
#             "19. Home Improvements",
#             "20. Quit",
#         ]
#     )
#
#     def update_expenses(item):
#         expense = input("Please enter the amount of the purchase?\n")
#         valid = Validators(number=expense, option=1)
#         check_salary = valid.check_number()
#
#         for key, value in column1.items():
#             try:
#                 check_salary == True
#             except TypeError:
#                 column1[item] = 0
#             else:
#                 column1[item] = float(value) + float(expense)
#
#     def check_lists(item):
#         if len(column1.keys()) < 15:
#             update_expenses(item)
#         else:
#             column2[item] = 0
#             update_expenses(item)
#
#     while True:
#         print(table)
#
#         items = select_option()
#         validators = Validators(number=items, option=20)
#         correct_answer = validators.check_number_and_option()
#
#         if correct_answer:
#             match int(items):
#                 case 1:
#                     check_lists("Clothing and Footwear")
#                 case 2:
#                     check_lists("Debit orders")
#                 case 3:
#                     check_lists("Groceries")
#                 case 4:
#                     check_lists("Eating Out")
#                 case 5:
#                     check_lists("Luxury Items")
#                 case 6:
#                     check_lists("Personal Care")
#                 case 7:
#                     check_lists("Transport")
#                 case 8:
#                     check_lists("General")
#                 case 9:
#                     check_lists("Monzo Flex (credit card)")
#                 case 10:
#                     check_lists("Bills")
#                 case 11:
#                     check_lists("Charity")
#                 case 12:
#                     check_lists("Entertainment")
#                 case 13:
#                     check_lists("Gifts")
#                 case 14:
#                     check_lists("Herbs, spices and sources")
#                 case 15:
#                     check_lists("Holidays")
#                 case 16:
#                     check_lists("Household chemicals")
#                 case 17:
#                     check_lists("Laundry")
#                 case 18:
#                     check_lists("Education")
#                 case 19:
#                     check_lists("Home Improvements")
#                 case 20:
#                     break
#
#     print("column1", column1)
#     print("column2", column2)
