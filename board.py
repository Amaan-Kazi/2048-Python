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

    self.merges = []
    self.slides = {}
    self.spawns = []

    self.spawn()
    self.spawns = [] # reset spawns

  def spawn(self: "Board") -> bool:
    emptyCells = []

    for row in range(len(self.grid)):
      for col in range(len(self.grid[row])):
        if (self.grid[row][col] == None):
          emptyCells.append((row, col))

    if emptyCells:
      row, col = random.choice(emptyCells)
      self.grid[row][col] = 2 if random.random() < 0.9 else 4
      self.spawns.append((row, col, self.grid[row][col]))
      return True
    else: return False

  def left(self: "Board"):
    for i in range(len(self.grid)):
      merged = []

      for j in range(len(self.grid[i])):
        if (self.grid[i][j] == None): continue
        k = j - 1
        moved = False
        movedTo = ()

        # move the tile left as much as possible
        while k >= 0:
          if (self.grid[i][k] == None): # Empty
            self.grid[i][k] = self.grid[i][k + 1]
            self.grid[i][k + 1] = None
            
            moved = True
            movedTo = (i, k, self.grid[i][k])
            k -= 1
          elif (self.grid[i][k] == self.grid[i][k + 1]) and ((i, k) not in merged): # Merge
            self.grid[i][k] *= 2
            self.grid[i][k + 1] = None
            
            moved = True
            movedTo = (i, k, self.grid[i][k] / 2)
            merged.append((i, k))
            break
          else: break

        if moved: self.slides[movedTo] = (i, j)

    self.spawn()

  def right(self: "Board"):
    for i in range(len(self.grid)):
      merged = []

      for j in range(len(self.grid[i]) - 1, -1, -1):
        if (self.grid[i][j] == None): continue
        k = j + 1
        moved = False
        movedTo = ()

        # move the tile right as much as possible
        while k < len(self.grid[i]):
          if (self.grid[i][k] == None): # Empty
            self.grid[i][k] = self.grid[i][k - 1]
            self.grid[i][k - 1] = None
            
            moved = True
            movedTo = (i, k, self.grid[i][k])
            k += 1
          elif (self.grid[i][k] == self.grid[i][k - 1]) and ((i, k) not in merged): # Merge
            self.grid[i][k] *= 2
            self.grid[i][k - 1] = None
            
            moved = True
            movedTo = (i, k, self.grid[i][k] / 2)
            merged.append((i, k))
            break
          else: break

        if moved: self.slides[movedTo] = (i, j)

    self.spawn()

  def up(self: "Board"):
    for j in range(len(self.grid)):
      merged = []

      for i in range(len(self.grid[j])):
        if (self.grid[i][j] == None): continue
        k = i - 1
        moved = False
        movedTo = ()

        # move the tile up as much as possible
        while k >= 0:
          if (self.grid[k][j] == None): # Empty
            self.grid[k][j] = self.grid[k + 1][j]
            self.grid[k + 1][j] = None
            
            moved = True
            movedTo = (k, j, self.grid[k][j])
            k -= 1
          elif (self.grid[k][j] == self.grid[k + 1][j]) and ((k, j) not in merged): # Merge
            self.grid[k][j] *= 2
            self.grid[k + 1][j] = None
            
            moved = True
            movedTo = (k, j, self.grid[k][j] / 2)
            merged.append((k, j))
            break
          else: break

        if moved: self.slides[movedTo] = (i, j)

    self.spawn()

  def down(self: "Board"):
    for j in range(len(self.grid)):
      merged = []

      for i in range(len(self.grid[j]) - 1, -1, -1):
        if (self.grid[i][j] == None): continue
        k = i + 1
        moved = False
        movedTo = ()

        # move the tile down as much as possible
        while k < len(self.grid):
          if (self.grid[k][j] == None): # Empty
            self.grid[k][j] = self.grid[k - 1][j]
            self.grid[k - 1][j] = None
            
            moved = True
            movedTo = (k, j, self.grid[k][j])
            k += 1
          elif (self.grid[k][j] == self.grid[k - 1][j]) and ((k, j) not in merged): # Merge
            self.grid[k][j] *= 2
            self.grid[k - 1][j] = None
            
            moved = True
            movedTo = (k, j, self.grid[k][j] / 2)
            merged.append((k, j))
            break
          else: break

        if moved: self.slides[movedTo] = (i, j)

    self.spawn()
