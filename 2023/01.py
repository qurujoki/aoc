import re

DATA = open("01.txt").readlines()
DIGIT_WORD_MAP = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def calibrate(line: str) -> int:
    digits = [int(i) for i in line if i.isdigit()]
    if not digits:
        return
    # Combine first and last digit by multiplying the first digit with 10.
    # For example, [4, 3, 2] --> 42.
    return digits[0] * 10 + digits[-1]


def convert_valid_digits(line: str) -> str:
    valid_digits = re.findall(rf"(?=(\d|{'|'.join(DIGIT_WORD_MAP)}))", line)
    converted_valid_digits = [
        i if i.isdigit() else DIGIT_WORD_MAP[i] for i in valid_digits
    ]
    return "".join(converted_valid_digits)


part_1 = [calibrate(i) for i in DATA if calibrate(i)]
print(sum(part_1))

part_2 = [calibrate(i) for i in [convert_valid_digits(j) for j in DATA] if calibrate(i)]
print(sum(part_2))
