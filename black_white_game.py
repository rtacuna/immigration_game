import pygame
import numpy as np
from matrix import Matrix
import time
import random

pygame.init()

matrix = Matrix((600, 600), 60, 60)
matrix.immigration_game()
backgroundColor = 25, 25, 25

screen = pygame.display.set_mode(matrix.size)
screen.fill(backgroundColor)

while True:

    new_gameState = np.copy(matrix.gameState)
    new_gameColor = np.copy(matrix.gameColor)
    screen.fill(backgroundColor)

    for y in range(0, matrix.nyCells):
        for x in range(0, matrix.nxCells):

            color = (128, 128, 128)
            if matrix.gameColor[x, y] == 1:
                color = (0, 0, 0)
            elif matrix.gameColor[x, y] == 2:
                color = (255, 255, 255)

            neighbors = matrix.neihbors(x, y)

            if matrix.gameState[x, y] == 0 and neighbors == 3:
                new_gameState[x, y] = 1
                neighborsColor = matrix.neihbors_color(x, y)
                if neighborsColor == 3 or neighborsColor == 4:
                    new_gameColor[x, y] = 1
                    color = (0, 0, 0)
                else:
                    new_gameColor[x, y] = 2
                    color = (255, 255, 255)

            elif matrix.gameState[x, y] == 1 and (neighbors < 2 or neighbors > 3):
                new_gameState[x, y] = 0
                new_gameColor[x, y] = 0
                color = (128, 128, 128)

            poly = matrix.poly(x, y)
            pygame.draw.polygon(screen, color, poly, int(abs(1 - new_gameState[x, y])))
    matrix.gameState = new_gameState
    matrix.gameColor = new_gameColor
    time.sleep(0.1)
    pygame.display.flip()
