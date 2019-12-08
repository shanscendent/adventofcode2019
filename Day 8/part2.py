with open('Day 8/input.txt') as f:
    for line in f:
        data = list(map(int, list(line.strip())))
width = 25
height = 6

loc = 0
layers = []
for i in range(int(len(data)/width/height)):
    layer = []
    for x in range(width):
        for y in range(height):
            layer.append(data[loc])
            loc += 1
    layers.append(layer)

loc = 0
image = []
for x in range(height):
    row = []
    for y in range(width):
        pixel = 2
        for layer in layers:
            if layer[loc] == 0:
                pixel = 0
                break
            elif layer[loc] == 1:
                pixel = 1
                break
        row.append(pixel)
        loc += 1
    image.append(row)

for row in image:
    for pixel in row:
        if pixel == 0:
            pixel = ' '
        elif pixel == 1:
            pixel = '█'
        print(pixel, end='')
    print()