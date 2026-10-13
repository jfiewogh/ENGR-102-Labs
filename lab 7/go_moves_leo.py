# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names:    David Chau
#           Zymraan Khan
#           Leonardo Valle Gomez
# Section: 571
# Assignment: Lab 2
# Date: 15 September 2026
#
print("Play Go Board")
print()
s = input("Type \"start\" to begin: ")
print()
blank = "."
board = [["." for _ in range(9)] for _ in range(9)]
if s == "start" or s == "Start" or s == "START":
    print("Player 1 is O and Player 2 is X")
    while any ("." in r for r in board):
        for r in board:
            print(" ".join(r))
        print()
        player1 = input("Player 1, please enter your move as row,column:")
        row_num = int(player1[0])
        col_num = int(player1[2])
        while board[row_num][col_num]!= ".":
            print("That space is already taken. Please choose another space.")
            player1 = input("Player 1, please enter your move as row,column:")
            row_num = int(player1[0])
            col_num = int(player1[2])
        else:
            board[row_num][col_num] = "O"
        for r in board:
            print(" ".join(r))
        player2 = input("Player 2, please enter your move as row,column:")
        row_num = int(player2[0])
        col_num = int(player2[2])
        while board[row_num][col_num] != ".":
            print("That space is already taken. Please choose another space.")
            player2 = input("Player 2, please enter your move as row,column:")
            row_num = int(player2[0])
            col_num = int(player2[2])
        else:
            board[row_num][col_num] = "X"
        
else:
    print("ok")
