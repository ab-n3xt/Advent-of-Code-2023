total_points = 0
with open("input.txt") as fr:
    lines = fr.readlines()
    for line in lines:
        points = 0
        [_, card] = line.split(":")
        [winning_numbers, current_numbers] = card.split("|")
        winning_numbers = winning_numbers.strip().split(" ")
        current_numbers = current_numbers.strip().split(" ")

        winning_numbers = [s for s in winning_numbers if s]
        current_numbers = [s for s in current_numbers if s]

        for winning_number in winning_numbers:
            if winning_number in current_numbers:
                # print("Found ", winning_number, "in ", current_numbers)
                if points == 0:
                    points = 1
                else:
                    points *= 2
        
        total_points += points

print(total_points)
