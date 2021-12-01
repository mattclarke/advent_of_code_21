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

previous = sum(puzzle_input[0:3])
count = 0

for i, depth in enumerate(puzzle_input[3:]):
    score = previous - puzzle_input[i] + depth
    if score > previous:
        count += 1
    previous = score

# Part 2 = 1728
print(f"answer = {count}")
