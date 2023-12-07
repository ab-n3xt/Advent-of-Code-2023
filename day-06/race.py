total_wins_with_error_margin = 1
with open("input.txt") as fr:
    lines = fr.readlines()
    times, distances = lines[0], lines[1]

    [_, times] = times.split(":")
    times = times.strip().split()
    time = int("".join(times))
    times.clear()
    times.append(time)

    [_, distances] = distances.split(":")
    distances = distances.strip().split()
    distance = int("".join(distances))
    distances.clear()
    distances.append(distance)

    for index, time in enumerate(times):
        distance = distances[index]
        
        min_time = 1
        found_min = False
        max_time = time - 1
        found_max = False

        while min_time < max_time:
            if not found_min:
                speed = min_time
                leftover_time = time - min_time
                if speed * leftover_time > distance:
                    found_min = True
                else:
                    min_time += 1
            if not found_max:
                speed = max_time
                leftover_time = time - max_time
                if speed * leftover_time > distance:
                    found_max = True
                else:
                    max_time -= 1

            if found_min and found_max:
                break
        
        total_wins = max_time - min_time + 1
        total_wins_with_error_margin *= total_wins

print(total_wins_with_error_margin)