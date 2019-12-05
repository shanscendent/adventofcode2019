with open('Day 5/input.txt') as f:
    for intcode in f:
        original_intcode = list(map(int, intcode.strip().split(',')))

intcode = original_intcode.copy()

# intcode = [1002,4,3,4,33]

program_input = 1
p = 0
while True:
    # Opcode handler #
    if intcode[p] == (3 or 4 or 99):
        opcode = intcode[p]
    else:
        temp = str(intcode[p])
        opcode = int(temp[-2:])
        modes = list(map(int, list(temp[0:-2])))[::-1]
    if opcode == 99:
        break
    # Instruction handler #
    params = []
    if opcode == 1:
        zeros = (3 - len(modes)) * [0]
        modes.extend(zeros)
        for mode in modes:
            p += 1
            if mode == 0:
                params.append(intcode[intcode[p]])
            elif mode == 1:
                params.append(intcode[p])
        intcode[intcode[p]] = params[0]+params[1]
    elif opcode == 2:
        zeros = (3 - len(modes)) * [0]
        modes.extend(zeros)
        for mode in modes:
            p += 1
            if mode == 0:
                params.append(intcode[intcode[p]])
            elif mode == 1:
                params.append(intcode[p])
        intcode[intcode[p]] = params[0]*params[1]
    elif opcode == 3:
        p += 1
        intcode[intcode[p]] = program_input
    elif opcode == 4:
        p += 1
        print("OUT: ", intcode[intcode[p]])
    p += 1