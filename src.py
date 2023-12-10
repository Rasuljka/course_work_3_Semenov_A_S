import json
from datetime import datetime


def load_json(file_name):
    """'Загружает данные из файла"""
    with open(file_name, 'r', encoding='UTF-8') as f:
        return json.load(f)


def filter_data(data):
    """Фильтрует данные"""
    data = [element for element in data if element and element['state'] == 'EXECUTED']
    return data


def sort_data(data):
    """Сортирует данные"""
    data = sorted(data, key=lambda x: x['date'], reverse=True)
    return data[:7]


def edit_date(date: str):
    """Изменяет формат времени на новый"""
    date = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%f")
    date = datetime.strftime(date, "%d.%m.%Y")
    return date


def replace_number(string_number):
    """Шифрует нужные цифры"""
    text_list = string_number.split()
    try:
        replace_number = ", ".join(([text_list[-1][length:length + 4] for length in range(0, len(text_list[-1]), 4)]))
    except IndexError:
        return ""
    replace_number_min = replace_number.replace(",", "")
    if text_list[0] != "Счет":
        replace_number_finally = replace_number_min[:7] + "** ****" + replace_number_min[-5:]
    else:
        replace_number_finally = "**" + replace_number_min[-4:]
    text_list_replace = text_list[:-1]
    text_list_replace.append(replace_number_finally)
    text_replace = ", ".join(text_list_replace).replace(",", "")
    return text_replace


def print_operation(data) -> list:
    """Возвращает операции в нужном формате"""
    operations = []
    for operation in data:
        try:
            date = edit_date(operation["date"])
            from_who = replace_number(operation["from"])
            to_who = replace_number(operation["to"])

            operations.append(f'{date} {operation["description"]}')
            operations.append(f'{from_who} -> {to_who}')
            operations.append(f'{operation["operationAmount"]["amount"]} '
                              f'{operation["operationAmount"]["currency"]["name"]}'
                              f'\n')
        except KeyError:
            continue
    return operations


for operation in print_operation(sort_data(filter_data(load_json('operations.json')))):
    print(operation)
