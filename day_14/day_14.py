import copy
from collections import Counter, defaultdict

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
    result = copy.deepcopy(counter)
    for n, v in counter.items():
        if v == 0:
            continue
        new_elem = FORMULAS[n]
        result[n[0] + new_elem] += v
        result[new_elem + n[1]] += v
        result[n] -= v
    return result


def get_element_count(counter):
    counts = {}

    for n, v in counter.items():
        # Avoid double counting by only counting the first in a pair
        p1 = n[0]
        p1c = counts.get(p1, 0)
        counts[p1] = p1c + v

    # Last element needs to be increased by one manually
    counts[START[~0]] += 1
    return counts


def find_max_min(counts):
    least = 10000000000000000000000000
    most = 0

    for v in counts.values():
        least = min(least, v)
        most = max(most, v)
    return least, most


# Create initial pairs
polymer_pairs_count = defaultdict(lambda: 0)
for i in range(len(START) - 1):
    pair = START[i : i + 2]
    polymer_pairs_count[pair] += 1

# Solve
for i in range(10):
    polymer_pairs_count = solve(polymer_pairs_count)

counts = get_element_count(polymer_pairs_count)
least, most = find_max_min(counts)


# Part 1 = 2891
print(f"answer = {most-least}")

# Create initial pairs
polymer_pairs_count = defaultdict(lambda: 0)
for i in range(len(START) - 1):
    pair = START[i : i + 2]
    polymer_pairs_count[pair] += 1

# Solve
for i in range(40):
    polymer_pairs_count = solve(polymer_pairs_count)

counts = get_element_count(polymer_pairs_count)
least, most = find_max_min(counts)

# Part 2 = 4607749009683
print(f"answer = {most-least}")
