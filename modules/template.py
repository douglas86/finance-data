from modules.settings import gc


def create_spreadsheet():
    """
    Creates a Spreadsheet and shares it with my email address
    :return:
    """
    sh = gc.create("finance")
    sh.share("douglasmaxton@gmail.com", perm_type="user", role="writer")
    print("Spreadsheet created")
