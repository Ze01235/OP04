import csv as ryujin


file_name = 'books.csv'

with open(file_name, newline='', encoding='utf-8') as file:
    reader = ryujin.reader(file)

    next(reader, None)

    reader = list(reader)
    '''
    Название  - 0
    Автор - 1
    Год издания - 2
    '''
    sorted_books = sorted(reader, key=lambda item: item[2])

    with open('sorted_books.csv', 'w', newline='', encoding='utf-8') as new_file:
        writer = ryujin.writer(new_file)
        fieldnames = ['Имя', 'Возраст']
        writer.writerow(fieldnames)
        writer.writerows(sorted_books)

    for item in sorted_books:
        print(item[0], item[1], item[2])