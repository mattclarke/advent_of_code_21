from collections import Counter

with open("input.txt") as f:
    PUZZLE_INPUT = f.read()

# PUZZLE_INPUT = """
# NNCB
#
# CH -> B
# HH -> N
# CB -> H
# NH -> C
# HB -> C
# HC -> B
# HN -> C
# NN -> C
# BH -> H
# NC -> B
# NB -> B
# BN -> B
# BB -> N
# BC -> B
# CC -> N
# CN -> C
# """

puzzle_input = [x.strip() for x in PUZZLE_INPUT.strip().split("\n")]
print(puzzle_input)

START = puzzle_input[0]
FORMULAS = {}

for i in range(1, len(puzzle_input)):
    line = puzzle_input[i]
    if line:
        a, b = line.replace(" -> ", " ").split(" ")
        FORMULAS[a] = b


def solve(counter):
    new_counter = Counter()
    for n, v in counter.items():
        if v == 0:
            continue
        new_elem = FORMULAS[n]
        new_counter[n[0] + new_elem] += v
        new_counter[new_elem + n[1]] += v
    return new_counter


def get_element_count(counter):
    element_counter = Counter()

    for n, v in counter.items():
        # Avoid double counting by only counting the first in a pair
        p1 = n[0]
        element_counter[p1] += v

    # Last element needs to be increased by one manually
    element_counter[START[~0]] += 1
    return element_counter


# Create initial pairs
polymer_pairs_count = Counter()
for i in range(len(START) - 1):
    pair = START[i : i + 2]
    polymer_pairs_count[pair] += 1

# Solve
for _ in range(10):
    polymer_pairs_count = solve(polymer_pairs_count)

elem_counts = get_element_count(polymer_pairs_count)
least, most = min(elem_counts.values()), max(elem_counts.values())


# Part 1 = 2891
print(f"answer = {most-least}")

# Create initial pairs
polymer_pairs_count = Counter()
for i in range(len(START) - 1):
    pair = START[i : i + 2]
    polymer_pairs_count[pair] += 1

# Solve
for _ in range(40):
    polymer_pairs_count = solve(polymer_pairs_count)

elem_counts = get_element_count(polymer_pairs_count)
least, most = min(elem_counts.values()), max(elem_counts.values())

# Part 2 = 4607749009683
print(f"answer = {most-least}")
