with open("input.txt") as f:
    PUZZLE_INPUT = f.read()

# PUZZLE_INPUT = "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"

# PUZZLE_INPUT = """
# be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
# edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
# fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
# fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
# aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
# fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
# dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
# bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
# egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
# gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce
# """

puzzle_input = [x for x in PUZZLE_INPUT.strip().split("\n")]
print(puzzle_input)

segments = {
    0: {"a", "b", "c", "e", "f", "g"},
    1: {"c", "f"},
    2: {"a", "c", "d", "e", "g"},
    3: {"a", "c", "d", "f", "g"},
    4: {"b", "c", "d", "f"},
    5: {"a", "b", "d", "f", "g"},
    6: {"a", "b", "d", "e", "f", "g"},
    7: {"a", "c", "f"},
    8: {"a", "b", "c", "d", "e", "f", "g"},
    9: {"a", "b", "c", "d", "f", "g"},
}

lines = []

for l in puzzle_input:
    front, back = l.split(" | ")
    lines.append((front.split(" "), back.split(" ")))
print(lines)


count = 0
for l in lines:
    _, back = l
    for x in back:
        if len(x) in [
            len(segments[1]),
            len(segments[4]),
            len(segments[7]),
            len(segments[8]),
        ]:
            count += 1


# Part 1 = 342
print(f"answer = {count}")


def solve(line):
    mapping = {}
    reverse_mapping = {}

    # Easy ones first
    front, back = line
    unsolved = []

    for f in front:
        f = sorted(f)
        if len(f) == len(segments[1]):
            mapping[1] = set(f)
            reverse_mapping["".join(f)] = 1
        elif len(f) == len(segments[4]):
            mapping[4] = set(f)
            reverse_mapping["".join(f)] = 4
        elif len(f) == len(segments[7]):
            mapping[7] = set(f)
            reverse_mapping["".join(f)] = 7
        elif len(f) == len(segments[8]):
            mapping[8] = set(f)
            reverse_mapping["".join(f)] = 8
        else:
            unsolved.append(set(f))

    # Hard ones
    for f in unsolved:
        s = "".join(sorted(f))
        if len(f) == 6:
            # 0, 6 or 9
            inter_1 = mapping[1].intersection(f)
            inter_4 = mapping[4].intersection(f)
            if len(inter_1) == 1:
                # 6
                reverse_mapping[s] = 6
            elif len(inter_4) == 4:
                # 9
                reverse_mapping[s] = 9
            else:
                # 0
                reverse_mapping[s] = 0
        elif len(f) == 5:
            # 2, 3 or 5
            inter_1 = mapping[1].intersection(f)
            inter_4 = mapping[4].intersection(f)
            if len(inter_1) == 2:
                # 3
                reverse_mapping[s] = 3
            elif len(inter_4) == 3:
                # 5
                reverse_mapping[s] = 5
            else:
                # 2
                reverse_mapping[s] = 2

    sorted_back = []
    for b in back:
        b = sorted(b)
        sorted_back.append("".join(b))

    answer = ""
    for b in sorted_back:
        answer += str(reverse_mapping[b])
    return int(answer)


result = 0
for line in lines:
    result += solve(line)

# Part 2 = 1068933
print(f"answer = {result}")
