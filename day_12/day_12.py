import copy

with open("input.txt") as f:
    PUZZLE_INPUT = f.read()

# PUZZLE_INPUT = """
# fs-end
# he-DX
# fs-he
# start-DX
# pj-DX
# end-zg
# zg-sl
# zg-pj
# pj-he
# RW-he
# fs-DX
# pj-RW
# zg-RW
# start-pj
# he-WI
# zg-he
# pj-fs
# start-RW
# """

puzzle_input = [x for x in PUZZLE_INPUT.strip().split("\n")]
print(puzzle_input)

NODES = {}

for line in puzzle_input:
    a, b = line.split("-")
    na = NODES.get(a, set())
    nb = NODES.get(b, set())
    na.add(b)
    nb.add(a)
    NODES[a] = na
    NODES[b] = nb


def solve_1(graph):
    def _solve(node, route, paths):
        connections = graph[node]
        for con in connections:
            if con == "start":
                continue
            if con == "end":
                r = copy.copy(route)
                r.append(con)
                paths.add(tuple(r))
                continue
            if con.islower() and con in route:
                continue
            r = copy.copy(route)
            r.append(con)
            _solve(con, r, paths)

    paths = set()
    _solve("start", ["start"], paths)
    return paths


paths = solve_1(NODES)

# Part 1 = 3856
print(f"answer = {len(paths)}")


def solve_2(graph):
    def _solve(node, route, paths, small_twice):
        connections = graph[node]
        for con in connections:
            new_small_twice = small_twice
            if con == "start":
                continue
            if con == "end":
                r = copy.copy(route)
                r.append(con)
                paths.add(tuple(r))
                continue
            if con.islower() and con in route:
                if small_twice:
                    continue
                new_small_twice = True
            r = copy.copy(route)
            r.append(con)
            _solve(con, r, paths, new_small_twice)

    paths = set()
    _solve("start", ["start"], paths, False)
    return paths


paths = solve_2(NODES)

# Part 2 = 116692
print(f"answer = {len(paths)}")
