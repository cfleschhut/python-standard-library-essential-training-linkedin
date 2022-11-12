def write_file():
    with open("testfile.txt", "w") as fp:
        fp.write("Some text\n")


def read_file():
    with open("testfile.txt", "r") as fp:
        data = fp.read()
        print(data)


def add_to_file():
    with open("testfile.txt", "a+") as fp:
        fp.write("Data added onto file\n")

        fp.seek(0)
        data = fp.read()

        print(data)


write_file()
read_file()
add_to_file()
