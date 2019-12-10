def computer(original_intcode, program_inputs):
    intcode = original_intcode.copy()
    program_inputs = program_inputs.copy()

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
            return 'HALT'
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
            # print("USING INPUT {} = {}".format(program_input_counter, program_inputs[program_input_counter]))
            if not modes:
                intcode[intcode[p]] = program_inputs[program_input_counter]
            else:
                if modes[0] == 0 or modes[0] == 1:
                    intcode[intcode[p]] = program_inputs[program_input_counter]
                elif modes[0] == 1:
                    intcode[p] == program_inputs[program_input_counter]
            program_input_counter += 1
        elif opcode == 4:
            p += 1
            if not modes:
                # print("OUT: ", intcode[intcode[p]])
                return intcode[intcode[p]]
            else:
                if modes[0] == 0:
                    # print("OUT: ", intcode[intcode[p]])
                    return intcode[intcode[p]]
                elif modes[0] == 1:
                    # print("OUT: ", intcode[p])
                    return intcode[p]
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
        # print("OPCODE: {}, START P: {}, END P: {}".format(opcode, start_p, p))
        # print(intcode)
        if jump:
            jump = False
        else:
            p += 1

def amp(intcode, phase_sequence):
    amp_input = 0
    for i in range(5):
        phase = phase_sequence[i]
        amp_input_old = amp_input
        amp_input = computer(intcode, [phase, amp_input])
        # print("COMPUTING {}, {} = {}".format(phase, amp_input_old, amp_input))
    return amp_input

with open('Day 7/input.txt') as f:
    for intcode in f:
        original_intcode = list(map(int, intcode.strip().split(',')))

# original_intcode = [3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0]
# original_intcode = [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]

# phase_sequence = [1,0,4,3,2]

# print(original_intcode)

# print(amp(original_intcode, phase_sequence))

from itertools import permutations
max_thruster_output = 0
for phase_sequence in permutations([0, 1, 2, 3, 4]):
    # print(phase_sequence)
    max_thruster_output = max(max_thruster_output, amp(original_intcode, list(phase_sequence)))

print("Max thruster output = {}".format(max_thruster_output))


# print(computer(original_intcode, [2, 16]))