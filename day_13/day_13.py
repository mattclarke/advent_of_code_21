with open("input.txt") as f:
    PUZZLE_INPUT = f.read()

# PUZZLE_INPUT = """
# 6,10
# 0,14
# 9,10
# 0,3
# 10,4
# 4,11
# 6,0
# 6,12
# 4,1
# 0,13
# 10,12
# 3,4
# 3,0
# 8,4
# 1,10
# 2,14
# 8,10
# 9,0
#
# fold along y=7
# fold along x=5
# """

puzzle_input = [x for x in PUZZLE_INPUT.strip().split("\n")]
print(puzzle_input)

points = set()
folds = []

for line in puzzle_input:
    if not line:
        continue

    if line.startswith("fold"):
        a, b = line.replace("fold along ", "").split("=")
        folds.append((a, int(b)))
    else:
        a, b = [int(x) for x in line.split(",")]
        points.add((a, b))
print(points)
print(folds)


def fold(points, axis, line):
    pts = set()
    if axis == "y":
        for p in points:
            if p[1] < line:
                pts.add(p)
            else:
                y = p[1] - 2 * (p[1] - line)
                pts.add((p[0], y))
    else:
        for p in points:
            if p[0] < line:
                pts.add(p)
            else:
                x = p[0] - 2 * (p[0] - line)
                pts.add((x, p[1]))
    return pts


def pprint(points):
    print("=====================")
    xm = 0
    ym = 0
    for p in points:
        xm = max(xm, p[0])
        ym = max(ym, p[1])
    for y in range(ym + 1):
        line = []
        for x in range(xm + 1):
            if (x, y) in points:
                line.append("#")
            else:
                line.append(" ")
        print("".join(line))


pprint(points)
answer_1 = None

for f in folds:
    axis, line = f
    points = fold(points, axis, line)
    # pprint(points)
    if not answer_1:
        answer_1 = len(points)

pprint(points)

# Part 1 = 781
print(f"answer = {answer_1}")

# Part 2 = PERCGJPB
# Done by reading the letters formed by the points
