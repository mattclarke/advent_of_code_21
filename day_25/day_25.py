with open("input.txt") as f:
    PUZZLE_INPUT = f.read()

# PUZZLE_INPUT = """
# v...>>.vv>
# .vv>>.vv..
# >>.>v>...v
# >>v>>.>.v.
# v>v.vv.v..
# >.>>..v...
# .vv..>.>v.
# v.v..>>v.v
# ....v..v.>
# """

puzzle_input = [[y for y in x] for x in PUZZLE_INPUT.strip().split("\n")]

east_herd = set()
south_herd = set()
num_rows = len(puzzle_input)
num_cols = len(puzzle_input[0])

for r, row in enumerate(puzzle_input):
    for c, ch in enumerate(row):
        if ch == ">":
            east_herd.add((r, c))
        elif ch == "v":
            south_herd.add((r, c))


def do_turn(east, south, num_rows, num_cols):
    n_east = set()
    n_south = set()
    moved = False

    for e in east:
        r, c = e
        new_c = (c + 1) % (num_cols)
        if (r, new_c) in east or (r, new_c) in south:
            n_east.add((r, c))
            continue
        n_east.add((r, new_c))
        moved = True

    for s in south:
        r, c = s
        new_r = (r + 1) % (num_rows)
        if (new_r, c) in n_east or (new_r, c) in south:
            n_south.add((r, c))
            continue
        n_south.add((new_r, c))
        moved = True

    return n_east, n_south, moved


def pprint(east, south, num_cols, num_rows):
    for r in range(num_rows):
        row = []
        for c in range(num_cols):
            if (r, c) in east:
                row.append(">")
            elif (r, c) in south:
                row.append("v")
            else:
                row.append(".")
        print("".join(row))
    print("")


moved = True
count = 0

while moved:
    # print(count)
    # pprint(east_herd, south_herd, num_cols, num_rows)
    east_herd, south_herd, moved = do_turn(east_herd, south_herd, num_rows, num_cols)
    count += 1

# Part 1 =
print(f"answer = {count}")
