from files import TXT_FILE_PATH

with open(TXT_FILE_PATH, "r") as file:
    print(file.read())
    # не нужно закрывать файл каждый раз

print("\n", 20 * "*", "\n")

with open(TXT_FILE_PATH, "r") as file:
    for line in file.readlines():
        print(line, end=' ')
