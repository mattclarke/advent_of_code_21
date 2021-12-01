with open("input.txt") as f:
    PUZZLE_INPUT = f.read()

# PUZZLE_INPUT = """
# 199
# 200
# 208
# 210
# 200
# 207
# 240
# 269
# 260
# 263
# """

puzzle_input = [int(x.strip()) for x in PUZZLE_INPUT.strip().split("\n")]
print(puzzle_input)

previous = None
count = 0

for depth in puzzle_input:
    if previous is None:
        previous = depth
        continue
    if depth > previous:
        count += 1
    previous = depth

# Part 1 = 1688
print(f"answer = {count}")

window = puzzle_input[0:3]
scores = [sum(window)]
previous = None
count = 0

for depth in puzzle_input[3:]:
    window.pop(0)
    window.append(depth)
    scores.append(sum(window))

for score in scores:
    if previous is None:
        previous = score
        continue
    if score > previous:
        count += 1
    previous = score

# Part 2 = 1728
print(f"answer = {count}")
