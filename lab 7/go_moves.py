# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names:    David Chau
#           Zymraan Khan
#           Leonardo Valle Gomez
# Section: 571
# Assignment: Lab 6
# Date: 15 October 2026

begin = "\x1b[1m"
end = "\x1b[39m\x1b[22m"
red = "\x1b[31m"
blue = "\x1b[34m"
green = "\x1b[32m"

# Initialize board
board = []
for _ in range(9):
    row = []
    for _ in range(9):
        row.append(".")
    board.append(row)

player_one_turn = True

while True:
    # Print board
    for row in board:
        print(" ".join(row))

    # Print turn
    if player_one_turn:
        print("It is player one's turn.")
    else:
        print("It is player two's turn.")

    # Repeatedly get position from user until appropriate
    while True:
        # Get position as string from user
        position_str = input("Enter position as \"x y\" or \"stop\" to quit: ")
        
        # Exit out of game if input is "stop"
        if position_str == "stop":
            exit_game = True
            break
        exit_game = False
    
        # Check if position is valid
        position_list = position_str.split()
        # Check if position has two components
        if len(position_list) == 2:
            # Extract x and y components from position string
            x = int(position_list[0])
            y = int(position_list[1])

            # Check if position is not on the board
            if not(x >= 1 and x <= 9 and y >= 1 and y <= 9):
                print(f"The position ({x}, {y}) is out of bounds.")
            # Check if space at that position is taken
            elif board[x - 1][y - 1] != ".":
                print("That space is already taken.")
            else:
                # Add stone to position
                if player_one_turn:
                    board[x - 1][y - 1] = begin + blue + chr(9679) + end
                else:
                    board[x - 1][y - 1] = begin + red + chr(9679) + end
                break
        else:
            print("Position must have exactly two components.")
        
        # Ask the user if they want to try again since input is invalid
        try_again = input("Do you want to try again? (Y/N) ")
        # Skip turn if no
        if try_again in "Nn":
            break
    if exit_game:
        break

    # Switch turn
    player_one_turn = not player_one_turn