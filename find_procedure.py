import os

migrations = 'Migrations'
current_dir = os.path.dirname(os.path.abspath(__file__))


def find_sql_files(dirname):
    files = os.listdir(dirname)
    list_of_sql_files = []
    for i in files:
        if i.endswith('.sql'):
            list_of_sql_files.append(os.path.join(migrations, i))
    return list_of_sql_files


def find_string_in_files(search_string, list_of_files):
    list_of_inclusions = []
    if len(list_of_files) == 0:
        list_of_files = find_sql_files(migrations)
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
