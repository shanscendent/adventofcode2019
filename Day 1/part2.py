sum_fuel = 0

def calc_fuel(mass):
    fuel = max(0, mass//3-2)
    if fuel > 0:
        fuel += calc_fuel(fuel)
    return fuel

with open('Day 1/input.txt') as f:
    for mass in f:
        fuel = calc_fuel(int(mass))
        sum_fuel += fuel

print(sum_fuel)