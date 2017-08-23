# Задание
# мне нужно отыскать файл среди десятков других
# я знаю некоторые части этого файла (на память или из другого источника)
# я ищу только среди .sql файлов
# 1. программа ожидает строку, которую будет искать (input())
# после того, как строка введена, программа ищет её во всех файлах
# выводит список найденных файлов построчно
# выводит количество найденных файлов
# 2. снова ожидает ввод
# поиск происходит только среди найденных на этапе 1
# 3. снова ожидает ввод
# ...
# Выход из программы программировать не нужно.
# Достаточно принудительно остановить, для этого можете нажать Ctrl + C

# Пример на настоящих данных

# python3 find_procedure.py
# Введите строку: INSERT
# ... большой список файлов ...
# Всего: 301
# Введите строку: APPLICATION_SETUP
# ... большой список файлов ...
# Всего: 26
# Введите строку: A400M
# ... большой список файлов ...
# Всего: 17
# Введите строку: 0.0
# Migrations/000_PSE_Application_setup.sql
# Migrations/100_1-32_PSE_Application_setup.sql
# Всего: 2
# Введите строку: 2.0
# Migrations/000_PSE_Application_setup.sql
# Всего: 1

# не забываем организовывать собственный код в функции

import os

migrations = 'Migrations'
current_dir = os.path.dirname(os.path.abspath(__file__))

if __name__ == '__main__':
    def find_sql_files(dirname):
        files = os.listdir(dirname)
        list_of_sql_files = []
        for i in files:
            if i.endswith('.sql'):
                list_of_sql_files.append(i)
        return list_of_sql_files

    def find_string_in_files(search_string, list_of_files):
        list_of_inclusions = []
        if len(list_of_files) == 0:
            list_of_files = find_sql_files(migrations)
            for i in list_of_files:
                file = os.path.join(migrations, i)
                with open(file, 'r') as f:
                    data = f.read()
                    if data.find(search_string) != -1:
                        list_of_inclusions.append(file)
        else:
            for i in list_of_files:
                with open(i, 'r') as f:
                    data = f.read()
                    if data.find(search_string) != -1:
                        list_of_inclusions.append(i)
        return list_of_inclusions

    def main():
        search_files = []
        while True:
            search_string = input('Введите строку:')
            search_files = find_string_in_files(search_string, search_files )
            if len(search_files) >= 3:
                print('... большой список файлов ...')
            else:
                for i in search_files:
                    print(i)
            print('Всего:', len(search_files))

    main()
    pass