import copy
import heapq
from collections import defaultdict, deque

with open("input.txt") as f:
    PUZZLE_INPUT = f.read()

# PUZZLE_INPUT = """
# 1163751742
# 1381373672
# 2136511328
# 3694931569
# 7463417111
# 1319128137
# 1359912421
# 3125421639
# 1293138521
# 2311944581
# """

# PUZZLE_INPUT = """
# 116
# 138
# 369
# """

puzzle_input = [[int(y) for y in x] for x in PUZZLE_INPUT.strip().split("\n")]
# print(puzzle_input)

RNUM = len(puzzle_input)
CNUM = len(puzzle_input[0])


def calculate_risk(r, c):
    orig = puzzle_input[r % RNUM][c % CNUM]
    # print(orig)
    cm = c // CNUM
    rm = r // RNUM
    result = orig + cm + rm
    if result > 9:
        result -= 9
    return result


def solve(size=1):
    ROWS = RNUM * size
    COLS = CNUM * size
    best = defaultdict(lambda: 100000000000)
    best[(0, 0)] = 0

    queue = [(0, (0, 0))]
    answer = 1000000000000

    while queue:
        total, pos = heapq.heappop(queue)
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            newr = pos[0] + dr
            newc = pos[1] + dc
            if 0 <= newr < ROWS and 0 <= newc < COLS:
                risk = calculate_risk(newr, newc)
                if total + risk < best[(newr, newc)]:
                    best[(newr, newc)] = total + risk
                    if (newr, newc) == (ROWS - 1, COLS - 1):
                        answer = total + risk
                        continue
                    if total + risk < answer:
                        heapq.heappush(queue, (total + risk, (newr, newc)))
    return answer


# Part 1 = 429
print(f"answer = {solve(1)}")

# Part 2 = 2844
print(f"answer = {solve(5)}")
