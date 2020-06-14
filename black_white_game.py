import pygame
import numpy as np
import time
import random

pygame.init()
background = 25, 25, 25
size = width, height = 600, 600

nxCells = 60
nyCells = 60

dimCellWidht = (width - 1) / nxCells
dimCellHeight = (height - 1) / nyCells

screen = pygame.display.set_mode(size)
screen.fill(background)

gameState = np.random.randint(0, 2, (nxCells, nyCells))
gameColor = np.zeros((nxCells, nyCells))

for y in range(0, nyCells):
    for x in range(0, nxCells):
        if gameState[x, y] == 1:
            gameColor[x, y] = random.randint(1, 2)

while True:

    new_gameState = np.copy(gameState)
    new_gameColor = np.copy(gameColor)
    screen.fill(background)

    for y in range(0, nyCells):
        for x in range(0, nxCells):

            color = (128, 128, 128)
            if gameColor[x, y] == 1:
                color = (0, 0, 0)
            elif gameColor[x, y] == 2:
                color = (255, 255, 255)

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
                neighborsColor = gameColor[(x - 1) % nxCells, (y - 1) % nyCells] + \
                                  gameColor[(x) % nxCells, (y - 1) % nyCells] + \
                                  gameColor[(x + 1) % nxCells, (y - 1) % nyCells] + \
                                  gameColor[(x - 1) % nxCells, (y) % nyCells] + \
                                  gameColor[(x + 1) % nxCells, (y) % nyCells] + \
                                  gameColor[(x - 1) % nxCells, (y + 1) % nyCells] + \
                                  gameColor[(x) % nxCells, (y + 1) % nyCells] + \
                                  gameColor[(x + 1) % nxCells, (y + 1) % nyCells]
                if neighborsColor == 3 or neighborsColor == 4:
                    new_gameColor[x, y] = 1
                    color = (0, 0, 0)
                else:
                    new_gameColor[x, y] = 2
                    color = (255, 255, 255)

            elif gameState[x, y] == 1 and (neighbors < 2 or neighbors > 3):
                new_gameState[x, y] = 0
                new_gameColor[x, y] = 0
                color = (128, 128, 128)

            poly = [
                    ((x) * dimCellWidht, (y) * dimCellHeight),
                    ((x + 1) * dimCellWidht, (y) * dimCellHeight),
                    ((x + 1) * dimCellWidht, (y + 1) * dimCellHeight),
                    ((x) * dimCellWidht, (y + 1) * dimCellHeight)
                  ]

            pygame.draw.polygon(screen, color, poly, int(abs(1 - new_gameState[x, y])))
    gameState = new_gameState
    gameColor = new_gameColor
    time.sleep(0.1)
    pygame.display.flip()
