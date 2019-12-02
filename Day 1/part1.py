fuel = 0

with open('Day 1/input.txt') as f:
    for mass in f:
        fuel += int(mass)//3-2

print(fuel)