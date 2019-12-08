orbit_map = {}
counts = {}

with open('Day 6/input.txt') as f:
    for orbit in f:
        bodies = orbit.strip().split(')')
        if bodies[0] not in orbit_map:
            orbit_map[bodies[0]] = []
        orbit_map[bodies[0]].append(bodies[1])

traversed_list_you = []
traversed_list_san = []

def traverse(body, orbit_map, traversed_list):
    global traversed_list_san
    global traversed_list_you
    # print("Traversing {}. ".format(body), end='')
    traversed_list_next = traversed_list.copy()
    traversed_list_next.append(body)
    if body in orbit_map:
        for child in orbit_map[body]:
            traverse(child, orbit_map, traversed_list_next)
    # print("Saving {} to {}".format(counter, body))
    if body == 'YOU':
        traversed_list_you = traversed_list_next.copy()
        # print(traversed_list_next)
    if body == 'SAN':
        traversed_list_san = traversed_list_next.copy()
        # print(traversed_list_next)

traversed_list = []
traverse('COM', orbit_map, traversed_list)

number = len(set(traversed_list_you)^set(traversed_list_san))-2

print(number)