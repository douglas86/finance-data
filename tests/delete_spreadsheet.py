from modules.settings import client


def delete_spreadsheet():
    title = []
    spreadsheet = client.open("finance")

    for sheet in client.open_all():
        title.append({"title": sheet.title, "id": sheet.id})
        print("titleBefore", title)

    for i in title:
        if i["title"] == "finance":
            spreadsheet.delete()
            print("titleAfter", title)
