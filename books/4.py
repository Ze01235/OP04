import csv

file_name = 'books.csv'

target_letter = input("Введите букву: ")

with open(file_name, encoding='utf-8') as file:
    reader = csv.reader(file)

    next(reader, None)

    for item in reader:
        book_name = item[1]
        if book_name and book_name.startswith(target_letter):
            print(book_name)