import re

re_card_id = r"Card\s*(\d+).*"
re_number = r"(\d+)"


def get_card_id_and_data(line: [str]):
    split_line = line.split(':')
    card_id = re.search(re_card_id, split_line[0])[1]
    card_data = split_line[1]

    return int(card_id), card_data


def data_to_numbers(data: str) -> [int]:
    return re.finditer(re_number, data)


def number_of_matches(data: str):
    winning_num_string = data.split('|')[0]
    played_num_string = data.split('|')[1]
    winning_numbers = [int(i.group(0)) for i in data_to_numbers(winning_num_string)]
    played_numbers = [int(i.group(0)) for i in data_to_numbers(played_num_string)]

    matches = [number for number in winning_numbers if number in played_numbers]
    return len(matches)


def point_value(num_matches: int):
    if num_matches == 0:
        return 0
    else:
        return pow(2, num_matches-1)


card_stack = [line for line in open('4/input.txt')]
card_count = {1: 1}

for card in card_stack:
    card_id, card_data = get_card_id_and_data(card)
    num_matches = number_of_matches(card_data)
    if num_matches == 0:
        card_count.setdefault(card_id, 1)
    for new_card_id in range(card_id+1, card_id+num_matches+1):
        card_count.setdefault(new_card_id, 1)
        card_count.setdefault(card_id, 1)
        card_count[new_card_id] += card_count[card_id]
    

card_total = 0
for card_id, card_copies in card_count.items():
    card_total += card_copies
print(card_total)