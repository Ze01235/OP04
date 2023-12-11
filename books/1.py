import csv


books_list = [
    {
        'Название': 'Евгений Онегин',
        'Автор': 'Пушкин',
        'Год издания': 2000
    },
    {
        'Название': 'Мцыри',
        'Автор': 'Лермонтов',
        'Год издания': 2001
    },
    {
        'Название': 'Мертвые души',
        'Автор': 'Гоголь',
        'Год издания': 2005
    },
]

file_name = 'books.csv'

with open(file_name, 'w', newline='', encoding='utf-8') as file:
    fieldnames = ['Название', 'Автор', 'Год издания']
    writer = csv.DictWriter(file, fieldnames)

    writer.writeheader()
    for item in books_list:
        writer.writerow(item)

print(f'Создан новый файл: {file_name}')