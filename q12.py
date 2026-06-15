def print_board(b):
    for row in b:
        print("|".join(row))

def check_win(b, p):
    win = [p, p, p]
    rows = any(r == win for r in b)
    cols = any([b[0][i], b[1][i], b[2][i]] == win for i in range(3))
    diag = [b[0][0], b[1][1], b[2][2]] == win or [b[0][2], b[1][1], b[2][0]] == win
    return rows or cols or diag

board = [[" "]*3 for _ in range(3)]
turn = "X"
for _ in range(9):
    print_board(board)
    r, c = map(int, input(f"Player {turn} (row col 0-2): ").split())
    if board[r][c] == " ":
        board[r][c] = turn
        if check_win(board, turn):
            print_board(board)
            print(f"Player {turn} wins!")
            break
        turn = "O" if turn == "X" else "X"
