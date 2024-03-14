#Problem 17: Tic-Tac-Toe
#Implement a simple text-based Tic-Tac-Toe game where two players can take turns making moves.

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 10)

def check_winner(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return True
        
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True

    return False

board = [[" " for _ in range(3)] for _ in range(3)]
player = "X"

print("Welcome to Tic-Tac-Toe!")

for _ in range(9):
    print_board(board)
    row = int(input(f"Player {player}, enter row (0, 1, 2): "))
    col = int(input(f"Player {player}, enter column (0, 1, 2): "))

    if board[row][col] != " ":
        print("That position is already taken. Try again.")
        continue

    board[row][col] = player

    if check_winner(board):
            print_board(board)
            print(f"Player {player} wins!")
            break

    player = "O" if player == "X" else "X"
else:
    print_board(board)
    print("It's a tie!")
   
