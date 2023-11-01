def title_formatting(worksheet, cell_value_starts_at, month_name):
    """
    Formats the Month name title
    :param worksheet:
    :param cell_value_starts_at:
    :param month_name:
    :return:
    """

    worksheet.merge_cells(f"B{cell_value_starts_at}:I{cell_value_starts_at+3}")
    worksheet.update(f"B{cell_value_starts_at}", month_name)

    worksheet.format(
        f"B{cell_value_starts_at}",
        {
            "horizontalAlignment": "CENTER",
            "verticalAlignment": "MIDDLE",
            "backgroundColor": {"red": 0.1, "green": 0.9, "blue": 0.3},
            "textFormat": {
                "foregroundColor": {"red": 0.0, "green": 0.1, "blue": 0.0},
                "fontSize": 40,
                "bold": True,
            },
            "borders": {
                "top": {
                    "style": "SOLID",
                    "width": 1,
                    "colorStyle": {"rgbColor": {"red": 0.0, "green": 0.1, "blue": 0.0}},
                },
                "bottom": {
                    "style": "SOLID",
                    "width": 1,
                    "colorStyle": {"rgbColor": {"red": 0.0, "green": 0.1, "blue": 0.0}},
                },
                "left": {
                    "style": "SOLID",
                    "width": 1,
                    "colorStyle": {"rgbColor": {"red": 0.0, "green": 0.1, "blue": 0.0}},
                },
                "right": {
                    "style": "SOLID",
                    "width": 1,
                    "colorStyle": {"rgbColor": {"red": 0.0, "green": 0.1, "blue": 0.0}},
                },
            },
        },
    )

    return worksheet
