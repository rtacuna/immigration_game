import pygame
import numpy as np
# import matplotlib.pyplot as plt
import time

pygame.init()

size = width, height = 600, 600
backgroundColor = 25, 25, 25

nxCells = 60
nyCells = 60

dimCellWidht = (width - 1) / nxCells
dimCellHeight = (height - 1) / nyCells

screen = pygame.display.set_mode(size)
screen.fill(backgroundColor)

gameState = np.zeros((nxCells, nyCells))
gameState = np.random.randint(0, 2, (nxCells, nyCells))


while True:

    new_gameState = np.copy(gameState)
    screen.fill(backgroundColor)

    for y in range(0, nyCells):
        for x in range(0, nxCells):

            neighbors = gameState[(x - 1) % nxCells, (y - 1) % nyCells] + \
                        gameState[(x) % nxCells, (y - 1) % nyCells] + \
                        gameState[(x + 1) % nxCells, (y - 1) % nyCells] + \
                        gameState[(x - 1) % nxCells, (y) % nyCells] + \
                        gameState[(x + 1) % nxCells, (y) % nyCells] + \
                        gameState[(x - 1) % nxCells, (y + 1) % nyCells] + \
                        gameState[(x) % nxCells, (y + 1) % nyCells] + \
                        gameState[(x + 1) % nxCells, (y + 1) % nyCells]

            if gameState[x, y] == 0 and neighbors == 3:
                new_gameState[x, y] = 1

            elif gameState[x, y] == 1 and (neighbors < 2 or neighbors > 3):
                new_gameState[x, y] = 0


            poly = [
              ((x) * dimCellWidht, (y) * dimCellHeight),
              ((x + 1) * dimCellWidht, (y) * dimCellHeight),
              ((x + 1) * dimCellWidht, (y + 1) * dimCellHeight),
              ((x) * dimCellWidht, (y + 1) * dimCellHeight)
            ]
            pygame.draw.polygon(screen, (128, 128, 128), poly, int(abs(1 - new_gameState[x, y])))
    gameState = new_gameState
    time.sleep(0.1)
    pygame.display.flip()
