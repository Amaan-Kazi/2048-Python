from typing import List, Optional
import random

class Board:
  def __init__(self: "Board"):
    self.grid: List[List[Optional[int]]] = [
      [None, None, None, None],
      [None, None, None, None],
      [None, None, None, None],
      [None, None, None, None],
    ]
    self.spawn()

  def spawn(self: "Board") -> bool:
    emptyCells = []

    for row in range(len(self.grid)):
      for col in range(len(self.grid[row])):
        if (self.grid[row][col] == None):
          emptyCells.append((row, col))

    if emptyCells:
      row, col = random.choice(emptyCells)
      self.grid[row][col] = 2 if random.random() < 0.9 else 4
      return True
    else: return False

  def left(self: "Board"):
    for i in range(len(self.grid)):
      for j in range(len(self.grid[i])):
        if (self.grid[i][j] == None): continue
        k = j - 1

        # move the tile to the left as much as possible
        while k >= 0:
          if (self.grid[i][k] == None): # Empty
            self.grid[i][k] = self.grid[i][k + 1]
            self.grid[i][k + 1] = None

            k -= 1
          elif (self.grid[i][k] == self.grid[i][k + 1]): # Merge
            self.grid[i][k] *= 2
            self.grid[i][k + 1] = None

            k -= 1
            break
          else: break

    self.spawn()

