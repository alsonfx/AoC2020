# Open and parse data into a list of adapters
jolts = open('jolts.txt', 'r')
adapters = [int(line.strip()) for line in jolts]
jolts.close()

# Sort the adapters into order
adapters.sort()

# Create a list that consists of:
# charging outlet jolts
# adapters jolts
# device jolts
adapters = [0] + adapters + [adapters[-1] + 3]

# Keep track of current adapter and the jolt differences
# of each adapter in the list from port to device
current_adapter, one_diff, three_diff = 0, 0, 0
for adapter in adapters:
    if adapter - current_adapter == 1:
        one_diff += 1
    elif adapter - current_adapter == 3:
        three_diff += 1
    current_adapter = adapter

print(f"The produce of the 1-jolt and 3-jolt adapters is: {one_diff * three_diff}")

# Default paths is one as calculated above
paths = [1]

# For each adapter in the adapter list we want to determine how many
# adapters can be attached to it.
for starting_adapter in range(1, len(adapters)):
    path = 0
    # For adapters already tested, we see if the new adapter is a path that is
    # within 3 jolts and each adapter that is within 3 jolts is a valid path
    # and added to the path count
    for pathway in range(starting_adapter):
        if adapters[pathway] + 3 >= adapters[starting_adapter]:
            path += paths[pathway]

    paths.append(path)
    print(paths)

print("The maximum combinations is: ", max(paths))
