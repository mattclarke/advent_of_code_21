import copy
from collections import defaultdict


# EXAMPLE
puzzle_input = [
    [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    ["#", "#", "B", "#", "C", "#", "B", "#", "D", "#", "#"],
    ["#", "#", "A", "#", "D", "#", "C", "#", "A", "#", "#"],
]

puzzle_input_2 = [
    [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    ["#", "#", "B", "#", "C", "#", "B", "#", "D", "#", "#"],
    ["#", "#", "D", "#", "C", "#", "B", "#", "A", "#", "#"],
    ["#", "#", "D", "#", "B", "#", "A", "#", "C", "#", "#"],
    ["#", "#", "A", "#", "D", "#", "C", "#", "A", "#", "#"],
]


# REAL
# puzzle_input = [
#     [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
#     ["#", "#", "D", "#", "D", "#", "C", "#", "C", "#", "#"],
#     ["#", "#", "B", "#", "A", "#", "B", "#", "A", "#", "#"],
# ]


puzzle_input_2 = [
    [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    ["#", "#", "D", "#", "D", "#", "C", "#", "C", "#", "#"],
    ["#", "#", "D", "#", "C", "#", "B", "#", "A", "#", "#"],
    ["#", "#", "D", "#", "B", "#", "A", "#", "C", "#", "#"],
    ["#", "#", "B", "#", "A", "#", "B", "#", "A", "#", "#"],
]


HOMES = {
    "A": ((1, 2), (2, 2), (3, 2), (4, 2)),
    "B": ((1, 4), (2, 4), (3, 4), (4, 4)),
    "C": ((1, 6), (2, 6), (3, 6), (4, 6)),
    "D": ((1, 8), (2, 8), (3, 8), (4, 8)),
}

COSTS = {
    "A": 1,
    "B": 10,
    "C": 100,
    "D": 1000,
}

FORBIDDEN = {(0, 2), (0, 4), (0, 6), (0, 8)}


def pprint(board):
    for y in board:
        print("".join(y))
    print()


def can_reach(start, end, board):
    rs, cs = start
    re, ce = end
    if rs < re:
        # From top row
        startx = min(cs, ce) + 1
        endx = max(cs, ce)
        for i in range(startx, endx):
            if board[0][i] in ["A", "B", "C", "D"]:
                return False
        return True
    else:
        # To top row
        startx = min(cs, ce) + 1
        endx = max(cs, ce) + 1
        for i in range(startx, endx):
            if board[0][i] in ["A", "B", "C", "D"]:
                return False
        return True


def is_home(pos, board):
    ch = board[pos[0]][pos[1]]
    r, c = pos
    if (r, c) not in HOMES[ch]:
        return False
    r2 = board[r + 1][c] if r + 1 < len(board) else ch
    r3 = board[r + 2][c] if r + 2 < len(board) else ch
    r4 = board[r + 2][c] if r + 3 < len(board) else ch

    if r2 == ch and r3 == ch and r4 == ch:
        return True

    return False


def can_move(board):
    result = defaultdict(lambda: [])
    # Can move home?
    for i, ch in enumerate(board[0]):
        if ch in ["A", "B", "C", "D"]:
            homes = HOMES[ch]
            home1 = board[homes[0][0]][homes[0][1]]
            home2 = board[homes[1][0]][homes[1][1]]
            home3 = board[homes[2][0]][homes[2][1]] if len(board) > 3 else ch
            home4 = board[homes[3][0]][homes[3][1]] if len(board) > 3 else ch
            if home4 == ".":
                if can_reach((0, i), homes[3], board):
                    result[(0, i)] = [homes[3]]
            elif home3 == "." and home4 == ch:
                if can_reach((0, i), homes[2], board):
                    result[(0, i)] = [homes[2]]
            elif home2 == "." and home3 == ch and home4 == ch:
                if can_reach((0, i), homes[1], board):
                    result[(0, i)] = [homes[1]]
            elif home1 == "." and home2 == ch and home3 == ch and home4 == ch:
                if can_reach((0, i), homes[0], board):
                    result[(0, i)] = [homes[0]]
    # Can move out from home row?
    for row in [1, 2, 3, 4]:
        if row >= len(board):
            continue
        for i, ch in enumerate(board[row]):
            if ch in ["A", "B", "C", "D"]:
                if board[row - 1][i] in ["A", "B", "C", "D"]:
                    # Blocked
                    continue
                if is_home((row, i), board):
                    # Home and safe
                    continue
                # Can go straight home
                homes = HOMES[ch]
                home1 = board[homes[0][0]][homes[0][1]]
                home2 = board[homes[1][0]][homes[1][1]]
                home3 = board[homes[2][0]][homes[2][1]] if len(board) > 3 else ch
                home4 = board[homes[3][0]][homes[3][1]] if len(board) > 3 else ch
                if home4 == ".":
                    if can_reach((row, i), homes[3], board):
                        result[(row, i)] = [homes[3]]
                        continue
                elif home3 == "." and home4 == ch:
                    if can_reach((row, i), homes[2], board):
                        result[(row, i)] = [homes[2]]
                        continue
                elif home2 == "." and home3 == ch and home4 == ch:
                    if can_reach((row, i), homes[1], board):
                        result[(row, i)] = [homes[1]]
                        continue
                elif home1 == "." and home2 == ch and home3 == ch and home4 == ch:
                    if can_reach((row, i), homes[0], board):
                        result[(row, i)] = [homes[0]]
                        continue

                for x in range(0, i):
                    if board[0][x] in ["A", "B", "C", "D"]:
                        result[(row, i)].clear()
                    elif (0, x) not in FORBIDDEN:
                        result[(row, i)].append((0, x))

                for x in range(i, len(board[0])):
                    if board[0][x] in ["A", "B", "C", "D"]:
                        break
                    elif (0, x) not in FORBIDDEN:
                        result[(row, i)].append((0, x))
    return result


def is_done(board):
    for c in ["A", "B", "C", "D"]:
        home1, home2, home3, home4 = HOMES[c]
        if len(board) == 3:
            if board[home1[0]][home1[1]] != c or board[home2[0]][home2[1]] != c:
                return False
        else:
            if (
                board[home1[0]][home1[1]] != c
                or board[home2[0]][home2[1]] != c
                or board[home3[0]][home3[1]] != c
                or board[home4[0]][home4[1]] != c
            ):
                return False

    return True


best = 1000000000000000000


def solve(board):
    global best
    best = 10000000000000000

    def _recurse(board, score):
        global best
        if score >= best:
            return

        done = is_done(board)

        if done:
            best = min(best, score)
            print(f"winner {score}, {best}")
            return

        moveable = can_move(board)
        for pos, options in moveable.items():
            for o in options:
                ch = board[pos[0]][pos[1]]
                new_board = copy.deepcopy(board)
                new_board[o[0]][o[1]], new_board[pos[0]][pos[1]] = (
                    new_board[pos[0]][pos[1]],
                    new_board[o[0]][o[1]],
                )
                steps = abs(pos[1] - o[1])
                steps += pos[0]
                steps += o[0]
                _recurse(new_board, score + steps * COSTS[ch])

    _recurse(board, 0)
    return best


# Part 1 = 16059
# print(f"answer = {solve(copy.deepcopy(puzzle_input))}")


# Part 2 = 43117
print(f"answer = {solve(copy.deepcopy(puzzle_input_2))}")
