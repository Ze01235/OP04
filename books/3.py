import csv

file_name = 'books.csv'

new_books = [
    {
        'Название': 'Война и мир',
        'Автор': 'Толстой',
        'Год издания': 1999
    },
    {
        'Название': 'Отцы и дети',
        'Автор': 'Тургенев',
        'Год издания': 2006
    },
]

with open(file_name,'a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    for item in new_books:
        writer.writerow([item['Название'], item['Автор'], item['Год издания']])

print(f'Данные успешно записаны в файл: {file_name}')