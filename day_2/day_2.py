with open("input.txt") as f:
    PUZZLE_INPUT = f.read()

# PUZZLE_INPUT = """
# forward 5
# down 5
# forward 8
# up 3
# down 8
# forward 2
# """

puzzle_input = [x.strip() for x in PUZZLE_INPUT.strip().split("\n")]
print(puzzle_input)

depth = 0
horizontal = 0

for line in puzzle_input:
    direction, size = line.split(" ")
    size = int(size)
    if direction.startswith("forward"):
        horizontal += size
    if direction.startswith("down"):
        depth += size
    if direction.startswith("up"):
        depth -= size

# Part 1 = 2039256
print(f"answer = {horizontal * depth}")

depth = 0
horizontal = 0
aim = 0

for line in puzzle_input:
    direction, size = line.split(" ")
    size = int(size)
    if direction.startswith("forward"):
        horizontal += size
        depth += size * aim
    if direction.startswith("down"):
        aim += size
    if direction.startswith("up"):
        aim -= size

# Part 2 = 1856459736
print(f"answer = {horizontal * depth}")
