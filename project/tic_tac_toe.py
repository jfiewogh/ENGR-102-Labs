
def print_board(board) :
    print("\n")
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print("\n")
board = [" " for _ in range(9)]
# print_board(board) # testing the print_board function
def check_winner(board, player) : 
    # Check rows
    for i in range(0, 9, 3) :
        if board[i] == board[i + 1] == board[i + 2] == player :
            return True
    # Check columns
    for i in range(3) :
        if board[i] == board[i + 3] == board[i + 6] == player :
            return True
    # Check diagonals
    if board[0] == board[4] == board[8] == player :
        return True
    if board[2] == board[4] == board[6] == player :
        return True
    return False
def play_game() :
    board = [" " for _ in range(9)]
    current_player = "X"
    moves_played = 0
    
    print("Welcome to Tic-Tac-Toe!")
    
    while True :
        print_board(board)
        move = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1

        # check that input is valid
        if not (0 <= int(move) <= 8) :
            print("Invalid input. Please enter a number between 1 and 9.")
            continue

        # check that spot is not taken
        if board[move] in {"X", "O", "x", "o"} :
            print("That spot is already taken. Please try again.")
            continue    

        # Place mark and move foward
        board[move] = current_player
        moves_played += 1
        
        # Check for winner or tie
        if check_winner(board, current_player) :
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        if moves_played == 9 :
            print_board(board)
            print("It's a tie!")
            break

        # switch turns
        current_player = "O" if current_player == "X" else "X"
if __name__ == "__main__" :
    play_game()