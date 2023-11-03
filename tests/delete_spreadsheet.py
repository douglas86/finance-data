from modules.settings import user


def delete_spreadsheet():
    title = []
    spreadsheet = user.open("finance")

    for sheet in user.open_all():
        title.append({"title": sheet.title, "id": sheet.id})
        print("titleBefore", title)

    for i in title:
        if i["title"] == "finance":
            spreadsheet.delete()
            print("titleAfter", title)
