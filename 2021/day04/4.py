with open("2021/day4/4.in", "r") as f:
    data = f.readlines()

# Parse input
numbers = [int(num) for num in data.pop(0).split(",")]
n_boards = len(data) // 6
bingo_boards = [[[int(num) for num in line.split()] for line in data[6 * i + 1: 6 * (i + 1)]] for i in range(n_boards)]

def check_win(board):
    #  Check for row win
    for row in board:
        if sum(row) == -5:
            return True
    
    # Check for col win, transpose and repeat row check
    board_transpose = [x for x in zip(*board)]    
    for row in board_transpose:
        if sum(row) == -5:
            return True
    return False
 
def play():
    called = []
    winners = []
    for num in numbers:
        called.append(num)
        for idx, board in enumerate(bingo_boards):
            # Change to -1 if number found
            for y in range(len(board)):
                for x in range(len(board[y])):
                    if board[y][x] == num:
                        board[y][x] = -1

            winner = check_win(board)
            # First bingo for part 1
            if winner and len(winners) == 0:
                best_board = idx
                first_win_num = called[-1]
                winners.append(idx)
            #  All next bingos, single board can't have two bingos
            elif winner and idx not in winners:
                winners.append(idx)

        # Check if all boards have had a bingo
        if len(winners) == len(bingo_boards):
            last_win_num = called[-1]
            worse_board = winners[-1]
            break

    return first_win_num, best_board, last_win_num, worse_board


final_num_best, winning_board, final_num_worse, losing_board  = play()
# replace -1 with 0 for summing, flatten list
winner = [num if num != -1 else 0 for num in sum(bingo_boards[winning_board],[])]
loser = [num if num != -1 else 0 for num in sum(bingo_boards[losing_board],[])]
part1 = final_num_best * sum(winner)
part2 = final_num_worse * sum(loser)
print(f"Part1: {part1}")
print(f"Part2: {part2}")
