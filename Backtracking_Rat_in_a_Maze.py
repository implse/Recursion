# A Maze is given as N*N binary matrix of blocks where source block is the upper left most block maze[0][0] and destination block is lower rightmost block maze[N-1][N-1].
# A rat starts from source and has to reach the destination. The rat can move only in two directions: forward and down.

maze = [
    [1, 1, 0, 0],
    [1, 1, 1, 1],
    [0, 1, 0, 0],
    [0, 1, 1, 1]
]



def isSafe(maze, row, col):
    if row >= 0 and row < len(maze) and col >= 0 and col < len(maze[0]) and maze[row][col] == 1 :
        return True
    return False

def solve(maze, row, col):

    path = [[0 for i in range(len(maze))] for j in range(len(maze[0]))]

    def solve_maze(maze, row, col, path):

        # Base case : goal
        if row == len(maze) - 1 and col == len(maze[0]) - 1 and maze[len(maze) - 1][len(maze[0]) - 1] == 1:
            path[len(maze) - 1][len(maze[0]) - 1] = 1
            return True

        # Constraints
        if isSafe(maze, row, col) == True:
            if path[row][col] == 1:
                return False

            path[row][col] = 1

            # Recursive Case row + 1
            if solve_maze(maze, row + 1, col, path) == True:
                return True
            # Recursive case col + 1
            if solve_maze(maze, row, col + 1, path) == True:
                return True

            # Backtrack
            path[row][col] = 0
            return False

    # Function call
    solve_maze(maze, 0, 0, path)
    
    return path

def print_maze(maze):
    for row in maze:
        for col in row:
            print(str(col) + " ", end="")
        print(" ")

# Test
print("Maze")
print_maze(maze)
print("Solution")
path = solve(maze, 0, 0)
print_maze(path)
