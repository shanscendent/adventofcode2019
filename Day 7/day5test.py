with open('Day 7/input.txt') as f:
    for intcode in f:
        original_intcode = list(map(int, intcode.strip().split(',')))

intcode = original_intcode.copy()

program_inputs = [0, 0]
program_input_counter = 0
p = 0
jump = False
modes = []
while True:
    # Opcode handler #
    if intcode[p] == (3 or 4 or 99):
        opcode = intcode[p]
    else:
        temp = str(intcode[p])
        if len(temp) == 1:
            opcode = intcode[p]
            modes = []
        else:
            opcode = int(temp[-2:])
            modes = list(map(int, list(temp[0:-2])))[::-1]
    if opcode == 99:
        print("STOP")
        break
    start_p = p
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
        if not modes:
            intcode[intcode[p]] = program_inputs[program_input_counter]
        else:
            if modes[0] == 0:
                intcode[intcode[p]] = program_inputs[program_input_counter]
            elif modes[0] == 1:
                intcode[p] == program_inputs[program_input_counter]
        program_input_counter += 1
    elif opcode == 4:
        p += 1
        if not modes:
            print("OUT: ", intcode[intcode[p]])
        else:
            if modes[0] == 0:
                print("OUT: ", intcode[intcode[p]])
            elif modes[0] == 1:
                print("OUT: ", intcode[p])
    elif opcode == 5:
        zeros = (2 - len(modes)) * [0]
        modes.extend(zeros)
        for mode in modes:
            p += 1
            if mode == 0:
                params.append(intcode[intcode[p]])
            elif mode == 1:
                params.append(intcode[p])
        if params[0] != 0:
            p = params[1]
            jump = True
    elif opcode == 6:
        zeros = (2 - len(modes)) * [0]
        modes.extend(zeros)
        for mode in modes:
            p += 1
            if mode == 0:
                params.append(intcode[intcode[p]])
            elif mode == 1:
                params.append(intcode[p])
        if params[0] == 0:
            p = params[1]
            jump = True
    elif opcode == 7:
        zeros = (3 - len(modes)) * [0]
        modes.extend(zeros)
        for mode in modes:
            p += 1
            if mode == 0:
                params.append(intcode[intcode[p]])
            elif mode == 1:
                params.append(intcode[p])
        if params[0] < params[1]:
            intcode[intcode[p]] = 1
        else:
            intcode[intcode[p]] = 0
    elif opcode == 8:
        zeros = (3 - len(modes)) * [0]
        modes.extend(zeros)
        for mode in modes:
            p += 1
            if mode == 0:
                params.append(intcode[intcode[p]])
            elif mode == 1:
                params.append(intcode[p])
        if params[0] == params[1]:
            intcode[intcode[p]] = 1
        else:
            intcode[intcode[p]] = 0
    print("OPCODE: {}, START P: {}, END P: {}".format(opcode, start_p, p))
    # print(intcode)
    if jump:
        jump = False
    else:
        p += 1