def calculate_winnings(winning_numbers, current_numbers) -> (int, int):
    number_of_matches = 0
    points = 0
    for winning_number in winning_numbers:
        if winning_number in current_numbers:
            number_of_matches += 1
            if points == 0:
                points = 1
            else:
                points *= 2
    
    return points, number_of_matches

total_points = 0
total_cards = 0
with open("input.txt") as fr:
    lines = fr.readlines()
    copies = [0] * len(lines) # Holds all the extra copies

    for index, line in enumerate(lines):
        total_cards += 1

        # Process strings into two cards: the winning portion, and the current portion
        # Looks like ** functional programming **
        [_, card] = line.split(":")
        [winning_numbers, current_numbers] = card.split("|")
        winning_numbers = winning_numbers.strip().split(" ")
        current_numbers = current_numbers.strip().split(" ")

        # Get rid of empty strings
        winning_numbers = [s for s in winning_numbers if s]
        current_numbers = [s for s in current_numbers if s]

        # Now process the card, plus its copies
        copies_of_card = 1
        if copies[index] > 0:
            copies_of_card = copies[index] + 1
        
        points, number_of_matches = calculate_winnings(winning_numbers, current_numbers)
        
        total_points += points * copies_of_card
        total_cards += number_of_matches * copies_of_card

        copies_index = index+1

        while number_of_matches > 0:
            copies[copies_index] += 1 * copies_of_card
            copies_index += 1
            number_of_matches -= 1

print(total_cards)
