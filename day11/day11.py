from collections import Counter

seating = open('seating.txt', 'r')
layout = [list(line.strip()) for line in seating]
seating.close()


def cycle(grid):
    # create new blank grid use to mark new layout
    new_grid = [['.' for _ in row] for row in grid]

    # cycle through each seat in the grid and create a hash table
    # that consists of the 8 seats surrounding the seat so we can count
    # how many seats are occupied
    for row_num, row in enumerate(grid):
        for pos_num, position in enumerate(row):
            seat_grid = Counter(grid[row_num + x][pos_num + y] for x in range(-1, 2) for y in range(-1, 2)
                                if 0 <= row_num + x < len(grid)
                                and 0 <= pos_num + y < len(grid[row_num])
                                and (x, y) != (0, 0))

            # Apply our rules for seating changes
            if position == 'L' and seat_grid['#'] == 0:
                new_grid[row_num][pos_num] = '#'
            elif position == '#' and seat_grid['#'] >= 4:
                new_grid[row_num][pos_num] = 'L'
            else:
                new_grid[row_num][pos_num] = grid[row_num][pos_num]

    # determine how many total seats are taken
    taken = 0
    for row in new_grid:
        taken += row.count('#')

    # return the new layout after the cycle, and seats taken
    return new_grid, taken


# Run the cycle until we get a repeating state
first, first_seats = layout, 0
second, second_seats = cycle(first)
while True:
    if first_seats == second_seats:
        print(f"The seats stabilize at: {second_seats}")
        break
    first, first_seats = second, second_seats
    second, second_seats = cycle(first)


def cycle2(grid):
    # create new blank grid use to mark new layout
    new_grid = [['.' for _ in row] for row in grid]

    # instantiate the length of the rows and positions
    rows, positions = len(grid), len(grid[0])

    # cycle through each seat in the grid and determine if
    # there is a seat that is taken in all 8 directions from
    # the seat.
    for row_num, row in enumerate(grid):
        for pos_num, position in enumerate(row):
            # keep track of how many seats are taken in all directions
            seats_taken = 0
            # create directional values to scan
            # NW = -1, -1
            # N = 0, -1
            # NE = 1, -1
            # W = -1, 0
            # Point = 0, 0 <-- skip
            # E = 1, 0
            # SW = 1, -1
            # S = 1, 0
            # SE = 1, 1
            for x in range(-1, 2):
                for y in range(-1, 2):
                    if (x, y) == (0, 0):
                        continue

                    # Starts the scan for each direction
                    rows_x = row_num + x
                    pos_y = pos_num + y
                    # Continue moving in direction if:
                    # 1. you are not at the top or bottom of the grid
                    # 2. you are not at the left or right of the grid
                    # 3. you encounter a marker that is a '.'
                    while 0 <= rows_x < rows and 0 <= pos_y < positions and grid[rows_x][pos_y] == '.':
                        rows_x += x
                        pos_y += y

                    # check if point is valid
                    if 0 <= rows_x < rows and 0 <= pos_y < positions:
                        # If the point is valid and an occupied seat, then add 1 to the seats_taken count
                        seats_taken += (grid[rows_x][pos_y] == '#')

            # Apply our rules for seating changes
            if position == 'L' and seats_taken == 0:
                new_grid[row_num][pos_num] = '#'
            elif position == '#' and seats_taken >= 5:
                new_grid[row_num][pos_num] = 'L'
            else:
                new_grid[row_num][pos_num] = grid[row_num][pos_num]

    # determine how many total seats are taken
    taken = 0
    for row in new_grid:
        taken += row.count('#')

    # return the new layout after the cycle, and seats taken
    return new_grid, taken


# Run the cycle until we get a repeating state
first, first_seats = layout, 0
second, second_seats = cycle2(first)
while True:
    if first_seats == second_seats:
        print(f"The seats stabilize at: {second_seats}")
        break
    first, first_seats = second, second_seats
    second, second_seats = cycle2(first)
