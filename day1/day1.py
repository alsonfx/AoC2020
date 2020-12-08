report = open("report.txt", 'r')
number_set = [int(line) for line in report]

for num1 in number_set:
    for num2 in number_set:
        if num1 + num2 == 2020:
            puzzle_input1 = num1 * num2
        for num3 in number_set:
            if num1 + num2 + num3 == 2020:
                puzzle_input2 = num1 * num2 * num3
                break

report.close()
print(f"Part 1 Solution: {puzzle_input1}")
print(f"Part 2 Solution: {puzzle_input2}")
