zones = open('zones.txt', 'r')
max_id = 0
my_seat = []

for line in zones:
    seat_id = 0
    rows = [*range(128)]
    columns = [*range(8)]

    for letter in line:
        if letter == 'F':
            mid_row = len(rows) // 2
            rows = rows[:mid_row]
        elif letter == 'B':
            mid_row = len(rows) // 2
            rows = rows[mid_row:]
        elif letter == 'L':
            mid_col = len(columns) // 2
            columns = columns[:mid_col]
        elif letter == 'R':
            mid_col = len(columns) // 2
            columns = columns[mid_col:]

    seat_id = rows[0] * 8 + columns[0]
    if seat_id > max_id:
        max_id = seat_id

    my_seat.append(seat_id)
zones.close()

my_seat.sort()
my_id = 0
for x in range(len(my_seat) - 1):
    if my_seat[x + 1] - my_seat[x] != 1:
        my_id = my_seat[x] + 1
        break

print(f"The highest Seat ID is: {max_id}")
print(f"My seat on the plane is: {my_id}")
