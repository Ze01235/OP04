import csv

file_name = 'books.csv'

with open(file_name, newline='', encoding='utf-8') as file:
    reader = csv.reader(file)

    next(reader, None)

    reader = list(reader)

    for item in reader:
        print(item[0], item[1], item[2])

    remove = input("Введите автора книги, которую хотите удалить:")

    remove_books = [item for item in reader if item[1] != remove]

    with open(file_name, 'w', newline='', encoding='utf-8') as new_file:
        writer = csv.writer(new_file)
        fieldnames = ['Название', 'Автор', 'Год издания']
        writer.writerow(fieldnames)
        writer.writerows(remove_books)
print(f'Книга автора {remove} успешно удалена из файла: {file_name}')

for item in remove_books:
    print(item[0], item[1], item[2])