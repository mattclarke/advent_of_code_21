from copy import copy

with open("input.txt") as f:
    PUZZLE_INPUT = f.read()

# PUZZLE_INPUT = """
# 00100
# 11110
# 10110
# 10111
# 10101
# 01111
# 00111
# 11100
# 10000
# 11001
# 00010
# 01010
# """

puzzle_input = [[y for y in x] for x in PUZZLE_INPUT.strip().split("\n")]
print(puzzle_input)

mcb = []
lcb = []

for x in range(len(puzzle_input[0])):
    ones = 0
    zeros = 0
    for y in range(len(puzzle_input)):
        if puzzle_input[y][x] == "1":
            ones += 1
        else:
            zeros += 1
    if ones > zeros:
        mcb.append("1")
        lcb.append("0")
    else:
        mcb.append("0")
        lcb.append("1")

mcb_int = int("".join(mcb), 2)
lcb_int = int("".join(lcb), 2)

# Part 1 = 2595824
print(f"answer = {mcb_int * lcb_int}")


def eliminate(data, index, least=False):
    if least:
        comparison = lambda o, z: o < z
    else:
        comparison = lambda o, z: o >= z
    ones = 0
    zeros = 0
    for d in data:
        if d[index] == "1":
            ones += 1
        else:
            zeros += 1

    to_keep = "1" if comparison(ones, zeros) else "0"
    result = []
    for d in data:
        if d[index] == to_keep:
            result.append(d)
    return result


oxy_data = copy(puzzle_input)
co2_data = copy(puzzle_input)

index = 0

while len(oxy_data) > 1 or len(co2_data) > 1:
    if len(oxy_data) > 1:
        oxy_data = eliminate(oxy_data, index)
    if len(co2_data) > 1:
        co2_data = eliminate(co2_data, index, True)
    index += 1

oxygen = int("".join(oxy_data[0]), 2)
co2 = int("".join(co2_data[0]), 2)

# Part 2 = 2135254
print(f"answer = {oxygen * co2}")
