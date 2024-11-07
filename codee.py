import random

# Define the goal state for reference.
goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

# Print the board.
def print_board(board):
    for row in board:
        print(" ".join(str(cell) if cell != 0 else " " for cell in row))
    print("\n")

# Find the position of the empty space (0).
def find_empty_space(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                return i, j
    return None

# Check if a move is valid.
def is_valid_move(x, y):
    return 0 <= x < 3 and 0 <= y < 3

# Move a tile into the empty space if the move is valid.
def make_move(board, direction):
    x, y = find_empty_space(board)
    if direction == 'up':
        new_x, new_y = x - 1, y
    elif direction == 'down':
        new_x, new_y = x + 1, y
    elif direction == 'left':
        new_x, new_y = x, y - 1
    elif direction == 'right':
        new_x, new_y = x, y + 1
    else:
        return False

    if is_valid_move(new_x, new_y):
        # Swap the empty space with the selected tile.
        board[x][y], board[new_x][new_y] = board[new_x][new_y], board[x][y]
        return True
    return False

# Check if the puzzle is solved.
def is_solved(board):
    return board == goal_state

# Shuffle the board for starting the game.
def shuffle_board(board):
    moves = ['up', 'down', 'left', 'right']
    for _ in range(100):  # Shuffle with 100 random moves.
        make_move(board, random.choice(moves))

# Main function to run the 8-puzzle game simulation.
def run_8_puzzle():
    # Initialize the board.
    board = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]
    
    # Shuffle the board.
    shuffle_board(board)
    print("Starting board:")
    print_board(board)
    
    while not is_solved(board):
        print("Enter your move (up, down, left, right):")
        move = input().strip().lower()
        if move in ['up', 'down', 'left', 'right']:
            if make_move(board, move):
                print_board(board)
            else:
                print("Invalid move. Try again.")
        else:
            print("Invalid input. Please enter 'up', 'down', 'left', or 'right'.")
    
    print("Congratulations! You solved the puzzle.")

# Run the 8-puzzle simulation.
run_8_puzzle()
