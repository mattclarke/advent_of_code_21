with open("input.txt") as f:
    PUZZLE_INPUT = f.read()

puzzle_input = [x for x in PUZZLE_INPUT.strip().split("\n")]


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


CACHE = set()


def solve(instructions, lowest=False):
    def _recurse(instructions, zed, depth, path, inputs):
        if depth == 14:
            # print(path)
            if zed == 0:
                return list(path)
            return []
        if zed > 10 ** 7:
            return []

        commands = instructions[depth]
        for i in inputs:
            ans = run(commands, zed, i)
            new_path = list(path)
            new_path.append(i)
            if (ans, depth) in CACHE:
                continue
            CACHE.add((ans, depth))
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

CACHE.clear()

# Part 2 = 17153114691118
# print(f"answer = {solve(programs, True)}")


# Version 2 - converted input code to Python
def is_zed_zero(W):
    # These values are unique to my input
    A = [1, 1, 1, 26, 1, 1, 1, 26, 26, 1, 26, 26, 26, 26]
    B = [14, 12, 11, -4, 10, 10, 15, -9, -9, 12, -15, -7, -10, 0]
    C = [7, 4, 8, 1, 5, 14, 12, 10, 5, 7, 6, 8, 4, 6]
    zed = 0
    # stack not used in calculation but illustrates the by-hand method below
    stack = []

    for i in range(14):
        w = W[i]
        x = zed % 26
        zed //= A[i]
        x += B[i]
        # x should be 0 on a pop, it isn't then W is wrong somewhere.
        # Seem likely that the mistake is on the first i where x isn't 0 or
        # the corresponding push.
        x = 0 if x == w else 1
        zed *= 25 * x + 1
        zed += (w + C[i]) * x
        if A[i] == 1:
            # we are pushing onto a stack
            stack.append(zed)
        else:
            # popping
            stack = stack[0:-1]

        print(
            zed, x, A[i] == 1, stack
        )
    return zed == 0


# W = [2, 9, 5, 9, 9, 4, 6, 9, 9, 9, 1, 7, 3, 9]
# print(is_zed_zero(W))

W = [1, 7, 1, 5, 3, 1, 1, 4, 6, 9, 1, 1, 1, 8]
print(is_zed_zero(W))

# By hand

# It is essentially a stack (zed), when A = 1 we push a value onto the stack
# (i.e. we add a number to zed).
# and when A is 26 we pop (i.e. we subtract a number from zed).
# For the final zed to be zero, when we pop the value "popped" must equal the
# last value pushed.

#      1   2   3   4   5   6   7   8   9   10  11   12  13   14
# A = [1,  1,  1,  26, 1,  1,  1,  26, 26, 1,  26,  26, 26,  26]
# B = [14, 12, 11, -4, 10, 10, 15, -9, -9, 12, -15, -7, -10, 0]
# C = [7,  4,  8,  1,  5,  14, 12, 10, 5,  7,   6,  8,  4,   6]

# Pushing => zed = (zed * 26) + C[i] + W[i]
# Popping => zed = (zed // 26) + (zed % 26) + B[i] - W[i]

# pushing for 2: zed = (9 * 26) + 4 + 9 = 247
# popping for 13: zed = (247 // 26) + (247 % 26) - 10 - 3 = 9
# pushing for 3: zed = (247 * 26) + 8 + 5 = 6435
# popping for 4: zed = (6435 // 26) + (6435 % 26) - 4 - 9 = 247

# Effectively, when pushing we are adding C[i] + W[i] to a multiple of 26.
# When we pop, we need to cancel out the remainder (i.e. C[i] + W[i]) by
# having a value of W[i+1] where W[i+1] - B[i+1] = C[i] + W[i].
# This implies that W[i+1] = W[i] + C[i] + B[i+1]

# Because it is a stack pairs of push and pop go together,
# e.g. 3 & 4, 7 & 8, 1 & 14 and so on.

# pair 3, 4
# w4 = w3 + 8 - 4 = w3 + 4

# pair 7, 8
# w8 = w7 + 12 - 9 = w7 + 3

# pair 10, 11
# w11 = w10 + 7 - 15 = w10 - 8
# => w10 = 9 and w11 = 1

# pair 6, 9
# w9 = w6 + 14 - 9 = w6 + 5

# pair 5, 12
# w12 = w5 + 5 - 7 = w5 - 2

# pair 2, 13
# w13 = w2 + 4 - 10 = w2 - 6

# pair 1, 14
# w14 = w1 + 7 - 0 = w1 + 7

# Pick the highest numbers that satisfy the equations.
# I.e. one of the pair must be 9

# for 1 and 14 => 1 = 2 and 14 = 9
# [2, x, x, x, x, x, x, x, x, x, x, x, x, 9]

# for 2 and 13
# [2, 9, x, x, x, x, x, x, x, x, x, x, 3, 9]

# for 5 and 12
# [2, 9, x, x, 9, x, x, x, x, x, x, 7, 3, 9]

# for 6 and 12
# [2, 9, x, x, 9, 4, x, x, 9, x, x, 7, 3, 9]

# for 10 and 11
# [2, 9, x, x, 9, 4, x, x, 9, 9, 1, 7, 3, 9]

# for 7 and 8
# [2, 9, x, x, 9, 4, 6, 9, 9, 9, 1, 7, 3, 9]

# for 3 and 4
# [2, 9, 5, 9, 9, 4, 6, 9, 9, 9, 1, 7, 3, 9]

# for the lowest (answer for part 2) do the same thing but
# pick the lowest value that will satisfy the pairs. I.e.
# one the pair is always 1.
