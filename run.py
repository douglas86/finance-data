from modules.settings import gc


def main():
    print("The json file is")
    sh = gc.open("love_sandwiches")
    print(sh)
    print("file opened")


main()
