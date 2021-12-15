import copy
import heapq
from collections import defaultdict

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

puzzle_input = [[int(y) for y in x ] for x in PUZZLE_INPUT.strip().split("\n")]
print(puzzle_input)

RNUM = len(puzzle_input)
CNUM = len(puzzle_input[0])

start = (0, 0)

heap = [(RNUM + CNUM, 0, start)]
best = defaultdict(lambda: 1000000000)

best[(0,0)] = 0


minimum = best[(RNUM-1, CNUM-1)]

while heap:
    _, total, pos = heapq.heappop(heap)
    if best[pos] < total:
        continue

    if total > minimum:
        continue

    if pos == (RNUM-1, CNUM-1):
        minimum = min(minimum, total)
        print(minimum, len(heap))
        continue

    for dr,dc in [(1,0), (-1,0), (0,1), (0,-1)]:
        newr = pos[0] + dr
        newc = pos[1] + dc
        if 0 <= newr < RNUM and 0 <= newc < CNUM:
            risk = puzzle_input[newr][newc]
            dist = RNUM - newr + CNUM - newc
            if total + risk < best[(newr, newc)] and total+ risk < minimum:
                best[(newr, newc)] = total + risk
                heapq.heappush(heap, (dist, total + risk, (newr, newc)))

print(minimum)
# Part 1 = 429
print(f"answer = {minimum}")
