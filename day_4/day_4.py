from copy import copy

with open("input.txt") as f:
    PUZZLE_INPUT = f.read()

# PUZZLE_INPUT = """
# 7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1
#
# 22 13 17 11  0
#  8  2 23  4 24
# 21  9 14 16  7
#  6 10  3 18  5
#  1 12 20 15 19
#
#  3 15  0  2 22
#  9 18 13 17  5
# 19  8  7 25 23
# 20 11 10 24  4
# 14 21 16 12  6
#
# 14 21 17 24  4
# 10 16 15  9 19
# 18  8 23 26 20
# 22 11 13  6  5
#  2  0 12  3  7
# """

puzzle_input = [x for x in PUZZLE_INPUT.strip().split("\n") if x]
print(puzzle_input)

numbers_called = [int(x) for x in puzzle_input.pop(0).split(",")]
print(numbers_called)

boards = []

board = []

for i, line in enumerate(puzzle_input):
    if i % 5 == 0 and i != 0:
        boards.append(board)
        board = []

    nums = [int(x) for x in line.replace("  ", " ").strip().split(" ")]
    board.append(nums)
boards.append(board)

print(boards)
marked_boards = copy(boards)


def do_game(marked_boards, numbers_called):
    for n in numbers_called:
        for b in marked_boards:
            for y in range(5):
                all_x = True
                for x in range(5):
                    if b[y][x] == n:
                        b[y][x] = "X"
                    elif b[y][x] != "X":
                        all_x = False
                if all_x:
                    return b, n
            # Check columns
            for x in range(5):
                all_x = True
                for y in range(5):
                    if b[y][x] != "X":
                        all_x = False
                if all_x:
                    return b, n
    raise RuntimeError("No winner")


winner, num = do_game(marked_boards, numbers_called)
print(winner, num)


def total_up(board):
    total = 0
    for y in range(5):
        for x in range(5):
            if board[y][x] != "X":
                total += board[y][x]
    return total


# Part 1 = 46920
print(f"answer = {total_up(winner) * num}")


def do_game_2(marked_boards, numbers_called):
    boards_remaining = {x for x in range(len(marked_boards))}

    for n in numbers_called:
        for i, b in enumerate(marked_boards):
            if i not in boards_remaining:
                continue
            for y in range(5):
                all_x = True
                for x in range(5):
                    if b[y][x] == n:
                        b[y][x] = "X"
                    elif b[y][x] != "X":
                        all_x = False
                if all_x:
                    if len(boards_remaining) == 1:
                        return b, n
                    boards_remaining.remove(i)
            # Check columns
            for x in range(5):
                all_x = True
                for y in range(5):
                    if b[y][x] != "X":
                        all_x = False
                if all_x:
                    if len(boards_remaining) == 1:
                        return b, n
                    if i in boards_remaining:
                        boards_remaining.remove(i)
    raise RuntimeError("No winner")


marked_boards = copy(boards)
loser, num = do_game_2(marked_boards, numbers_called)
print(loser, num)


# Part 2 = 12635
print(f"answer = {total_up(loser) * num}")
