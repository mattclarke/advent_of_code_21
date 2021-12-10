with open("input.txt") as f:
    PUZZLE_INPUT = f.read()

# PUZZLE_INPUT = """
# [({(<(())[]>[[{[]{<()<>>
# [(()[<>])]({[<{<<[]>>(
# {([(<{}[<>[]}>{[]{[(<()>
# (((({<>}<{<{<>}{[]{[]{}
# [[<[([]))<([[{}[[()]]]
# [{[{({}]{}}([{[{{{}}([]
# {<[[]]>}<{[{[{[]{()[[[]
# [<(<(<(<{}))><([]([]()
# <{([([[(<>()){}]>(<<{{
# <{([{{}}[<[[[<>{}]]]>[]]
# """

puzzle_input = [x for x in PUZZLE_INPUT.strip().split("\n")]
print(puzzle_input)

score = 0
incomplete = []  # for part 2

for line in puzzle_input:
    stack = []
    illegal = False
    for c in line:
        if c in ["(", "[", "{", "<"]:
            stack.insert(0, c)
        elif c == ")":
            if stack[0] != "(":
                illegal = True
                score += 3
                break
            else:
                stack.pop(0)
        elif c == "]":
            if stack[0] != "[":
                illegal = True
                score += 57
                break
            else:
                stack.pop(0)
        elif c == "}":
            if stack[0] != "{":
                illegal = True
                score += 1197
                break
            else:
                stack.pop(0)
        elif c == ">":
            if stack[0] != "<":
                illegal = True
                score += 25137
                break
            else:
                stack.pop(0)
        else:
            assert False
    if not illegal:
        incomplete.append(line)

print(incomplete)

# Part 1 = 389589
print(f"answer = {score}")

scores = []

for line in incomplete:
    stack = []
    for c in line:
        if c in ["(", "[", "{", "<"]:
            stack.insert(0, c)
        elif c == ")":
            stack.pop(0)
        elif c == "]":
            stack.pop(0)
        elif c == "}":
            stack.pop(0)
        elif c == ">":
            stack.pop(0)
        else:
            assert False
    score = 0
    for s in stack:
        score *= 5
        if s == "(":
            score += 1
        elif s == "[":
            score += 2
        elif s == "{":
            score += 3
        elif s == "<":
            score += 4
    scores.append(score)

scores.sort()

answer = scores[len(scores) // 2]

# Part 2 = 1190420163
print(f"answer = {answer}")
