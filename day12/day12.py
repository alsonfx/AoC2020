test = False

if test:
    instructions = open('directions_test.txt', 'r')
else:
    instructions = open('directions.txt', 'r')

commands = [line.strip() for line in instructions]
instructions.close()

# Possible moves on the plane
directions = {'N': (0, 1), 'S': (0, -1), 'E': (1, 0), 'W': (-1, 0)}

# N = 0, E = 1, S = 2, W = 4
headings = 'NESW'

loc_x, loc_y = 0, 0
current_heading = 1

for command in commands:
    action = command[0]
    units = int(command[1:])

    # move the ship in the desired direction by the units
    if action in directions:
        move_x, move_y = directions[action]
        loc_x += move_x * units
        loc_y += move_y * units
    else:
        # Rotate heading or execute forward movement
        rotation = units // 90
        if action == 'L':
            current_heading = (current_heading - rotation) % 4
        elif action == 'R':
            current_heading = (current_heading + rotation) % 4
        else:
            move_x, move_y = directions[headings[current_heading]]
            loc_x += move_x * units
            loc_y += move_y * units


print(f"The Manhattan distance from point 0,0 is: {abs(loc_x) + abs(loc_y)}")

# set starting coordinates and starting waypoint coordinate
loc_x, loc_y = 0, 0
wy_x, wy_y = 10, 1
current_heading = 1

for command in commands:
    action = command[0]
    units = int(command[1:])
    if action in directions:
        move_x, move_y = directions[action]
        wy_x += move_x * units
        wy_y += move_y * units
    # if not an action, then change waypoint or move ship forward
    else:
        rotation = (units // 90)
        rotation %= 4
        if action == 'L':
            rotation = 4 - rotation
        if action in 'LR':
            for _ in range(rotation):
                wy_x, wy_y = wy_y, -wy_x
        else:
            loc_x += wy_x * units
            loc_y += wy_y * units

print(f"The Manhattan distance from point 0,0 is: {abs(loc_x) + abs(loc_y)}")
