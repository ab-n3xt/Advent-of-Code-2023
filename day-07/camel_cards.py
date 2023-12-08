strength_map = {
    '2': 0,
    '3': 1,
    '4': 2,
    '5': 3,
    '6': 4,
    '7': 5,
    '8': 6,
    '9': 7,
    'T': 8,
    'J': 9,
    'Q': 10,
    'K': 11,
    'A': 12
}

def second_order(card, rival_card) -> int:
    if strength_map[card] > strength_map[rival_card]:
        return 1
    elif strength_map[card] < strength_map[rival_card]:
        return -1
    else:
        return 0

def compare_two_hands(hand, rival_hand) -> int:
    index = 0
    while index < len(hand):
        first_card, first_rival_card = hand[index], rival_hand[index]
        compare_value = second_order(first_card, first_rival_card)
        if compare_value == 1:
            return 1
        elif compare_value == -1:
            return -1
        else:
            index += 1
    return 0
    
def is_five_of_a_kind(hand: str) -> bool:
    first_card = hand[0]
    if hand.count(first_card) == 5:
        return True
    
    return False

def is_four_of_a_kind(hand: str) -> bool:
    first_card, second_card = hand[0], hand[1]
    if hand.count(first_card) == 4 or hand.count(second_card) == 4:
        return True
    
    return False

def is_full_house(hand: str) -> bool:
    for card in hand:
        c = hand.count(card, 0)
        if not(hand.count(card, 0) == 3 or hand.count(card, 0) == 2):
            return False
    
    return True

def is_three_of_a_kind(hand: str) -> bool:
    for card in hand:
        if hand.count(card) == 3:
            return True
        
    return False

def is_two_pair(hand):
    possible_pair_locations = [0,1,2,3,4]
    for index, card in enumerate(hand):
        if index in possible_pair_locations and hand.count(card) == 2:
            possible_pair_locations.remove(hand.index(card))
            possible_pair_locations.remove(hand.rindex(card))

        if len(possible_pair_locations) == 1:
            return True

    return False

def is_one_pair(hand):
    for card in hand:
        if hand.count(card) == 2:
            return True
    
    return False

def determine_type(hand) -> int:
    if (is_five_of_a_kind(hand)):
        return 6
    elif (is_four_of_a_kind(hand)):
        return 5
    elif (is_full_house(hand)):
        return 4
    elif (is_three_of_a_kind(hand)):
        return 3
    elif (is_two_pair(hand)):
        return 2
    elif (is_one_pair(hand)):
        return 1
    else:
        return 0

ranked_hands = {
    6: [],
    5: [],
    4: [],
    3: [],
    2: [],
    1: [],
    0: []
}

with open("input.txt") as fr:
    lines = fr.readlines()
    for line in lines:
        [hand, bet_value] = line.strip().split()
        type_value = determine_type(hand)
        rival_hands = ranked_hands[type_value]
        card_added = False
        for index, rival_hand in enumerate(rival_hands):
            result = compare_two_hands(hand=hand, rival_hand=rival_hand[0])
            if result == -1:
                continue
            else:
                card_added = True
                rival_hands[index:index] = [(hand, int(bet_value))]
                break
            
        if not card_added:
            rival_hands.append((hand, int(bet_value)))
        ranked_hands[type_value] = rival_hands
    
    rank = len(lines)
    total = 0
    sorted_hands = ranked_hands.values()
    for hands in ranked_hands.values():
        for hand in hands:
            total += int(hand[1]) * rank
            rank -= 1
    
    print(total)