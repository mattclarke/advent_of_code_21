from copy import copy

with open("input.txt") as f:
    PUZZLE_INPUT = f.read()

# PUZZLE_INPUT = "3,4,3,1,2"

puzzle_input = [int(x) for x in PUZZLE_INPUT.strip().split(",")]
print(puzzle_input)


def solve(days=80):
    fish = copy(puzzle_input)
    fish.sort()

    new_fish = []
    new_fish_days = []
    prev = 0
    count = 0

    for f in fish:
        if prev == 0:
            prev = f
        if f == prev:
            count += 1
        else:
            new_fish_days.append(prev)
            new_fish.append(count)
            count = 1
            prev = f
    new_fish_days.append(prev)
    new_fish.append(count)


    for i in range(days):
        num_born = 0
        for i, f in enumerate(new_fish):
            d = new_fish_days[i]
            if d == 0:
                num_born += 1 * f
                new_fish_days[i] = 6
            else:
                new_fish_days[i] -= 1
        if num_born:
            new_fish.append(num_born)
            new_fish_days.append(8)

    return sum(new_fish)



# Part 1 = 377263
print(f"answer = {solve()}")

# Part 2
print(f"answer = {solve(256)}")
