import re


def letters_to_number(number: str) -> str:
    match number:
        case "one":
            return '1'
        case "two":
            return '2'
        case "three":
            return '3'
        case "four":
            return '4'
        case "five":
            return '5'
        case "six":
            return '6'
        case "seven":
            return '7'
        case "eight":
            return '8'
        case "nine":
            return '9'
        case _:
            return number


def get_first_digit(line: str) -> str:

    return letters_to_number(re.search('(\d|one|two|three|four|five|six|seven|eight|nine)(.*)', line).group(1))


def get_last_digit(line: str) -> str:

    return letters_to_number(re.search('(.*)(\d|one|two|three|four|five|six|seven|eight|nine)', line).group(2))


total: int = 0
for line in open('1/input.txt'):
    # compose the two digits in a string and then cast to int
    # before updating total
    total += int(get_first_digit(line) + get_last_digit(line))

print(total)