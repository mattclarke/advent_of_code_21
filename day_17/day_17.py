import copy
import heapq
from collections import defaultdict, deque


PUZZLE_INPUT = """target area: x=192..251, y=-89..-59"""
# PUZZLE_INPUT = """target area: x=20..30, y=-10..-5"""

puzzle_input = PUZZLE_INPUT.strip()
puzzle_input = (
    puzzle_input.replace("target area: x=", "")
    .replace("..", " ")
    .replace(",", "")
    .replace("y=", "")
)

txmin, txmax, tymin, tymax = (int(x) for x in puzzle_input.split(" "))
print(txmin, txmax, tymin, tymax)


def step(x, y, vx, vy):
    x += vx
    y += vy
    if vx > 0:
        vx -= 1
    elif vx < 0:
        vx += 1
    vy -= 1
    return x, y, vx, vy


def solve(ivx, ivy):
    x_pos = 0
    y_pos = 0
    max_y = 0
    vx = ivx
    vy = ivy

    while x_pos <= txmax and y_pos >= tymin:
        x_pos, y_pos, vx, vy = step(x_pos, y_pos, vx, vy)

        if vx == 0 and x_pos < txmin:
            # No longer going forward
            return False, 0

        if y_pos > tymin and x_pos > txmax:
            # Overshot
            return False, 0

        max_y = max(max_y, y_pos)
        if txmin <= x_pos <= txmax and tymin <= y_pos <= tymax:
            return True, max_y
    return False, 0


vy = tymin
best = 0
solutions = set()

# What goes up must come down! On the way back down the probe always hits y = 0.
# The speed at y = 0 on the way down is the same as the initial speed.
# If that speed is greater than the depth of the target then we have the upper
# bound of speeds that can hit the target.
while vy < -tymin:
    was_hit = False
    for vx in range(1, txmax + 1):
        hit, maxy = solve(vx, vy)
        if hit:
            was_hit = True
            solutions.add((vx, vy))
            best = max(best, maxy)
        if not hit and was_hit:
            # have hit it and are now overshooting so can stop early
            break
    vy += 1


# Part 1 = 3916
print(f"answer = {best}")

# Part 2 = 2986
print(f"answer = {len(solutions)}")
