with open('Day 8/input.txt') as f:
    for line in f:
        data = list(map(int, list(line.strip())))
width = 25
height = 6

# line = '123456789012'
# data = list(map(int, list(line.strip())))
# width = 3
# height = 2

loc = 0
layers = []
layers0 = []
for i in range(int(len(data)/width/height)):
    counter0 = 0
    layer = []
    for x in range(width):
        for y in range(height):
            layer.append(data[loc])
            if data[loc] == 0:
                counter0 += 1
            loc += 1
    layers.append(layer)
    layers0.append(counter0)

val, idx = min((val, idx) for (idx, val) in enumerate(layers0))

counter1 = 0
counter2 = 0
for digit in layers[idx]:
    if digit == 1:
        counter1 += 1
    elif digit == 2:
        counter2 += 1

print(counter1*counter2)