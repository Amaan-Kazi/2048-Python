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

  def spawn(self: "Board"):
    emptyCells = []

    for row in range(len(self.grid)):
      for col in range(len(self.grid[row])):
        if (self.grid[row][col] == None):
          emptyCells.append((row, col))

    if emptyCells:
      row, col = random.choice(emptyCells)
      self.grid[row][col] = 2 if random.random() < 0.9 else 4
