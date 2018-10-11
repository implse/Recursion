# Write a function solveQueens that accepts a Board as a parameter and tries to place 8 queens on it safely.

class Chess(object):
  def __init__(self, n):
    self.board = [["-" for x in range(n)] for x in range(n)]
    self.size = n

  # Print board
  def printBoard(self):
    for i in range(self.size):
      for j in range(self.size):
        print(self.board[i][j]+"   ", end="")
      print("\n")
