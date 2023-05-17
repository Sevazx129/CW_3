import json
from utils import new_dict_format_data, sorted_dict, mask_for_str_with_from, mask_for_str_with_to


with open('operations.json', 'r', encoding='utf-8') as file:
    executions = json.load(file)

for item in executions:
    item['date'] = new_dict_format_data(item['date'])

new_executions = sorted_dict(executions)


counter = 0
while counter < 5:
    print(new_executions[counter]['date'].strftime("%d.%m.%Y"),
          new_executions[counter]['description'])

    if 'from' in new_executions[counter].keys():
        new_from = mask_for_str_with_from(new_executions[counter]['from'])
        new_to = mask_for_str_with_to(new_executions[counter]['to'])
        print(new_from, '->', new_to)
    else:
        new_to = mask_for_str_with_to(new_executions[counter]['to'])
        print('->', new_to)

    print(new_executions[counter]['operationAmount']['amount'], "руб.\n")

    counter += 1
