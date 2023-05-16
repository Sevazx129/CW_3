import json

from src.utils import format_str, sorted_dict

with open('operations.json', 'r', encoding='utf-8') as file:
    executions = json.load(file)

new_executions = sorted_dict(executions)


def test_sort():
    assert sorted_dict(executions) == new_executions


