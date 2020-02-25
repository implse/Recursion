# Write a function solveQueens that accepts a Board as a parameter and tries to place 8 queens on it safely.
# https://www.cs.usfca.edu/~galles/visualization/RecQueens.html
def queens(size):
    board = [-1] * size
    return n_queens(board, 0, size)

def n_queens(board, current, size):
    if current == size:
        return True
    else:
        for i in range(size):
            board[current] = i
            if is_safe(board, current):
                done = n_queens(board, current + 1, size)
                if done:
                    return True
        return False

def is_safe(board, current):
    for i in range(current):
        if board[i] == board[current]:
            return False
        if current - i == abs(board[current] - board[i]):
            return False
    return True

# Test
print(queens(8))
