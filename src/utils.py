import datetime

def new_dict_format_data(file):
    """функция преобразует дату из строкового формата в класс date"""
    for item in file:
        item['date'] = datetime.date.fromisoformat((item['date'])[:10])

def sorted_dict(dict):
    """функция сортирует список словарей по убыванию даты"""
    return sorted(dict, key=lambda x: x['date'], reverse=True)


def format_str(from_to, i=0):
    """функция форматирует вывод по заданным условиям"""
    if 'from' in from_to[i].keys():
        new_from = from_to[i]['from'].split(' ')
        new_from[-1] = f"{new_from[-1][:4]} {new_from[-1][6:8]}" \
                       f"** ****{new_from[-1][-4:]}"

        new_to = f"**{from_to[i]['to'][-4:]}"

        print(f"{' '.join(new_from)}-> {new_to}")

    elif 'from' not in from_to[i].keys():
        new_to = f"**{from_to[i]['to'][-4:]}"
        print(f"-> {new_to}")
