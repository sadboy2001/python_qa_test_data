import csv
from csv import DictReader

from files import CSV_FILE_PATH

with open(CSV_FILE_PATH, newline='') as f:
    reader = csv.reader(f)

    # Извлечение заголовка
    header = next(reader)

    # Итерируемся по данным делая из них словари
    for row in reader:
        print(dict(zip(header, row)))


# with open('../files/users.csv', newline='') as f:
#     reader = DictReader(f)
#
#     # Итерируемся по данным делая из них словари
#     for row in reader:
#         print(row)
