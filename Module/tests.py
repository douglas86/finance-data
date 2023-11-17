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


def daily_spending():
    column1 = []
    column2 = []

    table = PrettyTable()
    table.field_names = ["Column1", "Column2", "Column3", "Column4"]
    table.add_row(
        ["1. clothing and footwear", "2. Debit orders", "3. Groceries", "4. Eating Out"]
    )
    table.add_row(["5. Luxury Items", "6. Personal Care", "7. Transport", "8. General"])
    table.add_row(
        ["9. Monzo Flex (credit card)", "10. Bills", "11. Charity", "12. Entertainment"]
    )
    table.add_row(
        [
            "13. Gifts",
            "14. Herbs, spices and sources",
            "15. Holidays",
            "16. Household chemicals",
        ]
    )
    table.add_row(
        [
            "17. Laundry",
            "18. education",
            "19. Kitchen appliances and utensils",
            "20. Home Improvements",
        ]
    )

    print(table)

    number = select_option()
    validators = Validators(number=number, option=3)
    correct_answer = validators.check_number_and_option()

    if correct_answer:
        match int(number):
            case 1:
                print("clothing and footwear")
            case 2:
                print("Debit orders")
            case 3:
                print("Groceries")
            case 4:
                print("Eating Out")
            case 5:
                print("Luxury Items")
            case 6:
                print("Personal Care")
            case 7:
                print("Transport")
            case 8:
                print("General")
            case 9:
                print("Monzo Flex (credit card)")
            case 10:
                print("Bills")
            case 11:
                print("Charity")
            case 12:
                print("Entertainment")
            case 13:
                print("Gifts")
            case 14:
                print("Herbs, spices and sources")
            case 15:
                print("Holidays")
            case 16:
                print("Household chemicals")
            case 17:
                print("Laundry")
            case 18:
                print("education")
            case 19:
                print("Kitchen appliances and utensils")
            case 20:
                print("Home Improvements")
