with open("input.txt") as f:
    PUZZLE_INPUT = f.read()

# PUZZLE_INPUT = """
# 2199943210
# 3987894921
# 9856789892
# 8767896789
# 9899965678
# """

puzzle_input = [[int(y) for y in x] for x in PUZZLE_INPUT.strip().split("\n")]
print(puzzle_input)

lows_heights = []
lows = []

for y in range(len(puzzle_input)):
    for x in range(len(puzzle_input[0])):
        low = True
        val = puzzle_input[y][x]
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            tx = x + dx
            ty = y + dy
            if (
                tx < 0
                or tx >= len(puzzle_input[0])
                or ty < 0
                or ty >= len(puzzle_input)
            ):
                continue
            if puzzle_input[ty][tx] <= val:
                low = False
                break
        if low:
            lows_heights.append(val)
            lows.append((x, y))
# print(lows_heights)
# print(len(lows_heights))


# Part 1 = 486
print(f"answer = {sum(lows_heights) + len(lows_heights)}")

results = []

for low in lows:
    queue = [low]
    seen = set()
    while queue:
        x, y = queue.pop(0)
        seen.add((x, y))
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            tx = x + dx
            ty = y + dy
            if (
                tx < 0
                or tx >= len(puzzle_input[0])
                or ty < 0
                or ty >= len(puzzle_input)
            ):
                continue
            if puzzle_input[ty][tx] == 9 or (tx, ty) in seen:
                continue
            queue.append((tx, ty))
    results.append(len(seen))

results.sort(reverse=True)
answer = results[0] * results[1] * results[2]

# Part 2 = 1059300
print(f"answer = {answer}")
