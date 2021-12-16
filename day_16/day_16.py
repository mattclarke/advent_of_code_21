import functools

with open("input.txt") as f:
    PUZZLE_INPUT = f.read()

# PUZZLE_INPUT = "38006F45291200"
# PUZZLE_INPUT = "EE00D40C823060"
# PUZZLE_INPUT = "8A004A801A8002F478"
# PUZZLE_INPUT = "620080001611562C8802118E34"
# PUZZLE_INPUT = "C0015000016115A2E0802F182340"
# PUZZLE_INPUT = "A0016C880162017C3686B18A3D4780"
# PUZZLE_INPUT = "C200B40A82"
# PUZZLE_INPUT = "04005AC33890"
# PUZZLE_INPUT = "880086C3E88112"
# PUZZLE_INPUT = "D8005AC2A8F0"
# PUZZLE_INPUT = "9C0141080250320F1802104A08"

puzzle_input = [y for x in PUZZLE_INPUT.strip().split("\n") for y in x]
# print(puzzle_input)

MAPPING = {
    "0000": "0",
    "0001": "1",
    "0010": "2",
    "0011": "3",
    "0100": "4",
    "0101": "5",
    "0110": "6",
    "0111": "7",
    "1000": "8",
    "1001": "9",
    "1010": "a",
    "1011": "b",
    "1100": "c",
    "1101": "d",
    "1110": "e",
    "1111": "f",
}

RMAPPING = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}


def get_version(data, sp):
    result = "0"
    for _ in range(3):
        result += data[sp]
        sp += 1
    return MAPPING[result], sp


def get_id(data, sp):
    result = "0"
    for _ in range(3):
        result += data[sp]
        sp += 1
    return MAPPING[result], sp


def get_literal(data, sp):
    result = []
    not_last = True
    while not_last:
        not_last = data[sp] == "1"
        sp += 1
        value = ""
        for _ in range(4):
            value += data[sp]
            sp += 1
        result.append(MAPPING[value])
    ans = "".join(result).encode()
    return int(ans, 16), sp


def get_len_type(data, sp):
    result = data[sp]
    return result, sp + 1


def get_len_sub(id, data, sp):
    result = "0"
    size = 15 if id == "0" else 11
    for _ in range(size):
        result += data[sp]
        sp += 1
    return int(result, 2), sp


versions = []


def solve(data, sp):
    version, sp = get_version(data, sp)
    versions.append(version)
    id_, sp = get_id(data, sp)
    if id_ == "4":
        lit, sp = get_literal(data, sp)
        return sp, lit
    else:
        ltype, sp = get_len_type(data, sp)
        length, sp = get_len_sub(ltype, data, sp)
        values = []
        if ltype == "1":
            for _ in range(length):
                sp, val = solve(data, sp)
                if val is not None:
                    values.append(val)
        else:
            start_sp = sp
            while sp < start_sp + length:
                sp, val = solve(data, sp)
                if val is not None:
                    values.append(val)
        if id_ == "0":
            return sp, sum(values)
        elif id_ == "1":
            return sp, functools.reduce(lambda a, b: a * b, values)
        elif id_ == "2":
            return sp, min(values)
        elif id_ == "3":
            return sp, max(values)
        elif id_ == "5":
            return sp, 1 if values[0] > values[1] else 0
        elif id_ == "6":
            return sp, 1 if values[0] < values[1] else 0
        elif id_ == "7":
            return sp, 1 if values[0] == values[1] else 0
    assert False


data = []
for c in puzzle_input:
    for x in RMAPPING[c]:
        data.append(x)

_, part_2 = solve(data, 0)
part_1 = sum([int(x) for x in versions])

# Part 1 = 904
print(f"answer = {part_1}")

# Part 2 = 200476472872
print(f"answer = {part_2}")
