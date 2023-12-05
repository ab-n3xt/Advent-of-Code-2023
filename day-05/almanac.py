import re

# Utility function
def convert_seed(seed: int, mappings: list):
    for mapping in mappings:
        (src_range, dest_range) = mapping
        if src_range[0] <= seed <= src_range[1]:
            difference = seed - src_range[0]
            return dest_range[0] + difference
    
    return seed

with open("input.txt") as fr:
    lines = fr.readlines()
    # Get seeds
    (_, seed_numbers) = lines[0].split(":")
    seeds = list(map(int, seed_numbers.strip().split(" ")))
    
    # Get range of seeds
    range_of_seeds = []
    index = 0
    while index < len(seeds)-1:
        start_value, length = seeds[index], seeds[index+1]
        for i in range(start_value, start_value+length):
            range_of_seeds.append(i)
        index += 2

    # print("Seeds: ", range_of_seeds)

    pattern = re.compile("(\d*) (\d*) (\d*)")
    mappings = []

    for line in lines[1:]:
        is_match = pattern.match(line)
        if is_match:
            # print("Found match: ", is_match.groups())
            dest, src, length = is_match.groups()
            dest, src, length = int(dest), int(src), int(length) # Lovely
            mappings.append(((src, src+length-1), (dest, dest+length-1)))
        elif len(mappings) != 0:
            seed_index = 0
            while seed_index < len(range_of_seeds):
                seed = range_of_seeds[seed_index]
                range_of_seeds[seed_index] = convert_seed(seed, mappings)
                seed_index += 1
            # print("Converted seeds: ", seeds)
            mappings.clear()
    
    # Check one more time
    if len(mappings) != 0:
        seed_index = 0
        while seed_index < len(range_of_seeds):
            seed = range_of_seeds[seed_index]
            range_of_seeds[seed_index] = convert_seed(seed, mappings)
            seed_index += 1
        # print("Converted seeds: ", seeds)
        mappings.clear()
    
    # print(range_of_seeds)
    # print(len(range_of_seeds))
    print(min(seeds))
