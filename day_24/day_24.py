with open("input.txt") as f:
    PUZZLE_INPUT = f.read()

puzzle_input = [x for x in PUZZLE_INPUT.strip().split("\n")]
print(puzzle_input)


def inp(value, a, sp, registers):
    registers[a] = value
    return sp + 1, registers


def add(a, b, sp, registers):
    if b in ["w", "x", "y", "z"]:
        b = registers[b]
    else:
        b = int(b)
    registers[a] = b + registers[a]
    return sp + 1, registers


def mul(a, b, sp, registers):
    if b in ["w", "x", "y", "z"]:
        b = registers[b]
    else:
        b = int(b)
    registers[a] = b * registers[a]
    return sp + 1, registers


def div(a, b, sp, registers):
    if b in ["w", "x", "y", "z"]:
        b = registers[b]
    else:
        b = int(b)
    assert b != 0
    registers[a] = registers[a] // b
    return sp + 1, registers


def mod(a, b, sp, registers):
    if b in ["w", "x", "y", "z"]:
        b = registers[b]
    else:
        b = int(b)
    assert registers[a] >= 0
    assert b > 0
    registers[a] = registers[a] % b
    return sp + 1, registers


def eql(a, b, sp, registers):
    if b in ["w", "x", "y", "z"]:
        b = registers[b]
    else:
        b = int(b)
    if registers[a] == b:
        registers[a] = 1
    else:
        registers[a] = 0
    return sp + 1, registers


def run(instructions, z, input_):
    sp = 0
    registers = {
        "w": 0,
        "x": 0,
        "y": 0,
        "z": z,
    }

    while sp < len(instructions):
        if instructions[sp].startswith("inp"):
            _, a = instructions[sp].split(" ")
            sp, registers = inp(input_, a, sp, registers)
        else:
            inst, a, b = instructions[sp].split(" ")
            if inst == "add":
                sp, registers = add(a, b, sp, registers)
            elif inst == "mul":
                sp, registers = mul(a, b, sp, registers)
            elif inst == "div":
                sp, registers = div(a, b, sp, registers)
            elif inst == "mod":
                sp, registers = mod(a, b, sp, registers)
            elif inst == "eql":
                sp, registers = eql(a, b, sp, registers)
            else:
                assert False
    return registers["z"]


DP = set()


def solve(instructions, lowest=False):
    def _recurse(instructions, zed, depth, path, inputs):
        if depth == 14:
            print(path)
            if zed == 0:
                return list(path)
            return []
        commands = instructions[depth]
        for i in inputs:
            ans = run(commands, zed, i)
            new_path = list(path)
            new_path.append(i)
            if (ans, depth) in DP:
                continue
            DP.add((ans, depth))
            done = _recurse(instructions, ans, depth + 1, new_path, inputs)
            if done:
                return done

    if lowest:
        inputs = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    else:
        inputs = [9, 8, 7, 6, 5, 4, 3, 2, 1]

    for i in inputs:
        ans = run(instructions[0], 0, i)
        done = _recurse(instructions, ans, 1, [i], inputs)
        if done:
            return "".join([str(x) for x in done])


# Break into programs per input
programs = []

current = []
for line in puzzle_input:
    if current and line.startswith("inp"):
        programs.append(current)
        current = []
    current.append(line)
if current:
    programs.append(current)
    current = []

# Part 1 = 29599469991739
# print(f"answer = {solve(programs)}")

# Part 2 = 17153114691118
print(f"answer = {solve(programs, True)}")
