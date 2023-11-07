from Module.settings import file_list


def main():
    """
    This is the main function that runs the entire program
    :return:
    """

    for file in file_list:
        print(f'{file["title"]}')


main()
