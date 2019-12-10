import copy

program = []

with open("Day 5/input.txt") as f:
    program = f.read().split(",")

program = list(map(int, program))


def Run(program):
    pc = 0 #Program counter
    while True:
        pc_old = pc
        #extract Opcode and Mode
        opcode = int(str(program[pc])[-2:])
        mode = "000"
        if(len(str(program[pc])) > 2): #If mode is specified
            mode = str(program[pc])[:-2]
            mode = mode[::-1]
            if(len(mode) == 2):
                mode += "0"
            elif(len(mode) == 1):
                mode += "00"
            

        def Parameter(n):
            if mode[n-1] == "0":
                return int(program[program[pc+n]]) #Position mode
            else:
                return int(program[pc+n]) #Immediate mode       
        
        if(opcode == 1): #Add
            program[program[pc+3]] = Parameter(1) + Parameter(2)
            pc += 4
        elif(opcode == 2): #Mul
            program[program[pc+3]] = Parameter(1) * Parameter(2)
            pc += 4
        elif(opcode == 3): #Input
            program[program[pc+1]] = int(input())
            pc += 2
        elif(opcode == 4): #Print
            print(Parameter(1))
            pc += 2


        elif(opcode == 5): #Jump if true
            if(Parameter(1) != 0):
                pc = Parameter(2)
            else:
                pc += 3

        elif(opcode == 6): #Jump if false
            if(Parameter(1) == 0):
                pc = Parameter(2)
            else:
                pc += 3

        elif(opcode == 7): #Less than
            if(Parameter(1) < Parameter(2)):
                program[program[pc+3]] = 1
            else:
                program[program[pc+3]] = 0
            pc += 4

        elif(opcode == 8): #Equals
            if(Parameter(1) == Parameter(2)):
                program[program[pc+3]] = 1
            else:
                program[program[pc+3]] = 0
            pc += 4

        
        elif(opcode == 99):
            break
        else:
            print("Error")
            break
        print("OPCODE: {}, START P: {}, END P: {}".format(opcode, pc_old, pc))
    return program


Run(program)
