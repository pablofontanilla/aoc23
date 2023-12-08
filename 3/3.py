import re
from re import Match
re_number = r"(\d+)+"
re_symbol = r"[^\w\.]"
input_file = '3/input.txt'


def get_numbers_in_line(line: str) -> [Match]:
    return re.finditer(re_number, line)


def get_substring(line: str, start_pos: int, end_pos: int):
    # calculate substring taking into account that we might be at beggining or end of string
    segment = line[start_pos:end_pos+1]
    return segment


def is_there_symbol_in_string(substring: str) -> bool:
    if substring:
        is_symbol = re.search(re_symbol, substring)
        return is_symbol
    return False


def is_there_adjacent_symbol(line_number: int, start_pos: int, end_pos: int, map: [str]) -> bool: 
    left_pos = start_pos - 1 if start_pos != 0 else start_pos
    right_pos = end_pos + 1 if end_pos != len(map[line_number])-1 else end_pos

    adjacent_segment_above = get_substring(map[line_number-1], left_pos, right_pos) \
        if line_number != 0 else None
    adjacent_segment_below = get_substring(map[line_number+1], left_pos, right_pos) \
        if line_number != len(map)-1 else None
    adjacent_character_left = map[line_number][left_pos]
    adjacent_character_right = map[line_number][right_pos]

    if is_there_symbol_in_string(adjacent_segment_above) or \
       is_there_symbol_in_string(adjacent_segment_below) or \
       is_there_symbol_in_string(adjacent_character_left) or \
       is_there_symbol_in_string(adjacent_character_right):
        return True
    else:
        return False


def construct_map(file) -> [str]:
    map = []
    for line in open(file):
        map.append(line.strip())
    return map


engine_map = construct_map(file=input_file)
part_sum = 0
line_number = 0
for line in engine_map:
    for match in get_numbers_in_line(line):
        if is_there_adjacent_symbol(line_number, match.start(), match.end()-1, engine_map):
            part_sum += int(match.group(0))
            print(f'Number {match.group(0)} in line {line_number} is engine part')
    line_number += 1

print(part_sum)
