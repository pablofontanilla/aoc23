import re


def get_first_digit(line: str) -> str:

    return re.search('(\d)(.*)', line).group(1)


def get_last_digit(line: str) -> str:

    return re.search('(.*)(\d)', line).group(2)


total: int = 0
for line in open('1/input.txt'):
    # compose the two digits in a string and then cast to int
    # before updating total
    total += int(get_first_digit(line) + get_last_digit(line))

print(total)