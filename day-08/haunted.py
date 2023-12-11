import re, math

pattern = re.compile("(\w+) = \((\w+), (\w+)\)")

nodes = {}
current_nodes = []
steps = 0
with open("input.txt") as fr:
    lines = fr.readlines()

    # Get the L-R combination
    instructions = lines[0].strip()
    
    # Process all the nodes
    for node in lines[2:]:
        if (is_match := pattern.match(node)) is not None:
            key, left_node, right_node = is_match.groups()
            if key[2] == "A":
                current_nodes.append(key)
            nodes[key] = (left_node, right_node)

    # I figured out that the step distance between finding "Z"
    # Was the same every time. So I find all the differences,
    # then take the LCM of the differences
    found_z_at_step = []
    difference_list = []
    for i, node in enumerate(current_nodes):
        index = 0
        step = 0
        
        # Calculate the number of steps needed to reach
        # the first "Z" node and the second "Z" node
        while len(found_z_at_step) != 2:
            instruction = instructions[index]
            index += 1
            if index == len(instructions):
                index = 0
            match instruction:
                case "L":
                    node = nodes[node][0]
                case "R":
                    node = nodes[node][1]
            
            step += 1
            if node[2] == "Z":
                found_z_at_step.append(step)

        e1, e2 = found_z_at_step[0], found_z_at_step[1]
        found_z_at_step.clear()
        difference_list.append(e2-e1)
        index += 1

    print(math.lcm(*difference_list))
