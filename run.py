from Module.dates import current_year
from gspread.exceptions import SpreadsheetNotFound

from testing.delete_spreadsheet import delete_spreadsheet
from Module.settings import GSPREAD_CLIENT, client


def main():
    """
    This is the main function that runs the entire program
    :return:
    """

    # template.create_template()

    # Deleted spreadsheet
    delete_spreadsheet(
        gspread_client=GSPREAD_CLIENT,
        file_id="1nWidrsIuKUJW97d7JvuWt9l2BVSLQOrHmUcVsipiGYA",
    )

    # check to see if the spreadsheet with current_year is created
    try:
        client.open(
            title=str(current_year), folder_id="1jDCB53uToJ7nDm5_vxZr7019Zje9RmcX"
        )
        print("spreadsheet open")
    except SpreadsheetNotFound:
        client.copy(
            file_id="1-M5rHQY78wq_VWDUWLhz2hZvux3lY9y7lOT7PY4uGS0",
            title=current_year,
            copy_permissions=True,
            folder_id="1jDCB53uToJ7nDm5_vxZr7019Zje9RmcX",
        )
        print(f"{current_year} spreadsheet created")
        this_years_spreadsheet = client.open(title=str(current_year))
        fetch = this_years_spreadsheet.worksheet("data").batch_get(["D9:O24"])

        place_correct_values = this_years_spreadsheet.sheet1.batch_update(
            [
                {"range": "A1", "values": [[int(current_year)]]},
                {
                    "range": "BE5:DP5",
                    "values": [int(x) for x in fetch[0][0]],
                },
                {
                    "range": "BE6:DP6",
                    "values": [fetch[0][1]],
                },
                {
                    "range": "BE7:DP7",
                    "values": [fetch[0][2]],
                },
                {
                    "range": "BE8:DP8",
                    "values": [fetch[0][3]],
                },
                {
                    "range": "BE9:DP9",
                    "values": [fetch[0][4]],
                },
                {
                    "range": "BE10:DP10",
                    "values": [fetch[0][5]],
                },
                {
                    "range": "BE11:DP11",
                    "values": [fetch[0][6]],
                },
                {
                    "range": "BE12:DP12",
                    "values": [fetch[0][7]],
                },
                {
                    "range": "BE13:DP13",
                    "values": [fetch[0][8]],
                },
                {
                    "range": "BE14:DP14",
                    "values": [fetch[0][9]],
                },
                {
                    "range": "BE15:DP15",
                    "values": [fetch[0][10]],
                },
                {
                    "range": "BE16:DP16",
                    "values": [fetch[0][11]],
                },
                {
                    "range": "BE17:DP17",
                    "values": [fetch[0][12]],
                },
                {
                    "range": "BE18:DP18",
                    "values": [fetch[0][13]],
                },
                {
                    "range": "BE19:DP19",
                    "values": [fetch[0][14]],
                },
                {
                    "range": "BE20:DP20",
                    "values": [fetch[0][15]],
                },
            ]
        )
        print("fetch", [int(x) for x in fetch[0][0]])
        print("placed", place_correct_values)


main()
