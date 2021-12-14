from collections import Counter

with open("input.txt") as f:
    PUZZLE_INPUT = f.read()

PUZZLE_INPUT = """
NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C
"""

puzzle_input = [x.strip() for x in PUZZLE_INPUT.strip().split("\n")]
print(puzzle_input)

START = puzzle_input[0]
FORMULAS = {}

for i in range(1, len(puzzle_input)):
    line = puzzle_input[i]
    if line:
        a, b = line.replace(" -> ", " ").split(" ")
        FORMULAS[a] = b
print(FORMULAS)


def solve(polymer, counter):
    # result = []
    # for i in range(0, len(polymer) - 1):
    #     pair = polymer[i:i + 2]
    #     new_e = FORMULAS[pair]
    #     if i == 0:
    #         result += [pair[0], new_e, pair[1]]
    #     else:
    #         result += [new_e, pair[1]]
    # return "".join(result)
    curr = polymer
    while curr.next:
        nxt = curr.next
        pair = curr.value + nxt.value
        node = Node(FORMULAS[pair])
        curr.next = node
        node.next = nxt
        curr = nxt
        count = counter.get(node.value, 0)
        counter[node.value] = count + 1

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

counter = {START[0]:1}
HEAD = Node(START[0])
prev = HEAD
for i in range(1, len(START)):
    n = Node(START[i])
    prev.next = n
    prev = n
    count = counter.get(START[i], 0)
    counter[START[i]] = count + 1


polymer = START


for i in range(10):
    polymer = solve(HEAD, counter)
    # print(polymer)
    print(i)

# counter = Counter(polymer)

least = 100000
most = 0
for n,v in counter.items():
    least = min(least, v)
    most = max(most, v)

# Part 1 = 2891 14:50
print(f"answer = {most-least}")

# polymer = START
#
# for i in range(40):
#     polymer = solve(polymer)
#     # print(polymer)
#     least = 100000
#
# counter = Counter(polymer)
#
# least = 100000
# most = 0
# for n,v in counter.items():
#     least = min(least, v)
#     most = max(most, v)
#
# print(most-least)
