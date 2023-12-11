import csv as yeji

new_file_name = input(f'Введите имя нового файла: ')
new_file_name += '.csv'


with open(new_file_name, 'w', newline='', encoding='utf-8') as file:
    books_data = [
        {'Название': 'Мать', 'Автор': 'Горький', 'Год издания': 1998},
        {'Название': 'Легкое дыхание', 'Автор': 'Бунин', 'Год издания': 1997},
    ]

    writer = yeji.writer(file)
    for item in books_data:
        writer.writerow([item['Название'], item['Автор'], item['Год издания']])

with open(new_file_name, newline='', encoding='utf-8') as file:
    reader = yeji.reader(file)

    for item in reader:
        print(item[0], item[1], item[2])