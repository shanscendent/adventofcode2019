puzzle_input = '347312-805915'
input_range = list(map(int, puzzle_input.split('-')))
print(input_range)

def valid(password):
    password = str(password)
    previous = ''
    adjacent = False
    adjacent_chars = set()
    larger_chars = set()
    never_decrease = True
    for char in password:
        if char == previous:
            if char in adjacent_chars:
                larger_chars.add(char)
            adjacent_chars.add(char)
        if previous != '':
            if int(char) < int(previous):
                never_decrease = False
        previous = char

    difference = adjacent_chars - larger_chars
    if difference:
        adjacent = True
    return adjacent and never_decrease

counter = 0
for password in range(input_range[0], input_range[1] + 1):
    if valid(password):
        counter += 1

#print(valid(111333))
print(counter)