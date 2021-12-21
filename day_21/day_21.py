# Real
START_P1 = 4
START_P2 = 5

# Example
# START_P1 = 4
# START_P2 = 8

dice_pos = 0
players_pos = [START_P1, START_P2]
players_score = [0, 0]
total_rolls = 0


def roll_dice(pos):
    global total_rolls
    total_rolls += 1
    pos += 1
    if pos > 100:
        pos = 1
    return pos


def move_player(pos, dice):
    pos += dice
    while pos > 10:
        pos -= 10
    return pos


curr_player = 0
while True:
    for _ in range(3):
        dice_pos = roll_dice(dice_pos)
        players_pos[curr_player] = move_player(players_pos[curr_player], dice_pos)
    players_score[curr_player] += players_pos[curr_player]
    if players_score[curr_player] >= 1000:
        break
    curr_player = 1 if curr_player == 0 else 0

# Part 1 = 864900
print(f"answer = {min(players_score) * total_rolls}")

CACHE = {}


def solve2():
    def _recurse(positions, scores, player, num_rolls, roll):
        if (positions, scores, player, num_rolls, roll) in CACHE:
            return CACHE[(positions, scores, player, num_rolls, roll)]

        position = move_player(positions[player], roll)
        positions = (
            (position, positions[1]) if player == 0 else (positions[0], position)
        )
        if num_rolls == 3:
            num_rolls = 0
            score = scores[player] + positions[player]
            scores = (score, scores[1]) if player == 0 else (scores[0], score)
            if scores[player] >= 21:
                return (1, 0) if player == 0 else (0, 1)
            player = 1 if player == 0 else 0
        wins = (0, 0)
        for i in range(3):
            roll = i + 1
            p0, p1 = _recurse(positions, scores, player, num_rolls + 1, roll)
            CACHE[(positions, scores, player, num_rolls + 1, roll)] = (p0, p1)
            wins = (wins[0] + p0, wins[1] + p1)
        return wins

    total_wins = (0, 0)
    for i in range(3):
        p0, p1 = _recurse((START_P1, START_P2), (0, 0), 0, 1, i + 1)
        total_wins = (total_wins[0] + p0, total_wins[1] + p1)
    return total_wins


# Part 2 = 575111835924670
print(f"answer = {max(solve2())}")
