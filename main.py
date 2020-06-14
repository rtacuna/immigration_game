import pygame
import numpy as np
from matrix import Matrix
import time

pygame.init()

matrix = Matrix((600, 600), 60, 60)
matrix.game_of_life()
backgroundColor = 25, 25, 25

screen = pygame.display.set_mode(matrix.size)
screen.fill(backgroundColor)

while True:

    new_gameState = np.copy(matrix.gameState)
    screen.fill(backgroundColor)

    for y in range(0, matrix.nyCells):
        for x in range(0, matrix.nxCells):

            neighbors = matrix.neihbors(x, y)

            if matrix.gameState[x, y] == 0 and neighbors == 3:
                new_gameState[x, y] = 1

            elif matrix.gameState[x, y] == 1 and (neighbors < 2 or neighbors > 3):
                new_gameState[x, y] = 0

            poly = matrix.poly(x, y)
            pygame.draw.polygon(screen, (128, 128, 128), poly, int(abs(1 - new_gameState[x, y])))
    matrix.gameState = new_gameState
    time.sleep(0.1)
    pygame.display.flip()
