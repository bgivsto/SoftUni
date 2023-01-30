def check(board):
    if board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0]:
        return board[1][1]
    for line in board:
        if len(set(line)) == 1:
            return line[0]
    return 0


board = [[int(x) for x in input().split()], [int(x) for x in input().split()], [int(x) for x in input().split()]]
transposed = list(map(list, zip(*board)))

if check(board) == 0 and check(transposed) == 0:
    print("Draw!")
elif check(board) == 1 or check(transposed) == 1:
    print("First player won")
elif check(board) == 2 or check(transposed) == 2:
    print("Second player won")