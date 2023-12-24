from datetime import datetime
import json
from operator import itemgetter


def print_operations(operations):
    for operation in operations:
        print(normalize_date(operation['date']), operation['description'])
        try:
            print(card_num_converter(operation['from']) + ' -> ' + card_num_converter(operation['to']))
        except:
            print(card_num_converter(operation['to']))
        print(operation['operationAmount']['amount'], operation['operationAmount']['currency']['name'])
        print()


def load_json():
    with open('../utils/operations.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    sorted_data = []
    try:
        for el in data:
            if "date" not in el:
                data.remove(el)
            elif el['state'] == 'EXECUTED':
                data.remove(el)
        sorted_data = sorted(data, key=itemgetter('date'), reverse=True)
    except Exception as e:
        pass
    return sorted_data[:5]
    # return sorted_data[:5]


def normalize_date(date):
    date_obj = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%f')
    return date_obj.strftime('%d.%m.%Y')


def card_num_converter(card):
    mask_list = [6, 7, 8, 9, 10, 11]
    masked_card_num = ""
    if "Счет" in card:
        return f"Счет **{card[len(card) - 4:]}"
    else:
        card = card.split(" ")
        try:
            int(card[1])
            card_name = card[0]
            card_num = str(card[1])
        except:
            card_name = card[0] + card[1]
            card_num = str(card[2])
        for i in range(0, len(card_num)):
            if i in mask_list:
                masked_card_num += "*"
            else:
                masked_card_num += card_num[i]
            if (i == 3) | (i == 7) | (i == 11):
                masked_card_num += " "
        return f"{card_name} {masked_card_num}"
