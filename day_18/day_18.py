import copy

with open("input.txt") as f:
    PUZZLE_INPUT = f.read()

# PUZZLE_INPUT = """
# [[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
# [[[5,[2,8]],4],[5,[[9,9],0]]]
# [6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
# [[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
# [[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
# [[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
# [[[[5,4],[7,7]],8],[[8,3],8]]
# [[9,3],[[9,9],[6,[4,9]]]]
# [[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
# [[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]
# """

puzzle_input = [x for x in PUZZLE_INPUT.strip().split("\n")]
print(puzzle_input)


class Pair:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right
        self.parent = None

    def __repr__(self):
        return f"[{self.left},{self.right}]"


def generate_pair(data):
    if data.startswith("["):
        if not data[~0] == "]":
            assert False, "messed up"
        data = data[1:-1]
    if data.count("[") == 0:
        # Simple pair
        left, right = [
            int(x) for x in data.replace("[", "").replace("]", "").split(",")
        ]
        return Pair(left, right)
    else:
        num_open = 0
        for i, ch in enumerate(data):
            if ch == "[":
                num_open += 1
            if ch == "]":
                num_open -= 1
            if num_open == 0 and ch == ",":
                break
        # print(i)
        left = data[0:i]
        right = data[i + 1 :]
        if all([x.isdigit() for x in left]):
            left = int(left)
        if all([x.isdigit() for x in right]):
            right = int(right)
        return Pair(left, right)


def generate_tree(data):
    def _recurse(pair):
        if str(pair.left).startswith("["):
            subpair = generate_pair(pair.left)
            subpair = _recurse(subpair)
            subpair.parent = pair
            pair.left = subpair
        if str(pair.right).startswith("["):
            subpair = generate_pair(pair.right)
            subpair = _recurse(subpair)
            subpair.parent = pair
            pair.right = subpair
        return pair

    top_pair = generate_pair(data)
    top_pair = _recurse(top_pair)
    return top_pair


def explode(tree):
    def _recurse(node, depth, left=None, exploder=None, right=None):
        if depth == 4 and not exploder:
            # print(f"boom {node}")
            exploder = node
            return left, exploder, right
        if node.left is not None:
            if isinstance(node.left, int):
                if not exploder:
                    left = node
                elif not right:
                    right = node
            else:
                left, exploder, right = _recurse(
                    node.left, depth + 1, left, exploder, right
                )
        if node.right is not None:
            if isinstance(node.right, int):
                if not exploder:
                    left = node
                elif not right:
                    right = node
            else:
                left, exploder, right = _recurse(
                    node.right, depth + 1, left, exploder, right
                )
        return left, exploder, right

    left, exploder, right = _recurse(tree, 0)
    if not exploder:
        return False
    # print(left, exploder, right)
    if (
        exploder.parent
        and exploder.parent.right == exploder
        and isinstance(exploder.parent.left, int)
    ):
        exploder.parent.left += exploder.left
    elif exploder.parent and left == exploder.parent:
        left.left += exploder.left
    elif left:
        if isinstance(left.right, int):
            left.right += exploder.left
        elif isinstance(left.left, int):
            left.left += exploder.left
        else:
            assert False
    if (
        exploder.parent
        and exploder.parent.left == exploder
        and isinstance(exploder.parent.right, int)
    ):
        exploder.parent.right += exploder.right
    elif exploder.parent and right == exploder.parent:
        right.right += exploder.right
    elif right:
        if isinstance(right.left, int):
            right.left += exploder.right
        elif isinstance(right.right, int):
            right.right += exploder.right
        else:
            assert False
    if exploder.parent and exploder.parent.left == exploder:
        exploder.parent.left = 0
    elif exploder.parent and exploder.parent.right == exploder:
        exploder.parent.right = 0
    return True


def split(tree):
    def _recurse(node):
        if node.left:
            if isinstance(node.left, int):
                if node.left > 9:
                    left = node.left // 2
                    right = node.left // 2
                    if node.left % 2 == 1:
                        right += 1
                    node.left = Pair(left, right)
                    node.left.parent = node
                    return True
            else:
                done = _recurse(node.left)
                if done:
                    return True
        if node.right:
            if isinstance(node.right, int):
                if node.right > 9:
                    left = node.right // 2
                    right = node.right // 2
                    if node.right % 2 == 1:
                        right += 1
                    node.right = Pair(left, right)
                    node.right.parent = node
                    return True
            else:
                done = _recurse(node.right)
                return done
        return False

    return _recurse(tree)


def calculate(tree):
    def _recurse(node):
        if node.left is not None:
            if isinstance(node.left, int):
                left = node.left
            else:
                left = _recurse(node.left)
        if node.right is not None:
            if isinstance(node.right, int):
                right = node.right
            else:
                right = _recurse(node.right)
        return 3 * left + 2 * right

    return _recurse(tree)


def reduce(tree):
    reduced = False
    while not reduced:
        reduced = True
        if explode(tree):
            reduced = False
            continue
        if reduced:
            if split(tree):
                reduced = False
    return tree


top = None

for line in puzzle_input:
    if not top:
        top = generate_tree(line)
        continue

    addition = generate_tree(line)
    new_top = Pair(top, addition)
    top.parent = new_top
    addition.parent = new_top
    top = new_top
    top = reduce(top)

# Part 1 = 4033
print(f"answer = {calculate(top)}")

trees = {}

for i, line in enumerate(puzzle_input):
    trees[i] = generate_tree(line)

answer = 0
for k1 in trees.keys():
    base = trees[k1]
    for k2 in trees.keys():
        if k1 == k2:
            continue
        top = Pair(copy.deepcopy(base), copy.deepcopy(trees[k2]))
        top.left.parent = top
        top.right.parent = top
        top = reduce(top)
        answer = max(answer, calculate(top))

# Part 2 = 4864
print(f"answer = {answer}")
