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
        
    traversed.append(traverse)

traversed_set = []
for traversal in traversed:
    traversed_set.append(set(traversal))

intersections = traversed_set[0].intersection(traversed_set[1])

combined_steps = []
for intersection in intersections:
    combined = 0
    for path in traversed:
        steps = path.index(intersection) + 1
        combined += steps
    combined_steps.append(combined)

closest_distance = min(combined_steps)
print(closest_distance)