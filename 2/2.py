import re


red_cubes_in_bag = 12
green_cubes_in_bag = 13
blue_cubes_in_bag = 14

re_game_id_game_data = 'Game (\d+):(.*)'


def get_re_for_color(color: str):
    return f'(\d+) {color}'


def max_for_color(game_data: str, color: str) -> int:
    results = re.findall(get_re_for_color(color), game_data)
    int_results = []
    for result in results:
        int_results.append(int(result))
    return max(int_results)


def is_valid_game(game_data: str) -> bool:
    max_red = max_for_color(game_data, 'red')
    max_blue = max_for_color(game_data, 'blue')
    max_green = max_for_color(game_data, 'green')
    print(f'Max red cubes: {max_red}, max blue clubes: {max_blue} and max green cubes: {max_green}')
    if (max_red <= red_cubes_in_bag) and (max_blue <= blue_cubes_in_bag) and (max_green <= green_cubes_in_bag):
        return True
    return False


def get_game_power(game_data: str) -> int:
    max_red = max_for_color(game_data, 'red')
    max_blue = max_for_color(game_data, 'blue')
    max_green = max_for_color(game_data, 'green')
    return max_blue*max_green*max_red


def extract_game_id_game_data(line: str) -> tuple[str,str]:
    match = re.search(re_game_id_game_data, line)
    return match.group(1), match.group(2)


game_power_total = 0
for line in open('2/input.txt'):
    game_id, game_data = extract_game_id_game_data(line)
    game_power = get_game_power(game_data=game_data)
    print(f'Game {game_id} has {game_power} power')
    game_power_total += game_power

print(game_power_total)