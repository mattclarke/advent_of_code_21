with open("input.txt") as f:
    PUZZLE_INPUT = f.read()

# PUZZLE_INPUT = """
# 0,9 -> 5,9
# 8,0 -> 0,8
# 9,4 -> 3,4
# 2,2 -> 2,1
# 7,0 -> 7,4
# 6,4 -> 2,0
# 0,9 -> 2,9
# 3,4 -> 1,4
# 0,0 -> 8,8
# 5,5 -> 8,2
# """

puzzle_input = [x for x in PUZZLE_INPUT.strip().split("\n")]
print(puzzle_input)


def solve(part2=False):
    locations = {}

    for line in puzzle_input:
        parts = line.replace(" -> ", " ").replace(",", " ").split(" ")
        parts = [int(x) for x in parts]
        x1, y1, x2, y2 = parts

        if x1 != x2 and y1 == y2:
            if x2 < x1:
                x1, x2 = x2, x1
            for x in range(x1, x2 + 1):
                cnt = locations.get((x, y1), 0)
                locations[(x, y1)] = cnt + 1
        elif y1 != y2 and x1 == x2:
            if y2 < y1:
                y1, y2 = y2, y1
            for y in range(y1, y2 + 1):
                cnt = locations.get((x1, y), 0)
                locations[(x1, y)] = cnt + 1
        else:
            if not part2:
                continue
            xs = list(range(x1, x2 + 1))
            ys = list(range(y1, y2 + 1))
            if x1 > x2:
                xs = list(range(x1, x2 - 1, -1))
            if y1 > y2:
                ys = list(range(y1, y2 - 1, -1))
            for x, y in zip(xs, ys):
                cnt = locations.get((x, y), 0)
                locations[(x, y)] = cnt + 1
    return locations


count = 0
for v in solve().values():
    if v > 1:
        count += 1


# Part 1 = 4728
print(f"answer = {count}")

count = 0
for v in solve(True).values():
    if v > 1:
        count += 1

# Part 2 = 17717
print(f"answer = {count}")
