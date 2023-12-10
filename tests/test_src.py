import pytest
import os
from src import load_json, filter_data, sort_data, edit_date, replace_number, print_operation


@pytest.fixture
def test_func():
    return os.path.join("operations.json")


def test_load_json(test_func):
    assert load_json('test_load_json.json') == [{
    "word": "питон",
     "subwords":  [
         "пони", "тон", "ион", "опт", "пот", "тип", "топ", "пион", "понт"]
}]

def test_filter_data():
    assert filter_data([{
    "id": 895315941,
    "state": "EXECUTED",
    "date": "2018-08-19T04:27:37.904916",
    "operationAmount": {
      "amount": "56883.54",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    }},
{
    "id": 594226727,
    "state": "CANCELED",
    "date": "2018-09-12T21:27:25.241689",
    "operationAmount": {
        "amount": "67314.70",
        "currency": {
            "name": "руб.",
            "code": "RUB"
        }
    },
    "description": "Перевод организации",
    "from": "Visa Platinum 1246377376343588",
    "to": "Счет 14211924144426031657"
}]) == [{
    "id": 895315941,
    "state": "EXECUTED",
    "date": "2018-08-19T04:27:37.904916",
    "operationAmount": {
      "amount": "56883.54",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    }}]


def test_sort_data():
    assert sort_data([{"date": "2018-12-20T16:43:26.929246"},
                     {"date": "2019-07-12T20:41:47.882230"},
                     {"date": "2018-08-19T04:27:37.904916"}]) == [{"date": "2019-07-12T20:41:47.882230"},
                                                                  {"date": "2018-12-20T16:43:26.929246"},
                                                                  {"date": "2018-08-19T04:27:37.904916"}]


def test_edit_date():
    assert edit_date("2019-08-26T10:50:58.294041") == "26.08.2019"
    assert edit_date("2018-06-30T02:08:58.425572") == "30.06.2018"
    assert edit_date("2018-03-23T10:45:06.972075") == "23.03.2018"

#
def test_replace_number():
    assert replace_number("Счет 48894435694657014368") == "Счет **4368"
    assert replace_number("Visa Classic 6831982476737658") == "Visa Classic 6831 98** **** 7658"
    assert replace_number("Maestro 3928549031574026") == "Maestro 3928 54** **** 4026"
    assert replace_number("") == ""


def test_print_operation():
    pass
