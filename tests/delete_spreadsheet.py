from modules.settings import gc


def delete_spreadsheet():
    title = []

    for spreadsheet in gc.openall():
        title.append({"title": spreadsheet.title, "id": spreadsheet.id})
        print("titleBefore", title)

    for i in title:
        if i["title"] == "finance":
            gc.del_spreadsheet(i["id"])
            print("titleAfter", title)
