import datetime

def new_dict_format_data(str):
    """функция преобразует дату из строкового формата в класс date"""
    if 'T' in str:
        new_list = str.split('T')
        new_list.pop(-1)
        new_str = ''.join(new_list)
        return datetime.date.fromisoformat(new_str)
    else:
        return datetime.date.fromisoformat(str)

def sorted_dict(dict):
    """функция сортирует список словарей по убыванию даты"""
    return sorted(dict, key=lambda x: x['date'], reverse=True)


def mask_for_str_with_from(str) -> str:
    new_list = str.split(' ')
    new_list[-1] = f"{new_list[-1][:4]} {new_list[-1][4:6]}** **** {new_list[-1][-4:]}"
    return ' '.join(new_list)

def mask_for_str_with_to(str) -> str:
    new_list = str.split(' ')
    new_list[-1] = f"**{new_list[-1][-4:]}"
    return ' '.join(new_list)
