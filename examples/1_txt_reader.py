from files import TXT_FILE_PATH

some_file = open(TXT_FILE_PATH, "r")

# print(some_file.read(7))

# print(some_file.readline())
#
# print(some_file.readlines(), "\n")

print(some_file.read())

# вернуть курсор
# print(some_file.readline())
some_file.seek(0)
# print(some_file.readline())

some_file.close()
