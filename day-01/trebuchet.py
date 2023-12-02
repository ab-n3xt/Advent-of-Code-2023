def calibrate(string: str) -> int:
    n = 0
    three_letters = {"one": 1, "two": 2, "six": 6}
    four_letters = {"four": 4, "five": 5, "nine": 9}
    five_letters = {"three": 3,"seven": 7, "eight": 8}

    # Find first digit
    for i, c in enumerate(string):
        if c.isdigit():
            n += int(c) * 10
            break
        elif i <= len(string)-3 and string[i:i+3] in three_letters:
            n += three_letters[string[i:i+3]] * 10
            break
        elif i <= len(string)-4 and string[i:i+4] in four_letters:
            n += four_letters[string[i:i+4]] * 10
            break
        elif i <= len(string)-5 and string[i:i+5] in five_letters:
            n += five_letters[string[i:i+5]] * 10
            break

    i = len(string) - 1
    # Find last digit
    while i >= 0:
        c = string[i]
        if c.isdigit():
            n += int(c)
            return n
        elif i <= len(string)-3 and string[i:i+3] in three_letters:
            n += three_letters[string[i:i+3]]
            return n
        elif i <= len(string)-4 and string[i:i+4] in four_letters:
            n += four_letters[string[i:i+4]]
            return n
        elif i <= len(string)-5 and string[i:i+5] in five_letters:
            n += five_letters[string[i:i+5]]
            return n
        i -= 1


total = 0
with open("input.txt") as fr:
    lines = fr.readlines()

    for line in lines:
        total += calibrate(line)

print(total)