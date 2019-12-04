puzzle_input = '347312-805915'
input_range = list(map(int, puzzle_input.split('-')))
print(input_range)

def valid(password):
    password = str(password)
    previous = ''
    adjacent = False
    never_decrease = True
    for char in password:
        if char == previous: # adjacent digits
            adjacent = True
        if previous != '':
            if int(char) < int(previous):
                never_decrease = False
        previous = char
    return adjacent and never_decrease

counter = 0
for password in range(input_range[0], input_range[1] + 1):
    if valid(password):
        counter += 1

#print(valid(123789))
print(counter)