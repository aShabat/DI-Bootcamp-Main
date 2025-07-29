# Step 1: Representing the Game Board
#     You’ll need a way to represent the 3x3 grid.
#     A list of lists (a 2D list) is a good choice.
#     Initially, each cell in the grid should be empty (e.g., represented by a space ‘ ‘).
#
# Step 2: Displaying the Game Board
#     Create a function called display_board() to print the current state of the game board.
#     The output should visually represent the 3x3 grid.
#     Think about how to format the output to make it easy to read.
#
# Step 3: Getting Player Input
#     Create a function called player_input(player) to get the player’s move.
#     The function should ask the player to enter a position (e.g., row and column numbers).
#     Validate the input to ensure it’s within the valid range and that the chosen cell is empty.
#     Think about how to ask the user for input, and how to validate that input.
#
# Step 4: Checking for a Winner
#     Create a function called check_win(board, player) to check if the current player has won.
#     The function should check all possible winning combinations (rows, columns, diagonals).
#     If a player has won, return True; otherwise, return False.
#     Think about how to check every possible winning combination.
#
# Step 5: Checking for a Tie
#     Create a function to check if the game has resulted in a tie.
#     The function should check if all positions of the board are full, without a winner.
#
# Step 6: The Main Game Loop
#     Create a function called play() to manage the game flow.
#     Initialize the game board.
#     Use a while loop to continue the game until there’s a winner or a tie.
#     Inside the loop:
#         Display the board.
#         Get the current player’s input.
#         Update the board with the player’s move.
#         Check for a winner.
#         Check for a tie.
#         Switch to the next player.
#     After the loop ends, display the final result (winner or tie).


def new_board():
    return [[0] * 3, [0] * 3, [0] * 3]


def display_board(board):
    print("-" * 7)
    for row in board:
        row_str = "|"
        for cell in row:
            row_str += " X0"[cell] + "|"
        print(row_str)
        print("-" * 7)


def player_input(board, player):
    while True:
        try:
            row, col = map(
                int,
                input(
                    "Player "
                    + "X0"[player - 1]
                    + " write row and column of your next turn:\n"
                ).split(),
            )
        except:
            print("Incorrect input")
            continue
        if row <= 0 or row > 3 or col <= 0 or col > 3:
            print("Impossible turn.")
        elif board[row - 1][col - 1] != 0:
            print(f"The cell ({row}, {col}) isn't empty.")
        else:
            board[row - 1][col - 1] = player
            return board


def check_win(board, player):
    # rows
    for row in board:
        if row == [player] * 3:
            return True

    # columns
    for col in range(3):
        winning_column = True
        for row in range(3):
            if board[row][col] != player:
                winning_column = False
        if winning_column:
            return True

    # diagonals
    if (
        board[0][0] == board[1][1] == board[2][2] == player
        or board[0][2] == board[1][1] == board[2][0] == player
    ):
        return True

    # if nothing worked
    return False


def check_tie(board):
    for row in board:
        for cell in row:
            if cell == 0:
                return False
    return True


def play():
    board = new_board()
    next_player = 1
    display_board(board)
    while True:
        board = player_input(board, next_player)
        display_board(board)
        if check_win(board, next_player):
            print(f"Player {'X0'[next_player-1]} won!")
            break
        if check_tie(board):
            print("It's a tie!")
            break
        next_player = 3 - next_player


play()
