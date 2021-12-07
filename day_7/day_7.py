from functools import lru_cache

with open("input.txt") as f:
    PUZZLE_INPUT = f.read()

# PUZZLE_INPUT = "16,1,2,0,4,2,7,1,2,14"

puzzle_input = [int(x) for x in PUZZLE_INPUT.strip().split(",")]
puzzle_input.sort()
print(puzzle_input)


least_fuel = 10000000000


for i in range(puzzle_input[0], puzzle_input[~0] + 1):
    total = 0
    for x in puzzle_input:
        total += abs(x-i)
    least_fuel = min(least_fuel, total)


# Part 1 = 340056
print(f"answer = {least_fuel}")

least_fuel = 10000000000

@lru_cache(maxsize=puzzle_input[~0] + 1)
def sigma(i):
    if i == 0:
        return 0
    return i + sigma(i - 1)


for i in range(puzzle_input[0], puzzle_input[~0] + 1):
    total = 0
    for x in puzzle_input:
        # total += sigma(abs(x - i))
        v = abs(x - i)
        total += (v * v + v) // 2
    least_fuel = min(least_fuel, total)


# Part 2 = 96592275
print(f"answer = {least_fuel}")
