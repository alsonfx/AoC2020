code = open('code.txt', 'r')
code_list = [line.strip().split(' ') for line in code]
code_list = [(operation, int(num)) for operation, num in code_list]
code.close()


def execute_code(program, test=False):
    executed = set()
    acc = 0
    code_line = 0
    while code_line < len(program):
        if code_line in executed:
            if test:
                print(f"The first code line to repeat is line: {acc}")
                break
            return None
        executed.add(code_line)
        operation, num = program[code_line]
        if operation == 'acc':
            acc += num
            code_line += 1
        elif operation == 'jmp':
            code_line += num
        else:
            code_line += 1
    return acc


execute_code(code_list, True)

for num in range(len(code_list)):
    swap = ''
    if code_list[num][0] == 'jmp':
        swap = 'nop'
    elif code_list[num][0] == 'nop':
        swap = 'jmp'
    else:
        continue

    new_code = code_list[:num] + [(swap, code_list[num][1])] + code_list[num + 1:]
    executed = execute_code(new_code)
    if executed is not None:
        print(f"The acc of the corrected code is: {executed}")






