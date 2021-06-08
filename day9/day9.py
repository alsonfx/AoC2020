# Open and parse the input file into a list of integers
xmas = open('xmas.txt', 'r')
xmas_ints = [int(line.strip()) for line in xmas]
xmas.close()

# Create a variable for size of preamble: 5 for test data, 25 for actual
# Create a variable for the invalid number
preamble_size = 25
invalid = 0

# Look at each line in the list of integers past the preamble
for line in range(preamble_size, len(xmas_ints)):
    # Create a set of the preamble numbers and get the number to test
    preamble = set(xmas_ints[line-preamble_size:line])
    test_num = xmas_ints[line]
    valid = False

    # Check to see if the test number has a sum pair in the preamble set
    while preamble:
        difference = test_num - preamble.pop()
        if difference in preamble:
            valid = True
            break

    # If the preamble set is empty and the test_num wasn't validated
    # then the invalid number is the test_num
    if not preamble and valid is False:
        invalid = test_num
        print(f"The first invalid value is: {invalid}")
        break

# Create an answer variable
answer = 0
# For each number we have to create a contiguous sum/total
for num1 in range(len(xmas_ints)):
    total = 0
    for num2 in range(num1, len(xmas_ints)):
        total += xmas_ints[num2]
        # If the total of the contiguous list is our invalid number
        # we create a list of the contiguous numbers and find the
        # max and min and sum them together.
        if total == invalid:
            sum_values = xmas_ints[num1:num2 + 1]
            answer = max(sum_values) + min(sum_values)
            break
    # If we have an answer, no need to keep making contiguous lists
    if answer != 0:
        break

print(f"The sum of the max and min of the contiguous set is: {answer}")
