from Module.settings import client


def get_initial_data():
    spreadsheet = client.open("2023")
    # spreadsheet.share("douglasmaxton@gmail.com", role="writer")
    worksheet = spreadsheet.worksheet("index", 12)
    # client.drive.delete("1DqEqGNF-9oNQeMwmmEBt3fuPq8DPnDPHGB-2Ep3_Aqw")

    print(spreadsheet)
    print(worksheet)
