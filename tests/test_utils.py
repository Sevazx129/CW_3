from src.utils import mask_for_str_with_from, mask_for_str_with_to, new_dict_format_data, sorted_dict
import datetime
import json

with open('src/operations.json', 'r', encoding='utf-8') as file:
    executions = json.load(file)

def test_new_dict_format_data():
    assert new_dict_format_data('2019-08-26T10:50:58.29404') == datetime.date(2019, 8, 26)
    assert new_dict_format_data('2022-12-23') == datetime.date(2022, 12, 23)
    assert new_dict_format_data('2011-11-02T1232123') == datetime.date(2011, 11, 2)

def test_mask_for_str_with_from():
    assert mask_for_str_with_from("tinkoff black 1234432156783516") == "tinkoff black" \
                                                                       " 1234 43** **** 3516"
    assert mask_for_str_with_from("pochta_bank 1234432156783516") == "pochta_bank" \
                                                                       " 1234 43** **** 3516"

def test_mask_for_str_with_from():
    assert mask_for_str_with_to("счёт 32324212494345839") == "счёт **5839"
    assert mask_for_str_with_to("перевод бабушке 32324212494341232123") == "перевод бабушке **2123"

new_executions = sorted_dict(executions)

def test_sorted_dict():
    assert sorted_dict(executions) == new_executions
