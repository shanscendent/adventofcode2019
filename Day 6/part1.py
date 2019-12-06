orbit_map = {}
counts = {}

with open('Day 6/input.txt') as f:
    for orbit in f:
        bodies = orbit.strip().split(')')
        if bodies[0] not in orbit_map:
            orbit_map[bodies[0]] = []
        orbit_map[bodies[0]].append(bodies[1])

def traverse(body, orbit_map, counter):
    # print("Traversing {}. ".format(body), end='')
    if body in orbit_map:
        for child in orbit_map[body]:
            traverse(child, orbit_map, counter+1)
    # print("Saving {} to {}".format(counter, body))
    if body not in counts: counts[body] = counter+1

traverse('COM', orbit_map, -1)

number = sum(counts.values())

print(number)