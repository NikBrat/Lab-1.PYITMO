import csv

count = -1  # счётчик записей
Count30 = 0  # счётчик записей, название которых содерит более 30 символов
author_books = []  # список, в который будут записываться результат поиска по автору(c возможными повторами )
top_20 = []  # список со всеми книгами и их кол-вом выдачи
tp_20 = []  # итоговый список Топ-20 книг, без повторов
tp20 = open('Топ 20.txt', 'w+')  # файл c топ-20 книгами
tp20.write("Топ-20 Книг:\n")
tags = []  # Cписок тегов(для проверки на повтор)
d = False  # "Флажок", необходимый для поиска
f = open("bib_links.txt", "w")  # создание текстого файла для генератора библиографических ссылок
tg = open("Tags.txt", "w")  # текстовый файл со всеми тегами
tg.write('Список тэгов:\n')
num = int(
    input(
        "Введите число (не более 9389) для генератора библиографических ссылок: "))  # число для генератора
# библиографических ссылок
print("Поиск книги по автору")
name_author = input("\nВведите Имя и Фамилию автора: ")
with open('books.csv', encoding='cp1251') as r_file:
    book_list = csv.DictReader(r_file, delimiter=';')
    for row in book_list:

        count += 1

        if count > 0:  # Условия для создания файла с тэгами
            for n in row["Жанр книги"].replace('# ', '#').split('#'):
                if n not in tags:
                    tags.append(n)
                    tg.write(f'{n}\n')

        if count > 0:
            top_20.append((int(row["Кол-во выдач"]), row["Название"]))

        if num <= count < num + 20:  # Генератор библиографических ссылок
            f.write(f"""{count - num + 1}. ({row['Автор']}). "{row['Название']}" - {row['Дата поступления'][6:10]}\n""")

        if len(row["Название"]) > 30:  #
            Count30 += 1

        if row["Автор"] == name_author or row["Автор (ФИО)"] == name_author:
            if float(row["Цена поступления"]) <= 200:  # ограничение на выдачу книг(До 200 рублей)
                author_books.append(row["Название"])
                d = True

    a = set(author_books)  # избавляемся от повторяющихся наименований книг, полученных при поиске по автору
    b = list(a)
    if not d:  # Для случая, когда результаты поиска не будут удовлетворительными
        print("Ничего не найдено")
    else:
        print(f"Результаты поиска:\nКниги автора {name_author}:")
    for i in range(len(b)):
        print(f'{i + 1}. {b[i]}')

    a = input('\nВывести число записей в файле (Да, Нет): ')
    if a == 'Да':
        print(f'Число записей - {count}')
        print(F"\nKоличество записей, у которых в поле 'Название' строка длиннее 30 символов: {Count30}")

    if len(tags) > 0:
        print('\nВсе тэги находятся в файле Tags.txt')

    print('\nБиблиографические ссылки находятся в файле bib_links.txt')
    if num > 9389:
        print("Файл bib_links.txt содержит менее 20 ссылок!")
    if num > 9410:
        print("Файл bib_links.txt не содержит ссылок")

    top_20 = sorted(top_20, key=lambda x: x[0])
    k = -1
    while len(tp_20) < 20:
        if top_20[k][1] not in tp_20:
            tp_20.append(top_20[k][1])
        k -= 1
    for i in range(len(tp_20)):
        tp20.write(f'\n{i+1}. {tp_20[i]}')
    print("\nСписок Топ-20 книг находится в файле Топ 20.txt")
    tp20.close()
    f.close()
    tg.close()
    r_file.close()

pb = open("Publishers.txt", "w")  # текстовый файл со всеми издателями
pb.write("List of publishers:\n")
publishers = []  # Список издательств(для проверки на повтор)
count_en = 0
with open('books-en.csv', encoding='cp1251') as l_file:
    book_list = csv.DictReader(l_file, delimiter=';')
    for row in book_list:

        count_en += 1

        if count_en > 0:  # Условия для создания файла с издательствами
            if row["Publisher"] not in publishers:
                publishers.append(row["Publisher"])
                pb.write(f'\n{row["Publisher"]}')
    print('\nВсе издательства находятся в файле Publishers.txt\n')
    pb.close()
    l_file.close()
