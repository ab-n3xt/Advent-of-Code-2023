configuration = {
    "red": 12,
    "green": 13,
    "blue": 14
}

total = 0
power_total = 0
with open("input.txt") as fr:
    lines = fr.readlines()
    for line in lines:
        power = {
            "red": -1,
            "green": -1,
            "blue": -1
        }
        set_power = 1
        invalid_flag = False

        # Get game ID
        # Game _:
        first_index = 5
        last_index = line.find(":")

        game_id = int(line[first_index:last_index])

        # Split the game sets
        sets = line[last_index+2:]
        split_sets = sets.split(";")

        for set in split_sets:
            cubes = set.split(",")

            for cube in cubes:
                cube.strip()
                [value, key] = cube.split()
                if not invalid_flag and configuration[key] < int(value):
                    invalid_flag = True
                    
                if power[key] < int(value):
                    power[key] = int(value)
        
        if not invalid_flag:
            total += game_id

        for p in power.values():
            if p != -1:
                set_power *= p

        power_total += set_power
    
print(total)
print(power_total)