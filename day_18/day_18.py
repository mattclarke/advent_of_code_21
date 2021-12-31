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


class Node:
    def __init__(self, left=None, right=None, value=None):
        self.left = left
        self.right = right
        self.parent = None
        self.value = value

    def __repr__(self):
        if self.value is not None:
            return f"{self.value}"
        return f"[{self.left},{self.right}]"


def generate_pair(data):
    if data.startswith("["):
        if not data[~0] == "]":
            assert False, "messed up"
        data = data[1:-1]
    if data.count("[") == 0:
        # Simple pair
        vleft, vright = [
            int(x) for x in data.replace("[", "").replace("]", "").split(",")
        ]
        return Node(Node(value=vleft), Node(value=vright))
    else:
        num_open = 0
        for i, ch in enumerate(data):
            if ch == "[":
                num_open += 1
            if ch == "]":
                num_open -= 1
            if num_open == 0 and ch == ",":
                break
        left = data[0:i]
        right = data[i + 1 :]
        if all([x.isdigit() for x in left]):
            vleft = int(left)
            left = Node(value=vleft)
        if all([x.isdigit() for x in right]):
            vright = int(right)
            right = Node(value=vright)
        return Node(left, right)


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
            if node.left.value is not None:
                if exploder:
                    right = node.left
                else:
                    left = node.left
            else:
                left, exploder, right = _recurse(
                    node.left, depth + 1, left, exploder, right
                )
        if right:
            # No point continuing
            return left, exploder, right
        if node.right is not None:
            if node.right.value is not None:
                if not exploder:
                    left = node.right
                elif not right:
                    right = node.right
            else:
                left, exploder, right = _recurse(
                    node.right, depth + 1, left, exploder, right
                )
        return left, exploder, right

    left, exploder, right = _recurse(tree, 0)
    if not exploder:
        return False

    if left:
        left.value += exploder.left.value

    if right:
        right.value += exploder.right.value

    if exploder.parent.left == exploder:
        exploder.parent.left = Node(value=0)
    else:
        exploder.parent.right = Node(value=0)

    return True


def split(tree):
    def _recurse(node):
        if node.left:
            if node.left.value is not None:
                if node.left.value > 9:
                    value = node.left.value
                    left = value // 2
                    right = value // 2 + value % 2

                    node.left = Node(Node(value=left), Node(value=right))
                    node.left.parent = node
                    return True
            else:
                done = _recurse(node.left)
                if done:
                    return True
        if node.right:
            if node.right.value is not None:
                if node.right.value > 9:
                    value = node.right.value
                    left = value // 2
                    right = value // 2 + value % 2

                    node.right = Node(Node(value=left), Node(value=right))
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
            if node.left.value is not None:
                left = node.left.value
            else:
                left = _recurse(node.left)
        if node.right is not None:
            if node.right.value is not None:
                right = node.right.value
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
    new_top = Node(top, addition)
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
        top = Node(copy.deepcopy(base), copy.deepcopy(trees[k2]))
        top.left.parent = top
        top.right.parent = top
        top = reduce(top)
        answer = max(answer, calculate(top))

# Part 2 = 4864
print(f"answer = {answer}")
