from Module.settings import file_list
from Module.template import template


def main():
    """
    This is the main function that runs the entire program
    :return:
    """
    files_in_folder = {}

    for file in file_list:
        files_in_folder[file["title"]] = file["id"]
        print(f'title: {file["title"]} id: {file["id"]}')

    template.copy_file()

    print(files_in_folder)


main()
