# Video alternative: https://vimeo.com/954334009/67af9910fc#t=1054

# So far you've spent a lot of time writing new programs.

# This is great for learning the fundamentals of code, but
# actually isn't very realistic. Most software engineers
# spend their time modifying and maintaining existing
# programs, not writing entirely new ones.

# Below is the same program as in the example. Your
# challenge is to implement some improvements:

# 1. Right now users can place their tiles over the other
#    user's tiles. Prevent this.

# 2. Right now if the game reaches a draw with no more free
#    spaces, the game doesn't end. Make it end at that
#    point.

# 3. If you want a real challenge, try to rework this
#    program to support a 5x5 board rather than a 3x3 board.

# 4. If you're still not satisfied, try to rework this
#    program to take a parameter `board_size` and play a
#    game with a board of that size.

# This is getting really challenging now — and is entirely
# optional. Don't forget about your assessment!


def play_game(size=3):
    board = [["." for _ in range(size)] for _ in range(size)]
    free_spaces = size * size
    player = "X"
    while free_spaces:
        print(print_board(board))
        print("It's " + player + "'s turn.")
        # `input` asks the user to type in a string
        # We then need to convert it to a number using `int`
        while True:
            row = int(input("Enter a row: "))
            column = int(input("Enter a column: "))
            if is_space_free(board, (row, column)):
                make_move(board, row, column, player)
                free_spaces -= 1
                break
            else:
                print("Space is not free, try again.")
        groups_to_check = [
            [(row, i) for i in range(size)],
            [(i, column) for i in range(size)],
            [(i, i) for i in range(size)],
            [(i, size - i - 1) for i in range(size)],
        ]
        if is_game_over(board, groups_to_check, player):
            break
        if player == "X":
            player = "O"
        else:
            player = "X"
    print(print_board(board))
    print("Game over!")


def is_space_free(board, coord):
    return board[coord[0]][coord[1]] == "."


def print_board(board):
    formatted_rows = []
    for row in board:
        formatted_rows.append(" ".join(row))
    grid = "\n".join(formatted_rows)
    return grid


def make_move(board, row, column, player):
    board[row][column] = player
    return board


def is_game_over(board, groups_to_check, player):
    # We go through our groups
    opp = "X" if player == "O" else "O"
    for group in groups_to_check:
        won = True
        for coord in group:
            space = board[coord[0]][coord[1]]
            if space == "." or space == opp:
                won = False
                break
        if won:
            return True
    return False


# And test it out:

print("Game time!")
while not (n := int(input('Enter board size: '))) % 2:
    print('Size must be odd number')
play_game(n)
