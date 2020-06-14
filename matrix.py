import numpy as np
import random


class Matrix():
    def __init__(self, size, nxCells, nyCells):
        self.size = size
        self.nxCells = nxCells
        self.nyCells = nyCells
        self.dimCellWidht = (size[0] - 1) / nxCells
        self.dimCellHeight = (size[1] - 1) / nyCells

        self.gameState = None
        self.gameColor = None

    def game_of_life(self):
        self.gameState = np.random.randint(0, 2, (self.nxCells, self.nyCells))

    def immigration_game(self):
        self.gameState = np.random.randint(0, 2, (self.nxCells, self.nyCells))
        self.gameColor = np.zeros((self.nxCells, self.nyCells))
        self.set_game_color()

    def set_game_color(self):
      for y in range(0, self.nyCells):
        for x in range(0, self.nxCells):
            if self.gameState[x, y] == 1:
                self.gameColor[x, y] = random.randint(1, 2)

    def neihbors(self, x, y):
        neighbors = self.gameState[(x - 1) % self.nxCells, (y - 1) % self.nyCells] + \
                    self.gameState[(x) % self.nxCells, (y - 1) % self.nyCells] + \
                    self.gameState[(x + 1) % self.nxCells, (y - 1) % self.nyCells] + \
                    self.gameState[(x - 1) % self.nxCells, (y) % self.nyCells] + \
                    self.gameState[(x + 1) % self.nxCells, (y) % self.nyCells] + \
                    self.gameState[(x - 1) % self.nxCells, (y + 1) % self.nyCells] + \
                    self.gameState[(x) % self.nxCells, (y + 1) % self.nyCells] + \
                    self.gameState[(x + 1) % self.nxCells, (y + 1) % self.nyCells]
        return neighbors

    def poly(self, x, y):
        poly = [
              ((x) * self.dimCellWidht, (y) * self.dimCellHeight),
              ((x + 1) * self.dimCellWidht, (y) * self.dimCellHeight),
              ((x + 1) * self.dimCellWidht, (y + 1) * self.dimCellHeight),
              ((x) * self.dimCellWidht, (y + 1) * self.dimCellHeight)
              ]
        return poly

    def neihbors_color(self, x, y):
        neighborsColor = self.gameColor[(x - 1) % self.nxCells, (y - 1) % self.nyCells] + \
                        self.gameColor[(x) % self.nxCells, (y - 1) % self.nyCells] + \
                        self.gameColor[(x + 1) % self.nxCells, (y - 1) % self.nyCells] + \
                        self.gameColor[(x - 1) % self.nxCells, (y) % self.nyCells] + \
                        self.gameColor[(x + 1) % self.nxCells, (y) % self.nyCells] + \
                        self.gameColor[(x - 1) % self.nxCells, (y + 1) % self.nyCells] + \
                        self.gameColor[(x) % self.nxCells, (y + 1) % self.nyCells] + \
                        self.gameColor[(x + 1) % self.nxCells, (y + 1) % self.nyCells]
        return neighborsColor
