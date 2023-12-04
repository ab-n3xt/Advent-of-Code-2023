def find_adjacent_numbers(lines: str, line_index: int, char_index: int):
    above_line, below_line = line_index - 1, line_index + 1
    left_side, right_side = char_index - 1, char_index + 1

    total = 0

    part_number_count = 0
    gear_ratio = 1

    if above_line >= 0:
        # Check above
        if lines[above_line][char_index].isdigit():
            left_index, right_index = char_index, char_index
            while left_index-1 >= 0 and lines[above_line][left_index-1].isdigit():
                left_index -= 1
            while right_index+1 < len(lines) and lines[above_line][right_index+1].isdigit():
                right_index += 1
            total += int(lines[above_line][left_index:right_index+1])
            
            part_number_count += 1
            gear_ratio *= int(lines[above_line][left_index:right_index+1])
        else:
            # Check top-left
            if left_side >= 0 and lines[above_line][left_side].isdigit():
                left_index, right_index = left_side, left_side
                while left_index-1 >= 0 and lines[above_line][left_index-1].isdigit():
                    left_index -= 1
                total += int(lines[above_line][left_index:right_index+1])

                part_number_count += 1
                gear_ratio *= int(lines[above_line][left_index:right_index+1])
            # Check top-right
            if right_side < len(lines) and lines[above_line][right_side].isdigit():
                left_index, right_index = right_side, right_side
                while right_index+1 < len(lines) and lines[above_line][right_index+1].isdigit():
                    right_index += 1
                total += int(lines[above_line][left_index:right_index+1])

                part_number_count += 1
                gear_ratio *= int(lines[above_line][left_index:right_index+1])

    if below_line < len(lines):
        # Check below
        if lines[below_line][char_index].isdigit():
            left_index, right_index = char_index, char_index
            while left_index-1 >= 0 and lines[below_line][left_index-1].isdigit():
                left_index -= 1
            while right_index+1 < len(lines) and lines[below_line][right_index+1].isdigit():
                right_index += 1
            total += int(lines[below_line][left_index:right_index+1])
            
            part_number_count += 1
            gear_ratio *= int(lines[below_line][left_index:right_index+1])
        else:
            # Check below-left
            if left_side >= 0 and lines[below_line][left_side].isdigit():
                left_index, right_index = left_side, left_side
                while left_index-1 >= 0 and lines[below_line][left_index-1].isdigit():
                    left_index -= 1
                total += int(lines[below_line][left_index:right_index+1])

                part_number_count += 1
                gear_ratio *= int(lines[below_line][left_index:right_index+1])
            # Check below-right
            if right_side < len(lines) and lines[below_line][right_side].isdigit():
                left_index, right_index = right_side, right_side
                while right_index+1 < len(lines) and lines[below_line][right_index+1].isdigit():
                    right_index += 1
                total += int(lines[below_line][left_index:right_index+1])

                part_number_count += 1
                gear_ratio *= int(lines[below_line][left_index:right_index+1])
    # Check left
    if left_side >= 0 and lines[line_index][left_side].isdigit():
        left_index, right_index = left_side, left_side
        while left_index-1 >= 0 and lines[line_index][left_index-1].isdigit():
            left_index -= 1
        total += int(lines[line_index][left_index:right_index+1])

        part_number_count += 1
        gear_ratio *= int(lines[line_index][left_index:right_index+1])
    # Check right
    if right_side < len(lines) and lines[line_index][right_side].isdigit():
        left_index, right_index = right_side, right_side
        while right_index+1 < len(lines) and lines[line_index][right_index+1].isdigit():
            right_index += 1
        total += int(lines[line_index][left_index:right_index+1])
        
        part_number_count += 1
        gear_ratio *= int(lines[line_index][left_index:right_index+1])
    
    if part_number_count == 2:
        return gear_ratio
    else:
        return 0


total = 0
with open("input.txt") as fr:
    lines = fr.readlines()
    for line_index, line in enumerate(lines):
        line = line.strip()
        for char_index, char in enumerate(line):
            if char == '*':
                total += find_adjacent_numbers(lines, line_index, char_index)

print(total)