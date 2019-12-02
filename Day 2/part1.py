with open('Day 2/input.txt') as f:
    for intcode in f:
        original_intcode = list(map(int, intcode.strip().split(',')))

intcode = original_intcode.copy()
intcode[1] = 12
intcode[2] = 2
#intcode = [2,4,4,5,99,0]

p = 0
i = intcode[p]
while(i != 99):
    p1 = intcode[p+1]
    p2 = intcode[p+2]
    if intcode[p] == 1:
        intcode[intcode[p+3]] = intcode[p1]+intcode[p2]
    elif intcode[p] == 2:
        intcode[intcode[p+3]] = intcode[p1]*intcode[p2]
    p += 4
    i = intcode[p]

print(intcode[0])