import json
from utils import new_dict_format_data, sorted_dict, format_str


with open('operations.json', 'r', encoding='utf-8') as file:
    executions = json.load(file)


new_dict_format_data(executions)
new_executions = sorted_dict(executions)


counter = 0
while counter < 5:
    print(new_executions[counter]['date'].strftime("%d.%m.%Y"),
          new_executions[counter]['description'])

    format_str(new_executions, counter)

    print(new_executions[counter]['operationAmount']['amount'], "руб.\n")

    counter += 1
