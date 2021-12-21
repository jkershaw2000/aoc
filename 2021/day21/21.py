import itertools
from functools import cache

pos = [10, 3]
scores = [0, 0]
BOARD_SIZE = 10

count, die = 0, 0
win = False
while not win:
    for i in range(2):
        for _ in range(3):
            die = die % 100 + 1
            pos[i] = (pos[i] + die - 1) % BOARD_SIZE + 1
        count += 3

        scores[i] += pos[i]
        if scores[i] >= 1000:
            win = True
            break
part1 = min(scores) * count

throws = [sum(x) for x in itertools.product([1, 2, 3], repeat=3)]
scores = [0, 0]


@cache
def solve_part2(p_1, p_2, s_1, s_2, turn=True):
    # Base Case(s)
    if s_1 >= 21:
        return 1, 0
    if s_2 >= 21:
        return 0, 1

    # Position to be used depending on whose turn it is
    p = p_1 if turn else p_2
    # where player can end up with all possibilities on that turn
    new_pos = [(p + throw - 1) % 10 + 1 for throw in throws]

    # Recursive Case(s) - continue each game from all new available states
    if turn:
        quantum_games = (
            solve_part2(new_p, p_2, s_1 + new_p, s_2, False) for new_p in new_pos
        )
    else:
        quantum_games = (
            solve_part2(p_1, new_p, s_1, s_2 + new_p, True) for new_p in new_pos
        )
    # Interested in how many wins each player has
    return sum(x for x, _ in quantum_games), sum(x for _, x in quantum_games)


part2 = max(solve_part2(10, 3, 0, 0))
print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
