wires = []
with open('Day 3/input.txt') as f:
    for path in f:
        wires.append(path.strip().split(','))

traversed = []
for path in wires:
    traverse = []
    current = (0, 0)
    for coord in path:
        direction = coord[0]
        distance = int(coord[1:])
        if direction == 'U':
            for i in range(distance):
                current = (current[0], current[1] + 1)
                traverse.append(current)
        elif direction == 'D':
            for i in range(distance):
                current = (current[0], current[1] - 1)
                traverse.append(current)
        elif direction == 'L':
            for i in range(distance):
                current = (current[0] - 1, current[1])
                traverse.append(current)
        elif direction == 'R':
            for i in range(distance):
                current = (current[0] + 1, current[1])
                traverse.append(current)
        
    traversed.append(set(traverse))

intersections = traversed[0].intersection(traversed[1])

distances = []
for intersection in intersections:
    distance = abs(intersection[0])+abs(intersection[1])
    distances.append(distance)

closest_distance = min(distances)
print(closest_distance)