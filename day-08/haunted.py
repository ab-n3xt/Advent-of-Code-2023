import re

pattern = re.compile("(\w+) = \((\w+), (\w+)\)")

nodes = {}
current_node = "AAA"
steps = 0
with open("input.txt") as fr:
    lines = fr.readlines()

    # Get the L-R combination
    instructions = lines[0].strip()
    
    # Process all the nodes
    for node in lines[2:]:
        is_match = pattern.match(node)
        if is_match:
            key, left_node, right_node = is_match.groups()
            nodes[key] = (left_node, right_node)

    # Loop every node until ZZZ is found
    index = 0
    while True:
        instruction = instructions[index]    

        if instruction == "L":
            current_node = nodes[current_node][0]
        elif instruction == "R":
            current_node = nodes[current_node][1]
        
        steps += 1

        if current_node == "ZZZ":
            break
        
        index += 1
        if index == len(instructions):
            index = 0
    
    print(steps)