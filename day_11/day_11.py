import copy

with open("input.txt") as f:
    PUZZLE_INPUT = f.read()

# PUZZLE_INPUT = """
# 5483143223
# 2745854711
# 5264556173
# 6141336146
# 6357385478
# 4167524645
# 2176841721
# 6882881134
# 4846848554
# 5283751526
# """

# PUZZLE_INPUT = """
# 11111
# 19991
# 19191
# 19991
# 11111
# """

puzzle_input = [[int(y) for y in x] for x in PUZZLE_INPUT.strip().split("\n")]
print(puzzle_input)


def solve(grid):
    queue = []
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            grid[r][c] += 1
            if grid[r][c] > 9:
                queue.append((r, c))

    flashed = set()
    while queue:
        r, c = queue.pop(0)
        if (r, c) in flashed:
            continue
        flashed.add((r, c))
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                r_dr = r + dr
                c_dc = c + dc
                if r_dr < 0 or r_dr >= len(grid):
                    continue
                if c_dc < 0 or c_dc >= len(grid[0]):
                    continue
                grid[r_dr][c_dc] += 1
                if grid[r_dr][c_dc] > 9:
                    queue.append((r_dr, c_dc))
    for f in flashed:
        r, c = f
        grid[r][c] = 0
    return len(flashed)


grid = copy.copy(puzzle_input)
answer_1 = 0
num_octs = len(grid) * len(grid[0])
i = 1

while True:
    num_flashes = solve(grid)
    if i <= 100:
        answer_1 += num_flashes
    if num_flashes == num_octs:
        break
    i += 1


# Part 1 = 1679
print(f"answer = {answer_1}")

# Part 2 = 519
print(f"answer = {i}")
