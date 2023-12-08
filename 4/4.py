import re

re_card_id = r"Card (\d+)"
re_number = r"(\d+)"


def get_card_id_and_data(line: [str]):
    split_line = line.split(':')
    card_id = re.match(re_card_id, split_line[0])
    card_data = split_line[1]

    return card_id, card_data


def data_to_numbers(data: str) -> [int]:
    return re.finditer(re_number,data)


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


total_value = 0
for play in open('4/input.txt'):
    card_id, card_data = get_card_id_and_data(play)
    total_value += point_value(number_of_matches(card_data))

print(total_value)