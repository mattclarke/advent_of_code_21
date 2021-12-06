from copy import copy

with open("input.txt") as f:
    PUZZLE_INPUT = f.read()

PUZZLE_INPUT = "3,4,3,1,2"

puzzle_input = [int(x) for x in PUZZLE_INPUT.strip().split(",")]
print(puzzle_input)

def solve(days=80):
    fish = copy(puzzle_input)

    for i in range(days):
        new_fish = copy(fish)
        for i,f in enumerate(fish):
            if f == 0:
                new_fish.append(8)
                new_fish[i] = 6
            else:
                new_fish[i] -= 1
        # print(new_fish)
        fish = copy(new_fish)
    return len(fish)



# Part 1 = 377263
print(f"answer = {solve()}")

# Part 2
print(f"answer = {solve(256)}")
