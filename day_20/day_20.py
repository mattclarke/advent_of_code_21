import copy

with open("input.txt") as f:
    PUZZLE_INPUT = f.read()

# PUZZLE_INPUT = """
# ..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#
#
# #..#.
# #....
# ##..#
# ..#..
# ..###
# """

puzzle_input = [x for x in PUZZLE_INPUT.strip().split("\n")]
print(puzzle_input)

ALGORITHM = puzzle_input.pop(0)
puzzle_input.pop(0)

lights = set()

for r, line in enumerate(puzzle_input):
    for c, ch in enumerate(line):
        if ch == "#":
            lights.add((r, c))


def find_limits(data):
    c_min = 10000000000
    c_max = -10000000000
    r_min = 10000000000
    r_max = -10000000000
    for p in data:
        c_min = min(c_min, p[1])
        c_max = max(c_max, p[1])
        r_min = min(r_min, p[0])
        r_max = max(r_max, p[0])
    return r_min, r_max, c_min, c_max


def pprint(data, inverse=False):
    r_min, r_max, c_min, c_max = find_limits(data)
    for r in range(r_min - 1, r_max + 2):
        row = []
        for c in range(c_min - 1, c_max + 2):
            if (r, c) in data:
                if not inverse:
                    row.append("#")
                else:
                    row.append(".")
            else:
                if not inverse:
                    row.append(".")
                else:
                    row.append("#")
        print("".join(row))


def do_enhancement(data, inverted=False):
    # For the real input, an empty space surrounded by empty spaces blinks on and
    # off, so the number of lights outside the image is effectively infinity on
    # one turn and then they all switch off on the next turn.
    empty_default = "1" if inverted else "0"

    result = set()
    r_min, r_max, c_min, c_max = find_limits(data)
    for r in range(r_min - 1, r_max + 2):
        for c in range(c_min - 1, c_max + 2):
            bin_data = ""
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    ra = r + dr
                    ca = c + dc
                    if ra < r_min or ra > r_max or ca < c_min or ca > c_max:
                        # Out of bounds of "our" image, so depending on the turn
                        # is either on or off.
                        bin_data += empty_default
                    elif (ra, ca) in data:
                        # In our image and currently "on"
                        bin_data += "1"
                    else:
                        # In our image and currently "off"
                        bin_data += "0"
            as_dec = int(bin_data, 2)
            if ALGORITHM[as_dec] == "#":
                result.add((ra, ca))
    return result


result = copy.copy(lights)
answer_1 = 0

for i in range(50):
    result = do_enhancement(result, i % 2 != 0)
    if i == 1:
        answer_1 = len(result)

# Part 1 = 4968
print(f"answer = {answer_1}")

# Part 2 = 16793
print(f"answer = {len(result)}")
